"""
Data una stringa s, permutare l'ultimo ed il primo carattere.
"""

stringa = raw_input("Inserisci una stringa \n")

nuova_stringa = stringa[-1] + stringa[1:-1] + stringa[0]

print nuova_stringa
