import pytest
import numpy as np
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores

# SOMA #############################
@pytest.mark.op_simples 
@pytest.mark.positivos
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1, v2)

@pytest.mark.op_simples
def test_soma_um_valor_positivo_um_valor_negativo():
    v1 = -7.0
    v2 = 7.0
    assert 0 == soma(v1,v2)

# SUBTRAÇÃO ###############################
@pytest.mark.positivos
def test_sub_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert -2 == sub(v1, v2)

# MULTIPLICAÇÃO ############################
@pytest.mark.positivos
def test_multiplicacao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 35.0 == multiplicacao(v1,v2)

# DIVISÃO ##################################
@pytest.mark.positivos
def test_divisao_dois_valores_positivos():
    v1 = 35.0
    v2 = 5.0
    assert 7.0 == divisao(v1,v2)

@pytest.mark.exercicio_1
def test_divisao_por_zero():
    v1 = 7.0
    v2 = 0.0
    assert np.inf == divisao(v1,v2)

# MÉDIA ##################################
@pytest.mark.op_complexas
@pytest.mark.positivos
def test_media_lista_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 6.0 == media_lista_valores([v1,v2])

@pytest.mark.exercicio_1
def test_media_com_numeros_e_strings():
    lista = [1, 2, 3, 'mamão']
    assert 2 == media_lista_valores(lista)

@pytest.mark.exercicio_1
def test_media_lista_vazia():
    lista = []
    assert 0 == media_lista_valores(lista)
