"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import shellsort as Sh

from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList("LINKED_LIST") #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst
    


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- (Req-3)Consultar informacion de un director")
    print("5- (Req-2)Consultar las 10 mejores y peores peliculas por votos y calificación")
    print("6- (Req-4)Consultar informacion de un actor")
    print("7- (Req-5)Consultar peliculas por genero")
    print("8- (Req-6)Consultar el top de peliculas por genero")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, lst, lst2):
    if lst['size']==0 or lst2["size"]==0:
        print("Una de las listas esta vacia")  
        return 0
    else:
        t1 = process_time()
        Min = []
        calificacion = 0
        ide = 0
        a = 1
        total = 0
        while a <= lst2["size"]:
            Mon = lt.getElement(lst2, a)
            if criteria == Mon["director_name"]:
                ide =  Mon["id"]
                n = 1
                while n <= lst["size"]:
                    Man = lt.getElement(lst, n)
                    if ide == Man["id"]:
                        total +=1
                        ele = {Man["original_title"]:Man["vote_average"]}
                        Min.append(ele)
                        calificacion += float(Man["vote_average"])
                    n += 1
            a += 1
        if total != 0:
            calificacion = round(float(calificacion)/float(total),1)
        t2 = process_time()
        x = {"Nombre autor": criteria,
            "Peliculas realizadas": total,
            "Calificacion promedio": calificacion,
            "Lista peliculas": Min}
        print("Tiempo de ejecucion",t2-t1,"Segundos")
        if total == 0:
            print("Autor no se encuentra")
        else:
            return x
    
def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    return 0
def high_vote_count(ele1, ele2):
    if int(ele1["vote_count"]) > int(ele2["vote_count"]):
        return True
    return False
def less_vote_count(ele1, ele2):
    if int(ele1["vote_count"]) < int(ele2["vote_count"]):
        return True
    return False

def less_vote_average(ele1, ele2):
    if float(ele1["vote_average"]) < float(ele2["vote_average"]):
        return True
    return False

def high_vote_average(ele1, ele2):
    if float(ele1["vote_average"]) > float(ele2["vote_average"]):
        return True
    return False


def BestoPeliculas(lst):
    if lst["size"]==0:
        print("La lista esta vacia")
    else:
        time1 = process_time()
        Datos1 = []
        Datos2 = []
        ava = lst
        Sh.shellSort(ava, high_vote_count)
        B = 1
        Coco = it.newIterator(ava)
        while it.hasNext(Coco) and B < 11:
            Mina = it.next(Coco)
            S = [Mina["original_title"], Mina["vote_count"]]
            Datos1.append(S)
            B += 1
        vc = lst
        Sh.shellSort(vc, less_vote_average)
        A = 1
        Menhe = it.newIterator(vc)
        while it.hasNext(Menhe) and A < 6:
            Alta = it.next(Menhe)
            N = [Alta["original_title"], Alta["vote_average"]]
            Datos2.append(N)
            A +=1
        time2 = process_time()
        x = {"Mejores peliculas por conteo de votos": Datos1,
            "Peores peliculas por promedio": Datos2}
        print("Tiempo de ejecucion",time2-time1,"Segundos")
        return x

def dame_tu_autografo(lst, lst2, actor):
    if lst["size"] == 0 or lst2["size"]==0:
        print("Una de las listas esta vacia")
    else:
        Datos = []
        idPelis = []
        directores = {}
        conteo = 0
        mayor = 0
        name = None
        prom = 0
        A = 1
        time1 = process_time()
        while A < 6:
            Banri = it.newIterator(lst2)
            while it.hasNext(Banri):
                tada = it.next(Banri)
                A = str(A)
                if tada["actor"+A+"_name"] == actor:
                    idPelis.append(tada["id"])
                    conteo += 1
                    if tada["director_name"] in directores:
                        directores[tada["director_name"]] +=1
                    else:
                        directores[tada["director_name"]] = 1
            A = int(A)
            A += 1
        for Monika in idPelis:
            deku = it.newIterator(lst)
            while it.hasNext(deku):
                bakugo = it.next(deku)
                if bakugo["id"] == Monika:
                    Datos.append(bakugo["original_title"])
                    prom += float(bakugo["vote_average"])
        for sayori in directores:
            if directores[sayori] > mayor:
                mayor = directores[sayori]
                name = sayori
        if prom != 0:
            prom = round(prom/conteo, 1)
        time2 = process_time()
        x = {"Nombre actor": actor,
            "No. de peliculas realizadas": conteo,
            "Promedio de las peliculas": prom,
            "Director con mayor colaboracion":name,
            "Titulos de las peliculas":Datos}
        print("Tiempo de ejecucion",time2-time1,"Segundos")
        if conteo == 0:
            print("Actor no existe")
        else:
            return x

def peliculas_por_genero(lst, genero):
    if lst["size"] == 0:
        print("La lista esta vacia")
    else:
        time1 =process_time()
        genero = genero.lower()
        genero = genero.capitalize()
        a =[]
        conteo = 0
        prom = 0
        doki = it.newIterator(lst)
        while it.hasNext(doki):
            waku = it.next(doki)
            if genero in waku["genres"]:
                a.append(waku["original_title"])
                prom += float(waku["vote_average"])
                conteo += 1
        prom = round(float(prom/conteo),1)
        time2 = process_time()
        x = {"Genero": genero,
            "Numero de peliculas": conteo,
            "Promedio votacion de las peliculas": prom,
            "Lista de las peliculas": a}
        if conteo == 0:
            print("Genero no encontrado")
        else:
            print("tiempo ejecucion",time2-time1,"Segundos")
            return x

def ranking_por_genero(lst, genero, orden):
    if lst["size"] == 0:
        print("La lista es vacia")
    else:
        time1 = process_time()
        genero = genero.capitalize()
        orden = orden.lower()
        Datos1 = []
        Datos2 =[]
        conteo = 10
        promC = 0
        promCV = 0
        zed = lst
        if orden == "ascendente":
            Sh.shellSort(zed, high_vote_count)
        elif orden == "descendente":
            Sh.shellSort(zed, less_vote_count)
        B = 1
        D = 0
        Coco = it.newIterator(zed)
        while it.hasNext(Coco) and D < 10 and B < zed["size"]:
            Mina = it.next(Coco)
            if genero in Mina["genres"]:
                S = [Mina["original_title"], Mina["vote_count"]]
                Datos1.append(S)
                promCV += float(Mina["vote_count"])
                D += 1
            B += 1

        
        shen = lst
        if orden == "ascendente":
            Sh.shellSort(shen, high_vote_average)
        elif orden == "descendente":
            Sh.shellSort(shen, less_vote_average)
        A = 1
        C = 0
        Menhe = it.newIterator(shen)
        while it.hasNext(Menhe) and C < 10 and A < shen["size"]:
            Alta = it.next(Menhe)
            if genero in Alta["genres"]:
                N = [Alta["original_title"], Alta["vote_average"]]
                Datos2.append(N)
                promC += float(Alta["vote_average"])
                C += 1
            A +=1
        
        if conteo != 0:
            promC = round(float(promC/conteo),0)
            promCV = round(float(promCV/conteo),1)
            time2 = process_time()
        if conteo == None:
            print("No se encontro ninguna pelicula con el genero introducido")
        else:
            x = {"Genero": genero,
                "El top 10 de las peliculas con cantidad de votos "+orden+" son": Datos1,
                "Promedio de cantidad de votos": promCV,
                "El top 10 de las peliculas por valificacion en orden "+orden+" son": Datos2,
                "Promedio de calificacion": promC}
            print("Tiempo de ejecucion",time2-time1,"segundo")
            return x
            


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    lista2 = lt.newList()
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n')
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                #file = input("Escriba el nombre del archivo: ")
                file = inut("ingrese el archivo detalles")
                file2 = input("ingrese el archivo casting")
                lista = loadCSVFile(file) #llamar funcion cargar datos
                lista2 = loadCSVFile(file2)
                print("Datos cargados, ",lista['size']," elementos cargados")
                print("Datos cargados, ",lista2['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                    a = input("¿De cual lista quiere saber el tamaño?(Details:lista, Casting:lista2)  ")
                    if a == "lista": 
                        print("La lista tiene",lista["size"],"elementos")#obtener la longitud de la lista
                    elif a == "lista2":
                        print("La lista tiene",lista2["size"],"elementos")#obtener la longitud de la lista
                    elif a != "lista" and a != "lista2":
                        print("Eliga una de las listas predispuestas")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0 or lista2['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0 or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    print(countElementsByCriteria(criteria, lista, lista2))
            elif int(inputs[0])==5:
                if lista==None or lista["size"]==0 or lista2['size']==0:
                    print("La lista esta vacia mi colta")
                else:
                    print(BestoPeliculas(lista))
            elif int(inputs[0])==6:
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else: 
                    actor = input("Nombre del actor que desea conocer: ")
                    print(dame_tu_autografo(lista, lista2, actor))
            elif int(inputs[0])==7:
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else: 
                    genero = input("Nombre del genero: ")
                    print(peliculas_por_genero(lista, genero))
            elif int(inputs[0])==8:
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else: 
                    genero = str(input("Nombre del genero: "))
                    orden = input("Orden de las peliculas(ascendento o descendente): ")
                    print(ranking_por_genero(lista, genero, orden))
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()