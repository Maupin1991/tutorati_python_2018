'''
E' noto che una dose di aspirina superiore a 500 mg/kg al giorno possa
essere letale. Scrivere un programma Python che, da file "pazienti.txt" contente un
elenco di pazienti con nome, peso in kg e dose complessiva di aspirina, in mg,
ingerita in un giorno, scriva in un secondo file "a_rischio.txt", il nome di ogni paziente
a rischio di decesso.
Nel file "pazienti.txt" i dati del singolo paziente sono scritti in
un'unica riga e nome, peso e quantita' ingerita sono separati dal carattere ";".
Nell'implementare il programma, si scrivano le seguenti funzioni:
1) (7 punti) leggi_file, che, ricevendo in ingresso una stringa contenente il nome
del file con la lista dei pazienti e relativi peso e dose ingerita, memorizzi tali valori
in una lista di liste che restituisce in uscita.
2) (5 punti) valuta_paziente che, ricevendo in ingresso il peso corporeo e la
quantita' di farmaco ingerita in un giorno da un paziente, calcola la massima
quantita' in mg che il paziente puo' ingerire attraverso la relazione fornita sopra
(massimaquantita=500*peso corporeo) e restituisce True se questa quantita' e'
inferiore o uguale a quella ingerita, False altrimenti.
3) (8 punti) allerta che, ricevendo in ingresso la lista dei pazienti e i loro dati, scrive
su file "a_rischio.txt" il nome dei pazienti che hanno assunto una dose di farmaco
superiore a quella sostenibile e quindi sono a rischio di decesso.
'''


def leggi_file():
    """
    ricevendo in ingresso una stringa contenente il nome
    del file con la lista dei pazienti e relativi peso e dose ingerita, memorizzi tali valori
    in una lista di liste che restituisce in uscita
    """
    pass


def valuta_paziente():
    """
    ricevendo in ingresso il peso corporeo e la
    quantita' di farmaco ingerita in un giorno da un paziente, calcola la massima
    quantita' in mg che il paziente puo' ingerire attraverso la relazione fornita sopra
    (massimaquantita=500*peso corporeo) e restituisce True se questa quantita' e'
    inferiore o uguale a quella ingerita, False altrimenti.
    """
    pass


def allerta():
    """
    ricevendo in ingresso la lista dei pazienti e i loro dati, scrive
    su file "a_rischio.txt" il nome dei pazienti che hanno assunto una dose di farmaco
    superiore a quella sostenibile e quindi sono a rischio di decesso
    """
    pass
