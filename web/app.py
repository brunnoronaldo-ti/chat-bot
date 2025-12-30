from flask import Flask, render_template, request
from bot import Bot

app = Flask(__name__)
bot = Bot()
conversa = []  # 👈 histórico em memória

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mensagem = request.form.get("mensagem", "").strip()

        if mensagem:
            resposta = bot.responder(mensagem)

            conversa.append({
                "usuario": mensagem,
                "bot": resposta
            })

    return render_template("index.html", conversa=conversa)

if __name__ == "__main__":
    app.run(debug=True)
