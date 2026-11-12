
stringa=input("inserisci una stringa")

print(stringa)
stringa=stringa + "$"
print(stringa)


print("-------------------")
lista=[]
c= 0
for i in stringa:
    lista.append(stringa)
    print(stringa)
    s=stringa[0]
    stringa=stringa[1:]+s

print("--------------------")

for i in lista:
    print(i)

print("--------------------")

lista.sort()
for i in lista:
    print(i)

print("---------------------")

print("Compresiione bwt")
str_bwt=""
c=0
for i in lista:
    valore=lista[c]
    str_bwt= str_bwt + valore[-1]
    c = c + 1


print(str_bwt)
