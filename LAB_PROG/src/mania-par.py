##entrada ='''4 4
##1 2 2
##2 3 1
##2 4 10
##3 4 6'''
entrada = '''5 6
1 2 3
2 3 5
3 5 2
5 1 8
2 4 1
4 5 4'''
entrada = entrada.split("\n")
print(entrada)

final = entrada[0][0]
distancias = {}
arestas =[]
for i in range(1,len(entrada)):
    x = entrada[i].split()
    distancias[(x[0],x[1])]=int(x[2])
    
from collections import defaultdict
from heapq import *

def dijkstra(arestas, inicio, final):
    gasto = defaultdict(list)
    for l,r,c in arestas:
        gasto[l].append((c,r))
    cont = 0
    quantidade, visto = [(0,inicio,())], set()
    while quantidade:
        cont += 1
        (custo,v1,caminho) = heappop(quantidade)
        if v1 not in visto:#se não viu
            visto.add(v1)
            caminho = (v1, caminho) 
            if v1 == final:
                return custo
            for c, v2 in gasto.get(v1, ()):
                if v2 not in visto:
                    heappush(quantidade, (custo+c, v2, caminho))
    return -1

if __name__ == "__main__":
    arestas =[]
    for i,j in distancias.items():
        arestas.append((i[0],i[1],j))
        
inicio = str(1)

saida = (dijkstra(arestas, inicio, final))
print(saida)
