def validandoEscolha(escolha):
    while True:
        try:
            return int(escolha)
        
        except ValueError:
            print('Digite um número válido !')
            escolha = input('''
1 - Cadastrar pessoa
2 - Ver pessoas cadastradas
3 - fechar programa

Escolha: ''')

def validarIdade(idade):
    while True:
        try:
            return int(idade)
        except ValueError:
            print('Digite um número válido')
            idade = input('Informe sua idade novamente: ')

def cadastrarPessoa(nome, idade):
    import os, time
    if os.path.exists('cadastros.txt') == False:
        print('\nCriando arquivo de cadastro...')
        time.sleep(2)
        with open('cadastros.txt', 'a') as cadastro:
            cadastro.write(f'{nome};{idade}\n')
            print(f'{nome} cadastrado(a) com sucesso !!')
    else:
        with open('cadastros.txt', 'a') as cadastro:
            cadastro.write(f'{nome};{idade}\n')
            print(f'{nome} cadastrado(a) com sucesso !!')

def pessoasCadastradas():
    try:
        with open('cadastros.txt') as cadastro:
            print(f'{"\nNOME":<20} {"IDADE"}\n')
            for linha in cadastro:
                user = linha.split(';')
                user[1] = user[1].replace('\n', '')
                print(f'{user[0]:<20} {user[1]}')
    except FileNotFoundError:
        print('Faça o primeiro cadastro !')
        