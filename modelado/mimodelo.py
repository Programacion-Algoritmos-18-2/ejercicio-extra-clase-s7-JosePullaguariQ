class Ordenamiento:#Creamos la clase Ordenamiento
    def __init__(self, listado):#Contructor de la clase Ordenamiento que recibe el listado desordenado
        self.listaDatos = listado

    def __str__(self):
        temporal = ""                                         	#Concatenamos una cadena llamada temporal para ingresar datos despues
        for n in self.listaDatos:								#Creamos un form para recorrer la lista
            temporal = "%s %s" % (temporal, n)					#Asignamos a la varible temporal los elementos para presentar
        temporal = ("%s" % temporal) 

        return temporal											#retonamos toda la cadena temporal


    def ordenamientoSeleccion(self):										#Creamos un metodo para ordenar por seleccion
    	masPequenio = 0														#creamos un a variable indice del elemento mas pequeño
    	for  i in range( 0, (len(self.listaDatos)-1)): 						#Creamos un for que itera hasta el rango listaDatos.length - 1
            masPequenio = i                                                 #asignamos a la variable el indice del resto del arreglo
            for indice in range((i+1),len(self.listaDatos)): 					#Creamos un for que itera para buscar el indice del elemento mas pequeño
                if (self.listaDatos[indice] < self.listaDatos[masPequenio]): 	#Preguntamos si el elemento que esta en el la posicion indice es menor que el primer elemento
                    masPequenio = indice										#asignamos a la varible el nuevo indice
            self.intercambio(i, masPequenio)									#llamamos al metodo intercambio de posiciones enviandole i y el indice mas pequeño encontrado
            print(self.__str__())												#presentamos como va cambiando el arreglo 


    def intercambio(self, primero, segundo):									#creamos un metodo para intercambiar elementos
    	temp = self.listaDatos[primero]											#intercambiamos con una variable temporal para no perder el valor
    	self.listaDatos[primero] = self.listaDatos[segundo]
    	self.listaDatos[segundo] = temp 


    def ordenamientoInsercion(self):											#Creamos un metodo para ordenar por insercion
    	insercion = 0															#creamos una variable temporal para contener el elemento a insertar
    	for siguiente in range( 1, (len(self.listaDatos))): 									#Creamos un for que itera hasta el rango de de listaDatos.length
            insercion = self.listaDatos[siguiente]                                 				#Almacenamos el valor en el elemento de posicion siguiente                
            moverElemento = siguiente;															#Inicializamos la ubicacion para colocar el elemento
            while ( moverElemento > 0 and  self.listaDatos[ moverElemento - 1 ] > insercion):	   #Creamosun while para busca un lugar para colocar el elemento actual
            	self.listaDatos[ moverElemento ] = self.listaDatos[ moverElemento - 1 ]				#Desplazamos el elemento una posicion a la derecha
            	moverElemento-=1																	#Restamos el contador cada vez menos 1
            self.listaDatos[moverElemento] = insercion                                              #Coloca el elemento insertado en la posicion del indice moverElemento
            print(self.__str__())																	#Llamamos al str para que presente como va cmabiando el arreglo