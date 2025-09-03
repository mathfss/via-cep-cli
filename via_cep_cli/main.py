import requests

def formatar_endereco(data: dict) -> str:
    """
    Monta o endereço a partir dos campos retornados pela API.
    Ignora campos ausentes e remove vírgulas/hífens extras.
    """
    partes = []
    if data.get("logradouro"):
        partes.append(data["logradouro"])
    if data.get("bairro"):
        partes.append(data["bairro"])
    if data.get("localidade"):
        cidade_estado = data["localidade"]
        if data.get("uf"):
            cidade_estado += f"-{data['uf']}"
        partes.append(cidade_estado)

    return ", ".join(partes).strip(", -")

def buscar_cep(cep: str, salvar: bool = False, retornar_dict: bool = False):
    """
    Busca um CEP na API ViaCEP.
    - salva em resultado.txt se salvar=True
    - retorna o dicionário se retornar_dict=True
    """
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Informe exatamente 8 números.")
        return None

    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            try:
                data = response.json()
            except ValueError:
                print("Erro: resposta da API não é um JSON válido.")
                return None

            if "erro" in data:
                print("CEP não encontrado.")
                return None

            endereco = formatar_endereco(data)
            print(f"Endereço encontrado: {endereco}")

            if salvar:
                with open("resultado.txt", "w", encoding="utf-8") as f:
                    f.write(endereco)

            if retornar_dict:
                return data
        else:
            print(f"Erro: API retornou status {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("Erro: requisição excedeu o tempo limite (timeout).")
        return None
    except requests.exceptions.ConnectionError:
        print("Erro: falha na conexão com a API.")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None


if __name__ == "__main__":
    cep_input = input("Digite um CEP: ").strip()
    buscar_cep(cep_input, salvar=True)
