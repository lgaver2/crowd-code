import matplotlib.pyplot as plt
import numpy as np
from pip import main

field=np.zeros((1000,1000))
person=np.random.randint(0,999,2)
goal=np.random.randint(0,999,2)
path=np.zeros((1000,1000))

print(goal)
print(person)
path[goal[0]][goal[1]]=2

def depalcement(perso,but):
    if(perso[0]!=but[0]):
        if(perso[0]<but[0]):
            perso[0]+=1
        else:
            perso[0]-=1
        
    if(perso[1]!=but[1]):
        if(perso[1]<but[1]):
            perso[1]+=1
        else:
            perso[1]-=1
    path[perso[0]][perso[1]]+=1
    return perso

while(person[0]!=goal[0] and person[1]!=goal[1]):
    person = depalcement(person,goal)
    #print(goal[0],goal[1])
    #print(person[0],person[1])

print("finish")
print(path)
plt.figure()
plt.imshow(path)
plt.colorbar()
plt.title("la premiere")
plt.savefig("first.png")
