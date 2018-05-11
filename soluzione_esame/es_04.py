"""
Scrivere un programma Python che legga da file, il cui nome e' immesso da tastiera, le
coordinate x-y di un insieme di punti sul piano cartesiano, li inserisca in una lista o un
dizionario e calcoli, stampandolo a video, il baricentro. Per esempio, il formato del file da
leggere e' il seguente:

P1: 30.1, 29.3
P2: -5.0, 6.5
P3: 10.6, 9.2
"""
nome_file=raw_input("Inserisci nome del file:")
f=open(nome_file,"r")
L=[]
linea=f.readline()
while linea!="":
    linea=linea.split(":")
    coppia=linea[1].split(",")
    L=L+[[float(coppia[0]),float(coppia[1])]]
    #L=L+[coppia]
    linea=f.readline()
print L
f.close()
sommax=0
sommay=0

for el in L:
    sommax=sommax+el[0]
    sommay=sommay+el[1]


bx=sommax/len(L)
by=sommay/len(L)

print "Il baricentro e' ", bx, " , ", by

