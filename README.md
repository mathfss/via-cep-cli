
# 📦 Via CEP CLI

Um **CLI em Python** que consulta endereços através do serviço **ViaCEP**.

---

## 🚀 Funcionalidades
- Consulta de endereço a partir de um CEP.
- Retorno formatado diretamente no terminal.

---

## 🛠️ Configuração do Ambiente

### 1. Clonar o repositório
```bash
git clone https://github.com/mathfss/via-cep-cli.git
cd via-cep-cli
````

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar ambiente virtual

* Windows:

```bash
.venv\Scripts\activate
```

* Linux/Mac:

```bash
source .venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

Ou, se estiver usando **Poetry**:

```bash
poetry install
```

---

## ▶️ Execução do CLI

```bash
python -m via_cep_cli.main
```

Exemplo de uso:

```bash
Digite o CEP: 37540-000
Rua: Av. João de Camargo
Bairro: Centro
Cidade: Santa Rita do Sapucaí - MG
```

---

## 🧪 Build

Se estiver usando **Poetry**:

```bash
poetry build
```

Isso vai gerar os arquivos na pasta `dist/`.


---

## 🧪 Testes Unitários

O projeto conta com uma suíte de testes unitários implementada com **pytest**, cobrindo cenários **positivos** e **negativos** da aplicação.

### ▶️ Executando os testes

1. Certifique-se de ter instalado as dependências do projeto:

   ```bash
   poetry install
   ```

2. Execute os testes com o comando:

   ```bash
   poetry run pytest -v
   ```

3. Exemplo de saída esperada (todos os testes passando):

   ```
   ================================================= test session starts =================================================
   platform win32 -- Python 3.13
   collected 20 items

   via_cep_cli/tests/test_main.py::test_buscar_cep_valido PASSED
   via_cep_cli/tests/test_main.py::test_buscar_cep_valido_sem_logradouro PASSED
   ...
   via_cep_cli/tests/test_main.py::test_buscar_cep_sem_logradouro_negativo PASSED

   =============================================== 20 passed in 2.10s ====================================================
   ```

### 📝 Estrutura de testes

* **10 testes positivos** → validam o funcionamento esperado (CEPs válidos, salvamento em arquivo, formatação correta, etc).
* **10 testes negativos** → validam situações de erro (CEP inválido, CEP inexistente, API fora do ar, timeout, JSON inválido, etc).

Esses testes garantem que o código continue funcionando mesmo após alterações futuras, evitando regressões.

---

### 🐞 Simulação de Regressão
Um colega removeu parte do código, e ao rodar os testes a falha foi identificada:

<img width="1867" height="294" alt="image" src="https://github.com/user-attachments/assets/4470974e-d745-4b0f-8397-8ca53021cf28" />

Após corrigir a regressão do código os testes passaram normalmente:

<img width="1867" height="429" alt="image" src="https://github.com/user-attachments/assets/3edaf8f1-2b73-4a92-a6b8-87c7b80a6f28" />





