import json
from urllib import request

respuesta = request.get("http://chucknorris.io/jokes/random")



respuesta_diccionario =json.loads(respuesta.text)
value = respuesta_diccionario["value"]

if "Chuck Norris" not in value:
    raise AssertionError("Error")

print(value)