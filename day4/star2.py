import os
import numpy as np
from numpy.core.numeric import binary_repr
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

numbers=list(numbers[0].split())[0].split(',')

for n in range(len(inputs)):
    for m in range(5):
        inputs[n][m]=inputs[n][m].split()

for mat in inputs:
    for l in mat:
        for i in range(len(l)):
            l[i]=int(l[i])
        l=np.array(l)

for n in range(len(numbers)):
    numbers[n]=int(numbers[n])

#print(numbers)
# print((inputs[0][0]))

# print(np.sum(inputs[0][0]))

def check_mat(board):
    wonRow=True
    for n in range(5):
        wonRow=True
        for m in range(5):
            if(board[n][m]!='x'):
                wonRow=False
        if(wonRow):
            return 1
    
    wonColumn=True
    for n in range(5):
        wonColumn=True
        for m in range(5):
            if(board[m][n]!='x'):
                wonColumn=False
        if(wonColumn):
            return 1

    return -1


removed=[]
bingo_nums=[]
mat=-1

for num in range(len(numbers)):
    for i in range(len(inputs)):
        
        for n in range(5):
            for m in range(5):
                if(inputs[i][n][m]==numbers[num]):
                    inputs[i][n][m]='x'

        mat=check_mat(inputs[i])

        if(mat==1):
            removed.append(inputs[i])
            inputs[i]=[['100','100','100','100','100'],['100','100','100','100','100'],['100','100','100','100','100'],['100','100','100','100','100'],['100','100','100','100','100']]
            bingo_nums.append(numbers[num])
            mat=-1

    
total=0

for board in removed[len(removed)-1]:
    for num in board:
        if(num!='x'):
            total=total+num

total=total*bingo_nums[len(removed)-1]
print(total)
