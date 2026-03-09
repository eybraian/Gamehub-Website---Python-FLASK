from flask import request
import random


class JogodaForca:
    def __init__(self):
        self.lista_palavras = [
            "batata",
            "ameixa",
            "carro",
            "sorvete",
            "python",
            "moeda",
            "telhado",
        ]

    def iniciar_novo_jogo(self):
        palavra = random.choice(self.lista_palavras)
        palavra_upper = palavra.upper()
        print("Palavra Sorteada Com Sucesso! Palavra:" + palavra_upper)
        return {
            "palavra_secreta": list(palavra_upper),
            "palavra_aux": ["_"] * len(palavra_upper),
            "letras_chutadas": [],
            "tentativas_restantes": 6,
            "erros": 0,
            "jogo_terminado": False,
            "mensagem": "",
        }

    def arte_status(self, erros):
        match erros:
            case 0:
                return """
+---+
|   |
    |
    |
    |
    |
========="""
            case 1:
                return """
+---+
|   |
O   |
    |
    |
    |
========="""
            case 2:
                return """
+---+
|   |
O   |
|   |
    |
    |
========="""
            case 3:
                return """
+---+
|   |
O   |
/|  |
    |
    |
========="""
            case 4:
                return """
+---+
|   |
O   |
/|\ |
    |
    |
========="""
            case 5:
                return """
+---+
|   |
O   |
/|\ |
/   |
    |
========="""
            case 6:
                return """
+---+
|   |
O   |
/|\ |
/ \ |
    |
========="""
