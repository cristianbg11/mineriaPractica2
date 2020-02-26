cestas = {}

for c in range(1,101):
    cestas[c] = []
    p = 1
    while (c*p) <= 100:
        cestas[c].append(p*c)
        p += 1

sumaTotal = 0
for p in range(1,101):
	count = 0
	for c in range(1,101):
		if c in cestas[p]:
			count = count + 1
	sumaTotal += count
	print("producto: " + str(p) + "  cantidad de cestas: " + str(count))
			
			

print("\nPares frecuentes")

# encontrando los pares frecuentes utilizando un ciclo anidado para seleccionar los pares (x,y) que aparezcan en 5 o mas cestas
for x in range(1,20): # Estos son los 5 mas frecuentes que no son pares
    for y in range(x+1,21):
        cestaComun = [p for p in cestas[x] if p in cestas[y]]
        if len(cestaComun) >= 5:
            print (x,y),
			
			
			
print("\nSuma: " +str(sumaTotal))