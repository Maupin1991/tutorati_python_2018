"""
Scrivere un programma Python che, ricevuta da tastiera un valore numerico intero non
negativo, stampi a video la relativa tabellina. Per esempio, ricevendo il valore 2, stampi a
video:

2 x 0 = 0
2 x 1 = 1
...
2 x 10 = 20
"""

numero = input("Inserire un numero intero\n")

lista = range(11)
#
# for elemento in lista:
#     risultato = elemento * numero
#     print str(numero) + " x " + str(elemento) + " = " + str(risultato)
#     #print numero, " x ", elemento, " = ", risultato
i=0

while i<=10:
    risultato = i * numero
    print str(numero) + " x " + str(i) + " = " + str(risultato)
    i=i+1
