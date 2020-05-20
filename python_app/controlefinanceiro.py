from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/planejamento_geral', methods=["POST", "GET"])
def planejamento_geral():
    tcabecalhos = ["Grupo","Tipo","Descrição","Valor Planejado","Valor Consumado"]
    tdados = []
    req = request.form
    grupo = req.get("grupo")
    tipo = req.get("tipo")
    descricao = req.get("descricao")
    valorplanejado = req.get("valorplanejado")
    valorconsumado = req.get("valorconsumado")
    dados = [grupo,tipo,descricao,valorplanejado,valorconsumado]
    tdados.append(dados)
    #dados = ['Imóvel','Despesa Efetiva','Pagamento Aluguel','$870','870']
    #tdados.append(dados)
    return render_template('planejamento_geral.html', tcabecalhos=tcabecalhos, tdados=tdados)

@app.route('/planejamento_geral/novo')
def plang_novo():
    return render_template('plang_novo.html')

@app.route('/testes')
def testes():
    testes = ["Te amo","Te amo","Te amo"]
    return render_template('teste.html', testes=testes)
