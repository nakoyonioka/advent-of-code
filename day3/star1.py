import os
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/inputs.txt', 'r') as fd:
    inputs=[]
    for line in fd:
        inputs.append([x for x in line.split()])

gama=''
epsilon=''
total=[0,0,0,0,0,0,0,0,0,0,0,0]

for w in inputs:
    for i in range(len(w[0])):
        if(w[0][i]=='0'):
            total[i]=total[i]-1
        if(w[0][i]=='1'):
            total[i]=total[i]+1

for i in total:
    if(i<0):
        gama=gama+'0'
        epsilon=epsilon+'1'
    else:
        gama=gama+'1'
        epsilon=epsilon+'0'

gama=int(gama,2)
epsilon=int(epsilon,2)
print(gama, epsilon)
print(gama*epsilon)
