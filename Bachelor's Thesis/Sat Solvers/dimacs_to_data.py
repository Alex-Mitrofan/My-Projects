def get_data(file_name):
    nr_vars = 0
    clauses = []

    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        if line.startswith('p'):
            l = line.split(" ")
            nr_vars = int(l[2])
        elif line.startswith(' '):  #first clause starts with ' '
            l = line[1:].split(" ")[:-1] 
            l = [int(i) for i in l]
            clauses.append(l)
        elif  line[0] not in "c%0'\n'":
            l = line.split(" ")[:-1]
            l = [int(i) for i in l]
            clauses.append(l)

    return nr_vars, clauses 