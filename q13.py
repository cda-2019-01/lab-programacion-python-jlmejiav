##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
data2=open('data.csv','r').readlines()
data3 = [row[0:-1] for row in data2]
data4 = [row.split('\t') for row in data3]
data5 = [z[0:4] + [ z[4].split(',')] + z[5:] for z in data4]
data6 = [z[0:4] + [x.split(':') for x in z[4] ]+ z[5:] for z in data5]
for row in data6:
    sum=0
    for x in row[4:]:
                sum = sum + int(x[1])        
    print(row[0],',',sum)