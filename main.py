import requests
from datetime import date, timedelta
import json
import os.path
import time


class Platform:

    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        # Url che ordina le criptovalute per incremento percentuale nelle ultime 24 ore
        self.percentUrl = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=percent_change_24h'
        self.params = {
            'start': '1',
            'limit': '5000',
            'convert': 'USD'
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '---- API KEY HERE ----',
        }

        # La criptovaluta con il volume maggiore nelle ultime 24h
        self.greaterVolume = {}

        # La quantità di denaro per acquistare un'unità di tutte le criptovalute con volume maggiore a $76 milioni
        self.priceHighVolume = 0

        # La quantità di denaro per acquistare un'unità delle prime 20 criptovalute per capitalizzazione
        self.pricefor20 = 0

        # Migliori 10 valute per incremento percentuale in 24h
        self.bestCrypto = []

        # Peggiori 10 valute per incremento percentuale in 24h
        self.wrongCrypto = []

        # Percentuale guadagnata se avessi comprato le prime 20 crypto ieri e le avessi rivendute oggi
        self.percentEarned = []

    def getData(self):

        print('Sto analizzando i dati di tutte le criptovalute nel mercato, attendi...')

        data = requests.get(url=self.url, params=self.params, headers=self.headers).json()
        dataOrderForPercent = requests.get(url=self.percentUrl, params=self.params, headers=self.headers).json()

        # Per inizializzare greaterVolume gli assegno i dati della prima valuta che l'API invia
        self.greaterVolume = {
            'symbol': data['data'][0]['symbol'],
            'volume': data['data'][0]['quote']['USD']['volume_24h'],
        }

        for currency in data['data']:

            # Se il volume di una valuta supera quello predefinito, prende il suo posto
            if currency['quote']['USD']['volume_24h'] > self.greaterVolume['volume']:
                self.greaterVolume['symbol'] = currency['symbol']
                self.greaterVolume['volume'] = round(currency['quote']['USD']['volume_24h'], 2)

            # Se il volume di una valuta supera i $76 milioni, il suo prezzo viene aggiunto al totale richiesto
            if currency['quote']['USD']['volume_24h'] > 76000000:
                self.priceHighVolume += currency['quote']['USD']['price']

        # L'API dispone di default le valute in ordine di capitalizzazione, quindi prendo le prime 20
        for x in range(20):
            self.pricefor20 += round(data['data'][x]['quote']['USD']['price'], 2)

        # Utilizzo un url diverso ordinato per incremento percentuale, da qui prendo le prime 10 e le ultime 10
        for x in range(10):
            self.bestCrypto.append({
                'symbol': dataOrderForPercent['data'][x]['symbol'],
                'percent_change_24h': round(dataOrderForPercent['data'][x]['quote']['USD']['percent_change_24h'], 2)
            })

            self.wrongCrypto.append({
                'symbol': dataOrderForPercent['data'][(-x - 1)]['symbol'],
                'percent_change_24h': round(dataOrderForPercent['data'][(-x - 1)]['quote']['USD'][
                    'percent_change_24h'], 2)
            })

        # Controllo se il programma ha creato un file json ieri, in quel caso calcolo il guadagno percentuale
        if os.path.exists(f'jsonData/{date.today() - timedelta(days=1)}.json'):
            ydayData = json.load(open(f'jsonData/{date.today() - timedelta(days=1)}.json'))
            ydayPrice20 = ydayData['dollarsForFirstTwenty']
            percentEarned = ((self.pricefor20 - ydayPrice20) / self.pricefor20) * 100
            self.percentEarned.append(round(percentEarned, 3))

        else:
            self.percentEarned.append('Dato non disponibile')

        # Nel terminale faccio un resoconto sintetico dei dati
        print('----------------------------')
        print('Ecco cosa ho scoperto:')

        print('Moneta con più volume nelle ultime 24 ore --> ', self.greaterVolume['symbol'])

        print(f'Denaro necessario per acquistare criptovalute con volume sopra ai $76 milioni -->'
              f' ${round(self.priceHighVolume)}')

        print(f'Denaro necessario per acquistare le prime 20 criptovalute per capitalizzazione --> '
              f'${round(self.pricefor20)}')

        print('Tutte le altre informazioni più approfondite, sono disponibili nel file json che sta per essere creato!')

        print('----------------------------')

    # Funzione che raccoglie i dati in un dizionario e scrive il file json
    def writeJson(self):

        print('Il file json sta per essere creato...')

        dataJson = {
            'greaterVolumeValue' : self.greaterVolume,
            'dollarsForHighVolume' : round(self.priceHighVolume, 2),
            'dollarsForFirstTwenty' : self.pricefor20,
            'percentChange' : {
                'bestValue' : self.bestCrypto,
                'wrongValue': self.wrongCrypto,
            },
            'percentEarned': self.percentEarned,
        }
        # Scrittura del file
        with open(f"jsonData/{date.today()}.json", "w+") as outfile:
            json.dump(dataJson, outfile, indent=4)

        # Messaggio di conferma
        print("Ok! Tutto è andato secondo i piani! Ricomincerò da capo domani.")
        print('----------------------------')

# Funzione che crea il bot e chiama i metodi
def programFunction():
    newPlatform = Platform()

    newPlatform.getData()

    newPlatform.writeJson()

# Funzione ricorsiva, separata dalla principale per evitare che i dati del bot si sovrappongano
def ricorsiveFunction():
    programFunction()
    print('......... ')
    seconds = 24 * 60 * 60
    time.sleep(seconds)

    print("Sono di nuovo operativo!")

    ricorsiveFunction()


ricorsiveFunction()
