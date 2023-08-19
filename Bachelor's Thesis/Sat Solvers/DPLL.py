from formula import Formula
from implication_graph import ImplicationGraph
import random
import copy

#Example
 
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
nvars = 12

''' 
clauses = [[-1, -2],
           [-1, 3],
           [-3, -4],
           [2, 4, 5],
           [-5, 6, -7],
           [2, 7, 8],
           [-8, -9],
           [-8, 10],
           [9, -10, 11],
           [-10, -12],
           [-11, 12],]
nvars = 12
''' 

'''
clauses = [[1, 2, 3],
        [1, 2, -3],
        [1, -2, 3],
        [1, -2, -3],
        [-1, 2, 3],
        [-1, 2, -3],
        [-1, -2, 3],
        [-1, -2, -3]]
nvars = 3
'''

class DPLL():
    all_decisions = []                   #list of dictionaries with all decisions; used for GUI; it is static
    problem_data = [{"decisions": [], "literals_values": [], "clauses": [], "action": "Init"}]  #list with all data necessary for GUI
    iteration = 0

    def __init__(self, clauses, nvars) -> None:
        self.nvars = nvars
        self.clauses = clauses
        self.formula = Formula(clauses)
        self.original_formula = Formula(clauses)
        self.decisions = []     #list of dictionaries
        self.decision_level = -1
        self.graph = ImplicationGraph()
        self.state = dict()                       #every state of the problem will be stored in problem_data; used for GUI


    
    def pick_branching_variable(self):
        self.decision_level += 1
        #variable = 0
        #pick a random unassigned variable from formula and assign True of False
        #if(len(self.formula.unassigned_vars)):
        variable = random.choice(self.formula.unassigned_vars)
        assignment = random.choice([1, -1])
        #assignment = -1
        #print(variable, self.formula.unassigned_vars)
        return variable, assignment  #returned values are used only for GUI
    

    def update_after_picking_variable(self, variable, assignment):
        #add variable to implication graph
        if assignment == 1:
            self.graph.add_node(variable, 0, self.decision_level, "arbitrary_decision")  #parent = 0 means this node doesen't have a parent
                                                                                         #only nodes added during unit propagation have a parent
        elif assignment == -1:
             self.graph.add_node(-variable, 0, self.decision_level, "arbitrary_decision")

        self.formula.update_assignment_of_all_occurrences(variable, assignment)  
        self.formula.update_unassigned_vars(variable)

        #Update decisions list
        if variable > 0:    #if literal is not negated
            self.decisions.append({variable:assignment})
            DPLL.all_decisions.append({variable:assignment})
        elif variable < 0:  #if literal is negated
            self.decisions.append({-variable:-assignment})
            DPLL.all_decisions.append({-variable:-assignment})

        return self

    def pure_literal_elimination(self):
        out = []
        for i in range(len(self.formula.unassigned_vars)):
            var = self.formula.unassigned_vars[i]
            assignment = 0
            literal = 0
            if self.formula.is_pure(var):
                #assign value such as literal will be true
                for clause in self.formula.formula:
                    for l in clause.literals:
                        if var == l:
                            literal = l
                            if var > 0:
                                assignment = 1
                            else:
                                assignment = -1
                            self.formula.update_assignment_of_all_occurrences(literal, assignment)  
                            if literal > 0:    #if literal is not negated
                                self.decisions.append({literal:assignment})
                                DPLL.all_decisions.append({literal:assignment})
                            elif literal < 0:  #if literal is negated
                                self.decisions.append({-literal:-assignment})
                                DPLL.all_decisions.append({-literal:-assignment})
                            out.append((literal, assignment))
                        elif var == -l:
                            literal = -l
                            if var > 0:
                                assignment = -1
                            else:
                                assignment = 1
                            self.formula.update_assignment_of_all_occurrences(literal, assignment)  
                            if literal > 0:    #if literal is not negated
                                self.decisions.append({literal:assignment})
                                DPLL.all_decisions.append({literal:assignment})
                            elif literal < 0:  #if literal is negated
                                self.decisions.append({-literal:-assignment})
                                DPLL.all_decisions.append({-literal:-assignment})
                            out.append((literal, assignment))
        
        for literal in out:
            self.formula.update_unassigned_vars(literal[0])
        return out
            
                        
    def unit_propagation(self):
        conflict_literal = 0
        repeat = True
        while repeat == True:
            repeat = False
            for clause in self.formula.formula:
                if clause.is_unit_clause():
                    repeat = True
                    #Find the unassigned literal
                    unassigned_literal = 0     #we'll add the unassigned literal to implication graph
                    parents = []               #list of parents for unassigned literal that we'll add in implication graph
                    for i in range(clause.size):
                        if clause.literals_values[i] == 0: #if this is the unassigned literal, then assign value True
                            unassigned_literal = clause.literals[i]
                            conflict = self.formula.find_conflict()
                            if conflict != 0:    #we found a conflict
                                conflict_literal = conflict 

                            self.formula.update_assignment_of_all_occurrences(clause.literals[i], 1)
                            self.formula.update_unassigned_vars(clause.literals[i])
                            
                            if clause.literals[i] < 0:  
                                if self.decision_level == -1:
                                    self.decisions.append({-clause.literals[i] : -1}) 
                                else:                    
                                    self.decisions[self.decision_level][-clause.literals[i]] = -1  #update list of decisions
                            else:
                                if self.decision_level == -1 or self.decision_level >= len(self.decisions):
                                    self.decisions.append({clause.literals[i] : 1}) 
                                else:   
                                    self.decisions[self.decision_level][clause.literals[i]] = 1

                        else: #if the literal is assigned then it is the parent for the unassigned literal in implication graph
                            if clause.literals[i] in self.graph.graph.keys():
                                parents.append(clause.literals[i])
                            elif -clause.literals[i] in self.graph.graph.keys():
                                parents.append(-clause.literals[i])
                    #add unassigned literal to implication graph
                   # print("UNASSIGNED: ", unassigned_literal, " PARENTS: ", parents)
                    self.graph.add_node(unassigned_literal, parents, self.decision_level, "forced_assignment")

        #Search for clause that has all literals assigned to False because it is in a conflict
 
        
        for clause in self.formula.formula:
            if clause.get_value() == -1:
                parents = []
                for literal in clause.literals:
                    if literal != -conflict_literal:
                        parents.append(literal)
                if conflict_literal != 0 and parents != []:        
                    self.graph.add_node(-conflict_literal, parents, self.decision_level, "forced_assignment")
        return conflict_literal
            
    def solve(self):      
        DPLL.iteration +=1
        self.unit_propagation()

        self.state = {
                    "clauses": list(self.clauses),
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "decisions": list(self.all_decisions),
                    "graph": copy.deepcopy(self.graph),
                    "variable": None,
                    "assignment": None,
                    "action": "UnitPropagation"
                    }
        DPLL.problem_data.append(self.state)

        if self.pure_literal_elimination() != []:
            self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.all_decisions),
                        "graph": copy.deepcopy(self.graph),
                        "variable": None,
                        "assignment": None,
                        "action": "PureLiteralElimination"
                        }
            DPLL.problem_data.append(self.state)

        if self.formula.all_true() == 1:
            DPLL.all_decisions.append({"SAT":None})
            self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.all_decisions),
                        "graph": copy.deepcopy(self.graph),
                        "variable": None,
                        "assignment": None,
                        "action": "SAT"
                        }
            DPLL.problem_data.append(self.state)   
            return True
        
        if self.formula.all_true() == -1:
            DPLL.all_decisions.append({"UNSAT":None})   
            self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.all_decisions),
                        "graph": copy.deepcopy(self.graph),
                        "variable": None,
                        "assignment": None,
                        "action": "UNSAT"
                        }
            DPLL.problem_data.append(self.state)
            return False
        if len(self.formula.unassigned_vars) == 0:
            DPLL.all_decisions.append({"UNSAT":None})
            self.state = {
                    "clauses": list(self.clauses),
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "decisions": list(self.all_decisions),
                    "graph": copy.deepcopy(self.graph),
                    "variable": None,
                    "assignment": None,
                    "action": "UNSAT"
                    }
            DPLL.problem_data.append(self.state)    
            return False

        variable, assignment = self.pick_branching_variable()
        self.state = {
                    "clauses": list(self.clauses),
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "decisions": list(self.all_decisions),
                    "graph": copy.deepcopy(self.graph),
                    "variable": variable,
                    "assignment": assignment,
                    "action": "PickBranchingVariable"
                    }
        DPLL.problem_data.append(self.state)
        dpll2 = copy.deepcopy(self)

        return  self.update_after_picking_variable(variable, assignment).solve() or  dpll2.update_after_picking_variable(variable, -assignment).solve()
        

    def get_solution(self, clauses, nvars):
        reset = 1
        result = False
        while result == False and reset > 0:
            try:
                dpll = DPLL(clauses, nvars)
                result = dpll.solve()
            except:
                result = False
            reset -=1

        if result == True:
            result = "SAT"
        else:
            result = "UNSAT"
        return result, DPLL.problem_data
    
   

'''
dpll = DPLL(clauses, nvars)
print(dpll.formula.unassigned_vars)
print(dpll.pick_branching_variable())
for clause in dpll.formula.formula:
    print(clause.literals)
print()
for clause in dpll.formula.formula:
    print(clause.literals_values)

print(dpll.decisions)
print(dpll.pure_literal_elimination())
dpll.unit_propagation()
print()
for clause in dpll.formula.formula:
    print(clause.literals_values)
 
print(dpll.solve())
print(dpll.decisions)
for clause in dpll.formula.formula:
    print(clause.literals_values)

print(DPLL.all_decisions)
print(dpll.decisions)
print()
for i in DPLL.problem_data:
    print(i["action"])
'''