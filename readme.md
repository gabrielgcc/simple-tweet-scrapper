## descripcion
script de python que scrappea en busca de las ultimas ocurrencias de una palabra en twitter y las devuelve en un csv
## modo de empleo
- instalar twikit
```
pip install twikit
```
- poner los parametros necesarios para la ejecucion del script. 
```
COOKIE = 'CARACTERES ALFANUMERICOS DE LA COOKIE DE AUTENTIFICACION DE TU NAVEGADOR'
WORD = 'PALABRA(S) QUE QUIERAS BUSCAR'
N = NUMERO DE OCURRENCIAS QUE QUIERAS BUSCAR (DEFAULT = 50)
```
- si quieres, puedes modificar los parametros que quieres obtener en tu .csv. 
```
writer.writerow([tweet.user, tweet.text, tweet.lang])
```
los default son el user id, el texto y el lenguaje del tweet, pero para añadir mas parametros puedes atender a la libreria usada [twikit](https://twikit.readthedocs.io/en/latest/twikit.html#module-twikit.tweet)
- ejecutar
```
python3 main.py
```