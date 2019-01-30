#Importamos todas la clases que vamos a utilizar
from modelado.mimodelo import *


listaDatos = [88, 55,0, 7, 2, 56, 34, 1, 99, 15]						#Creamos una lista con los elementos a ordenar
objOr = Ordenamiento(listaDatos)										#Creamos un objeto tipo Ordenamiento para obtener los metodos que ordenan
print("Arreglo desordenado")
print(listaDatos,"\n");													#Presentamos primero  la lista desordenada

op = int(input("Ordenamiento por seleccion(1) Insercion(2)\n"))			
if (op == 1):
	print("Ordenamiento por Selección")
	objOr.ordenamientoSeleccion()										#Por metodo de seleccion
if (op == 2):
	print("Ordenamiento por Inserción")
	objOr.ordenamientoInsercion()										#Por metodo de insercion

print("\nArreglo Ordenado")												#Lista ordenada
print(objOr)