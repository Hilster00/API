import requests

nome = "Bruna"
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
pessoas = requests.get(url).json()

print(len(pessoas))
print(pessoas[0])
