print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[23,33,45,8,24,0,100]
print(numeros)

lista=""
for i in numeros:
    lista=lista+str(i)+", "
    lista+=f"{i}, "
print(f"[{lista}]")


lista=""
for i in range(0,len(numeros)):
    lista+=f"{numeros[i]}, "
print(f"[{lista}]")

lista=""
i=0
while i<len(numeros):
    lista+=f"{numeros[i]}, "
    i+=1
print(f"[{lista}]")
#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
palabras=["UTD", "tercer", "cuatrimestre", "TI"]
palabra=input("Ingrese una palabra a buscar: ").strip()

if palabra in palabras:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")


#2DA FORMA
palabras=["UTD", "tercer", "cuatrimestre", "TI"]
palabra=input("Ingrese una palabra a buscar: ").strip()

encontro=False
for i in palabras:
    if i==palabra:
        encontro=True
if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:
    print(f"No encontre la palabra {palabra} en la lista")

#3er FORMA
palabras=["UTD", "tercer", "cuatrimestre", "TI"]
palabra=input("Ingrese una palabra a buscar: ").strip()
encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==palabra:
        encontro=True
if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:    
    print(f"No encontre la palabra {palabra} en la lista")

#4ta FORMA
palabras=["UTD", "tercer", "cuatrimestre", "TI"]
palabra=input("Ingrese una palabra a buscar: ").strip()
encontro=False
i=0
while i<len(palabras):
    if palabras[i]==palabra:
        encontro=True
    i+=1
if encontro:
    print(f"Encontre la palabra {palabra} en la lista")
else:    
    print(f"No encontre la palabra {palabra} en la lista")

#Ejemplo 3 Añadir elementos a la lista
lista=[]

valor=input("Ingrese un elemento a la lista: ").strip()
lista.append(valor)
lista.append(input("Ingrese un elemento a la lista: ").strip())

#opcion 1
true=True
while true:
    valor=input("Ingrese un elemento a la lista: ").strip()
    lista.append(valor)
    opcion=input("Desea agregar otro elemento? True/False: ").strip().lower()
    if opcion=="false":
        true=False


#opcion 2
opcion="si"
while opcion=="si":
    valor=input("Ingrese un elemento a la lista: ").strip()
    lista.append(valor)
    opcion=input("Desea agregar otro elemento? (si/no): ").strip().lower()


print(lista)

"Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda"

agenda=[
    ["Carlos", "1234567890"],
    ["Adrian", "0987654321"],
    ["Luis", "5678901234"]
]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])
print(agenda)

lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]}, "
    lista+="\n"
print(f"[{lista}]")


