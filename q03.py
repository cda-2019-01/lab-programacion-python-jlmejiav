##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
data2=open('data.csv','r').readlines()
data3 = [row[0:-1] for row in data2]
data4 = [row.split('\t') for row in data3]
col1 = [row[0] for row in data4]
letras = sorted(set(col1))
##
sum=0
vec=[]
for w in letras:
    sum=0
    for row in data4:
        if row[0] == w:
            sum = sum + int(row[1])        
    print(w,',',sum)
##