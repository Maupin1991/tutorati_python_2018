nome_file = raw_input("Inserisci il nome del file: \n")

f = open(nome_file, "r")

linea = f.readline()

d = {}

while linea != "":
    lista = linea.split()
    coppia = [lista[1][:-1], lista[2]]
    d[lista[0]] = coppia

    linea = f.readline()

i = 0
sommax = 0
sommay = 0

chiavi = d.keys()
while i < len(chiavi):
    chiave_i = chiavi[i]
    elemento = d[chiave_i]
    sommax += float(elemento[0])
    sommay += float(elemento[1])
    i += 1

bx = sommax / i
by = sommay / i

print "Il baricentro e' [" + str(bx) + ", " + str(by) + "]"

f.close()
