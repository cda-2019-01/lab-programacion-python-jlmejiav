##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
data2=open('data.csv','r').readlines()
data3 = [row[0:-1] for row in data2]
data4 = [row.split('\t') for row in data3]
data5 = [z[0:4] + [ z[4].split(',')] + z[5:] for z in data4]
data6 = [z[0:3] + [ z[3].split(',')] + z[4:] for z in data5]
for row in data6:
    print(row[0]+','+str(len(row[3]))+','+str(len(row[4])))