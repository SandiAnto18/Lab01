
from domanda import Domanda
from giocatore import Giocatore

"""
1 leggere le domande dal file -> aprire il file,leggere tutte le righe, scorrere il file a blocchi di 7.
2 salvarle in strutture dati
3 organizzare le domande per livello
4 ciclo di gioco
    scegliere domanda casuale
    mischiare le risposte
    chiedere risposta
    controllare risposta
5 calcolare punteggio
6 chiedere nickname
7 salvare punteggio nel file

RISPOSTE
tutte_risposte = errate + [corretta]
random.shuffle(tutte_risposte)

così poi controllo con:
if tutte_risposte[scelta] == corretta

ogni domanda occupa 6 righe + una vuota

"""
#1 apro filein modalità lettura r.leggo tutto.divido in righe (0,1,2..)
righe_file=open("domande.txt","r").read().splitlines()
print(righe_file)



#definisco metodo per caricare/leggere le domande, fuori dalla classe
#FUNZIONE FUORI DALLA CLASSE NON DEVE AVERE SELF def funzione() altrimenti da errore:TypeError: carica_domande() missing 1 required positional argument: 'self'
def carica_domande():
        file = open("domande.txt", "r")  # apro file in modalità lettura
        # leggo tutte le righe del file e le salvo in una lista
        righe = file.readlines()
        file.close()
        # lista che conterrà tutti gli oggetti Domanda
        lista_domande = []


        for i in range(0, len(righe), 7):  # righe da 0 a max lunghezza delle righe
            # con passo 7, ogni 7 righe equivale a un quiz (6 righe+1 vuota)
            # prima riga
            testo = righe[i]
            # 2da riga = numero livello quindi è un intero
            livello = int(righe[i + 1])
            # 3za riga = risposta corretta
            corretta = righe[i + 2]
            # 4ta,5ta e 6ta riga = risposte errate
            errate = [
                righe[i + 3],
                righe[i + 4],
                righe[i + 5]
            ]
            # creo  oggetto Domanda con i dati letti
            d = Domanda(testo, livello, corretta, errate)
            lista_domande.append(d)  # aggiungi domanda alla lista

        # restituisco la lista completa di domande
        return lista_domande
    #ora chiamo il metodo per visualizzarlo a console
lista_domande = carica_domande()
print(lista_domande)

#in Python il dizionario (dict) funziona esattamente come una Map in java.
"""
Possiamo usarlo per organizzare le domande per livello, dove:
chiave → livello (0, 1, 2…)
valore → lista di oggetti Domanda di quel livello
"""
# dizionario vuoto
livelli = {}

for d in lista_domande:
    # se il livello non esiste ancora, creo la lista
    if d.livello not in livelli:
        livelli[d.livello] = []
    # aggiungo la domanda alla lista del livello
    livelli[d.livello].append(d)
print(livelli)
#COSTRUIRE LA LOGICA DEL GIOCO

#creazione giocatore
giocatore=Giocatore(nickname="", punteggio="")

#variabili gioco
livello_iniziale=0
