import funcoes

print('Bem vindo(a) ao aplicativo de cadastro !!')

while True:
    escolha = funcoes.validandoEscolha(input('''
1 - Cadastrar pessoa
2 - Ver pessoas cadastradas
3 - fechar programa
                    
Escolha: '''))

    match escolha:
        case 1:
            nome = input('Informe seu nome: ')
            
            idade = input('Informe sua idade: ')
            funcoes.validarIdade(idade)

            funcoes.cadastrarPessoa(nome, idade)

        case 2:
            funcoes.pessoasCadastradas()
            
        case 3:
            print('Muito obrigado por usar nosso programa, volte sempre !!')
    if escolha == 3:
        break