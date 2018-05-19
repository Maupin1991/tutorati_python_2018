def leggi_dizionario():
    """
    Legge un dizionario inserito da tastiera
    nella forma chiave:valore,chiave:valore,...

    Restituisce il dizionario letto
    """
    print "Inserire i dizionari nella forma chiave:valore,chiave,valore..."
    stringa = raw_input("Inserire il dizionario:\n")

    # in questo modo si ottiene una lista di elementi "chiave:valore"
    lista_elementi = stringa.split(',')

    dizionario = {}

    for elemento in lista_elementi:
        # qui dividiamo chiave e valore e li mettiamo in una lista
        chiave_valore = elemento.split(':')
        dizionario[chiave_valore[0]] = chiave_valore[1]

    return dizionario


def fondi_dizionari(d1, d2):
    """
    Fonde i due dizionari dati in ingresso in uno solo,
    se una chiave e' presente in entrambi inserisce nel
    nuovo dizionario una lista contentente entrambi i valori

    Restituisce il dizionario composto
    """
    dizionario = d1

    # ora dobbiamo unire il dizionario 2
    for chiave in d2:

        # se la chiave e' anche in d1, bisogna mettere
        # il valore presente in una lista e aggiungere
        # il nuovo valore con una concatenazione
        if chiave in dizionario:
            # ATTENZIONE: se concateniamo senza mettere in liste
            # otteniamo la concatenazione delle stringhe!!!
            dizionario[chiave] = [dizionario[chiave]] + [d2[chiave]]

        # altrimenti basta mettere il valore nel dizionario
        else:
            dizionario[chiave] = d2[chiave]

    return dizionario


def main():
    # leggiamo i due dizionari
    dizionario1 = leggi_dizionario()
    dizionario2 = leggi_dizionario()

    dizionario_totale = fondi_dizionari(dizionario1, dizionario2)
    print dizionario_totale


main()
