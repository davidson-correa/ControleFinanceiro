from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/planejamento_geral')
def planejamento_geral():
    tcabecalhos = ["Grupo","Tipo","Descrição","Valor Planejado","Valor Consumado"]
    tdados = []
    dados = ['Salário Mensal','Receita Efetiva','Salário LFDA','$3400','3400']
    tdados.append(dados)
    dados = ['Imóvel','Despesa Efetiva','Pagamento Aluguel','$870','870']
    tdados.append(dados)
    return render_template('planejamento_geral.html', tcabecalhos=tcabecalhos, tdados=tdados)

@app.route('/testes')
def testes():
    testes = ["Te amo","Te amo","Te amo"]
    return render_template('teste.html', testes=testes)
