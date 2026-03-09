from flask import request
import random

class Pedrapapeltesoura():
    def get_escolha_maquina(self):
        numero_maquina = random.randint(1,3)
        return numero_maquina
    
    def get_escolha_jogador(self):
        numero_jogador = request.form['numero_escolhido']
        return int(numero_jogador)

    def get_vencedor(self, maquina, jogador):
        if maquina == jogador:
            return "Empate!"
        else:
            if ((maquina == 1 and jogador == 2) or (maquina == 2 and jogador == 3) or (maquina == 3 and jogador == 1)):
                return "Jogador!"
            else:
                return "Máquina!"