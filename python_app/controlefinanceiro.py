from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/planejamento_geral')
def titulo(pagina="Planjemento . Visão Geral"):
    return render_template('template.html', titulo=pagina)
