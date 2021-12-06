import os
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/inputs.txt', 'r') as fd:
    inputs=[]
    for line in fd:
        inputs.append([int(x) for x in line.split()])

first=0
second=0
total=0
for i in range(len(inputs)):
    try:
        first=inputs[i][0]+inputs[i+1][0]+inputs[i+2][0]
        second=inputs[i+1][0]+inputs[i+2][0]+inputs[i+3][0]
        if(second>first):
            total=total+1
    except:
        print("End of index")

print(total)