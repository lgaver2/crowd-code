import numpy as np
class Map_create:
    def open_doc(src,i):
        with open(src+".txt") as f:
            res=np.zeros((i,i))
            j=0
            for line in f:
                k=0
                for n in line:
                    if n!="\n":
                        if n=="X":
                            res[j][k]=0
                        else:
                            res[j][k]=4
                    k+=1
                j+=1
        return res