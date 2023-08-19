from dimacs_to_data import get_data
from formula import Formula
from implication_graph import ImplicationGraph
import random
import copy

#Example

''' 
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

#nvars, clauses = get_data('uf50-01.cnf')
#nvars, clauses = get_data('uuf50-01.cnf')
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
clauses = [[1],
           [-1, -2],
           [-1, 2]]
nvars = 3
'''

class CDCL():
    def __init__(self, clauses, nvars) -> None:
        self.nvars = nvars
        self.clauses = clauses
        self.formula = Formula(clauses)
        self.original_formula = Formula(clauses)
        self.decisions = []     #list of dictionaries
        self.decision_level = -1
        self.graph = ImplicationGraph()
        self.problem_data = []  #list with all data necessary for GUI
        self.state = dict()     #every state of the problem will be stored in problem_data; used for GUI

    
    def pick_branching_variable(self):
        self.decision_level += 1
        #pick a random unassigned variable from formula and assign True of False
        variable = random.choice(self.formula.unassigned_vars)
        assignment = random.choice([1, -1])
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
        elif variable < 0:  #if literal is negated
            self.decisions.append({-variable:-assignment})
        
        return variable, assignment  #returned values are used only for GUI
 

    def unit_propagation(self):
        conflict_literal = 0
        repeat = True
        while repeat == True:
            repeat = False
            for clause in self.formula.formula:
                #print("CC: ", clause.literals, ' ', clause.literals_values, ' ', clause.is_unit_clause())
                if clause.is_unit_clause():
                    #print("CLASUE: ", clause.literals)
                    repeat = True
                    #Find the unassigned literal
                    unassigned_literal = 0     #we'll add the unassigned literal to implication graph
                    parents = []               #list of parents for unassigned literal that we'll add in implication graph
                    for i in range(clause.size):
                        if clause.literals_values[i] == 0: #if this is the unassigned literal, then assign value True
                            unassigned_literal = clause.literals[i]
                            #print("UNASSIGNED: ", unassigned_literal)
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
                                if self.decision_level == -1:
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
    

    def add_new_clause(self, literal):  #add new clause with negated parents of literal parameter
        parents = self.graph.get_parents(literal)
        parents2 = self.graph.get_parents(-literal)
        parents = list(set(parents + parents2))
        #print("PARENTS: ", parents)
        ''' 
        for parent in parents:       #if in clause we have x and -x we remove one of them
            if -parent in parents:
                parents.remove(parent)
        '''
        for parent in parents:                                        #<Modificare 23.5 15:43
            #if parent in parents and parent not in self.graph.graph.keys():
            #    parents.remove(parent)
            
            if -parent in parents:                  #daca apare x si -x elimin una dintre ele
                #if parent in self.graph.graph.keys():
                parents.remove(-parent)
            

        #print("PARENTS2: ", parents)
       # print("DECISIONS: ", self.decisions)
 
        '''
        for i in range(len(parents)):
            parents[i] = -parents[i]
        '''
        for i in range(len(parents)):
            if parents[i] in self.graph.graph.keys():
                parents[i] = -parents[i]


        #if parents in self.clauses:   #if the new clause already exists in clauses the return "UNSAT"
        #    return -100, parents      #-100 is a code meaning UNSAT, functions returns the new clause for the GUI
        parents_set = set(parents)
        for clause in self.clauses:
            if parents_set == set(clause):
                return -100, parents

        
        self.clauses.append(parents)
        return 1, parents             #1 = everything is ok

    
    def flip_decision(self, variable, assignment):
        #print("FLIP: ", variable, assignment)
        #self.decisions[self.decision_level] = dict()
        #self.graph.back_jump(self.decision_level-1)
        self.construct_formula_from_decision_level(self.decision_level)
        #print("FLIP GRAPH: ", self.graph.graph)
        
        #print("PREV DECISIONS: ", self.decisions)
        self.decisions[self.decision_level][variable] = -assignment
        #print("NEW DECISIONS: ", self.decisions)
        #self.construct_formula_from_decision_level(self.decision_level)
    

    def first_assigned_variable_level(self, literal):
        parents = self.graph.get_parents(literal)
        parents2 = self.graph.get_parents(-literal)
        parents = list(set(parents + parents2))
 
        if parents == []:      #conflict cannot be resolved
            lowest_level = 0
        else:
            if parents[0] in self.graph.graph.keys():
                lowest_level = self.graph.graph[parents[0]][1]
            elif -parents[0] in self.graph.graph.keys(): 
                lowest_level = self.graph.graph[-parents[0]][1]
            else: 
                lowest_level = 0
    
        for parent in parents:
            if parent in self.graph.graph.keys():
                if self.graph.graph[parent][1] < lowest_level:
                    lowest_level = self.graph.graph[parent][1]
            elif -parent in self.graph.graph.keys():
                if self.graph.graph[-parent][1] < lowest_level:
                    lowest_level = self.graph.graph[-parent][1]

        return lowest_level


    def construct_formula_from_decision_level(self, decision_level):
        last_picked_variable = list(self.decisions[len(self.decisions)-1])[0]
        assignment = -self.decisions[len(self.decisions)-1][last_picked_variable]
        #self.decisions[len(self.decisions)-1] = {last_picked_variable: assignment}

        if assignment == 1:
            self.graph.add_node(last_picked_variable, 0, decision_level, "arbitrary_decision")
        elif assignment == -1:
             self.graph.add_node(-last_picked_variable, 0, decision_level, "arbitrary_decision")

        self.formula.update_assignment_of_all_occurrences(last_picked_variable, assignment)  
        self.formula.update_unassigned_vars(last_picked_variable)

        #Update decisions list
        if last_picked_variable > 0:    #if literal is not negated
            self.decisions[len(self.decisions)-1] = {last_picked_variable: assignment}
        elif last_picked_variable < 0:  #if literal is negated
            self.decisions[len(self.decisions)-1] = {-last_picked_variable: -assignment}


        #if decision_level != -100:             #if function flip_decision was not called
        self.decision_level = decision_level
        self.formula.__init__(self.clauses)    #reset formula
        self.unit_propagation()
        ###########################################################<----------------------------DE ADAUGAT STATE
        for i in range(decision_level+1):     #for i in range(decision_level + 1):     <modificat pe 23.5 13:14 
            for variable in self.decisions[i]:
                assignment = self.decisions[i][variable]
                #if variable not in self.graph.graph.keys() and -variable not in self.graph.graph.keys():     ####<NU STIU DACA E BUAN CONFITIA
                self.formula.update_assignment_of_all_occurrences(variable, assignment)
                #Update unsassigned vars
                self.formula.update_unassigned_vars(variable)
        #Update self.decisions
        if decision_level != -100:
            self.decisions = self.decisions[:decision_level + 1]
  


    def solve(self):
        self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.decisions),
                        "decision_level": self.decision_level,
                        "graph": copy.deepcopy(self.graph),
                        "back_jump_level": None,
                        "conflict": None,
                        "new_clause": None,
                        "variable": None,
                        "assignment": None,
                        "action": "Init"
                    }
        self.problem_data.append(self.state)

        k = 100
        while len(self.formula.unassigned_vars)>0:
            conflict = self.unit_propagation()

            self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.decisions),
                        "decision_level": self.decision_level,
                        "graph": copy.deepcopy(self.graph),
                        "back_jump_level": None,
                        "conflict": conflict,
                        "new_clause": None,
                        "variable": None,
                        "assignment": None,
                        "action": "UnitPropagation"
                    }
            self.problem_data.append(self.state)


            while conflict != 0: #conflict found
                back_jump_level = self.first_assigned_variable_level(conflict)

                self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.decisions),
                        "decision_level": self.decision_level,
                        "graph": copy.deepcopy(self.graph),
                        "back_jump_level": back_jump_level,
                        "conflict": conflict,
                        "new_clause": None,
                        "variable": None,
                        "assignment": None,
                        "action": "BackJump"
                    }
                self.problem_data.append(self.state)


                result, new_clause = self.add_new_clause(conflict)

                self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.decisions),
                        "decision_level": self.decision_level,
                        "graph": copy.deepcopy(self.graph),
                        "back_jump_level": back_jump_level,
                        "conflict": conflict,
                        "new_clause": new_clause,
                        "variable": None,
                        "assignment": None,
                        "action": "AddNewClause"
                    }
                self.problem_data.append(self.state)

                if result == -100:         #function tried to add an already existing clause, this means formula is UNSAT   
                    self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.decisions),
                        "decision_level": self.decision_level,
                        "graph": copy.deepcopy(self.graph),
                        "back_jump_level": None,
                        "conflict": None,
                        "new_clause": None,
                        "variable": None,
                        "assignment": None,
                        "action": "AddAlreadyExistingClause"
                    }
                    self.problem_data.append(self.state)

                    return "UNSAT"


                self.graph.back_jump(back_jump_level)
                self.construct_formula_from_decision_level(back_jump_level)

                self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.decisions),
                        "decision_level": self.decision_level,
                        "graph": copy.deepcopy(self.graph),
                        "back_jump_level": None,
                        "conflict": None,
                        "new_clause": None,
                        "variable": None,
                        "assignment": None,
                        "action": "ConstructFormula"
                    }
                self.problem_data.append(self.state)
    
                conflict = self.unit_propagation()

                self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.decisions),
                        "decision_level": self.decision_level,
                        "graph": copy.deepcopy(self.graph),
                        "back_jump_level": None,
                        "conflict": conflict,
                        "new_clause": None,
                        "result": None,
                        "variable": None,
                        "assignment": None,   
                        "action": "UnitPropagation"
                    }
                self.problem_data.append(self.state)

            if len(self.formula.unassigned_vars)>0:  #this is is to avoid exception for random.choice(seq) when seq is empty
                variable, assignment = self.pick_branching_variable()
                self.state = {
                        "clauses": list(self.clauses),
                        "literals_values": copy.deepcopy(self.formula.formula),
                        "decisions": list(self.decisions),
                        "decision_level": self.decision_level,
                        "graph": copy.deepcopy(self.graph),
                        "back_jump_level": None,
                        "conflict": conflict,
                        "new_clause": None,
                        "result": None,
                        "variable": variable,
                        "assignment": assignment,   
                        "action": "PickBranchingVariable"
                    }
                self.problem_data.append(self.state)

            k-=1
        if k > 0 and self.formula.all_true() == 1:   
            self.state = {
                    "clauses": list(self.clauses),
                    "literals_values": copy.deepcopy(self.formula.formula),
                    "decisions": list(self.decisions),
                    "decision_level": self.decision_level,
                    "graph": copy.deepcopy(self.graph),
                    "back_jump_level": None,
                    "conflict": conflict,
                    "new_clause": None,
                    "result": None,
                    "variable": None,
                    "assignment": None,   
                    "action": "SAT"
                        }
            self.problem_data.append(self.state)
            return "SAT"
        
        
        self.state = {
                "clauses": list(self.clauses),
                "literals_values": copy.deepcopy(self.formula.formula),
                "decisions": list(self.decisions),
                "decision_level": self.decision_level,
                "graph": copy.deepcopy(self.graph),
                "back_jump_level": None,
                "conflict": conflict,
                "new_clause": None,
                "result": None,
                "variable": None,
                "assignment": None,   
                "action": "UNSAT"
                        }
        self.problem_data.append(self.state)
     
        return "UNSAT"

    
    def get_solution(self, clauses, nvars):
        reset = 1
        result = "UNSAT"
        while result == "UNSAT" and reset > 0:
            try:
                cdcl = CDCL(clauses, nvars)
                result = cdcl.solve()
            except:
                result = "UNSAT"
            reset -=1
        return result, cdcl.problem_data


'''
cdcl = CDCL(list(clauses), nvars) 
#result, problem_data = cdcl.get_solution()
#print(result, len(problem_data))

cdcl.decision_level += 1
variable, assignment = 1, 1
if assignment == 1:
    cdcl.graph.add_node(variable, 0, cdcl.decision_level, "arbitrary_decision")  
elif assignment == -1:
    cdcl.graph.add_node(-variable, 0, cdcl.decision_level, "arbitrary_decision")

cdcl.formula.update_assignment_of_all_occurrences(variable, assignment)  
cdcl.formula.update_unassigned_vars(variable)

#Update decisions list
if variable > 0:    #if literal is not negated
    cdcl.decisions.append({variable:assignment})
elif variable < 0:  #if literal is negated
    cdcl.decisions.append({-variable:-assignment})

conflict = cdcl.unit_propagation()



for c in cdcl.formula.formula:
    print(c.literals)
print()
for c in cdcl.formula.formula:
    print(c.literals_values)
          
print("CONFLICT: ", conflict)
print("GRAPH: ", cdcl.graph.graph)
print("DECISIONS: ", cdcl.decisions)



back_jump_level = cdcl.first_assigned_variable_level(conflict)
print("BACKJUMP: ", back_jump_level)

result, new_clause = cdcl.add_new_clause(conflict)
print("RESULT, NEW CLAUSE", result, new_clause)

print("GRAPH: ", cdcl.graph.graph)
print("DECISIONS BEFORE CONSTRUCT: ", cdcl.decisions)
print("UNASSIGNED VARAIBLES: ", cdcl.formula.unassigned_vars)
cdcl.graph.back_jump(back_jump_level)
cdcl.construct_formula_from_decision_level(back_jump_level)
print()
print("GRAPH AFTER CONSTRUCT: ", cdcl.graph.graph)
print()
print("DECISIONS AFTER CONSTRUCT: ", cdcl.decisions)
print("CONSTRUCT:")
for c in cdcl.formula.formula:
    print(c.literals)
print()
for c in cdcl.formula.formula:
    print(c.literals_values)
print()
 

conflict = cdcl.unit_propagation()
print("CONFLICT2:", conflict)
for c in cdcl.formula.formula:
    print(c.literals_values)
 
print("REZ: ", cdcl.formula.all_true())

print("------------------------------")



cdcl.decision_level += 1
variable, assignment = 4, 1
if assignment == 1:
    cdcl.graph.add_node(variable, 0, cdcl.decision_level, "arbitrary_decision")  
elif assignment == -1:
        cdcl.graph.add_node(-variable, 0, cdcl.decision_level, "arbitrary_decision")

cdcl.formula.update_assignment_of_all_occurrences(variable, assignment)  
cdcl.formula.update_unassigned_vars(variable)

#Update decisions list
if variable > 0:    #if literal is not negated
    cdcl.decisions.append({variable:assignment})
elif variable < 0:  #if literal is negated
    cdcl.decisions.append({-variable:-assignment})

conflict = cdcl.unit_propagation()



for c in cdcl.formula.formula:
    print(c.literals)
print()
for c in cdcl.formula.formula:
    print(c.literals_values)
          
print("CONFLICT: ", conflict)

print("GRAPH: ", cdcl.graph.graph)
print("DECISION: ", cdcl.decisions) 
 

conflict = cdcl.unit_propagation()
print("CONFLICT2:", conflict)
for c in cdcl.formula.formula:
    print(c.literals_values)
 
print("-------------------------------")

 
cdcl.decision_level += 1
variable, assignment = 10, -1
if assignment == 1:
    cdcl.graph.add_node(variable, 0, cdcl.decision_level, "arbitrary_decision")  
elif assignment == -1:
        cdcl.graph.add_node(-variable, 0, cdcl.decision_level, "arbitrary_decision")

cdcl.formula.update_assignment_of_all_occurrences(variable, assignment)  
cdcl.formula.update_unassigned_vars(variable)

#Update decisions list
if variable > 0:    #if literal is not negated
    cdcl.decisions.append({variable:assignment})
elif variable < 0:  #if literal is negated
    cdcl.decisions.append({-variable:-assignment})

conflict = cdcl.unit_propagation()



for c in cdcl.formula.formula:
    print(c.literals)
print()
for c in cdcl.formula.formula:
    print(c.literals_values)
          
print("CONFLICT: ", conflict)

print("GRAPH: ", cdcl.graph.graph)
print("DECISION: ", cdcl.decisions) 
 

conflict = cdcl.unit_propagation()
print("CONFLICT2:", conflict)
for c in cdcl.formula.formula:
    print(c.literals_values)
 
print("-------------------------------")

 
cdcl.decision_level += 1
variable, assignment = 3, 1
if assignment == 1:
    cdcl.graph.add_node(variable, 0, cdcl.decision_level, "arbitrary_decision")  
elif assignment == -1:
        cdcl.graph.add_node(-variable, 0, cdcl.decision_level, "arbitrary_decision")

cdcl.formula.update_assignment_of_all_occurrences(variable, assignment)  
cdcl.formula.update_unassigned_vars(variable)

#Update decisions list
if variable > 0:    #if literal is not negated
    cdcl.decisions.append({variable:assignment})
elif variable < 0:  #if literal is negated
    cdcl.decisions.append({-variable:-assignment})

conflict = cdcl.unit_propagation()



for c in cdcl.formula.formula:
    print(c.literals)
print()
for c in cdcl.formula.formula:
    print(c.literals_values)
          
print("CONFLICT: ", conflict)

print("GRAPH: ", cdcl.graph.graph)
print("DECISION: ", cdcl.decisions) 
 

conflict = cdcl.unit_propagation()
print("CONFLICT2:", conflict)
for c in cdcl.formula.formula:
    print(c.literals_values)
 

print("-------------------------------")

 
cdcl.decision_level += 1
variable, assignment = 7, 1
if assignment == 1:
    cdcl.graph.add_node(variable, 0, cdcl.decision_level, "arbitrary_decision")  
elif assignment == -1:
        cdcl.graph.add_node(-variable, 0, cdcl.decision_level, "arbitrary_decision")

cdcl.formula.update_assignment_of_all_occurrences(variable, assignment)  
cdcl.formula.update_unassigned_vars(variable)

#Update decisions list
if variable > 0:    #if literal is not negated
    cdcl.decisions.append({variable:assignment})
elif variable < 0:  #if literal is negated
    cdcl.decisions.append({-variable:-assignment})

conflict = cdcl.unit_propagation()



for c in cdcl.formula.formula:
    print(c.literals)
print()
for c in cdcl.formula.formula:
    print(c.literals_values)
          
print("CONFLICT: ", conflict)

print("GRAPH: ", cdcl.graph.graph)
print("DECISION: ", cdcl.decisions) 
 

back_jump_level = cdcl.first_assigned_variable_level(conflict)
print("BACKJUMP: ", back_jump_level)

result, new_clause = cdcl.add_new_clause(conflict)
print("RESULT, NEW CLAUSE", result, new_clause)

print("GRAPH: ", cdcl.graph.graph)
print("DECISIONS BEFORE CONSTRUCT: ", cdcl.decisions)
print("UNASSIGNED VARAIBLES: ", cdcl.formula.unassigned_vars)
cdcl.graph.back_jump(back_jump_level)
cdcl.construct_formula_from_decision_level(back_jump_level)
print()
print("GRAPH AFTER CONSTRUCT: ", cdcl.graph.graph)
print()
print("DECISIONS AFTER CONSTRUCT: ", cdcl.decisions)
print("CONSTRUCT:")
for c in cdcl.formula.formula:
    print(c.literals)
print()
for c in cdcl.formula.formula:
    print(c.literals_values)
print()

conflict = cdcl.unit_propagation()

print("CONFLICT2:", conflict)

back_jump_level = cdcl.first_assigned_variable_level(conflict)
print("BACKJUMP: ", back_jump_level)

result, new_clause = cdcl.add_new_clause(conflict)
print("RESULT, NEW CLAUSE", result, new_clause)

print("GRAPH: ", cdcl.graph.graph)
cdcl.graph.back_jump(back_jump_level)
cdcl.construct_formula_from_decision_level(back_jump_level)
print("GRAPH: ", cdcl.graph.graph)
print("CONSTRUCT:")
for c in cdcl.formula.formula:
    print(c.literals)
print()

for c in cdcl.formula.formula:
    print(c.literals_values)
 
print("DECISIONS AFTER UNIT PROP: ", cdcl.decisions)
print("GRAPH AFTER UNIT PROP: ", cdcl.graph.graph)


conflict = cdcl.unit_propagation()

print("CONFLICT3:", conflict)

print("-------------------------------")

cdcl.decision_level += 1
variable, assignment = 12, 1
if assignment == 1:
    cdcl.graph.add_node(variable, 0, cdcl.decision_level, "arbitrary_decision")  
elif assignment == -1:
    cdcl.graph.add_node(-variable, 0, cdcl.decision_level, "arbitrary_decision")

cdcl.formula.update_assignment_of_all_occurrences(variable, assignment)  
cdcl.formula.update_unassigned_vars(variable)

#Update decisions list
if variable > 0:    #if literal is not negated
    cdcl.decisions.append({variable:assignment})
elif variable < 0:  #if literal is negated
    cdcl.decisions.append({-variable:-assignment})

conflict = cdcl.unit_propagation()



for c in cdcl.formula.formula:
    print(c.literals)
print()
for c in cdcl.formula.formula:
    print(c.literals_values)
          
print("CONFLICT: ", conflict)
print("GRAPH: ", cdcl.graph.graph)
print("DECISIONS: ", cdcl.decisions)

 

conflict = cdcl.unit_propagation()
print("CONFLICT2:", conflict)
for c in cdcl.formula.formula:
    print(c.literals_values)
 
print("------------------------------")

'''