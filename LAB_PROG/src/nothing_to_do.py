
def juvenal(n):   
    if n == 1:
        return 1
    else:
        count=1
        while n>1:    
            if n % 2 == 0:
                count+=1
                n=n//2
            else:
                count+=1
                n = 3*n+1
        return count
cont = 0
entrada = int(input())
for i in range(entrada):
    cont += 1
    zum = [int (x) for x in input().split()]
    saida = 0
    print(juvenal(#botar um maior primo < zum[1])
print(time.time()-inicio)


  
'''