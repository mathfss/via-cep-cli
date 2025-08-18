import requests

def buscar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "erro" in data:
            print("CEP não encontrado.")
        else:
            print(f"Endereço: {data['logradouro']}, {data['bairro']}, {data['localidade']}-{data['uf']}")
    else:
        print("Erro na requisição.")

if __name__ == "__main__":
    cep = input("Digite o CEP: ").strip()
    buscar_cep(cep)
