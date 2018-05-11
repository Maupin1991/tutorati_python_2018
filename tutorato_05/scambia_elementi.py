def scambia_elementi(lista, indice1, indice2):
    lista_aggiornata = list(lista)

    if len(lista) < indice1 or len(lista) < indice2:
        return "Errore, indice fuori dalla lista.\n"

    elemento1 = lista[indice1]
    elemento2 = lista[indice2]

    lista_aggiornata[indice2] = elemento1
    lista_aggiornata[indice1] = elemento2

    lista_aggiornata="".join(lista_aggiornata)
    return lista_aggiornata


lista = "ciao"

lista_nuova = scambia_elementi(lista, 2, 0)

print lista_nuova

