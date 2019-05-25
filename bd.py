from flaskext.mysql import MySQL

# função para configurar o acesso a banco
def config(app):
    # Configurando o acesso ao MySQL
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'prova2'

# Retorna conexao e cursor
def get_db(mysql):
    # Obtendo o cursor para acessar o BD
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

#insere url
def url_cadastrar(conn,cursor, url_original):
    print(url_original)
    cursor.execute(f'INSERT INTO prova2.url (original_url) VALUES ({url_original})')
    conn.commit()

# Pega ID
def get_id_url(cursor):

    cursor.execute(f'SELECT max(id_url) FROM prova2.url')


    # Recuperando o retorno do BD
    id_url = cursor.fetchone()

    # Retornar os dados
    return id_url[0]


# Atualiza a tabela
def update_nova_url(conn, cursor, id_url, url_nova):
    cursor.execute(f'update prova2.url SET nova_url = "{url_nova}" WHERE id_url = {id_url}')
    conn.commit()