from formula import Formula
import random
from dimacs_to_data import get_data
import copy
from buildGraphs import build_walksat_graph

#nvars, clauses = get_data('uf50-01.cnf')
nvars, clauses = get_data('uuf50-01.cnf')

clauses = [[1, 4],
           [1, -3, -8],
           [1, 8, 12],
           [2, 11],
           [-7, -3, 9],
           [-7, 8, -9],
           [7, 8, -10],
           [7, 10, -12],
           [-1, 5],
           [-1,-5]]

class WalkSAT():
    def __init__(self, clauses):
        self.clauses = clauses
        self.formula = Formula(clauses)
        self.nr_clauses = len(self.formula.formula)
        self.original_formula = Formula(clauses)
        self.max_iter = 1000
        self.p = 0.90
        self.nr_flips = 0
        

    def init_GUI(self):
        self.problem_data = []       #list with all data necessary for GUI
        self.state = dict()          #every state of the problem will be stored in problem_data; used for GUI 
        self.nodes = []              #used for GUI 
        self.edges = []              #used for GUI  
        self.graph = build_walksat_graph(self.nodes, self.edges, None)
        
        self.state = {
                    "clauses": list(self.clauses),
                    "probability": self.p,
                    "nr_flips": self.nr_flips,
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "graph": copy.deepcopy(self.graph),
                    "iteration": None,
                    "action": "Init WalkSAT"
                }
        self.problem_data.append(self.state)

        index_clause = -1
        for clause in self.formula.formula:
            index_clause += 1
            self.edges.append([])
            for literal in clause.literals:
                if abs(literal) not in self.nodes:
                    self.nodes.append(abs(literal))
                self.edges[index_clause].append(abs(literal))
        



    def random_assignment(self):
        while len(self.formula.unassigned_vars) > 0:
            variable = random.choice(self.formula.unassigned_vars)
            assignment = random.choice([1, -1])

            self.formula.update_assignment_of_all_occurrences(variable, assignment)  
            self.formula.update_unassigned_vars(variable)
    

    def select_unsat_clause(self):
        unsat_clauses_index = []
        for i in range(self.nr_clauses):
            if self.formula.formula[i].get_value() == -1: #if clause from index i is UNSAT
                unsat_clauses_index.append(i)
        
        if len(unsat_clauses_index) > 0:                  #condition to avoid exception at random.choice
            return random.choice(unsat_clauses_index)
        else: 
            return -1


    def get_break_count(self, clause_index, variable_index):
        try:
            variable = self.formula.formula[clause_index].literals[variable_index]
            assignment = self.formula.formula[clause_index].literals_values[variable_index]
        except:       
            return None
        current_count = 0                   #nr of satisfied clauses in current formula
        for clause in self.formula.formula:
            if clause.get_value() == 1:
                current_count +=1
        self.formula.update_assignment_of_all_occurrences(variable, -assignment)   #flip variable truth value
        flipped_count = 0                   #nr of satisfied clauses in flipped variable formula
        for clause in self.formula.formula:
            if clause.get_value() == 1:
                flipped_count +=1
        
        self.formula.update_assignment_of_all_occurrences(variable, -assignment)   #rest variable truth value
        break_count = current_count - flipped_count
        return break_count


    def select_variable(self, clause_index):
        clause = self.formula.formula[clause_index]
        break_counts = []
        for i in range(len(clause.literals)):
            break_counts.append(self.get_break_count(clause_index, i))     
        max_break_count = max(break_counts)
        min_break_count = min(break_counts)

        max_counts = [] 
        min_counts = []
        for i in range(len(break_counts)):         #if there are multiple variables with max/min break-count select one randomly
            if break_counts[i] == max_break_count:
                max_counts.append(i)
            if break_counts[i] == min_break_count:
                min_counts.append(i)

        return (random.choice(max_counts), random.choice(min_counts))    #return indexes of variable with max break-count and min break-count


    def flip_variable(self, variable):
        for clause in self.formula.formula:
            for i in range(len(clause.literals)):
                if clause.literals[i] == variable:
                    assignment = clause.literals_values[i]
        
        self.formula.update_assignment_of_all_occurrences(variable, -assignment)  


    def solve(self):
        self.random_assignment()
        for iteration in range(self.max_iter):
            if self.formula.all_true() == 1:
                return "SAT" 
            clause_index = self.select_unsat_clause()
            max_break_count_index, min_break_count_index = self.select_variable(clause_index)

            probability = random.random()
            if probability <= self.p:
                variable = self.formula.formula[clause_index].literals[max_break_count_index]
            else:
                variable = self.formula.formula[clause_index].literals[min_break_count_index]
            
            self.flip_variable(variable)
        return "UNSAT" 
    

    def get_assignments(self):   #get assignments of all variables; used for GUI
        assignments = []
        for var in self.nodes:
            found = False
            for clause in self.formula.formula:
                if found == False:
                    for i in range(len(clause.literals)):
                        if found == False:
                            if var == abs(clause.literals[i]):
                                if clause.literals[i] > 0:
                                    assignments.append(clause.literals_values[i])
                                    found = True
                                else:
                                    assignments.append(-clause.literals_values[i])
                                    found = True
        return assignments


    def solve_with_GUI(self):
        assignments = self.get_assignments()
        self.graph = build_walksat_graph(self.nodes, self.edges, assignments)
        self.state = {
                    "clauses": list(self.clauses),
                    "probability": self.p,
                    "nr_flips": self.nr_flips,
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "graph": copy.deepcopy(self.graph),
                    "iteration": None,
                    "action": "Init WalkSAT"
                }
        self.problem_data.append(self.state)

        self.random_assignment()
        
        assignments = self.get_assignments()
        self.graph = build_walksat_graph(self.nodes, self.edges, assignments)
        self.state = {
                    "clauses": list(self.clauses),
                    "probability": self.p,
                    "nr_flips": self.nr_flips,
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "graph": copy.deepcopy(self.graph),
                    "iteration": None,
                    "action": "RandomAssignment"
                }
        self.problem_data.append(self.state)

        assignments = self.get_assignments()
        self.graph = build_walksat_graph(self.nodes, self.edges, assignments)
        for iteration in range(self.max_iter):
            if self.formula.all_true() == 1:
                self.state = {
                    "clauses": list(self.clauses),
                    "probability": self.p,
                    "nr_flips": self.nr_flips,
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "graph": copy.deepcopy(self.graph),
                    "iteration": iteration,
                    "action": "SAT walksat"
                }
                self.problem_data.append(self.state)
                return "SAT"
            
            clause_index = self.select_unsat_clause()
            max_break_count_index, min_break_count_index = self.select_variable(clause_index)

            probability = random.random()
            if probability <= self.p:
                variable = self.formula.formula[clause_index].literals[max_break_count_index]
                self.nr_flips +=1
                assignments = self.get_assignments()
                self.graph = build_walksat_graph(self.nodes, self.edges, assignments)
                self.state = {
                    "clauses": list(self.clauses),
                    "probability": self.p,
                    "nr_flips": self.nr_flips,
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "graph": copy.deepcopy(self.graph),
                    "iteration": iteration,
                    "variable": variable,
                    "break-count": "max",
                    "action": "FlipVariable max"
                }
                self.problem_data.append(self.state)
            else:
                assignments = self.get_assignments()
                self.graph = build_walksat_graph(self.nodes, self.edges, assignments)
                self.nr_flips +=1
                variable = self.formula.formula[clause_index].literals[min_break_count_index]
                self.state = {
                    "clauses": list(self.clauses),
                    "probability": self.p,
                    "nr_flips": self.nr_flips,
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "graph": copy.deepcopy(self.graph),
                    "iteration": iteration,
                    "variable": variable,
                    "break-count": "min",
                    "action": "FlipVariable min"
                }
                self.problem_data.append(self.state)      
            
            self.flip_variable(variable)

        assignments = self.get_assignments()
        self.graph = build_walksat_graph(self.nodes, self.edges, assignments)
        self.state = {
                    "clauses": list(self.clauses),
                    "probability": self.p,
                    "nr_flips": self.nr_flips,
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "graph": copy.deepcopy(self.graph),
                    "iteration": iteration,
                    "action": "UNSAT walksat"
                }
        self.problem_data.append(self.state)
        return "UNSAT"


    def get_solution(self, clauses):
        reset = 1
        result = "UNSAT"
        while result == "UNSAT" and reset > 0:
            try:
                walksat = WalkSAT(clauses)
                walksat.init_GUI()
                result = walksat.solve_with_GUI()
            except:
                result = "UNSAT"
            reset -=1
        return result, walksat.problem_data

        
'''
w = WalkSAT(clauses)
result, data = w.get_solution(clauses)
print(result)
print(data)
'''
 
 