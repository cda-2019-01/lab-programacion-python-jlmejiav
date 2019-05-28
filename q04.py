##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
data2=open('data.csv','r').readlines()
data3 = [row[0:-1] for row in data2]
data4 = [row.split('\t') for row in data3]
data5 = [z + [ z[2].split('-')[1]] for z in data4]
mesestotal = [row[5] for row in data5]
meses = sorted(set(mesestotal))
for m in meses:
    print(m+','+str(mesestotal.count(m))) 