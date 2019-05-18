##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
data2=open('data.csv','r').readlines()
data3 = [row[0:-1] for row in data2]
data4 = [row.split('\t') for row in data3]
data5 = [z[0:3] + [ z[3].split(',')] + z[4:] for z in data4]
grupoletras = [row[3] for row in data5]
colsololetras=[]
for fila in grupoletras:
    for x in fila:
        colsololetras.append(x)
sololetrasord = sorted(set(colsololetras))
##
for w in sololetrasord:
    sum=0
    for row in data5:
        for x in row[3]:
            if x == w:
                sum = sum + int(row[1])        
    print(w,',',sum)
##
