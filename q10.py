##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
data2=open('data.csv','r').readlines()
data3 = [row[0:-1] for row in data2]
data4 = [row.split('\t') for row in data3]
data5 = [z + [ z[4].split(',')] for z in data4]
grupoletras = [row[5] for row in data5]
colsololetras=[]
for fila in grupoletras:
    for x in fila:
        colsololetras.append(x)
letrasynum = [ x.split(':') for x in colsololetras]
setletras = sorted(set([x[0] for x in letrasynum]))
sololetras = [s[0] for s in letrasynum]
for w in setletras:
    print(w,',',sololetras.count(w))