"""
Introdottosi di nascosto nello studio del Prof. Marcialis, qualcuno si e' impossessato del
testo d'esame di "Fondamenti di Informatica". I sospetti dell'Ing. Orru' e dell'Ing. Pintor
cadono su due studenti, uno dei quali ha lasciato nello studio le impronte delle sue scarpe.
Dall'ampiezza del passo ottenuta misurando la distanza fra le impronte, pari a 0.65 m,
esse possono calcolare l'altezza approssimativa dalla formula h=3*p, dove p e' l'ampiezza
del passo e h e' appunto l'altezza. I due sospettati si chiamano Fermo e Lucia. Scrivere un
programma Python che, letti da tastiera i valori di altezza dei due sospettati, scriva a video
il nome del sospettato piu' verosimile.
Suggerimento: si usi l'operatore abs(x) che restituisce il valore assoluto di x.
"""

p = 0.65
h = 3 * p

f = float(input("Inserire altezza di Fermo:\n"))
l = float(input("Inserire altezza di Lucia:\n"))

df = abs(h - f)
dl = abs(h - l)

# passo_f=f/3
# passo_l=l/3
#
# dpasso_f=abs(passo_f-p)
# dpasso_l=abs(passo_l-p)

if df < dl:
    print "Il colpevole e' Fermo"
elif df > dl:
    print "Il colpevole e' Lucia"
else:
    print "Non possiamo dire chi e' il colpevole"
