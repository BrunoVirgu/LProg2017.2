from math import sqrt
entrada1 = [int(x) for x in input().split(" ")]
entrada2 = [int(x) for x in input().split(" ")]

pontoeraio1 = [(entrada1[0],entrada1[1]), entrada1[2]]
pontoeraio2 = [(entrada2[0],entrada2[1]), entrada2[2]]

SomaRaios = pontoeraio1[1] + pontoeraio2[1]
deish = (pontoeraio1[0][0] - pontoeraio2[0][0])**2
qdeish = (pontoeraio1[0][1] - pontoeraio2[0][1])**2

distancia = sqrt(deish + qdeish)

if distancia <= SomaRaios:
    print(1)
else:
    print(0)


