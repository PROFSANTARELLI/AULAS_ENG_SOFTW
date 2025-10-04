# tests/test_calculadora.py

import pytest
from app.calculadora import somar

def test_soma_positiva():
    """
    Testa a soma de dois números positivos.
    Cenário: 2 + 3 = 5
    """
    # Preparação (Arrange) - já temos os números
    # Ação (Act)
    resultado = somar(2, 3)
    # Verificação (Assert)
    assert resultado == 5

def test_soma_com_negativo():
    """
    Testa a soma de um número positivo com um negativo.
    Cenário: 10 + (-5) = 5
    """
    assert somar(10, -5) == 5

def test_soma_com_zero():
    """
    Testa a soma de um número com zero.
    Cenário: 7 + 0 = 7
    """
    assert somar(7, 0) == 7

def test_soma_deve_lancar_excecao_com_nao_inteiros():
    """
    Testa se a função lança um TypeError ao receber entradas que não são inteiras.
    """
    with pytest.raises(TypeError):
        somar("2", 3) # "2" é uma string, não um inteiro
