##
## Imprima la suma de la segunda columna.
##Por acá se convierte en líneas y texto
data2=open('data.csv','r').readlines()
data3 = [row[0:-1] for row in data2]
data4 = [row.split('\t') for row in data3]
sum=0
for row in data4:
    sum = sum + int(row[1])
print(sum)