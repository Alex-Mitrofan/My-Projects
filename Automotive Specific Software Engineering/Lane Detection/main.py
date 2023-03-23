import cv2
import numpy as np

print(*(cv2.__dict__.keys()), sep='\n')
print(cv2.VideoCapture)

cam = cv2.VideoCapture('Lane Detection Test Video 01.mp4')
cam.set(cv2.CAP_PROP_FPS, 30)

width = 420
height = 220
sobel_horizontal = np.float32([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])
sobel_vertical = np.float32([[-1, -2, -1],
                             [0, 0, 0],
                             [1, 2, 1]])

upper_left = (int(0.47 * width), int(height * 0.75))
upper_right = (int(0.53 * width), int(height * 0.75))

lower_left = (0 * width, 1 * height)
lower_right = (1 * width, 1 * height)

trapezoid_polygon = np.array([upper_right, upper_left, lower_left, lower_right], dtype=np.int32)
trapezoid_frame = np.zeros((height, width), dtype=np.uint8)
cv2.fillConvexPoly(trapezoid_frame, trapezoid_polygon, 1)

trapezoid_bounds = np.float32(trapezoid_polygon)
magic_matrix = cv2.getPerspectiveTransform(trapezoid_bounds,
                                           np.float32([(width, 0), (0, 0), (0, height), (width, height)]))

prev_left_top_x = int(3 / 4 * width)
prev_left_bottom_x = int(3 / 4 * width)
prev_right_top_x = int(3 / 4 * width)
prev_right_bottom_x = int(3 / 4 * width)

magic_matrix_reverse = cv2.getPerspectiveTransform(np.float32([(width, 0), (0, 0), (0, height), (width, height)]),
                                                   trapezoid_bounds)

global final_frame

while True:
    ret, frame = cam.read()

    if ret is False:
        break

    frame = cv2.resize(frame, (width, height))
    final_frame = frame.copy()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    road_trapezoid_frame = frame * trapezoid_frame
    stretched_frame = cv2.warpPerspective(road_trapezoid_frame, magic_matrix, (width, height))
    blur_frame = cv2.blur(stretched_frame, ksize=(5, 5))
    frame_sobel_vertical = cv2.filter2D(np.float32(blur_frame), -1, sobel_vertical)
    frame_sobel_horizontal = cv2.filter2D(np.float32(blur_frame), -1, sobel_horizontal)
    frame_sobel_float32 = np.sqrt(frame_sobel_vertical ** 2 + frame_sobel_horizontal ** 2)
    frame_sobel = cv2.convertScaleAbs(frame_sobel_float32)
    ret, frame_threshold_binary = cv2.threshold(frame_sobel, 125, 255, cv2.THRESH_BINARY)

    black_columns_frame = frame_threshold_binary.copy()
    black_columns_frame[:, 0:int(0.17 * width)] = 1
    black_columns_frame[:, int(0.83 * width):] = 1

    left_side_of_frame = black_columns_frame[:, :width // 2]
    right_side_of_frame = black_columns_frame[:, width // 2:]

    left = np.array(np.argwhere(left_side_of_frame == 255))
    right = np.array(np.argwhere(right_side_of_frame == 255))

    left_xs = [l[1] for l in left]
    left_ys = [l[0] for l in left]

    right_xs = [r[1] for r in right]
    right_ys = [r[0] for r in right]


    '''
    for i in range(0, len(black_columns_frame)):
        for j in range(0, len(black_columns_frame[0])):
            if black_columns_frame[i][j] == 255:
                if j < len(black_columns_frame[0]) / 2:
                    left_xs.append(j)
                    left_ys.append(i)
                else:
                    right_xs.append(j - width / 2)
                    right_ys.append(i)
    '''

    if len(left_xs) != 0:
        left_b_a = np.polynomial.polynomial.polyfit(left_xs, left_ys, deg=1)
    if len(right_xs) != 0:
        right_b_a = np.polynomial.polynomial.polyfit(right_xs, right_ys, deg=1)

    left_top_y = height
    left_top_x = int((height - left_b_a[0]) / left_b_a[1])

    left_bottom_y = 0
    left_bottom_x = int((0 - left_b_a[0]) / left_b_a[1])

    right_top_y = height
    right_top_x = int((height - right_b_a[0]) / right_b_a[1]) + int(width / 2)

    right_bottom_y = 0
    right_bottom_x = int((0 - right_b_a[0]) / right_b_a[1]) + int(width / 2)

    if left_top_x < 10 or left_top_x > width // 2 - 10:
        left_top_x = prev_left_top_x
    if left_bottom_x < 30 or left_bottom_x > width // 2 - 30:
        left_bottom_x = prev_left_bottom_x
    if right_top_x < width//2 or right_top_x > width - 20:
        right_top_x = prev_right_top_x
    if right_bottom_x < width//2 + 30 or right_bottom_x > width - 30:
        right_bottom_x = prev_right_bottom_x

    prev_left_top_x = left_top_x
    prev_left_bottom_x = left_bottom_x
    prev_right_top_x = right_top_x
    prev_right_bottom_x = right_bottom_x

    # print(right_top_x, " ", right_top_y, " ", right_bottom_x, " ", right_bottom_y)
    cv2.line(black_columns_frame, (left_top_x, left_top_y), (left_bottom_x, left_bottom_y), (100, 0, 0), 5)
    cv2.line(black_columns_frame, (right_top_x, right_top_y), (right_bottom_x, right_bottom_y), (200, 0, 0), 5)

    # create a blank frame
    final_blank_frame = np.zeros((height, width), dtype=np.uint8)
    # draw left line on the blank frame
    cv2.line(final_blank_frame, (left_top_x, left_top_y), (left_bottom_x, left_bottom_y), (255, 0, 0), 5)
    stretched_frame_left_line = cv2.warpPerspective(final_blank_frame, magic_matrix_reverse, (width, height))

    '''
    for i in range(0, len(stretched_frame_left_line)):
        for j in range(0, len(stretched_frame_left_line[0])):
            if stretched_frame_left_line[i][j] == 255:
                left_line_coordinates.append((i, j))
    '''

    left_line_coordinates = np.argwhere(stretched_frame_left_line == 255)
    if len(left_line_coordinates) > 0:
        left_line_coordinates[:][0, 1] = left_line_coordinates[:][1, 0]

    final_blank_frame2 = np.zeros((height, width), dtype=np.uint8)
    cv2.line(final_blank_frame2, (right_top_x, right_top_y), (right_bottom_x, right_bottom_y), (255, 0, 0), 5)
    stretched_frame_right_line = cv2.warpPerspective(final_blank_frame2, magic_matrix_reverse, (width, height))

    right_line_coordinates = []
    '''
    for i in range(0, len(stretched_frame_right_line)):
        for j in range(0, len(stretched_frame_right_line[0])):
            if stretched_frame_right_line[i][j] == 255:
                right_line_coordinates.append((i, j))
    '''
    right_line_coordinates = np.argwhere(stretched_frame_right_line == 255)
    if len(right_line_coordinates) > 0:
        right_line_coordinates[:][0, 1] = right_line_coordinates[:][1, 0]

    for x, y in left_line_coordinates:
        final_frame[x][y] = (50, 50, 250)
    for x, y in right_line_coordinates:
        final_frame[x][y] = (50, 250, 50)

    cv2.imshow('Original', frame)
    cv2.imshow('Trapezoid', road_trapezoid_frame)
    cv2.imshow('Stretched', stretched_frame)
    cv2.imshow('Blur', blur_frame)
    cv2.imshow('Sobel Filter', frame_sobel)
    cv2.imshow('Threshold Binary', frame_threshold_binary)
    cv2.imshow('Black Columns', black_columns_frame)
    # cv2.imshow('Final Blank Frame', final_blank_frame)
    # cv2.imshow('Stretched Frame Left Line', stretched_frame_left_line)
    # cv2.imshow('Stretched Frame Right Line', stretched_frame_right_line)
    cv2.imshow('Final Frame', final_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
