import numpy as np

def soma(va: float, vb: float):
    ''' Função que retorna a soma entre dois valores
    '''
    return va + vb

def sub(va: float, vb: float):
    ''' Função que retorna a subtração entre dois valores
    '''
    return va - vb

def multiplicacao(va: float, vb: float):
    ''' Função que retorna a multiplicação entre dois valores
    '''
    return va * vb

def divisao(va: float, vb: float):
    ''' Função que retorna a divisão entre dois valores
    '''
    if vb == 0:
        return np.inf
    return va / vb

def media_lista_valores(v:list):
    ''' Função que retorna a média entre N valores
    '''
    lista_numeros = []
    for i in v:
        if type(i) is int or type(i) is float:
            lista_numeros.append(i)

    if len(lista_numeros) == 0:
        return 0
    return np.mean(lista_numeros)

print(media_lista_valores([5,7]))