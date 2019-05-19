##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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
maximo=0
minimo=0
for w in setletras:
    vec=[]
    for row in letrasynum:
        if row[0] == w:
            vec.append(row[1])
    maximo = max(vec)
    minimo = min(vec)
    print(w,',',minimo,',',maximo)
    print(w+','+str(minimo)+','+str(maximo))
    ##RESPUESTA MALA - ver ejemplo de 'aaa', en la fila 14 de data tiene un 8, 'eee' y 'ddd' se ven de una