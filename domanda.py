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
#rappresentazione dell' oggetto Domanda
#DENTRO CLASSE def metodo(self)
class Domanda:
    def __init__(self,testo,livello,risposta_corretta,risposte_errate):
        self.testo = testo
        self.livello = livello
        self.risposta_corretta = risposta_corretta
        self.risposte_errate = risposte_errate


