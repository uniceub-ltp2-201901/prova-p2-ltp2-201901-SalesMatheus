# Matheus Carvalho Sales
# 21804995

# Importando bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
import short_url
from bd import *


# Instanciando a app Flask
app = Flask(__name__)
# Instanciar o objeto MySQL
mysql = MySQL()
# Ligar o MYSQL ao Flask
mysql.init_app(app)

config(app)

'''url = short_url.encode_url(12)

print(url)

key = short_url.decode_url(url)

print (key)

id = 2
domain = '127.0.0.1:5000'

shortened_url = "{}/{}".format(
                                     domain,
                                     short_url.encode_url(id)
                               )
'''
# Rota para /
@app.route('/')
def principal():
    return render_template('index.html')

# rota para salvar a alteração
@app.route('/url' , methods=['GET','POST'])
def salvar_url():

    # recuperar os parametros
    url_original = request.form.get('url')

    # recupera conexao e cursor
    conn, cursor = get_db(mysql)

    # função que cadastra url no banco
    url_cadastrar(conn, cursor, url_original)

    # retornando id da ultima url cadastrada
    id_url = get_id_url(cursor)


    # transformando em uma nova url
    url_nova = short_url.encode_url(id_url)

    # Inserindo nova url no banco de daods
    update_nova_url(conn, cursor, id_url, url_nova)

    # dar update na tabela
    return render_template('index.html', nova_url = get_nova_url(id_url, cursor))

    #return redirect(url_for('index'))

# Rota para listar todas urls
@app.route('/urls_novas')
def listar_urls():

    cursor = mysql.get_db().cursor()
    return render_template('url.html', urls=get_urls(cursor))



# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)