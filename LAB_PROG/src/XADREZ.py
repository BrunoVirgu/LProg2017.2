entrada = int(input())
entrada1 = [int(x) for x in input().split(" ")]

furos =[(1,3),(2,3),(2,5),(5,4)]
pos = (4,3)
cont = 0

for i in entrada1:
    if i == 1:
        pos = (pos[0]+1,pos[1]+2)
        cont+=1
    elif i == 2:
        pos = (pos[0]+ 2,pos[1]+ 1)        
        cont+=1
    elif i == 3:
        pos = (pos[0]+ 2,pos[1]- 1)                
        cont+=1
    elif i == 4:
        pos = (pos[0]+ 1,pos[1]- 2)               
        cont+=1
    elif i == 5:
        pos = (pos[0]- 1,pos[1]- 2)              
        cont+=1
    elif i == 6:
        pos = (pos[0]- 2,pos[1]- 1)       
        cont+=1
    elif i == 7:
        pos = (pos[0]- 2,pos[1]+ 1)        
        cont+=1
    elif i == 8:
        pos = (pos[0]- 1,pos[1]+ 2)                
        cont+=1
    
    if pos in furos:
        break
    if pos[0] <0 or pos[0] >7:
        break
    if pos[1] <0 or pos[1] >7:
        break
    
print(cont)