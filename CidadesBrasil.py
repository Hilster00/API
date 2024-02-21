import requests

def buscar_dados_da_api(url):
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

# Exemplo de URL de uma API
url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"

# Chama a função para buscar os dados da API
estados = buscar_dados_da_api(url)



# Verifica se os dados foram recebidos com sucesso
if estados:
    print("Lista de estados:",end="")
    nomes_estados={}
    for i in estados:
        print(f"{i['sigla']},",end="")
        nomes_estados[i['sigla']] = i["nome"]
        
    print()
    while (estado:=input("Digite a sigla do estado:").upper()) in nomes_estados:
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/municipios"
        cidades = buscar_dados_da_api(url)
        print(f"O estado {nomes_estados[estado]}[{estado}] tem {len(cidades)} cidades")
        if input("Deseja a lista de cidades?:")[0].lower() == "s":
            with open(f"Cidades - {estado}.txt","a") as arquivo:
                for cidade in cidades:
                    arquivo.write(f"{cidade['nome']},\n")

    print("Programa finalizado") 
    
        
        
else:
    print("Não foi possível obter os dados da API.")
