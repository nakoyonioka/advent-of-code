import os
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/inputs.txt', 'r') as fd:
    inputs=[]
    for line in fd:
        inputs.append([int(x) for x in line.split()])

total=0
for i in range(len(inputs)-1):
    if(inputs[i+1][0]>inputs[i][0]):
        total=total+1

print(total)