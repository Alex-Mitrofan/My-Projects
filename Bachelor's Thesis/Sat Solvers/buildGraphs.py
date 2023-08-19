import graphviz
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from PIL import Image as PILImage
from io import BytesIO
 
 
 
def build_decision_tree(decisions, back_jump_level):
    #decisions = [{11: -1}, {5: -1}, {4: 1, 3: -1, 1: -1}, {9: 1, 8: -1}, {10: -1}, {12: -1}, {6: -1}, {7: -1, 2: 1}]

    nodes = []
    assignments = []
    xlabels = []

    for dictionary in decisions:
        keys = list(dictionary.keys())       
        node = keys[0]
        nodes.append(node)
        assignment = dictionary[keys[0]]
        assignments.append(assignment)
        forced_decisions = keys[1:]
        xlabel = "X" + str(keys[0]) + "=" + str(dictionary[keys[0]]) + ", "
        for decision in forced_decisions:
            xlabel = xlabel + "X" + str(decision) + ":" + str(dictionary[decision]) + ", "
        xlabel = xlabel[:-2]
        
        xlabel += (40-len(xlabel))*" "
        xlabels.append(xlabel)

    graph = graphviz.Digraph()

    if len(nodes)>0 and len(xlabels)>0:
        graph.node('X'+str(nodes[0]), xlabel = xlabels[0], fillcolor='#B8BA7B', style='filled')

    for i in range(1, len(nodes)):
        if assignments[i-1] == 1:
            graph.node('X'+str(nodes[i]), xlabel=xlabels[i], fillcolor='#B8BA7B', style='filled')
            graph.node('0'+str(nodes[i]), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            graph.edge('X'+str(nodes[i-1]), 'X'+str(nodes[i]), color="green")
            graph.edge('X'+str(nodes[i-1]), '0'+str(nodes[i]), color="red", style='dashed')
        elif assignments[i-1] == -1:
            graph.node('0'+str(nodes[i]), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            graph.node('X'+str(nodes[i]), xlabel=xlabels[i], fillcolor='#B8BA7B', style='filled') 
            graph.edge('X'+str(nodes[i-1]), 'X'+str(nodes[i]), color="red")
            graph.edge('X'+str(nodes[i-1]), '0'+str(nodes[i]), color="green", style='dashed')

    if len(assignments) > 0:
        if assignments[len(assignments)-1] == 1:
            graph.node('0x'+str(len(nodes)-1), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            graph.node('0y'+str(len(nodes)-1), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            graph.edge('X'+str(nodes[len(nodes)-1]), '0x'+str(len(nodes)-1), color="green")
            graph.edge('X'+str(nodes[len(nodes)-1]), '0y'+str(len(nodes)-1), color="red", style='dashed')
        elif assignments[len(assignments)-1] == -1:
            graph.node('0x'+str(len(nodes)-1), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            graph.node('0y'+str(len(nodes)-1), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            graph.edge('X'+str(nodes[len(nodes)-1]), '0x'+str(len(nodes)-1), color="green", style='dashed')
            graph.edge('X'+str(nodes[len(nodes)-1]), '0y'+str(len(nodes)-1), color="red")

    if back_jump_level != None:      #draw back jump arrow
        last_node = 'X' + str(nodes[len(nodes)-1])
        backjump_node = 'X' + str(list(decisions[back_jump_level].keys())[0])
        graph.edge(last_node, backjump_node, color="blue")

    # Set the background color of the graph
    graph.attr('graph', bgcolor='#FFE6CC')  # RGBA color code

    # Generate and render the graph to a file
    graph.format = 'png'
    graph.render(filename='decision_tree')

    '''
    # Load the image using PIL
    with open('decision_tree.png', 'rb') as f:
        pil_image = PILImage.open(BytesIO(f.read()))

    # Flip the image vertically
    pil_image = pil_image.transpose(PILImage.FLIP_TOP_BOTTOM)
    pil_image.close()
    '''

 

def build_implication_graph(graph_dictionary, conflict):

    nodes = list(graph_dictionary.keys())
    graph = graphviz.Digraph()
    nodes_added = []

    for node in nodes:
        label = ""
        color = "#B8BA7B"
        if node<0:
            label = "¬X" + str(-node)
        else:
            label = "X" + str(node)
        if graph_dictionary[node][2] == 'forced_assignment':
            color = "#B9B9B3"

        graph.node(name=label, fillcolor=color, style='filled')
        nodes_added.append(label)

    for node in nodes:
        node_name = ''
        parents = graph_dictionary[node][0]
        if node<0:
            node_name = "¬X" + str(-node)
        else: 
            node_name = "X" + str(node)
        if parents != 0:
            for parent in parents:
                parent_name = ''
                negated_parent_name = ''
                if parent<0:
                    parent_name = "¬X" + str(-parent)
                    negated_parent_name = "X" + str(-parent)
                else: 
                    parent_name = "X" + str(parent)
                    negated_parent_name = "¬X" + str(parent)
                
                if parent_name not in nodes_added and negated_parent_name not in nodes_added:
                    nodes_added.append(parent_name)
                    graph.node(parent_name, fillcolor=color, style='filled')  #this node leads to conflict nodes
                
               
                if negated_parent_name in nodes_added:
                    if node == conflict or -node == conflict:
                        graph.edge(negated_parent_name, node_name, color="red")
                    else:
                        graph.edge(negated_parent_name, node_name)
                else:
                    if node == conflict or -node == conflict:
                        graph.edge(parent_name, node_name, color="red")
                    else:
                        graph.edge(parent_name, node_name)
        
    # Set the background color of the graph
    graph.attr('graph', bgcolor='#FFE6CC')  # RGBA color code

    # Generate and render the graph to a file
    graph.format = 'png'
    graph.render(filename='implication_graph')


def build_dpll_tree(decisions, back_jump_level):
    nodes = []
    assignments = []
    xlabels = []

    for dictionary in decisions:
        keys = list(dictionary.keys())     
        node = keys[0]
        nodes.append(node)
        assignment = dictionary[keys[0]]
        assignments.append(assignment)
     
        xlabel = "X" + str(keys[0]) + "=" + str(dictionary[keys[0]])
        xlabel += (40-len(xlabel))*" "

        xlabels.append(xlabel)

    graph = graphviz.Digraph()

    if len(nodes)>0 and len(xlabels)>0:
        graph.node('X'+str(nodes[0]), xlabel = xlabels[0], fillcolor='#B8BA7B', style='filled')

    for i in range(1, len(nodes)):
        if assignments[i-1] == 1:
            if nodes[i] == "SAT":
                graph.node('S'+str(nodes[i-1]), fillcolor='#00FF00', style='filled', fontcolor='#00FF00')  
                graph.edge('X'+str(nodes[i-1]), 'S'+str(nodes[i-1]), color="green") 
            elif nodes[i] == "UNSAT":
                graph.node('U'+str(nodes[i-1]), fillcolor='#FF0000', style='filled', fontcolor='#FF0000')
                graph.edge('X'+str(nodes[i-1]), 'U'+str(nodes[i-1]), color="green") 
            else:
                graph.node('X'+str(nodes[i]), xlabel=xlabels[i], fillcolor='#B8BA7B', style='filled')   
                graph.edge('X'+str(nodes[i-1]), 'X'+str(nodes[i]), color="green")
            
                graph.node('0'+str(nodes[i]), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
                if nodes.count(nodes[i-1]) == 1:
                    graph.edge('X'+str(nodes[i-1]), '0'+str(nodes[i]), color="red", style='dashed')
        elif assignments[i-1] == -1:   
            if nodes[i] == "SAT":
                graph.node('S'+str(nodes[i-1]), fillcolor='#00FF00', style='filled', fontcolor='#00FF00')  
                graph.edge('X'+str(nodes[i-1]), 'S'+str(nodes[i-1]), color="red") 
            elif nodes[i] == "UNSAT":
                graph.node('U'+str(nodes[i-1]), fillcolor='#FF0000', style='filled', fontcolor='#FF0000')
                graph.edge('X'+str(nodes[i-1]), 'U'+str(nodes[i-1]), color="red") 
            else:
                graph.node('0'+str(nodes[i]), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
                graph.node('X'+str(nodes[i]), xlabel=xlabels[i], fillcolor='#B8BA7B', style='filled') 
                if nodes.count(nodes[i-1]) == 1:
                    graph.edge('X'+str(nodes[i-1]), '0'+str(nodes[i]), color="green", style='dashed')
                graph.edge('X'+str(nodes[i-1]), 'X'+str(nodes[i]), color="red")
                
        

    if len(assignments) > 0:
        if assignments[len(assignments)-1] == 1:
            graph.node('0x'+str(len(nodes)-1), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            graph.node('0y'+str(len(nodes)-1), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            graph.edge('X'+str(nodes[len(nodes)-1]), '0x'+str(len(nodes)-1), color="green")
            if nodes.count(nodes[len(nodes)-1]) == 1:
                graph.edge('X'+str(nodes[len(nodes)-1]), '0y'+str(len(nodes)-1), color="red", style='dashed')
        elif assignments[len(assignments)-1] == -1:
            graph.node('0x'+str(len(nodes)-1), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            graph.node('0y'+str(len(nodes)-1), fontcolor='#FFE6CC', color='#FFE6CC', style='filled')
            if nodes.count(nodes[len(nodes)-1]) == 1:
                graph.edge('X'+str(nodes[len(nodes)-1]), '0x'+str(len(nodes)-1), color="green", style='dashed')
            graph.edge('X'+str(nodes[len(nodes)-1]), '0y'+str(len(nodes)-1), color="red")
   

    # Set the background color of the graph
    graph.attr('graph', bgcolor='#FFE6CC')  # RGBA color code

    # Generate and render the graph to a file
    graph.format = 'png'
    graph.render(filename='decision_tree')

 

def build_walksat_graph(nodes, edges, assignments):
    graph = graphviz.Digraph()
    for i in range(len(nodes)):
        if assignments == None:
            graph.node('X'+str(nodes[i]), fillcolor='#D3D3D3', style='filled')
        elif assignments[i] == 1:
            graph.node('X'+str(nodes[i]), fillcolor='green', style='filled')
        elif assignments[i] == -1:
            graph.node('X'+str(nodes[i]), fillcolor='red', style='filled')

    graph_edges = set()
    for edge in edges:
        for i in range(len(edge)-1):
            for j in range(i+1, len(edge)):
                if ('X'+str(edge[i]), 'X'+str(edge[j])) not in graph_edges:
                    graph.edge('X'+str(edge[i]), 'X'+str(edge[j]), arrowhead="none")
                    graph_edges.add(('X'+str(edge[i]), 'X'+str(edge[j])))

    return graph


def show_walksat_graph(graph):
    # Set the background color of the graph
    graph.attr('graph', bgcolor='#FFE6CC')  # RGBA color code

    # Generate and render the graph to a file
    graph.format = 'png'
    graph.render(filename='implication_graph')

 