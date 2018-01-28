def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A, p,q-1)
        quicksort(A,p+1,r)

        
def partition(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p,r):
        if a[j] >=x:
            i = i+1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    
    return i+1
def teste():
    lista = [3,7,8.9,11]
    a = quicksort(lista, 0,len(lista)-1)
    return print(lista)
q = teste()