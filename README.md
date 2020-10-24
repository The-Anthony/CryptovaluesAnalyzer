# CryptovaluesAnalyzer
## ITALIANO

### In cosa consiste 
Il progetto è un programma assegnato da Start2Impact. Esso utilizza l'API offerta da CoinMarketCap, per ricevere dati su tutte le criptovalute
del mercato, analizzandoli e estraendo delle informazioni.
Nello specifico esso permette di scoprire:
- la criptovaluta che avesse il volume maggiore nelle ultime 24 ore
- la quantità di denaro necessaria per acquistare un'unità di tutte le prime 20 criptovalute per capitalizzazione
- la percentuale di denaro guadagnata se si vendessero oggi le prime 20 criptovalute acquistate ieri
- La quantità di denaro necessaria per acquistare una unità di tutte le criptovalute il cui volume delle ultime 24 ore sia superiore a 76.000.000$
- le migliori e le peggiori 10 criptovalute per incremento percentuale nelle ultime 24h

### Cosa serve per provarlo 
1) Creare con python un ambiente virtuale 
2) Installare al suo interno la libreria 'requests' tramite pip
3) Richiedere una chiave API al link raggiungibile [qui](https://pro.coinmarketcap.com/)
4) Inserire l'API ottenuta nel 'main.py' alla riga 21 al posto di '---- API KEY HERE ----'
5) Crea nella stessa directory del file 'main.py' una nuova cartella chiamata 'jsonData'
6) Fai partire il programma

Esso mostrerà alcuni dati sul terminale e andrà a creare un file Json nella nuova cartella, dove saranno elencate in maniera precisa tutte le informazioni.

________________________
## ENGLISH

### What's it about
The project is a program assigned by Start2Impact. It uses the API offered by CoinMarketCap, to receive data on all cryptocurrencies
of the market, analyzing them and extracting information.
Specifically, it allows you to discover:
- the cryptocurrency that had the largest volume in the last 24 hours
- the amount of money needed to purchase a unit of all the top 20 cryptocurrencies by capitalization
- the percentage of money earned if the top 20 cryptocurrencies bought yesterday were sold today
- The amount of money required to purchase one unit of all cryptocurrencies whose last 24-hour volume exceeds $ 76,000,000
- the best and worst 10 cryptocurrencies by percentage increase in the last 24h

### What it takes to prove it
1) Create a virtual environment with python
2) Install the 'requests' library inside it via pip
3) Request an API key at the link accessible [here] (https://pro.coinmarketcap.com/)
4) Insert the API obtained in the 'main.py' on line 21 instead of '---- API KEY HERE ----'
5) Create a new folder called 'jsonData' in the same directory as the 'main.py' file
6) Run the file

It will show some data on the terminal and will create a Json file in the new folder, where all the information will be listed in a precise manner.

