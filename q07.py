##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras de la primera columna que aparecen
## asociadas a dicho valor de la segunda columna. Esto es:
##
##    ('0', ['C'])
##    ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##    ('2', ['A', 'E', 'D'])
##    ('3', ['A', 'B', 'D', 'E', 'E'])
##    ('4', ['E', 'B'])
##    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##    ('6', ['C', 'E', 'A', 'B'])
##    ('7', ['A', 'C', 'E', 'D'])
##    ('8', ['E', 'E', 'A', 'B'])
##    ('9', ['A', 'B', 'E', 'C'])
##
##
data2=open('data.csv','r').readlines()
data3 = [row[0:-1] for row in data2]
data4 = [row.split('\t') for row in data3]
col1 = [row[1] for row in data4]
numeros = sorted(set(col1))
##
for n in numeros:
    vec=[]
    for row in data4:
        if row[1] == n:
            vec.append(row[0])
    print('('+str(n)+','+str(vec)+')')