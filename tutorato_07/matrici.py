import matplotlib.pyplot as plt


def leggiDati():
    """
    riceve in ingresso il nome di un file e restituisce una lista di coppie di
    valori [t, f(t)]

    esempio di file:

    1.0, 2.0
    2.0, 5.0
    3.0, 7.0
    4.0, 12.0
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


        i(x) = somma( f(x) * h )

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
