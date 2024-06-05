from flask import Flask, render_template #(importação da classe Flask)

lista_produtos = [ 
    {"nome": "Coca-cola", "descricao": "veneno"},
    {"nome": "Doritos", "descricao": "suja mão"},
    {"nome": "Água", "descricao": "mata sede"},
]

app = Flask("minha app")

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return f"{produto['nome']}, {produto['descricao']}"
    return "produto não existe"
