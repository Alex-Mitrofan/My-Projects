class Clause():
    def __init__(self, clause, index_in_formula):
        self.literals = clause
        self.value = 0           #value of entire clause: 0=unassigned, 1=true, -1=false
        self.size = len(clause)  #number of unassigned variables
        self.nr_of_unassigned_literals = len(clause) 
        self.index_in_formula = index_in_formula
        self.literals_values = [0 for l in self.literals]    #0=unassigned, 1=true, -1=false
         
         

    def get_value(self):
        all_false = True
        for val in self.literals_values:
            if val == 1:       #if there is a literal with value 1 the clause is true
                self.value = 1
                return 1
            elif val == 0: 
                all_false = False

        if all_false == True:      #if all literals have value -1 clause is false
            self.value = -1          
            return -1
        return 0                   #clause has unassigned value
            

    def all_assigned(self):
        for val in self.literals_values:
            if val == 0:
                return 0
        return 1
    
    
    def is_unit_clause(self):
        true_literals = 0
        unassigned_literals = 0
        for value in self.literals_values:
            if value == 0:
                unassigned_literals += 1
            elif value == 1:
                true_literals += 1
        if unassigned_literals == 1 and true_literals == 0:
            return True
        return False
        '''
        if self.nr_of_unassigned_literals == 1 and self.get_value() == 0:
            return True
        else: 
            return False
        '''
            
    def assign_literal(self, index, value):
        #value 1=true, -1=false, 0 is by default
        self.literals_values[index] = value
        self.nr_of_unassigned_literals -= 1

    def get_literals_values(self):
        return self.literals_values
