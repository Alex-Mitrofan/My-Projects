import tarfile 
import random
from CDCL import CDCL
from DPLL import DPLL
from WalkSAT import WalkSAT
import time
 

def get_data(content):
    clauses = []
    nvars = 0
    content = str(content.read()).replace(r"\n", "\n").split("\n")[1:]
  

    for line in content:
        if line.startswith('p'):
            l = line.split(" ")
            nr_vars = int(l[2])
        elif line.startswith(' '):  #first clause starts with ' '
            l = line[1:].split(" ")[:-1] 
            l = [int(i) for i in l]
            clauses.append(l)
        elif line != '':
            if  line[0] not in "c%0'\n'":
                l = line.split(" ")[:-1]
              
                l = [int(i) for i in l]
                clauses.append(l)

    return nvars, clauses 

 

def get_train_and_test_data(tar1: tarfile.TarFile) :
    data = []
    i = 0  
    
    for member in tar1.getmembers():
        file = tar1.extractfile(member)
    
        n, clauses = get_data(file)       
        data.append(clauses)
        i+=1
        if i == 1:
            break
 
    return data


tar = tarfile.open("flat2.gz", "r:gz")
data = get_train_and_test_data(tar)

results = []
times = []
iterations = []

for formula in data:
    start_time = time.time()
    DPLL.iteration = 0
    DPLL.all_decisions = []
    DPLL.problem_data = []
    dpll = DPLL(formula, 1)
    result,  iteration = dpll.get_solution(formula, 1)
    
    
    

    end_time = time.time()
    execution_time = end_time - start_time
    results.append(result)
    iterations.append(iteration)
    times.append(execution_time)
 
     
sat = 0     

for r in results:
    if r == "SAT":
        sat+=1

print("SAT: ", sat)
print("TIMES: ", times)
print()
print("ITER: ", iterations)