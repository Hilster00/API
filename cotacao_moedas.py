import requests
def buscar_dados(url):
    try:
        response = requests.get(url)
        # Verifica se a requisição foi bem sucedida (status code 200)
        if response.status_code == 200:
            # Retorna os dados da API no formato JSON
            return response.json()
        else:
            print(f"Erro ao fazer a requisição: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

moedas = ('Iene Japonês','Real Brasileiro', 'Dólar Americano', 'Euro')

#moedas a serem comparadas
while (moeda := input(f"Digite a moeda desejada {moedas}:")) not in moedas:
    ...
while (meda_comparada := input(f"Digite a moeda desejada {moedas}:")) not in moedas:
    ...


moedas = {
'Iene Japonês':'JPY',
'Real Brasileiro':'BRL',
'Dólar Americano':'USD',
'Euro':'EUR'
}

dados=buscar_dados(f"https://economia.awesomeapi.com.br/last/{moedas[moeda]}-{moedas[meda_comparada]}")
dados=dados[f"{moedas[moeda]}{moedas[meda_comparada]}"]
print(f'Compra: {dados["bid"]}')
print(f'Venda: {dados["ask"]}')
print(f'Variação: {dados["varBid"]}')
print(f'Máximo: {dados["high"]}')
print(f'Mínimo: {dados["low"]}')


              
