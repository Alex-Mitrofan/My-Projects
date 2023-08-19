from clause import Clause

class Formula():
    def __init__(self, clauses):
        #self.formula = [Clause(c) for c in clauses]
        self.formula = [Clause(clauses[i], i) for i in range(len(clauses))]
        self.size = len(clauses)
        self.unassigned_vars = []
        self.unassigned_clauses = []

        for clause in self.formula:
            for i in range(clause.size):
                #if clause.literals_values[i] == 0: #?
                if abs(clause.literals[i]) not in self.unassigned_vars:
                    #self.unassigned_vars.append((clause.literals[i], clause.index_in_formula, i))  
                    self.unassigned_vars.append(abs(clause.literals[i]))  

    def update_unassigned_vars(self, variable):
        for var in self.unassigned_vars:
            if var == variable:
                self.unassigned_vars.remove(var)
            if var == -variable:
                self.unassigned_vars.remove(var)

    def update_assignment_of_all_occurrences(self, variable, assignment):
        for clause in self.formula:
            for i in range(clause.size):
                if clause.literals[i] == variable:
                    clause.assign_literal(i, assignment)
                elif clause.literals[i] == -variable:
                    clause.assign_literal(i, -assignment)
            

    def find_conflict(self):
        unit_clause_literals = []  #unassigned literals from unit clauses
        for clause in self.formula:
            if clause.is_unit_clause():
                #Find the unassigned literal
                for i in range(clause.size):
                    if clause.literals_values[i] == 0: #if this is the unassigned literal, then search for conflict and append to list
                        for literal in unit_clause_literals:
                            if clause.literals[i] == -literal:
                                
                                return literal   #if there are 2 unit clauses with the same unassigned variable appearing negated in one clause
                                                 #and unnegated in the other one then we found a conflict
                        unit_clause_literals.append(clause.literals[i])
        return 0
    
    def all_true(self):
        for clause in self.formula:
            if clause.get_value() == -1:
                return -1
        for clause in self.formula:
            if clause.get_value() == 0:
                return 0
            
        return 1
    

    def is_pure(self, literal):
        ok = 0
        for clause in self.formula:
            for l in clause.literals:
                if literal == -l:
                    ok+=1
                if literal == l:
                    ok+=1
                if ok > 1:    #we found literal in positive and negative
                    return False
        return True