from flask import Flask, render_template
from flask import request   #para trabalhar com os métodos GET e POST
from flask import flash     #para msgs popup
from flask import redirect  #para redirecionar páginas


# os templates coloca em outra pasta. 
# Por padrão, fica na pasta templates e não precisa informar no template_folder,
# mas se quiser armazenar em outra pasta indique nesse parâmetro.
app_vini = Flask(__name__, template_folder='templates') 
# no caso de usar flash pede a configuração de uma chave secreta
app_vini.config['SECRET_KEY'] = "palavra-secreta-IFRO"


@app_vini.route("/")      
@app_vini.route("/index")  
def index():
    return render_template ("t_index.html") 

@app_vini.route("/contato")
def contato():
    return render_template("t_contato.html") 

@app_vini.route("/usuario/<nome_usuario>;<nome_profissao>")
@app_vini.route("/usuario", defaults={"nome_usuario":"usuário?","nome_profissao":""})  

def dados_usuario (nome_usuario, nome_profissao):
    dados_usu = {"profissao": nome_profissao, "disciplina":"Tecnnologia em Análise e Desenvolvimento de Sistemas"}
    return render_template ("t_usuario.html", nome=nome_usuario, dados = dados_usu)  

#new
@app_vini.route("/login")
def login():
    return render_template("t_login_flash_js_cadastro.html")
    
#new
@app_vini.route("/autenticar", methods=['GET', 'POST']) 
def autenticar():
    
    usuario = request.form.get('nome_usuario')
    senha = request.form.get('senha')
    
    if usuario == "admin" and senha == "ifro":
        return f"usuario: {usuario} e senha: {senha}"
    else:
        flash("Dados inválidos!")
        flash("Login ou senha inválidos!")
        return redirect ('/login')


if __name__ == "__main__": 
     app_vini.run(port = 8000) 
     