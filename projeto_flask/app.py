from flask import Flask, render_template, request, redirect, url_for 

lista_produtos = [ 
    {"nome": "Coca-cola", "descricao": "veneno", "preco": "10,00", "imagem": "https://www.coca-cola.com.br/assets/images/home/no-sugar/mobile/414w/no-sugar-banner.png?v=7a2730c7709c993e22636bc201ef6118" },
    {"nome": "Doritos", "descricao": "suja mão","preco": "7,00", "imagem": "https://http2.mlstatic.com/D_NQ_NP_843674-MLB75571159538_042024-O.webp" },
    {"nome": "Água", "descricao": "mata sede", "preco": "2,50", "imagem": "https://fontagua.com.br/wp-content/uploads/2019/02/FONTAGUA_GARRAFA-350ML-GAS.jpg"},
]

app = Flask("minha app")

@app.route("/")
def home():
    return render_template("home.html")

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
            return render_template("produto.html", produto=produto) 
    return "produto não existe"

# GET
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

# POST
@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = request.form['preco']
    imagem = request.form['imagem']
    produto = {"nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))
