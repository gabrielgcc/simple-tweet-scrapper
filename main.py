import asyncio
import csv
import time
import datetime
import sys
import twikit

## CONSTANTES: la cookie, palabra que quieres buscar, cuantas veces quieres buscarla
COOKIE = '635f037f6628522e74445c37f8736dcfa401ecf7'
WORD = sys.argv[1]
N = int(sys.argv[2])

## SETTEAMOS EL CLIENTE
client = twikit.Client(
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
        try:
            for tweet in tweets:
                if WORD in tweet.text and tweet.lang == sys.argv[3] and "lawless" not in tweet.text:
                    #print(tweet.text)
                    sample.append(tweet)
            time.sleep(1)
            print('hay ', len(sample), 'tweets de un total de ', N)
            tweets = await tweets.next()
        except twikit.errors.TooManyRequests as e:
            rate_limit_reset = datetime.datetime.fromtimestamp(e.rate_limit_reset)
            print(f'{datetime.datetime.now()} - Rate limit alcanzado. Esperar hasta {rate_limit_reset}')
            wait_time = rate_limit_reset - datetime.datetime.now()
            time.sleep(wait_time.total_seconds())
            continue

    ## TENEMOS LOS TWEETS EN UN ARRAY AHORA LOS PASAMOS A UN CSV
    with open(sys.argv[4], 'w', newline='') as file:
        writer = csv.writer(file)

        for tweet in sample:
            writer.writerow([tweet.user, tweet.text, tweet.lang])

## LANZAMOS MAIN CONCURRENTEMENTE 
asyncio.run(main())