
entrada = [int(x) for x in input().split(" ")]       
t1 =  [int(x) for x in input().split(" ")]
media = entrada[1]

for i in range(entrada[0]):
    zaza = t1[i] + media
    if i == len(t1) -1:
        if zaza < 42195:
            print("N")
            break
        else:
            print("S")
            break    
    if zaza < t1[i+1]:
        print("N")
        break
    if zaza >= 42195:
        print("S")
        break
    
    
    
