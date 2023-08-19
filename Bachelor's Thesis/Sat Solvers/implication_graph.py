class ImplicationGraph():
    def __init__(self):
        self.graph = dict()
        self.literals = []

    def add_node(self, literal, parent, decision_level, decision_type): #decision_type could be "arbitrary_decision" made by picking a branching
        self.literals.append(literal)                                   #variable or a "forced_assignment" during unit propagation; this parameter
        self.graph[literal] = (parent, decision_level, decision_type)   #is used for chosing color of node in GUI
                    
        
    def remove_node(self, literal):
        if literal in self.literals:
            self.graph.pop(literal)
        if literal in self.literals:
            self.literals.remove(literal)
    
    def back_jump(self, back_level):
        for key in list(self.graph):
            if self.graph[key][1] >= back_level:
                self.remove_node(key)

    def get_parents(self, literal):
        if literal in self.literals:
            return self.graph[literal][0]