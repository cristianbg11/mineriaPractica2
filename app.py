def p1_in_p2(x,y):
    for i in y:
        if i not in x:
            return False
    return True

trans = []
file = open( "transaccion.txt", "r") 
for line in file: 
    trans.append(line.strip('\n'))

trans = tuple(trans)
atributos = []
comb = []
cantAtributos = 0
cantTrans = len(trans)
    
soporte = float(input("Digite el soporte: "))
confianza = float(input("Digite la confianza:"))


for j in range(1,len(trans)):     
    for i in trans[j]:
        if [i,0] not in atributos and i != " ":
            atributos.append([i,0])
            cantAtributos = cantAtributos + 1
atributos.sort()
for j in range (0,cantAtributos):
    count = 0
    for i in range(1,cantTrans):     
        if p1_in_p2(trans[i].split(" "),atributos[j][0]):
            count = count + 1
    atributos[j][1] = count

RE = ""

for i in atributos:
    if i[1] >= soporte:
        RE += i[0]
    
for i in RE:
    for j in RE:
        if sorted(i+j) not in comb and i!=j:
            comb.append(sorted(i+j))

for i in comb:
    for j in RE:
        if sorted("".join(i)+j) not in comb and j not in i and len(sorted("".join(i)+j))<len(RE):
            comb.append(sorted("".join(i)+j))

for i in range(0,len(comb)):
    comb[i] = [" ".join(comb[i]),0]
    
cantComb = len(comb)

for j in range (0,cantComb):
    count = 0
    for i in range(1,cantTrans):     
        if p1_in_p2(trans[i].split(" "),comb[j][0].split(" ")):
            count = count + 1
    comb[j][1] = count

sets = []

for i in range(0,cantAtributos):
    if atributos[i][1] >= soporte:
        sets.append(atributos[i])

for i in range(0,cantComb):
    if comb[i][1] >= soporte:
        sets.append(comb[i])
             
cantSets = len(sets)

for i in range(0,cantComb):
    comb[i][0] = comb[i][0].replace(" ","")

for i in range(cantAtributos,cantSets):
    for j in range(0, len(sets)):
        if i!=j and sets[j][0] in sets[i][0] and float(sets[i][1])/float(sets[j][1]) >= confianza:
            print(sets[j][0] , '->',sets[i][0].replace(sets[j][0],"") ,'confianza :', float(sets[i][1])/float(sets[j][1]))
