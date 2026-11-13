Python
from analizador import contar_frecuencias

def test_contar_frecuencias_basico():
    texto = "hola mundo hola"
    resultado = contar_frecuencias(texto)
    esperado = {"hola": 2, "mundo": 1}
    assert resultado == esperado

def test_contar_frecuencias_vacio():
    texto = ""
    resultado = contar_frecuencias(texto)
    esperado = {}
    assert resultado == esperado

def test_contar_frecuencias_mayusculas():
    texto = "Python PYTHON python"
    resultado = contar_frecuencias(texto)
    esperado = {"python": 3}
    assert resultado == esperado
