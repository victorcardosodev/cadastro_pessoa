import sqlite3

def validandoTipo(escolha): # Válida se o número esolhido é do tipo inteiro
    while True:
        try:
            num = int(escolha)
            validandoEscolha(num)
            return num
        
        except ValueError:
            print('Digite um número válido !')
            escolha = input('''
1 - Cadastrar pessoa
2 - Ver pessoas cadastradas
3 - fechar programa

Escolha: ''')
            

def validandoEscolha(escolha): # Válida se a escolha é de 1 a 3
    while True:
        if escolha < 1 or escolha > 3:
            print('Escolha um número de 1 a 3 !')
            return ValueError
        
        else:
            return escolha


def validarIdade(idade): # Válida se a idade informada é do tipo inteiro
    while True:
        try:
            return int(idade)
        
        except ValueError:
            print('Digite um número válido')
            idade = input('Informe sua idade novamente: ')


def cadastrarPessoa(nome, idade): # Aqui faremos a conexão ao BD e iremos verificar se a tabela já existe, caso não exista criaremos ou se existir, apenas o cadastro
    with sqlite3.connect('cadastros.bd') as conexao:
        cursor = conexao.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS pessoas(nome TEXT, idade INTEGER)") # Cria a tabela

        cursor.execute(f"INSERT INTO pessoas VALUES(?, ?)", (nome, idade)) # implementando os dados da pessoa
        conexao.commit()
        print(f'{nome} cadastrado(a) com sucesso !!')


def pessoasCadastradas(): # Faz apresentação da lista de cadastros
    with sqlite3.connect('cadastros.bd') as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT nome, idade FROM pessoas ORDER BY idade') # Puxa as informações de nome e idade da tabela pessoas

        print(f'{"NOME":<20} {"IDADE"}')
        for dados in cursor.fetchall(): # Puxo todos os itens do banco em formato de lista com o fetchall e com "dados" acesso cada linha (tupla) do BD
            print(f'{dados[0]:<20} {dados[1]}')


def infoBD(): # Aqui mostro as informações das colunas do banco de dados
    with sqlite3.connect('cadastros.bd') as conexao:
        cursor = conexao.cursor()
        cursor.execute('PRAGMA table_info(pessoas)')
        print(cursor.fetchall())