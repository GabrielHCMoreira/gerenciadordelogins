import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import servidor


class MeuApp(QWidget):
    def __init__(self):
        super().__init__()

        self.servidor = servidor.Servidor()
        self.dados = self.servidor.buscar_todos_usuarios()

        self.setWindowTitle("App")
        self.setFixedSize(QSize(1200, 700))
        self.setStyleSheet('''background-color: #222''')

        self.titulo = QLabel('Gerenciador de Logins', self)
        self.titulo.setGeometry(QRect(50, 10, 300, 25))
        self.titulo.setStyleSheet('''font-size: 17px; color: white''')

        self.botoes = QListWidget(self)
        self.botoes.setGeometry(QRect(10, 50, 200, 90))
        self.botoes.setStyleSheet(
            '''background-color: white; border: 1px solid black''')
        self.botoes.currentRowChanged.connect(self.mudar_layout)

        self.botao_ver_logins = QListWidgetItem('Visualizar Logins')
        self.botoes.addItem(self.botao_ver_logins)
        self.botao_adicionar_login = QListWidgetItem('Adicionar Novo Usuário')
        self.botoes.addItem(self.botao_adicionar_login)
        self.botao_alterar_login = QListWidgetItem('Alterar Dados Do Usuário')
        self.botoes.addItem(self.botao_alterar_login)
        self.botao_deletar_usuario = QListWidgetItem('Deletar Usuário')
        self.botoes.addItem(self.botao_deletar_usuario)

        self.layout_logins = QWidget()
        self.layout_logins.setStyleSheet('''background-color: white''')

        self.layout_adicionar_login = QWidget()
        self.layout_adicionar_login.setStyleSheet('''background-color: white''')

        self.layout_alterar_login = QWidget()
        self.layout_alterar_login.setStyleSheet('''background-color: white''')

        self.layout_deletar_usuario = QWidget()
        self.layout_deletar_usuario.setStyleSheet('''background-color: white''')

        self.titulo_layout_adicionar_login = QLabel('Adicionar Usuário', self.layout_adicionar_login)
        self.titulo_layout_adicionar_login.move(10, 10)
        self.titulo_layout_adicionar_login.setStyleSheet('''font-size: 23px''')

        self.label_nome_layout_adicionar_login = QLabel('Nome:', self.layout_adicionar_login)
        self.label_nome_layout_adicionar_login.move(15, 60)
        self.label_nome_layout_adicionar_login.setStyleSheet('''font-size: 17px''')
        self.label_email_layout_adicionar_login = QLabel('E-mail:', self.layout_adicionar_login)
        self.label_email_layout_adicionar_login.move(15, 106)
        self.label_email_layout_adicionar_login.setStyleSheet('''font-size: 17px''')
        self.label_senha_layout_adicionar_login = QLabel('Senha:', self.layout_adicionar_login)
        self.label_senha_layout_adicionar_login.move(15, 152)
        self.label_senha_layout_adicionar_login.setStyleSheet('''font-size: 17px''')
        self.label_status_layout_adicionar_login = QLabel('', self.layout_adicionar_login)
        self.label_status_layout_adicionar_login.move(15, 228)
        self.label_status_layout_adicionar_login.setStyleSheet('''font-size: 17px''') 

        self.input_nome_layout_adicionar_login = QLineEdit(self.layout_adicionar_login)
        self.input_nome_layout_adicionar_login.setGeometry(70, 60, 270, 25)
        self.input_nome_layout_adicionar_login.setStyleSheet('''border: 1px solid #222''')
        self.input_email_layout_adicionar_login = QLineEdit(self.layout_adicionar_login)
        self.input_email_layout_adicionar_login.setGeometry(70, 106, 270, 25)
        self.input_email_layout_adicionar_login.setStyleSheet('''border: 1px solid #222''')
        self.input_senha_layout_adicionar_login = QLineEdit(self.layout_adicionar_login)
        self.input_senha_layout_adicionar_login.setGeometry(70, 152, 270, 25)
        self.input_senha_layout_adicionar_login.setStyleSheet('''border: 1px solid #222''')

        self.botao_criar_usuario_layout_adicionar_login = QPushButton('Criar Usuário', self.layout_adicionar_login)
        self.botao_criar_usuario_layout_adicionar_login.setGeometry(150, 190, 190, 25)
        self.botao_criar_usuario_layout_adicionar_login.setStyleSheet('''border: 1px solid #222''')
        self.botao_atualizar_tabela_layout_adicionar_login = QPushButton('Recarregar Tabela', self.layout_logins)
        self.botao_atualizar_tabela_layout_adicionar_login.setGeometry(700, 555, 190, 35)
        self.botao_atualizar_tabela_layout_adicionar_login.setStyleSheet('''border: 1px solid #222''')

        self.titulo_layout_alterar_dados = QLabel('Alterar Dados', self.layout_alterar_login)
        self.titulo_layout_alterar_dados.move(10, 10)
        self.titulo_layout_alterar_dados.setStyleSheet('''font-size: 23px''')

        self.label_nome_layout_alterar_login = QLabel('Nome:', self.layout_alterar_login)
        self.label_nome_layout_alterar_login.move(15, 60)
        self.label_nome_layout_alterar_login.setStyleSheet('''font-size: 17px''')
        self.label_email_layout_alterar_login = QLabel('E-mail:', self.layout_alterar_login)
        self.label_email_layout_alterar_login.move(15, 106)
        self.label_email_layout_alterar_login.setStyleSheet('''font-size: 17px''')
        self.label_senha_layout_alterar_login = QLabel('Senha:', self.layout_alterar_login)
        self.label_senha_layout_alterar_login.move(15, 152)
        self.label_senha_layout_alterar_login.setStyleSheet('''font-size: 17px''')
        self.label_status_layout_alterar_login = QLabel('', self.layout_alterar_login)
        self.label_status_layout_alterar_login.move(15, 228)
        self.label_status_layout_alterar_login.setStyleSheet('''font-size: 17px''')
        self.label_id_layout_alterar_login = QLabel('Id:', self.layout_alterar_login)
        self.label_id_layout_alterar_login.move(28, 198)
        self.label_id_layout_alterar_login.setStyleSheet('''font-size: 17px''')
        self.label_status_layout_alterar_login = QLabel('', self.layout_alterar_login)
        self.label_status_layout_alterar_login.move(17, 266)
        self.label_status_layout_alterar_login.setStyleSheet('''font-size: 17px''')

        self.input_nome_layout_alterar_login = QLineEdit(self.layout_alterar_login)
        self.input_nome_layout_alterar_login.setGeometry(70, 60, 270, 25)
        self.input_nome_layout_alterar_login.setStyleSheet('''border: 1px solid #222''')
        self.input_email_layout_alterar_login = QLineEdit(self.layout_alterar_login)
        self.input_email_layout_alterar_login.setGeometry(70, 106, 270, 25)
        self.input_email_layout_alterar_login.setStyleSheet('''border: 1px solid #222''')
        self.input_senha_layout_alterar_login = QLineEdit(self.layout_alterar_login)
        self.input_senha_layout_alterar_login.setGeometry(70, 152, 270, 25)
        self.input_senha_layout_alterar_login.setStyleSheet('''border: 1px solid #222''')
        self.input_id_layout_alterar_login = QLineEdit(self.layout_alterar_login)
        self.input_id_layout_alterar_login.setGeometry(70, 198, 270, 25)
        self.input_id_layout_alterar_login.setStyleSheet('''border: 1px solid #222''')

        self.botao_alterar_dados_layout_adicionar_login = QPushButton('Alterar Dados', self.layout_alterar_login)
        self.botao_alterar_dados_layout_adicionar_login.setGeometry(150, 236, 190, 25)
        self.botao_alterar_dados_layout_adicionar_login.setStyleSheet('''border: 1px solid #222''')

        self.titulo_layout_deletar_usuario = QLabel('Deletar Usuário', self.layout_deletar_usuario)
        self.titulo_layout_deletar_usuario.move(10, 10)
        self.titulo_layout_deletar_usuario.setStyleSheet('''font-size: 23px''')

        self.label_id_layout_deletar_usuario = QLabel('Id:', self.layout_deletar_usuario)
        self.label_id_layout_deletar_usuario.move(28, 68)
        self.label_id_layout_deletar_usuario.setStyleSheet('''font-size: 17px''')
        self.label_status_layout_deletar_usuario = QLabel('', self.layout_deletar_usuario)
        self.label_status_layout_deletar_usuario.move(17, 136)
        self.label_status_layout_deletar_usuario.setStyleSheet('''font-size: 17px''')

        self.input_id_layout_deletar_usuario = QLineEdit(self.layout_deletar_usuario)
        self.input_id_layout_deletar_usuario.setGeometry(70, 68, 270, 25)
        self.input_id_layout_deletar_usuario.setStyleSheet('''border: 1px solid #222''')

        self.botao_layout_deletar_usuario = QPushButton('Deletar Usuário', self.layout_deletar_usuario)
        self.botao_layout_deletar_usuario.setGeometry(150, 106, 190, 25)
        self.botao_layout_deletar_usuario.setStyleSheet('''border: 1px solid #222''')

        def atualizar_tabela_de_logins():

            self.dados = self.servidor.buscar_todos_usuarios()
            print(self.dados)

            cont = 0

            self.tabela_logins.setRowCount(0)
            self.tabela_logins.setRowCount(len(self.dados))

            for c in self.dados:
                usuario = QTableWidgetItem(c[0])
                email = QTableWidgetItem(c[1])
                senha = QTableWidgetItem(c[2])
                id = QTableWidgetItem(c[3])

            
                self.tabela_logins.setItem(cont, 0, usuario)
                self.tabela_logins.setItem(cont, 1, email)
                self.tabela_logins.setItem(cont, 2, senha)
                self.tabela_logins.setItem(cont, 3, id)

                cont += 1
        
        self.botao_atualizar_tabela_layout_adicionar_login.clicked.connect(atualizar_tabela_de_logins)

        def novo_usuario():
            nome = self.input_nome_layout_adicionar_login.text()
            email = self.input_email_layout_adicionar_login.text()
            senha = self.input_senha_layout_adicionar_login.text()

            login = [nome, email, senha]

            resposta = self.servidor.enviar_novo_usuario(login)

            self.input_nome_layout_adicionar_login.setText('')
            self.input_email_layout_adicionar_login.setText('')
            self.input_senha_layout_adicionar_login.setText('')
            self.label_status_layout_adicionar_login.setText(resposta)
            self.label_status_layout_adicionar_login.adjustSize()

        self.botao_criar_usuario_layout_adicionar_login.clicked.connect(novo_usuario)

        def alterar_dados():
            nome = self.input_nome_layout_alterar_login.text()
            email = self.input_email_layout_alterar_login.text()
            senha = self.input_senha_layout_alterar_login.text()
            id = self.input_id_layout_alterar_login.text()


            usuario = [nome, email, senha]

            resposta = self.servidor.alterar_usuario(usuario, id)

            self.input_nome_layout_alterar_login.setText('')
            self.input_email_layout_alterar_login.setText('')
            self.input_senha_layout_alterar_login.setText('')
            self.label_status_layout_alterar_login.setText(resposta)
            self.input_id_layout_alterar_login.setText('')
            self.label_status_layout_alterar_login.adjustSize()

        self.botao_alterar_dados_layout_adicionar_login.clicked.connect(alterar_dados)

        def deletar_usuario():

            id = self.input_id_layout_deletar_usuario.text()

            resposta = self.servidor.deletar_usuario(id)

            self.label_status_layout_deletar_usuario.setText(resposta)
            self.label_status_layout_deletar_usuario.adjustSize()

        self.botao_layout_deletar_usuario.clicked.connect(deletar_usuario)

        self.abas = QTabWidget(self)
        self.abas.setGeometry(QRect(220, 50, 970, 630))
        self.abas.addTab(self.layout_logins, 'Visualizar Logins')
        self.abas.addTab(self.layout_adicionar_login, 'Adicionar Novo Usuário')
        self.abas.addTab(self.layout_alterar_login, 'Alterar Dados Do Usuário')
        self.abas.addTab(self.layout_deletar_usuario, 'Deletar Usuário')
        self.abas.setCurrentIndex(0)

        self.tabela_logins = QTableWidget(self.layout_logins)
        self.tabela_logins.setGeometry(10, 10, 948, 536)
        self.tabela_logins.setColumnCount(4)
        self.tabela_logins.setRowCount(len(self.dados))
        self.tabela_logins.setHorizontalHeaderLabels(
            ["Usuário", "E-mail", "Senha", "ID"])
        self.tabela_logins.setColumnWidth(0, 200)
        self.tabela_logins.setColumnWidth(1, 329)
        self.tabela_logins.setColumnWidth(2, 200)
        self.tabela_logins.setColumnWidth(3, 200)

        cont = 0

        for c in self.dados:
            usuario = QTableWidgetItem(c[0])
            email = QTableWidgetItem(c[1])
            senha = QTableWidgetItem(c[2])
            id = QTableWidgetItem(c[3])

        
            self.tabela_logins.setItem(cont, 0, usuario)
            self.tabela_logins.setItem(cont, 1, email)
            self.tabela_logins.setItem(cont, 2, senha)
            self.tabela_logins.setItem(cont, 3, id)

            cont += 1

    def mudar_layout(self, index):
        self.abas.setCurrentIndex(index)

        for c in range(self.botoes.count()):
            item = self.botoes.item(c)
            if isinstance(item, QListWidgetItem):
                if c == index:
                    item.setBackground(QBrush(QColor('white')))
                else:
                    item.setBackground(QBrush(QColor('white')))

    def iniciar(self):
        janela.show()
        app.exec()


app = QApplication(sys.argv)
janela = MeuApp()


janela.iniciar()