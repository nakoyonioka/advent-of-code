import os
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/inputs.txt', 'r') as fd:
    inputs=[]
    for line in fd:
        inputs.append([x for x in line.split()])

for i in inputs:
    i[1]=int(i[1])

horizontal=0
vertical=0

for i in inputs:
    if(i[0]=='forward'):
        horizontal=horizontal+i[1]
    elif (i[0]=='down'):
        vertical=vertical+i[1]
    elif (i[0]=='up'):
        vertical=vertical-i[1]
    
print(horizontal, vertical)
print(horizontal*vertical)