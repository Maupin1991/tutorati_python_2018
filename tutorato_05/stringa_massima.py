"""
Scrivere una funzione che prese due stringhe, stabilisca quale e' la maggiore e dica quale e' l'indice massimo di tale stringa.

"""


def trova_stringa_massima(stringa1, stringa2):
    """
    stringa1 --> una stringa
    """
    lunghezza1 = len(stringa1)
    lunghezza2 = len(stringa2)

    if lunghezza1 < lunghezza2:
        # stringa 2 piu' lunga
        print "indice massimo della stringa 2: ", lunghezza2 - 1
    elif lunghezza2 == lunghezza1:
        # lunghezze uguali
        print "lunghezze uguali, indice massimo: ", lunghezza1 - 1
    else:
        # stringa 1 piu' lunga
        print "indice massimo della stringa 1: ", lunghezza1 - 1


trova_stringa_massima(8, "43")