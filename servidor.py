import requests, json

class Servidor:
    def __init__(self):
        super().__init__()
    
    def enviar_novo_usuario(self, dados):

        url = 'http://127.0.0.1:5000/api-rest'

        usuario = {
            'desc': 'NOVO USUARIO',
            'nome': dados[0],
            'email': dados[1],
            'password': dados[2]
        }

        resposta = requests.post(url, json=usuario)

        if resposta.ok:
            dado = json.loads(resposta.text)
            resposta = dado.get('resposta', [])

            if resposta == 'Usuário >> {nome} << Inserido Com Sucesso!':
                resposta = f'Usuário >> {usuario["nome"]} << Inserido Com Sucesso!'

                return resposta
            
            else:
                return resposta

        return 

    def buscar_todos_usuarios(self):
        
        url = 'http://127.0.0.1:5000/api-rest'

        requisicao = {
            'desc': 'PEGAR TODOS USUARIOS'
        }

        resposta = requests.post(url, json=requisicao)
        
        if resposta.ok:
            dados = json.loads(resposta.text)
            usuarios = dados.get('usuarios', [])

            return usuarios

        else:
            print('-=-' * 20)
            print('Erro')
            print('-=-' * 20)

    def alterar_usuario(self, alteracoes, id):
        
        url = 'http://127.0.0.1:5000/api-rest'

        usuario = {
            'desc': 'ALTERAR DADOS USUARIO',
            'dados': alteracoes,
            'id': id
        }

        resposta = requests.post(url, json=usuario)

        if resposta.ok:
            dado = json.loads(resposta.text)
            resposta = dado.get('resposta', [])

            return resposta

    def deletar_usuario(self, id):
        
        url = 'http://127.0.0.1:5000/api-rest'

        usuario = {
            'desc': 'DELETAR USUARIO',
            'id': id
        }

        resposta = requests.post(url, json=usuario)

        if resposta.ok:
            dado = json.loads(resposta.text)
            resposta = dado.get('resposta', [])

            return resposta