import requests


nome_filme = input("Digite o filme (ingles): ")

def get_movies(nome):

    chave_key = "696e2563"
    OMDb_API= f"http://www.omdbapi.com/?apikey={chave_key}&t={nome}"
    r = requests.get(OMDb_API)
    return r.json()

print(get_movies(nome_filme))
