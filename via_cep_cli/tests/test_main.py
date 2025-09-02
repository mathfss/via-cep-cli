import os
import pytest
from unittest.mock import patch
import requests
from via_cep_cli import main

# -------------------- Testes Positivos --------------------

@patch("requests.get")
def test_buscar_cep_valido(mock_get, capsys):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "logradouro": "Praça da Sé",
        "bairro": "Sé",
        "localidade": "São Paulo",
        "uf": "SP"
    }
    main.buscar_cep("01001000")
    captured = capsys.readouterr()
    assert "Praça da Sé" in captured.out

@patch("requests.get")
def test_buscar_cep_valido_sem_logradouro(mock_get, capsys):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "bairro": "Centro",
        "localidade": "Cidade X",
        "uf": "MG"
    }
    main.buscar_cep("37540000")
    captured = capsys.readouterr()
    assert "Centro" in captured.out

@patch("requests.get")
def test_buscar_cep_salvar_arquivo(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "logradouro": "Rua A",
        "bairro": "Bairro B",
        "localidade": "Cidade C",
        "uf": "SP"
    }
    main.buscar_cep("01001001", salvar=True)
    assert os.path.exists("resultado.txt")
    with open("resultado.txt", "r", encoding="utf-8") as f:
        assert "Rua A" in f.read()
    os.remove("resultado.txt")

@patch("requests.get")
def test_buscar_cep_retorna_dict(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"logradouro": "Rua X", "bairro": "Bairro Y", "localidade": "Cidade Z", "uf": "SP"}
    data = main.buscar_cep("01001002", retornar_dict=True)
    assert isinstance(data, dict)
    assert data["logradouro"] == "Rua X"

def test_formatar_endereco_completo():
    data = {"logradouro": "Rua A", "bairro": "Bairro B", "localidade": "Cidade C", "uf": "MG"}
    endereco = main.formatar_endereco(data)
    assert endereco == "Rua A, Bairro B, Cidade C-MG"

def test_formatar_endereco_faltando_campos():
    data = {"localidade": "Cidade C", "uf": "MG"}
    endereco = main.formatar_endereco(data)
    assert endereco == "Cidade C-MG"

@patch("requests.get")
def test_buscar_cep_vazio_logradouro(mock_get, capsys):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"bairro": "Centro", "localidade": "BH", "uf": "MG"}
    main.buscar_cep("30140071")
    captured = capsys.readouterr()
    assert "BH" in captured.out

@patch("requests.get")
def test_dois_ceps_consecutivos(mock_get, capsys):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.side_effect = [
        {"logradouro": "Rua 1", "bairro": "Bairro 1", "localidade": "Cidade 1", "uf": "SP"},
        {"logradouro": "Rua 2", "bairro": "Bairro 2", "localidade": "Cidade 2", "uf": "RJ"},
    ]
    main.buscar_cep("11111111")
    main.buscar_cep("22222222")
    captured = capsys.readouterr()
    assert "Rua 1" in captured.out and "Rua 2" in captured.out

def test_formatar_endereco_strip_extra():
    data = {"logradouro": "", "bairro": "", "localidade": "Cidade C", "uf": ""}
    endereco = main.formatar_endereco(data)
    assert endereco == "Cidade C"

@patch("requests.get")
def test_buscar_cep_valido_msg_correta(mock_get, capsys):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"logradouro": "Rua A", "bairro": "Bairro B", "localidade": "Cidade C", "uf": "SP"}
    main.buscar_cep("01001000")
    captured = capsys.readouterr()
    assert "Endereço encontrado" in captured.out

# -------------------- Testes Negativos --------------------

def test_cep_com_menos_de_8_digitos(capsys):
    main.buscar_cep("123")
    captured = capsys.readouterr()
    assert "CEP inválido" in captured.out

def test_cep_com_mais_de_8_digitos(capsys):
    main.buscar_cep("123456789")
    captured = capsys.readouterr()
    assert "CEP inválido" in captured.out

def test_cep_com_letras(capsys):
    main.buscar_cep("ABC12345")
    captured = capsys.readouterr()
    assert "CEP inválido" in captured.out

def test_cep_vazio(capsys):
    main.buscar_cep("")
    captured = capsys.readouterr()
    assert "CEP inválido" in captured.out

@patch("requests.get")
def test_api_retorna_erro(mock_get, capsys):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"erro": True}
    main.buscar_cep("99999999")
    captured = capsys.readouterr()
    assert "não encontrado" in captured.out.lower()

@patch("requests.get")
def test_api_status_404(mock_get, capsys):
    mock_get.return_value.status_code = 404
    main.buscar_cep("01001001")
    captured = capsys.readouterr()
    assert "404" in captured.out

@patch("requests.get", side_effect=requests.exceptions.Timeout)
def test_api_timeout(mock_get, capsys):
    main.buscar_cep("01001002")
    captured = capsys.readouterr()
    assert "timeout" in captured.out.lower()

@patch("requests.get", side_effect=requests.exceptions.ConnectionError)
def test_api_connection_error(mock_get, capsys):
    main.buscar_cep("01001003")
    captured = capsys.readouterr()
    assert "falha na conexão" in captured.out.lower()

@patch("requests.get")
def test_api_resposta_invalida(mock_get, capsys):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.side_effect = ValueError("JSON inválido")
    main.buscar_cep("01001004")
    captured = capsys.readouterr()
    assert "não é um JSON válido" in captured.out

@patch("requests.get")
def test_buscar_cep_sem_logradouro_negativo(mock_get, capsys):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"bairro": "Centro"}
    main.buscar_cep("01001005")
    captured = capsys.readouterr()
    assert "Centro" in captured.out

