import mysql.connector
import PySimpleGUI as sg

# conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testepython"
)
cursor = conn.cursor()


# POO
class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    
    def armazenar(self) :
        try:
            # criando a query
            query = "INSERT INTO pessoas (nome, idade, email) VALUES (%s, %s, %s)"
            values = (self.nome, self.idade, self.email)

            # executando a query
            cursor.execute(query, values)
            conn.commit()
            # print(f'A pessoa "{self.nome}" foi armazenada com sucesso')
            return True
        except mysql.connector.Error as erro:
            # tratamento de erros
            print(f"Erro ao armazenar usuário: {erro}")
            return False

# criando a interface gráfica
Layout = [
    [sg.Text("Nome:"), sg.Input(key="nome")],
    [sg.Text("Email:"), sg.Input(key="email")],
    [sg.Text("Idade:"), sg.Input(key="idade")],
    [sg.Button("Salvar"), sg.Button("Sair")]
]

window = sg.Window("Cadastro de pessoas", Layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Sair":
        break
    if event == "Salvar":
        nome = values['nome']
        idade = values['idade']
        email = values['email']

        # caso alguma das coisas não forem preenchidas
        if not nome or not idade or not email:
            sg.popup_error("Todos os campos devem estar preenchidos.")
            continue
        
        # verifica se o valor de "idade" é um número
        try:
            idade = int(idade)
        except ValueError:
            sg.popup_error("Idade deve ser um número.")
            continue
        
        # cria o objeto para logo em seguida armazena-lo
        pessoa = Pessoa(nome, idade, email)
        if pessoa.armazenar():
            sg.popup("Sucesso!", f'A pessoa "{nome}" foi armazenada com sucesso')
            window["nome"].update("")
            window["idade"].update("")
            window["email"].update("")
        else:
            sg.popup_error("Falha ao armazenar o usuário")
            

window.close()