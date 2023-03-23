import pickle, gzip
import numpy as np

with gzip.open('mnist.pkl.gz', 'rb') as fd:
    train_set, valid_set, test_set = pickle.load(fd, encoding='latin')


def random_weights():
    w =[0 for i in range(7840)] 
    w=np.array(w)
    for i in range(7840):
        w[i]  = np.random.randint(-100,100)
    w.reshape(784,10)
    return w


def target_array(n):
    t=[0 for i in range(10)]
    t = np.array(t)
    t[n] = 1
    return t

 
def activation(n):
    for i in range(10):
        if n[0][i]>0:
            n[0][i] = 1
        else:
            n[0][i] = 0
              
    n = np.array(n)
    return n

def generate_bias():
    b = [0 for i in range(10)]
    for i in range(10):
        b[i] = np.random.randint(-100,100)
    b = np.array(b)
    b = b.reshape(1,10)
    return b



#TRAINING

l = len(train_set[0])  #50000
nrIterations = 30
allClassified = False
w = random_weights()
w = w.reshape(784,10)
b = generate_bias()


 
while (not allClassified )and nrIterations>0:
    allClassified = True
    for i in range(l):

        x = np.array( train_set[0][i])        
        x = x.reshape(1,784) 

        z = x.dot(w) + b   #compute net input
        
        y = activation(z)  #output #classify the sample
                           #adjust the weights     
        t = train_set[1][i]  
        t = np.array(t)
        t = target_array(t)
        
        xT = np.transpose(x)
        w = w + (t - y)*xT*0.3

        b = b + (t-y)*0.3 #adjust the bias
        if not np.array_equal(y.reshape(10,1),t.reshape(10,1)):
            allClassified = False

    nrIterations-=1
 
#VALIDARE


l = len(valid_set[0])  #50000
nrIterations = 100
allClassified = False

while (not allClassified )and nrIterations>0:
    allClassified = True
    for i in range(l):

        x = np.array( valid_set[0][i])        
        x = x.reshape(1,784) 

        z = x.dot(w) + b   #compute net input
        
        y = activation(z)  #output #classify the sample
                            #adjust the weights     
        t = valid_set[1][i]  
        t = np.array(t)
        t = target_array(t)
        
        xT = np.transpose(x)
        w = w + (t - y)*xT*0.001

        b = b + (t-y)*0.001 #adjust the bias
        if not np.array_equal(y.reshape(10,1),t.reshape(10,1)):
            allClassified = False

    nrIterations-=1
 


#TEST
 
correct = 0
maybe_correct = 0
l = len(test_set[0])  #10000

 
for i in range(l):
    x = np.array( test_set[0][i])        
    x = x.reshape(1,784) 

    z = x.dot(w) + b   #compute net input
    
    y = activation(z)  #output #classify the sample
                    #adjust the weights     
  
    t = test_set[1][i]  
    t = np.array(t)
    t = target_array(t)
    if np.array_equal(y.reshape(10,1),t.reshape(10,1)):
        correct+=1
    else:
        n = test_set[1][i]
        y = y.reshape(10)
        z = z.reshape(10)
        max = 0
        pos = 0
        for j in range(10):
            if z[j]>max:
                max = z[j]
                pos = j           
        if y[pos] == 1 and t[pos] == 1:
            maybe_correct+=1

print(correct)
print(maybe_correct)
print(correct+maybe_correct) 