import os
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path+'/inputs.txt', 'r') as fd:
    second_o=[]
    second_c=[]
    for line in fd:
        second_o.append([x for x in line.split()])
        second_c.append([x for x in line.split()])


totalo=[0,0,0,0,0,0,0,0,0,0,0,0]
totalc=[0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(totalo)):
    temp2=second_c
    temp=second_o
    for w in temp:
        if(w[0][i]=='0'):
            totalo[i]=totalo[i]-1
        if(w[0][i]=='1'):
            totalo[i]=totalo[i]+1
    for w in temp2:
        if(w[0][i]=='0'):
            totalc[i]=totalc[i]-1
        if(w[0][i]=='1'):
            totalc[i]=totalc[i]+1
    second_o=[] 
    second_c=[]
    if(len(temp2)>1):
        if(totalc[i]<0):
            for w in temp2:
                if(w[0][i]=='1'):
                    second_c.append(w)
        else:
            for w in temp2:
                if(w[0][i]=='0'):
                    second_c.append(w)
    else:
        second_c=temp2;
    
    if(len(temp)>1):
        if(totalo[i]<0):
            for w in temp:
                if(w[0][i]=='0'):
                    second_o.append(w)
        else:
            for w in temp:
                if(w[0][i]=='1'):
                    second_o.append(w)
    else:
        second_o=temp;
    
print(totalo)
print(totalc)
print(second_c, temp2)
print(second_o, temp)
oxygen=second_o[0][0]
co2=second_c[0][0]

oxygen=int(oxygen,2)
co2=int(co2,2)

print(oxygen, co2)
print(oxygen*co2)