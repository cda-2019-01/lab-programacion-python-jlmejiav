##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
data2=open('data.csv','r').readlines()
data3 = [row[0:-1] for row in data2]
data4 = [row.split('\t') for row in data3]
col1 = [row[0] for row in data4]
letras = sorted(set(col1))
##
maximo=0
minimo=0
for w in letras:
    vec=[]
    for row in data4:
        if row[0] == w:
            vec.append(row[1])
    maximo = max(vec)
    minimo = min(vec)
    print(w+','+str(maximo)+','+str(minimo))