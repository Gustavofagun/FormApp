from flask import Flask, request, render_template
from pymongo import MongoClient
import datetime

app = Flask(__name__)
cliente = MongoClient('localhost', 27017)
banco = cliente['cadastro']
tabela = banco['formulario']

@app.route('/')
def principal():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def mainpage():
	base=banco.tabela
	if request.method == 'POST' and request.form['submit'] == 'save':
		formulario = {
          "nome": request.form['nome'],
          "email": request.form['email'],
          "sugestao": request.form['sugestao'],
          "data": datetime.datetime.now()
         }
		formulario_id = base.insert_one(formulario).inserted_id
		if(formulario_id):
			mensagem = 'Dados Gravados com sucesso'
			return mensagem

if __name__ == '__main__':
    app.run(host='0.0.0.0')
