import random
import sys


botao = Element("botaoEnviar")
campoSaida = Element("resultado")
campoEntrada = Element("campoTexto")

def obter_valor():
    valor = campoEntrada.value
    campoSaida.write(valor)

botao.element.onkeypress = obter_valor
