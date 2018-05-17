# Tutorati di Python 2018

Questo **repository** è stato creato per il corso di Fondamenti di Informatica (Ing. Meccanica e Chimica) dell'università di Cagliari.

# Formulario di Python

Il seguente formulario è stato realizzato per aiutare nello studio del linguaggio Python. L'unico vero modo per imparare il linguaggio è quello di provare a eseguire i programmi al computer, per cui il consiglio è quello di usare questo formulario solo in caso di necessità. Come quando si studia una lingua straniera, esecitarsi con delle persone "madrelingua" è l'esercizio migliore, e in questo caso il nostro insegnante è lo stesso computer. Ovviamente dobbiamo parlargli con un linguaggio che possa capire, quindi è molto importante dargli delle istruzioni molto precise, che rispettino la sua "grammatica".

Nella sezione finale è presente una sezione di esercizi in ordine di presentazione degli argomenti e di difficoltà.

# Funzioni base


## Print
```python
print "Buongiorno\n"
a = raw_input("Inserisci il tuo nome")
print "Buongiorno ", nome
```

## Commenti

Attenzione: il commento su una linea si chiude automaticamente al termine della linea, mentre il commento su più linee deve essere chiuso!
```python
# commento su una linea

"""
Commento
su piu'
linee
"""
```

## Tipi di variabili

```python
numero = 100 # Intero   
num_virgola = 10.6 # Floating point
nome= "John" # Stringa
carattere= "a" # Char
iscritto_in_informatica = True # Booleano
```

## Input dell'utente

Nella programmazione capita che sia chiesto all'utente di inserire dei dati, che Python dovrà interpretare ed elaborare. Sono disponibili due funzioni, ma bisogna fare attenzione a cosa queste funzioni si aspettano:
```python
s = raw_input("Iserisci il nome")
n = input("Inserisci un numero")
```

* La *raw_input* prende qualunque cosa sia stata scritta e la salva come stringa. Se vogliamo fare su questa variabile delle elaborazioni numeriche bisognerà cambiare il tipo di dato. 
* La *input* cerca di capire da sola il tipo di dato. Se l'utente deve inserire una stringa, dovrà ricordare di inserire anche le virgolette o gli apici, una cosa che solitamente viene trascurata.

Come fare a scegliere? La funzione più generale è la *raw_input*, con lo svantaggio di doversi di ricordare di effettuare la conversione. In poche parole, se so che l'utente deve inserire dei numeri utilizzo:

```python
s = raw_input("Inserire un numero") # s diventa una stringa come "32"
n = float(s) # il valore di s viene salvato in n come float (32.0)
```

## ASCII

Per ottenere, dato un carattere, il suo corrispondente numero nel codice [ASCII](https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html) si utilizza la funzione ord(). Il suo inverso è la funzione chr().

```python
x = ord("f")
p = ord("1") # Nel codisce ASCII il carattere "1" ha indice 49, non 1!
c = chr("51") # carattere che corrisponde al numero 3
```

## Stringhe

Python accetta sia singole che doppie virgolette (ma uguali tra apertura e chiusura)

**Le stringhe sono IMMUTABILI!**

I caratteri accentati (è, ì, ò, à ... ) danno errore in Python
```python
frase = "Questa e' una stringa"
altra_frase = 'Altra stringa, singoli apici'
```
Operazioni con le stringhe

```python
len(frase) # lunghezza della stringa
frase.upper() # restituisce la stringa tutta maiuscola
frase.lower() # resituisce la stringa tutta minuscola

# per vedere se una sottostringa e' contenuta in una stringa
"una" in frase
```

## Conversione di tipi di dato

```python
int(4.5) # converte il float a intero (taglia le cifre decimali)    
int("42") # converte la stringa a intero
float(3) # converte intero a float (ci mette le cifre decimali)
float("23.8") # converte la stringa in float
str(74) # converte in stringa l'intero
```

## Librerie

In Python possiamo usare del codice già pronto, scritto da altri. Quello che bisogna fare è importare questo codice, ovvero dire a Python che vogliamo usare quello che c'è scritto dentro una specifica libreria.

Tutti questi modi di importare sono alternativi. Il consiglio è quello di imparare a usarne bene uno.

In questo caso bisogna ricordarsi di scrivere math prima di ogni funzione.
```python
import math # importiamo la libreria math
print math.pi
print math.sqrt(10)
```

In questo caso si può usare ogni funzione della libreria math.
```python
from math import * # importiamo tutte le funzioni (simbolo *)
print pi
print sqrt(10)
```

In questo caso si può usare solo la funzione che ho importato
```python
from math import sqrt # importiamo solo la funzione per la radice quadrata
print sqrt(10)
```
Posso però importare tutte e solo le funzioni che mi servono.
```python
from math import cos, pi, sin # importiamo piu' funzioni
```

## Liste
Sequenza **ordinata** di elementi, anche eterogenei, separati da virgole e racchiuse tra due parentesi quadre [ ]

```python
voti = [30, 29, 29, 30, 18,31]
lista = ["parola", 3, 'f', 34.56]
```
Accesso agli elementi di una lista. Tutti questi si possono applicare anche alle stringhe.
La sintassi è *[inizio : fine : passo]*. 
**L'elemento corrispondente all'indice *fine* non è incluso**
```python
voti[0] # primo elemento
voti[-1] # ultimo elemento (per qualunque lunghezza)
voti[::-1] # legge la lista al contrario
```

## Operazioni sulle stringhe e le liste

* join: lista --> stringa
* split: stringa --> lista

Bisogna fare attenzione al formato delle due operazioni.

```python
lista = ["parola", 3, 'f', 34.56]
stringa = "20-03-1992"

# la join inizia con il carattere o la stringa
# che vogliamo usare per unire la lista che compare tra parentesi
s = "-".join(lista) 

# la split inizia con la stringa, poi ha il carattere
# che vogliamo usare per dividere tra parentesi
l = stringa.split('-')

# se non mettiamo niente nelle parentesi, viene usato
# lo spazio per spezzare gli elementi
frase = "fondamenti di informatica"
parole = frase.split()
```

## Dizionari

I dizionari permettono di salvare elementi con il formato chiave-valore. **Le chiavi devono essere univoche**, perché Python deve sapere, data una chiave, a cosa questa corrisponde. I valori possono invece ripetersi, perché non sono usati come "indice" per ritrovare qualcos'altro.

Se si cerca di scrivere un valore usando una chiave già utilizzata in precedenza, il valore che prima corrispondeva a quella chiave viene sovrascritto.

```python
dati = {'temperatura':25.2, 'tempo': 'sereno', 'neve': False}

# aggiungi un nuovo elemento chiave-valore
dati['massima'] = 30 

# cambia il valore che prima corrispondeva alla chiave tempo da sereno a nuvoloso
dati['tempo'] = 'nuvoloso' 

# stampa il valore corrispondente alla chiave temperatura
print dati['temperatura']

# cancella la chiave neve
dati.pop('neve') 

# tutte le chiavi in una lista
chiavi = dati.keys() 

# tutti i valori in una lista
valori = dati.values() 

```




# Strutture di controllo

Nelle strutture di controllo si andrà a modificare il flusso di esecuzione del programma. I programmi che abbiamo scritto fino ad ora eseguono infatti le istruzioni nell'ordine esatto in cui sono scritte. In questa sezione andremo invece a presentare delle scelte all'interprete, che dovrà valutarle e modificare il flusso di esecuzione nel modo che gli diremo.

## Costrutto if

Il costrutto *if* serve a dire a Python di eseguire delle istruzioni solo se una condizione è verificata. Le istruzioni indentate dopo l'*if* devono essere indentate.

```python
voto = input("inserisci il voto")
superato = False # valore iniziale
if voto >= 18:
	superato = True # eseguita solo se la condizione e' vera
print superato # viene eseguita in ogni caso
```


## Costrutto if-else

Con l'*else* possiamo dare delle istruzioni alternative a Python, e saranno eseguite SOLO se la condizione non è verificata.
```python
voto = input("inserisci il voto")

if voto < 18:
	print "Dovrai ridare l'esame"
	
else:
	print "Hai superato l'esame"
```

## Costrutto if elif else

Possiamo anche dare più condizioni possibili. *Elif* sta per *else + if*. In questo caso, se la prima condizione non è verificata, viene verificata la seconda. Se nessuna delle due è vera, si passa al ramo *else*,  che in questo caso agisce come caso di *default* (cioè quello in cui si finisce se non ci sono altre condizioni che modificano la scelta).

```python
voto = input("inserisci il voto\n")

if voto < 18:
	print "Dovrai rifare l'esame"
elif voto < 24:
	print "Devi fare l'orale per superare l'esame"
else:
	print "Hai superato l'esame"
```

## Ciclo while

I cicli sono utili per eseguire una serie di istruzioni ripetute molte volte senza doverle riscrivere. Solitamente si utilizza il ciclo *while* quando non si conosce quante volte si deve eseguire una serie di istruzioni. Il ciclo *while* esegue le istruzioni contenute nel blocco indentato fino a quando la condizione espressa non diventa falsa. **ATTENZIONE**: se la condizione non diventa mai falsa, il computer resta a eseguire il ciclo in continuazione!

```python
c = 0
# fare attenzione alla condizione
# serve per uscire dal ciclo se l'utente inserisce
# la lettera k minuscola o maiuscola
while (c != 'k' and c != 'K'):
	c = raw_input("Inserisci un carattere:\n")

# questo viene stampato solo dopo l'uscita dal while
print "Complimenti, hai indovinato!"

i = 0
while i<100:
	print i
	i += 1 # incrementa la variabile i
```

## Ciclo for

Il ciclo *for* permette come il *while* di eseguire le istruzioni nel blocco indentato un numero di volte specifico. In particolare, il *for* è molto comodo per accedere a stringhe, liste o dizionari.

```python
stringa = "Sopra la panca la capra campa, sotto la panca la capra crepa."

for x in stringa:
	print ord(l)
```

La lettura del ciclo è questa: per ogni elemento *x* nella stringa, stampa *ord(x)*.
Una funzione molto utile da usare con i cicli *for* è la funzione *range(n)*, che genera una lista di numeri da 0 a n.

```python
stringa = "Sopra la panca la capra campa, sotto la panca la capra crepa."

# len(stringa) ci dice il numero di elementi, ma ricordiamo che l'elemento 
# stringa[len(stringa)] non esiste!
for i in range(len(stringa)-1):
	print stringa[i]
```
## Come scegliere tra while e for?

Non c'è solitamente una scelta giusta o una sbagliata. Il ciclo while è molto adatto per quando non sappiamo quante volte dovremo eseguire l'operazione. Per esempio, immaginiamo un programma che dice all'utente di indovinare un numero inserendolo con una input. Non sappiamo a priori quanti tentativi dovrà fare l'utente, quindi sarà difficile far funzionare questo programma con un ciclo for. Il ciclo for consente invece di risparmiare qualche istruzione (e quindi di sbagliare meno) quando dobbiamo lavorare con stringhe e liste. In questo caso spesso sappiamo quante volte le istruzioni devono essere eseguite, quindi il for potrebbe risultarci più utile. A parte rari casi è comunque possibile far funzionare il programma usando uno a scelta tra i due costrutti, ovviamente facendo attenzione a come sono scritti (per esempio ricordandosi di mettere una condizione di uscita dal while).

# File

## Apertura di un file

La prima cosa da fare per aprire un file con Python è utilizzare la funzione *open()*. La open si utilizza solitamente con due parametri di input: il nome del file da aprire e la modalità con cui si vuole aprire (lettura, scrittura, append). Una volta aperto il file, si procederà con le operazioni che si vogliono fare su di esso. Quando abbiamo finito di usare il nostro file, dobbiamo ricordarci di chiuderlo. Questo è importante soprattutto nel caso si siano svolte operazioni di scrittura, altrimenti le modifiche che abbiamo fatto non saranno salvate. Il file si chiude con la funzione *close()*.

```python
f = open("test.txt", 'r') #apriamo il file e salviamo in f il valore restituito
# ...
# operazioni sul file
# ...
f.close() # chiudiamo il file
```
Le possibili modalità di accesso al file sono:
* r: lettura
* w: scrittura (sovrascrive tutto)
* a: append (continua a scrivere da dove era finito il file)

## Lettura da file

Per leggere un file in Python dobbiamo per prima cosa aprirlo in modalità lettura. In seguito, usiamo un costrutto che abbiamo già incontrato per leggere una riga alla volta: i cicli. La funzione per leggere una riga in un file è la *readline()*.

```python
f = open("test.txt", 'r') #apriamo il file e salviamo in f il valore restituito

line = f.readline() # leggiamo la prima linea, in modo da poter entrare nel while
lines = [] # qui salveremo tutte le linee lette

while line != "":

	 # concatena la nuova linea in una lista di linee (stringhe)
	lines += [line]

	# legge una nuova linea, se il file finisce legge "" (condizione di uscita dal while)
	line = f.readline() 
f.close() # chiudiamo il file, alla fine del ciclo

print lines # stampa la lista di linee
```


## Scrittura su file

Per scrivere su file, il procedimento è molto simile. Apriamo il file, questa volta in modalità scrittura (o append), e scriviamo con la funzione *write()*. 

```python
f = open("test.txt", 'w') #apriamo il file e salviamo in f il valore restituito

lines = ["ciao", "sono", "un", "file!"] # linee che vogliamo scrivere
for l in lines:
	f.write(l) # scrivi una linea
	f.write("\n") # a capo dopo ogni linea
f.close() # chiudiamo il file, alla fine del ciclo -- IMPORTANTE!!!!

```

# Funzioni

Le funzioni ci permettono di scrivere del codice "isolato", per aumentare la leggibilità del nostro programma e renderlo **modulare**. Una funzione non è altro che un blocco di codice riutilizzabile usato per compiere una singola e precisa elaborazione. Abbiamo già visto alcune funzioni, come per esempio la len(). Quelle che andiamo a vedere adesso sono le funzioni definite dall'utente. Possiamo vederle come delle scatole in cui mettiamo degli ingressi e preleviamo delle uscite, senza curarci troppo di cosa sta succedendo al loro interno.

Ci sono delle semplici regole per definire le funzioni in Python:
* I blocchi di funzione iniziano con la parola chiave **def**, seguita dal nome della funzione e le parentesi tonde (()) e i due punti (:).
* I parametri in ingresso sono messi tra le parentesi che seguono il nome della funzione (vedi punto precedente).
* Il blocco di codice che compone la funzione è tutto indentato.
* L'istruzione **return** termina la funzione, e può restituire dei parametri a chi ha chiamato la funzione (chiamante).

Esempio:
```python
def somma(a, b):
  s = a + b
  return s
```

N.B.: i parametri sono dei "segnaposto" per i veri parametri che saranno passati. Chi chiama questa funzione non ha l'obbligo di chiamare i parametri di ingresso "a" e "b". E attenzione, l'ordine è importante!

## Chiamare una funzione

Per chiamare una funzione è necessario utilizzare il nome della funzione stessa. Se la funzione restituisce qualcosa, ricordiamoci di salvare il risultato in una o più variabili!

```python
v1 = 1
v2 = 4

s1 = somma(v1, v2)

# esempio di funzione che restituisce piu' variabili
massimo, minimo = trova_estremi(lista)
```

# Materiale aggiuntivo

* Installazione ambiente di sviluppo [Spyder](https://www.anaconda.com/download/) (si consiglia di installare la versione 2.x)
* [Tutorial](https://youtu.be/Yg0mPuRoNl8) su come usare i file .py su Spyder


# Esercizi

1. Scrivere un programma in Python che accetti una stringa dall'utente e la stampi al contrario (fare attenzione al fatto che la stringa messa dall'utente ha una lunghezza che non possiamo sapere a priori).
2. Scrivere un programma Python che, letti due valori numerici interi da tastiera, scriva su video quoziente e resto della divisione del primo per il secondo.
3. Scrivere un programma che valuti un'espressione booleana che date le variabili *ha_quattro_zampe* e *abbaia*, dica se l'animale è un cane (deve stampare a video la seguente frase: "l'animale e' un cane: True"  o "l'animale e' un cane: False").
4. Scrivere un programma che data una stringa inserita dall'utente, stampi a video quanti caratteri ci sono. 
5. Scrivere un programma che dati giorno, mese e anno inseriti dall'utente, stampi la data nel formato "Giorno-Mese-Anno". 
6. Scrivere un programma che dica se il carattere inserito dall'utente è un numero oppure una lettera. L'output deve essere un semplice True o False.
7. Scrivere un programma che dato un carattere inserito dall'utente stampi il carattere successivo del codice ASCII. Per ora non considerare un utente "obbediente" che inserisce solo lettere o numeri (sarebbe comunque meglio dirgli di inserire solo lettere o numeri).
8. Scrivere un programma che inserito un numero tra 1 e 12 stampi il mese scritto in lettere (usare una lista e fare attenzione agli indici).
9. Dato il programma precedente, far inserire ora all'utente anche il giorno e l'anno. Stampare poi la data in formato "Giorno-Mese(in lettere) -Anno". (Vedere es. 4 e 8)
10. Scrivere  un programma che inserisca un "_" tra le lettere di una parola scritta dall'utente. Es. "gatto" --> "g_a_t_t_o".
11. Scrivere un programma che stampi i numeri da 0 a 1000. Usare un ciclo while, poi fare lo stesso programma con un ciclo for.
12. Scrivere un programma che chieda all'utente di indovinare un numero. Il programma deve anche dare suggerimenti all'utente, dicendogli di inserire un numero più grande o più piccolo dell'ultimo inserito. Quando l'utente ha indovinato, il programma deve terminare scrivendo "hai vinto!". Usare un ciclo while e un if-else.
13. Scrivere un programma che chieda all'utente di inserire una frase e cancelli tutte le lettere 'a', sostituendole con un '-'.
14. Creare un programma che dica all'utente di inserire due numeri, e stampare se il secondo numero è un multiplo del primo.
15. Scrivere un programma che apre un file e stampa tutto quello che è contenuto in esso.
16. Scrivere un programma che apre un file, legge tutti i numeri contenuti in esso e li somma. Stampare a video il risultato.
17. Ripetere il precedente esercizio scrivendo il risultato in un altro file.
