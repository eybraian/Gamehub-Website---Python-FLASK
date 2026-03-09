from flask import Flask, render_template, request, session, redirect
from jogodaforca_logic import JogodaForca
from pedrapapeltesoura_logic import Pedrapapeltesoura

app = Flask(__name__)
app.secret_key = 'chave_secreta'

#menu
@app.route("/")
def homepage():
    return render_template("menu.html")

#db_manager
@app.route("/db_manager.html")
def db_manager():
    return render_template("db_manager.html")

#pedrapapeltesoura
@app.route('/pedrapapeltesoura.html', methods=["GET", "POST"])
def index():
    resultado = ""
    escolha_jogador = ""
    escolha_maquina = ""

    if request.method =="POST":
        jogo = Pedrapapeltesoura()
        maquina = jogo.get_escolha_maquina()
        jogador = jogo.get_escolha_jogador()
        resultado = jogo.get_vencedor(maquina,jogador)
        match jogador:
            case 1:
                escolha_jogador = "Pedra"
            case 2:
                escolha_jogador = "Papel"
            case 3:
                escolha_jogador = "Tesoura"

        match maquina:
            case 1:
                escolha_maquina = "Pedra"
            case 2:
                escolha_maquina = "Papel"
            case 3:
                escolha_maquina = "Tesoura"

    return render_template('pedrapapeltesoura.html', resultado=resultado, escolha_jogador=escolha_jogador, escolha_maquina=escolha_maquina)

#jogodaforca
@app.route('/jogodaforca.html', methods = ["GET", "POST"])
def jogodaforca():
    jogo_forca = JogodaForca()

    if request.args.get("reset") == "1" or 'jogo' not in session:
        session['jogo'] = jogo_forca.iniciar_novo_jogo()

    estado_jogo = session['jogo']

    if request.method == "POST":
        chute = request.form.get('chute','').strip().upper()

        if chute and len(chute) == 1 and not estado_jogo['jogo_terminado']:
            if chute in estado_jogo['letras_chutadas']:
                estado_jogo['mensagem'] = "Letra já chutada!"
            else:
                estado_jogo['letras_chutadas'].append(chute)

                acertou = False
                for i in range(len(estado_jogo['palavra_secreta'])):
                    if estado_jogo['palavra_secreta'][i] == chute:
                        estado_jogo['palavra_aux'][i] = chute
                        acertou = True

                if not acertou:
                    estado_jogo['erros'] += 1
                    estado_jogo['tentativas_restantes'] -= 1
                
                if '_' not in estado_jogo['palavra_aux']:
                    estado_jogo['jogo_terminado'] = True
                    estado_jogo['mensagem'] = "Parabéns! Você ganhou!"

                if estado_jogo['tentativas_restantes'] <= 0:
                    estado_jogo['jogo_terminado'] = True
                    estado_jogo['mensagem'] = f"Game Over! Palavra: {''.join(estado_jogo['palavra_secreta'])}"

        session['jogo'] = estado_jogo
        return redirect('/jogodaforca.html')

    ascii_art = jogo_forca.arte_status(estado_jogo['erros'])

    return render_template('jogodaforca.html', 
                           ascii_art = ascii_art,
                           palavra_secreta = estado_jogo['palavra_aux'],
                           erros = estado_jogo['erros'],
                           tentativas_restantes = estado_jogo['tentativas_restantes'],
                           letras_chutadas = estado_jogo['letras_chutadas'],
                           jogo_terminado = estado_jogo['jogo_terminado'],
                           mensagem = estado_jogo['mensagem'])

#db_manager
@app.route('/jogodavelha.html')
def jogodavelha():
    return render_template("jogodavelha.html")

if __name__ == "__main__":
    app.run()