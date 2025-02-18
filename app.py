
from flask import Flask, request, render_template, redirect
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/index.html')


@app.route('/submit', methods=['POST'])
def submit_API():
    nome = request.form['nome']  # Pegando o valor do campo "nome"
    email = request.form['email']  # Pegando o valor do campo "email"
    empresa = request.form['empresa']  # Pegando o valor do campo "empresa"
    telefone = request.form['telefone']  # Pegando o valor do campo "telefone"
    mensagem = request.form['mensagem']  # Pegando o valor do campo "mensagem"
    
    response = requests.post('https://formsubmit.co/miguelneto275@gmail.com', data= {'nome': nome, 'email': email, 'empresa': empresa , 'telefone': telefone, 'mensagem': mensagem})

    
    if response.status_code == 200: #200 indica que a requisição foi bem sucedida
        return render_template('index.html', sucesso=True)
        
    else:
        return render_template('index.html', sucesso=False)
    
    
if __name__ == '__main__':
    app.run(debug=True)

