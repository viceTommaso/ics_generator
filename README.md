# ics_generator


## Prerequisites
python 3

## Program
Il progarmma genera un evento per il calendario (file ics) attraverso i dati inseriti.
Se non vengono inseriti i campi obbligatori il programma automatizza questi dati nella seguente logica:

    Nome File: "evento"
    Numero di eventi: 1
    Titolo: "Evento personale" (se sono più eventi verrà aggiunto il numero dell'evento)
    UID: "YYYYmmddHHMMSS"
    Data inizio: Data attuale
    Ora inizio: Evento impostato senza orario
    Data fine: Stessa data di inizio
    Ora fine: L'inizio dell'ora dopo

P.S. nel nome del file è preferibile utilizzare nomi brevi e senza spazi.

## Author
Vicentini Tommaso
