Sistema de Cadastro de Pessoas (Python + SQLite)

Aplicação de terminal desenvolvida em Python com foco em prática de fundamentos de backend, persistência de dados e boas práticas de organização de código.

O projeto começou utilizando armazenamento em arquivo .txt e foi posteriormente refatorado para utilizar SQLite, trazendo estrutura relacional, tipagem de dados e maior segurança nas operações.

Funcionalidades
- Cadastro de pessoas (nome e idade)
- Validação de entradas do usuário
- Persistência de dados utilizando SQLite
- Criação automática da tabela (CREATE TABLE IF NOT EXISTS)
- Inserção segura com queries parametrizadas (proteção contra SQL Injection)
- Listagem de pessoas cadastradas
- Ordenação dos registros por idade
- Criação automática do banco de dados, caso não exista

Tecnologias Utilizadas
- Python 3
- SQLite3 (módulo padrão do Python)
- Estrutura modular com separação de responsabilidades

Conceitos aplicados
- Este projeto foi desenvolvido com foco na prática de:
- Modularização do código
- Validação de dados de entrada
- Manipulação de banco de dados relacional
- Queries parametrizadas
- Organização de responsabilidades em funções
- Persistência estruturada de dados
- Uso de with para gerenciamento de conexão


Estrutura do Projeto
cadastro_pessoa/

-- main.py         # Arquivo principal do programa

-- funcoes.py      # Módulo com as funções do sistema

-- cadastros.bd    # Banco de dados SQLite (gerado automaticamente)

-- README.md

Como executar
- Certifique-se de ter o Python 3 instalado.
- Clone o repositório:
- git clone <url-do-repositorio>
- Execute o programa:
- python main.py
- O banco de dados será criado automaticamente na primeira execução.

Próximos passos (evolução planejada)
- Implementar atualização e exclusão de registros (CRUD completo)
- Aplicar separação em camada de acesso a dados
- Melhorar tratamento de exceções
- Adicionar testes automatizados
