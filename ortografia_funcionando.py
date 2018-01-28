def corretor(s1,s2):
    tabela = [None]*(len(s2)+1)
    for i in range(len(s2)+1):
        tabela[i]=[0]*(len(s1)+1)
    for i in range(1, len(s2)+1):
        tabela[i][0] = i
    for i in range(1,len(s1)+1):
        tabela[0][i]=i
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s1[j-1]==s2[i-1]:
                distancia=0
            else:
                distancia=1
            tabela[i][j]=min(tabela[i-1][j-1]+distancia,tabela[i][j-1]+1,tabela[i-1][j]+1)
    if tabela[i][j] <= 2:
        return s2 + ' '
    return ''


Entrada = input().split(" ")
Dic = ""
for x in range(int(Entrada[0])):
    Dic += input()+" "
Split = Dic.split(" ")
del Split[-1]
for x in range(int(Entrada[-1])):
    Palavra = input()
    Conca = ""
    for y in Split:
        if len(Palavra)-len(y) <= 2 or len(y)-len(Palavra) <= 2:
            Conca += corretor(Palavra,y)
    print(Conca[:-1])
     
