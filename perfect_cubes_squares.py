# find perfect cubes and squares like 64, perfect square of 8 and cube of 64
import math

def perfect_sc(num):
    l = []

    for i in range(1,num):
            #for squares
        sq = str(i**(1/2))
        sp = sq.split('.')
        ze = int(sp[1])
        
        #for cubes
        cu = str((round(i**(1./3.), 2)))
        csp = cu.split('.')
        z2 = int(csp[1])
        
        if ze == 0 and z2 ==0:
            l.append(i)
        else:
            continue
    return l
    
print(perfect_sc(1000000))
