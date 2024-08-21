import asyncio
import csv

from twikit import Client

## CONSTANTES: la cookie, palabra que quieres buscar, cuantas veces quieres buscarla
COOKIE = ''
WORD = ''
N = 50

## SETTEAMOS EL CLIENTE
client = Client(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 14_6_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15',
    language='en-US'
    )

## MAIN
async def main():
    sample = []

    ## NOS LOGGEAMOS EN LA CUENTA
    client.set_cookies({'auth_token':COOKIE})
    await client.get('https://x.com', raise_exception=False)

    ## PRUEBA PARA VER QUE FUNCIONA
    tweets = await client.search_tweet(WORD, 'Latest')
    ## REPETIMOS HASTA QUE TENGAMOS, COMO MINIMO, N TWEETS
    while len(sample) < N:
        for tweet in tweets:
            sample.append(tweet)
        tweets = await tweets.next()
    
    ## TENEMOS LOS TWEETS EN UN ARRAY AHORA LOS PASAMOS A UN CSV
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        for tweet in sample:
            writer.writerow([tweet.user, tweet.text, tweet.lang])

## LANZAMOS MAIN CONCURRENTEMENTE 
asyncio.run(main())