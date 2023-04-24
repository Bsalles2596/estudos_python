import requests


cep = input("Digite seu Cep: ")

resp = requests.get(f"https://viacep.com.br/ws/{cep}/json")
cep_json = resp.json()
print(cep_json)
