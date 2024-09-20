from pyamaze import maze,agent
from queue import PriorityQueue

def h(cell1,cell2): #manathan distance
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2)+abs(y1-y2)

def aStar(m,goal):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,goal) #distance entre start et goal
    print(f_score)

    open=PriorityQueue()
    open.put((h(start,goal),h(start,goal),start))
    aPath={}#solution
    while not open.empty():
        currCell=open.get()[2] #cost du carreau
        if currCell==goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,goal)#calcule des scores temporaire

                if temp_f_score < f_score[childCell]:#mise a jour des données
                    g_score[childCell]=temp_g_score
                    f_score[childCell]=temp_f_score
                    open.put((temp_f_score,h(childCell,goal),childCell))
                    aPath[childCell]=currCell#mise a jour du chemin
    
    fwdPath={}#reconstitution de solution (inverser)
    cell=goal
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]

    return fwdPath

if __name__=="__main__":
    m=maze(15,15)
    m.CreateMaze()

    print(m.maze_map)
    print(m.grid)
    path=aStar(m,(1,1))

    a=agent(m,footprints=True)
    m.tracePath({a:path})
    for n in range(0,4):
        print(n)

    m.run()