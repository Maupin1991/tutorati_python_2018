"""
E' dato un file <dati.txt> caratterizzato dal seguente formato rappresentante delle coppie nome/eta':

Pippo 23
Ada 19
Felice 32
Geronima 40
Ciccio 19

Si legga tutto il file creando un dizionario le cui chiavi sono fornite da eta' ed il valore associato ad una lista con i nomi corrispondenti all'eta'.

"""

f = open("dati.txt", "r")

l = f.readline()

d = {}

while (l != ""):
    lista = l.split()
    lista[1] = int(lista[1])

    eta = lista[1]
    nome = lista[0]

    if eta in d:
        d[eta] = d[eta] + [nome]
    else:
        d[eta] = [nome]
    l = f.readline()

print d
f.close()
