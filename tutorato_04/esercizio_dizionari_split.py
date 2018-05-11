stringa_diz = "nome:sss,cognome:cxc"

stringa_split_virgola = stringa_diz.split(',')

print "\ndopo la prima split:\n"
print stringa_split_virgola

# e' una lista di stringhe, non puoi fare la split su questa
# devi fare la split su ogni elemento
for chiave_valore in stringa_split_virgola:
    print chiave_valore
    elemento_del_dizionario = chiave_valore.split(":")
    chiave = elemento_del_dizionario[0]
    # ovviamente manca il controllo sulla chiave,
    # prova a farlo tu
    valore = [elemento_del_dizionario[1]]
