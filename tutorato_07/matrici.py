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


def leggiDati():
    """
    riceve in ingresso il nome di un file e restituisce una lista di coppie di
    valori [t, f(t)]

    esempio di file:

    1.0 2.0
    2.0 5.0
    3.0 7.0
    4.0 12.0
    """

    pass


def calcolaDerivata():
    """
    riceve in ingresso una lista formata dalle coppie [t, f(t)] e restituisce
    una lista contente le relative derivate, per ogni t, secondo la definizione

                      f(x) - f(x+h)
        d(x) =        -------------
                             h

    dove h e' la distanza tra due campioni consecutivi.


    """

    pass


def calcolaIntegrale():
    """
    riceve in ingresso una lista formata dalle coppie [t, f(t)] e restituisce
    una lista contente i relativi integrali, per ogni t, secondo la definizione

        i(0) = 0
        i(x) = i(x-1) + ( f(x) * h )

    dove h e' la distanza tra due campioni consecutivi.


    """

    pass


def salvaDati():
    """
    riceve in ingresso una linea con la tripla formata dai valori [t, d(f(t)), i(f(t))]
    (t, derivata di f(t), integrale di f(t)], li salva, riga per riga, nel file "elaborazione.txt".
    """

    pass


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
