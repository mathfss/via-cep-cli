import requests

def buscar_cep(cep: str, salvar: bool = False):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "erro" in data:
            print("CEP não encontrado.")
        else:
            endereco = f"{data['logradouro']}, {data['bairro']}, {data['localidade']}-{data['uf']}"
            print(f"Endereço achado: {endereco}")

            if salvar:
                with open("enderecos.txt", "a", encoding="utf-8") as f:
                    f.write(f"{cep}: {endereco}\n")
                print("Endereço salvo em 'enderecos.txt'")
    else:
        print("Erro na requisição.")

if __name__ == "__main__":
    cep = input("Digite o CEP: ").strip()
    opcao = input("Deseja salvar o resultado em um arquivo? (s/n): ").strip().lower()
    buscar_cep(cep, salvar=(opcao == "s"))
