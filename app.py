"""
Casa Inteligente
    Autor: Júlia Onora da Silva
    Data: 31 de março de 2022
"""

from flask import Flask, render_template

app = Flask(__name__)

state = {
    'geladeira': False,
    'liquidificador': False,
    'fogao': False,
    'lampada': False
}


@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/princ")
def index():
    text_to_display = ""
    return render_template("principal.html", text_to_display=text_to_display)

@app.route("/princ/gel_on")  # Inicializa a rotina do estado onde a geladeira está ligada, já na página principal
def gel_on(): # Declaração da função “gel_on()”
    state["geladeira"] = True   # Muda o vetor de estados cuja a chave é geladeira, que inicialmente está como falso, para “True”

    print(state) # Apresenta o vetor de estados dos componentes no terminal
    text_to_display = "Você ligou a geladeira!"  # Apresenta o texto para identificar a mudança de estado do componente

    return render_template("principal.html", text_to_display=text_to_display)
 # Retorna, já no navegador do usuário a página “principal.html” mas agora apresentando o texto do display

@app.route("/princ/gel_off")
def gel_off():
    state["geladeira"] = False
    print(state)
    text_to_display = "Você desligou a geladeira!"
    return render_template("principal.html", text_to_display=text_to_display)


@app.route("/princ/liq_on")
def liq_on():
    state["liquidificador"] = True
    print(state)
    text_to_display = "Você ligou o liquidificador!"
    return render_template("principal.html", text_to_display=text_to_display)

@app.route("/princ/liq_off")
def liq_off():
    state["liquidificador"] = False
    print(state)
    text_to_display = "Você desligou o liquidificador!"
    return render_template("principal.html", text_to_display=text_to_display)


@app.route("/princ/fog_on")
def fog_on():
    state["fogao"] = True
    print(state)
    text_to_display = "Você ligou o fogão!"
    return render_template("principal.html", text_to_display=text_to_display)

@app.route("/princ/fog_off")
def fog_off():
    state["fogao"] = False
    print(state)
    text_to_display = "Você desligou o fogão!"
    return render_template("principal.html", text_to_display=text_to_display)

@app.route("/princ/lamp_on")
def lamp_on():
    state["lampada"] = True
    print(state)
    text_to_display = "Você ligou a lampada!"
    return render_template("principal.html", text_to_display=text_to_display)

@app.route("/princ/lamp_off")
def lamp_off():
    state["lampada"] = False
    print(state)
    text_to_display = "Você desligou a lampada!"
    return render_template("principal.html", text_to_display=text_to_display)

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8089)