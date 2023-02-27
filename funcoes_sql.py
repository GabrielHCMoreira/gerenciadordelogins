from random import choice
import sqlite3
import string

class BancoDeDados:
    def __init__(self):
        super().__init__()
        
        
    def conectar(self):
        self.banco = sqlite3.connect('C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\Python\\SQLite\\GerenciadorDeLogins\\banco_de_dados.db')
        self.cursor = self.banco.cursor()
        
    def desconetar(self):
        self.banco.close()

    def pegar_usuarios(self):
        self.cursor.execute('SELECT * FROM logins')
        self.dados = self.cursor.fetchall()

        self.banco.commit()
        self.desconetar()
        
        return self.dados


    def novo_usuario(self, nome='', email='', password=''):
        if nome == '' or email == '' or password == '':
            return 'Informações De Usuário Inválidas.'
        
        elif len(nome) < 6:
            return 'Nome Deve Conter Mais De 6 Caracteres.'

        elif '@gmail.com' not in email:
            return 'Email Inválido.'
        
        elif len(password) < 6:
            return 'Senha Deve Conter Mais De 6 Caracteres.'
        
        else:
            tamanho = 10    
            valores = string.ascii_uppercase + string.digits
            id = ''

            for c in range(tamanho):
                id += choice(valores)
            
            self.cursor.execute('SELECT * FROM logins WHERE id = ?', (id,))
            verificao = self.cursor.fetchall()
            
            if len(verificao) == 0:
                self.cursor.execute('INSERT INTO logins VALUES (?, ?, ?, ?)', (nome, email, password, id,))
                
                del verificao

                self.cursor.execute('SELECT * FROM logins WHERE id = ?', (id,))
                verificao = self.cursor.fetchall()

                if len(verificao) == 1:
                    
                    self.banco.commit()
                    self.desconetar()

                    return 'Usuário >> {nome} << Inserido Com Sucesso!'

            else:
                id = ''

                while True:
                    for c in range(tamanho):
                        id += choice(valores)
                    
                    self.cursor.execute('SELECT * FROM logins WHERE id = ?', (id,))
                    verificao = self.cursor.fetchall()

                    if verificao == 0:
                        break
                
                self.cursor.execute('INSERT INTO logins VALUES (?, ?, ?, ?)', (nome, email, password, id,))
                
                del verificao

                self.cursor.execute('SELECT * FROM logins WHERE id = ?', (id,))
                verificao = self.cursor.fetchall()

                if len(verificao) == 1:
                    
                    self.banco.commit()
                    self.desconetar()
                    
                    return 'Usuário >> {nome} << Inserido Com Sucesso!'

    def alterar_informacoes(self, alteracao, id=''):
        if alteracao == '' or id == '':
            return 'Informações Inválidas.'
        
        elif len(id) == 10: 
            if len(alteracao) != 3:
                return 'Faltando Dados.'

            else:
                if len(alteracao[0]) < 6:
                    return 'Valor Nome Inválido.'

                elif type(alteracao[1]) != str:
                    return 'Valor Email Inválido.'
                
                elif '@gmail.com' not in alteracao[1]:
                    return 'Valor Email Inválido.'

                elif len(alteracao[2]) < 6:
                    return 'Valor Senha Inválido.'

                else:  
                    self.cursor.execute('SELECT * FROM logins WHERE id = ?', (id,))
                    dados = self.cursor.fetchall()

                    if len(dados) == 1:

                        self.cursor.execute('UPDATE logins SET nome = ? WHERE id = ?', (alteracao[0], id))
                        self.cursor.execute('UPDATE logins SET email = ? WHERE id = ?', (alteracao[1], id))
                        self.cursor.execute('UPDATE logins SET password = ? WHERE id = ?', (alteracao[2], id))

                        self.banco.commit()
                        self.desconetar()

                        return 'Dados Alterados Com Sucesso!'
            
                    else:
                        return 'Usuário Não Encontrado!'       

        else:
            return 'ID Inválido.'
        
        self.banco.commit()
        self.desconetar()
 
    def deletar_login(self, id=''):
        if len(id) != 10:
        
            self.banco.commit()
            self.desconetar()

            return 'ID Inválido.'
        
        else:
            self.cursor.execute('SELECT * FROM logins WHERE id = ?', (id,))
            dado = self.cursor.fetchall()

            if len(dado) != 0:
                self.cursor.execute('DELETE FROM logins WHERE id = ?', (id,))

                self.banco.commit()
                self.desconetar()

                return 'Usuário >> '+ dado[0][0] +' << Deletado Com Sucesso!'        
            
            else:
                return 'Usuário Não Encontrado.'
        