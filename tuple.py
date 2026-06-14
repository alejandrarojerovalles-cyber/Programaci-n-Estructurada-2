"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises1=("México", "Canada", "EUA")

print(paises1)

varios=("Hola", True, 33.31416)

print(paises1)
print(varios)


for i in paises1:
    print(i)

for i in range(len(paises1)):
    print(paises1[i]) 

while i < len(paises1):
    print(paises1[i])
    i+=1

print(f"El pais que inagura la copa del mundo 2026 es: {paises1[0]}")

edades=(23, 24, 18, 20,20,23, 24)
print(edades)
numero=int(input("Dame el numero a buscar: ").strip())
posiciones=[]
for i in range(len(edades)):
    if edades[i]==numero:
        posiciones.append(i)

tuple_posiciones=tuple(posiciones)
for i in tuple_posiciones:
    print(f"El numero {numero} aparece en la posicion: {i}")