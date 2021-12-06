import os
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/inputs.txt', 'r') as fd:
    inputs=[]
    for line in fd:
        inputs.append(line.rstrip())
    
from itertools import takewhile, dropwhile
iteri=iter(inputs)
inputs=[[e] + list(takewhile(lambda e: e != "", iteri)) for e in iteri if e != ""]

numbers=inputs[0]
inputs=list(inputs[1:])


# inputs=np.array(inputs)
# numbers=np.array(numbers)
numbers=list(numbers[0].split())[0].split(',')

#print(numbers[0])
#print(inputs)

def check_mat(mat):
    total=0
    for n in range(5):
        for m in range(5):
            if(mat[n][m]=='x'):
                total=total+1
            else:
                total=0
        if(total==5):
            return 1
    total=0
    for n in range(5):
        for m in range(5):
            if(mat[m][n]=='x'):
                total=total+1
            else:
                total=0
        if(total==5):
            return 1
    return -1

for n in range(len(inputs)):
    for m in range(5):
        inputs[n][m]=inputs[n][m].split()

board=[]
board_x=[]

import copy
index=0;
clean_in=copy.deepcopy(inputs)

for n in range(len(numbers)):
    for w in inputs:
        for l in w:
            for i,j in enumerate (l):
                if(j==numbers[n]):
                    l[i]='x'
        temp=check_mat(w)
        if(temp!=-1):
            board=w
            board_x.append(n)
        if(len(board)>0):
            break;
    if(len(board)>0):
        break;
    index+=1

total=0
for n in board:
    for i in n:
        if(i!='x'):
            total=total+int(i)

number=board_x[0]
number=int(numbers[number])
total=int(total)*number

print(total)
