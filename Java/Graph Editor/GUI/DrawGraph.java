package GUI;

import CityEditor.Intersection;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Objects;

public class DrawGraph extends JPanel {
    private final MainFrame frame;
    private final HashMap<Intersection, Integer> hashMapX = new HashMap<>();
    private final HashMap<Intersection, Integer> hashMapY = new HashMap<>();
    int xMiddle = 450;
    int yMiddle = 400;
    int math = Math.min(xMiddle, yMiddle);
    int radius = 4 * math / 5;
    int radius1 = Math.abs(math - radius) / 2;
    private List<Intersection> nodeList = new ArrayList<Intersection>();
    private BufferedImage graphImage;

    /**
     * Getter
     */
    public BufferedImage getGraphImage() {
        return graphImage;
    }
    /**
     * Setter
     */
    public void setGraphImage(BufferedImage graphImage) {
        this.graphImage = graphImage;
    }
    /**
     * Creates a Graphics2D object in order draw the graph.
     */
    public DrawGraph(MainFrame frame, List<Intersection> nodeList) throws IOException {
        this.frame = frame;

        this.nodeList = nodeList;
        BufferedImage bufferedImage = new BufferedImage(900, 800, BufferedImage.TYPE_INT_ARGB);
        Graphics2D imageGraphics = bufferedImage.createGraphics();
        imageGraphics.setPaint(new Color(88,88,88));
        imageGraphics.fillRect(0, 0, 900, 800);

        this.paintNodes(imageGraphics);
        this.paintEdges(imageGraphics);
        this.paintNumbers(imageGraphics);

        setGraphImage(bufferedImage);
        ImageIO.write(bufferedImage, "PNG", new File("C:\\Users\\Alex\\Desktop\\graph.png"));


        setLayout(new BorderLayout());
        setBounds(300,0,900,800);

        ImageIcon graph = new ImageIcon(bufferedImage);
        JLabel graphLabel = new JLabel(graph);
        graphLabel.setOpaque(true);
        graphLabel.setBounds(0,0,600,800);
        graphLabel.setLayout(new BorderLayout());
        add(graphLabel, BorderLayout.CENTER);


    }

    /**
     * Paints the nodes of the graph.
     */
    public void paintNodes(Graphics2D graphics2D) {
        for (int index = 0; index < this.nodeList.size(); index++) {
            double tangent = 2 * Math.PI * index / this.nodeList.size();
            int xCoordonate = (int) Math.round(xMiddle + radius * Math.cos(tangent));
            int yCoordonate = (int) Math.round(yMiddle + radius * Math.sin(tangent));

            graphics2D.setPaint(new Color(56,210,82));
            graphics2D.fillOval(xCoordonate - radius1, yCoordonate - radius1, 2 * radius1, 2 * radius1);
            hashMapX.put(this.nodeList.get(index), xCoordonate - radius1 + 10);
            hashMapY.put(this.nodeList.get(index), yCoordonate - radius1 + 25);
        }
    }

    /**
     * Prints the edges of the graph.
     */
    public void paintEdges(Graphics2D graphics2D) {
        graphics2D.setPaint(new Color(56,210,82));
        graphics2D.setStroke(new BasicStroke(4));
        for (Intersection node : nodeList) {
            node.getNeighbours().stream().forEach(neighbour -> graphics2D.drawLine(hashMapX.get(node),
                    hashMapY.get(node), hashMapX.get(neighbour), hashMapY.get(neighbour)));
        }
    }

    /**
     * Paints the number of the nodes.
     */
    public void paintNumbers(Graphics2D graphics2D) {
        Integer number = 1;
        for (int index = 0; index < this.nodeList.size(); index++) {
            double tangent = 2 * Math.PI * index / this.nodeList.size();
            int xCoordonate = (int) Math.round(xMiddle + radius * Math.cos(tangent));
            int yCoordonate = (int) Math.round(yMiddle + radius * Math.sin(tangent));

            graphics2D.setFont(graphics2D.getFont().deriveFont(20f));
            graphics2D.setPaint(Color.blue);
            this.nodeList.get(index).setNumberName(number);
            number++;
            graphics2D.drawString(String.valueOf(this.nodeList.get(index).getNumberName()),
                    xCoordonate - radius1 + 20, yCoordonate - radius1 + 35);
        }
    }
}
