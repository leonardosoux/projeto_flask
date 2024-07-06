from flask import Flask, render_template, request, redirect, url_for 
from validate_docbr import CPF, CNPJ


def lista_produtos():
    with open("produtos.csv",'r') as file:
        lista_produtos = []
        for linha in file:
            nome, descricao, preco, imagem = linha.strip().split(",")
            produto={
                "nome": nome,
                "descricao": descricao,
                "preço": float(preco),
                "imagem": imagem
            }

            lista_produtos.append(produto)
    return lista_produtos

def adicionar_produto(p): 
    linha = f"\n{p['nome']},{p['descricao']},{p['preco']},{p['imagem']}"
    with open("produtos.csv",'a') as file:
        file.write(linha)

# [ 
#    {"nome": "Coca-cola", "descricao": "veneno", "preco": "10,00", "imagem": "https://www.coca-cola.com.br/assets/images/home/no-sugar/mobile/414w/no-sugar-banner.png?v=7a2730c7709c993e22636bc201ef6118" },
#    {"nome": "Doritos", "descricao": "suja mão","preco": "7,00", "imagem": "https://http2.mlstatic.com/D_NQ_NP_843674-MLB75571159538_042024-O.webp" },
#   {"nome": "Água", "descricao": "mata sede", "preco": "2,50", "imagem": "https://fontagua.com.br/wp-content/uploads/2019/02/FONTAGUA_GARRAFA-350ML-GAS.jpg"},
#]

app = Flask("minha app")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos", methods=['GET', 'POST'])
def produtos():
    return render_template("produtos.html", produtos=lista_produtos())

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos():
        if produto['nome'].lower() == nome.lower():
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

@app.route("/gerarCPF")
def gerar_cpf():
    cpf = CPF()
    novo_cpf = cpf.generate()
    return render_template("gerarCPF.html", exibir_cpf=novo_cpf)

@app.route("/validarCPF")
def validacao_cpf():
    return render_template("validarCPF.html")

app.route("/validar-CPF", methods=["POST"])
def validar_cpf():
    cpf_validate = request.form['cpf']
    cpf = CPF()
    if cpf.validate(cpf_validate):
        result = {"status":"CPF Válido","info":cpf_validate}
    else:
        result = {"status":"CPF Inválido","info":cpf_validate}
    return render_template('resultado.html',result=result)

@app.route("/gerarCNPJ")
def gerar_cnpj():
    cnpj = CNPJ()
    novo_cnpj = cnpj.generate()
    return render_template("gerarCNPJ.html", exibir_cnpj=novo_cnpj)

@app.route("/validarCNPJ")
def validacao_cnpj():
    return render_template("validarCNPJ.html")

@app.route("/validar-CNPJ", methods=['POST'])
def validar_cnpj():
    cnpj_validate = request.form['cnpj']
    cnpj = CNPJ()
    if cnpj.validate(cnpj_validate):
        result = {"status":"CNPJ Válido","info":cnpj_validate}
    else:
        result = {"status":"CNPJ Inválido","info":cnpj_validate}
    return render_template('resultado.html',result=result)


    
