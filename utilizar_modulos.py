# 1er utilizar los modulos 
import modulos

modulos.borrarPanntalla()
modulos.funcion1()

nom="Daniel"
ape="Carreon"
name,lastname=modulos.funcion4(nom,ape)
print(f"Nombre: {name} Apellidos: {lastname}")


#2da formar de utilizar modulos
from modulos import borrarPanntalla, funcion1, funcion4 

borrarPanntalla()
funcion1()

nom="Daniel"
ape="Carreon"
name,lastname=funcion4(nom,ape)
print(f"Nombre: {name} Apellidos: {lastname}")
