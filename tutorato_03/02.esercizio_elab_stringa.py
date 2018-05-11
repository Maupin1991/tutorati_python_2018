"""
Si consideri la seguente stringa: 'Paolo nato nel 2001 a Cagliari.'
Scrivere una sequenza di istruzioni Python che stampi a video la stringa: 'Paolo ha x anni.'  sulla base del nome e dell'anno estratti dalla stringa data (dove x e' l'eta' di Paolo).

"""
stringa = "Paolo nato nel 2001 a Cagliari"

stringa_lista = stringa.split()

nome = stringa_lista[0]

anno = stringa_lista[3]
anno_numero = int(anno)

eta = 2018 - anno_numero

stringa_2 = nome + " ha " + str(eta) + " anni"

stringa_3 = " ".join([nome, "ha", str(eta), "anni"])

print stringa_2
print stringa_3
