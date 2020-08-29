import config
from ADT import list as lt
from DataStructures import listiterator as it
from App import app as load

N = load.loadCSVFile("Data\SmallMoviesDetailsCleaned.csv")


def peliculas_por_genero(lst, genero):
    a =[]
    doki = it.newIterator(lst)
    while it.hasNext(doki):
        waku = it.next(doki)
        if genero in waku["genres"]:
            a.append(waku["original_title"])
    return a
print(peliculas_por_genero(N, "Comedy"))
    