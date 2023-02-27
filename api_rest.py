from flask import Flask, request
import funcoes_sql

app = Flask(__name__)
banco = funcoes_sql.BancoDeDados()

@app.route('/api-rest', methods=['GET', 'POST'])
def api_rest():
    if request.method == 'POST':
        resposta = request.get_json()
        if resposta['desc'] == 'PEGAR TODOS USUARIOS':

            banco.conectar()
            usuarios = banco.pegar_usuarios()
            banco.desconetar()

            return {'usuarios': usuarios}

        elif resposta['desc'] == 'NOVO USUARIO':
        
            banco.conectar()
            resposta = banco.novo_usuario(resposta['nome'], resposta['email'], resposta['password'])
            banco.desconetar()

            return {'resposta': resposta}

        elif resposta['desc'] == 'ALTERAR DADOS USUARIO':

            banco.conectar()
            resposta = banco.alterar_informacoes(resposta['dados'], resposta['id'])
            banco.desconetar()

            return {'resposta': resposta}

        elif resposta['desc'] == 'DELETAR USUARIO':

            banco.conectar()
            resposta = banco.deletar_login(resposta['id'])
            banco.desconetar()

            return {'resposta': resposta}

    return 'API REST'


if __name__ == '__main__':
    app.run(debug=True)