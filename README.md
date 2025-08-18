
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

*passo a passo prático dos comandos Git para cada etapa** (branch, PR, conflito, stash, revert, rebase) para você só seguir como se fosse um roteiro?
