"""
Scrivere un programma Python che legge da file
"funzione.txt", una sequenza di coppie t, f(t), dove t
rappresenta l'istante di tempo nel quale e' stato
campionata una certa misura f(t) (si pensi per esempio
al segnale vocale visto a lezione, un segnale di tensione
o di corrente, di potenza dissipata e cosi via). Le coppie
lette, che nel file sono separate dal carattere "a capo"
(quindi due valori per riga), devono essere memorizzate
in una lista di liste.
"""

# ci serve per fare i grafici
import matplotlib.pyplot as plt


def leggiDati(nomefile):
    """
    riceve in ingresso il nome di un file e restituisce una lista di coppie di
    valori [t, f(t)]

    esempio di file:

    1.0 2.0
    2.0 5.0
    3.0 7.0
    4.0 12.0
    """

    f = open(nomefile, 'r')
    lista = []

    linea = f.readline()
    while linea != "":
        s = linea.split()
        s[0] = float(s[0])
        s[1] = float(s[1])

        lista = lista + [s]
        linea = f.readline()
    f.close()
    return lista


lista_di_punti = leggiDati("dati.txt")
print lista_di_punti


def calcolaDerivata(lista):
    """
    riceve in ingresso una lista formata dalle coppie [t, f(t)] e restituisce
    una lista contente le relative derivate, per ogni t
    """
    derivate=[]
    i=1
    while i<len(lista):
        d=(lista[i][1]-lista[i-1][1])/(lista[i][0]-lista[i-1][0])
        derivate=derivate+[d]
        i=i+1
    return derivate


def calcolaIntegrale(lista):
    """
    riceve in ingresso una lista formata dalle coppie [t, f(t)] e restituisce
    una lista contente i relativi integrali, per ogni t.
    """
    integrale=[0]
    integ=0.0
    k=1
    while k<len(lista):
        integ = integ +lista[k][1]*(lista[k][0]-lista[k-1][0])
        integrale=integrale+[integ]
        k=k+1

    return integrale




def salvaDati(t, ft, d, i):
    """
    riceve in ingresso una linea con la tripla formata dai valori [t, d(f(t)), i(f(t))]
    (t, derivata di f(t), integrale di f(t)], li salva, riga per riga, nel file "elaborazione.txt".
    Scrive una riga alla volta (il file va aperto in modalita' append)
    """
    f = open("elaborazione.txt", 'a')
    f.write(",".join([str(t), str(ft), str(d), str(i)]))
    f.write("\n")
    f.close()


def grafico(t, ft):
    """
    prende in ingresso le liste di campioni relative a t e f(t) e visualizza il grafico
    come linee continue

    t e ft DEVONO avere la stessa len()
    """
    if len(t) != len(ft):
        print "servono liste di lunghezza uguale!"
        return
    plt.plot(t, ft)
    plt.show()


def scatter_plot(t, ft):
    """
    prende in ingresso le liste di campioni relative a t e f(t) e visualizza il grafico
    come punti nel piano

    t e ft DEVONO avere la stessa len()
    """
    if len(t) != len(ft):
        print "servono liste di lunghezza uguale!"
        return
    plt.scatter(t, ft)
    plt.show()

def main():
    lista_di_punti = leggiDati("dati.txt")
    derivate = calcolaDerivata(lista_di_punti)
    integrali = calcolaIntegrale(lista_di_punti)
    for indice in range(len(lista_di_punti) - 1):
        salvaDati(lista_di_punti[indice][0], lista_di_punti[indice][1],
                  derivate[indice], integrali[indice])

main()