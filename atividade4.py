"""
Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de
gerenciamento de livros. Este software deve ter o seguinte menu e opções:
    - Cadastrar Livro
    - Consultar Livro
    - Consultar Todos 
    - Consultar por Id
    - Consultar por Autor
    - Retornar ao menu
    - Remover Livro
    - Encerrar Programa

Elabore um programa em Python que: 
Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 8];

Deve-se implementar uma lista vazia com o nome de lista_livro e a variável id_global com valor inicial igual
a 0 [EXIGÊNCIA DE CÓDIGO 2 de 8];

Deve-se implementar uma função chamada cadastrar_livro(id) em que: [EXIGÊNCIA DE CÓDIGO 3 de 8];

Pergunta nome, autor, editora do livro;

Armazena o id (este é fornecido via parâmetro da função), nome, autor, editora dentro de um dicionário;

Copiar o dicionário para dentro da lista_livro;

Deve-se implementar uma função chamada consultar_livro() em que: [EXIGÊNCIA DE CÓDIGO 4 de 8];

Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por
Autor / 4. Retornar ao menu):
    Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados;
    Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados;
    Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados cadastrados;
    Se Retornar ao menu, deve-se retornar ao menu principal;
    Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta D.a.
    Enquanto o usuário não escolher a opção 4, o menu consultar livros deve se repetir.
    Deve-se implementar uma função chamada remover_livro() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
    Deve-se pergunta pelo id do livro a ser removido;
    Remover o livro da lista_livro;
    Se o id fornecido não for de um livro da lista, printar “Id inválido” e repetir a pergunta E.a.
    Deve-se implementar uma estrutura de menu no código principal (main), ou seja, não pode estar dentro de
    função, em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
    Deve-se pergunta qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa):
    Se Cadastrar Livro, acrescentar em um id_ global e chamar a função cadastrar_livro(id_ global);
    Se Consultar Livro, chamar função consultar_livro();
    Se Remover Livro, chamar função remover_livro();
    Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
    Se Entrar com um valor diferente de 1, 2, 3 ou 4, printar “Opção inválida" e repetir a pergunta F.a.
    Enquanto o usuário não escolher a opção 4, o menu deve se repetir.
    Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8];
    Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
    Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];
    Deve-se apresentar na saída de console um cadastro de 3 livros (sendo 2 deles no mesmo autor) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];
    Deve-se apresentar na saída de console uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];
    Deve-se apresentar na saída de console uma consulta por código (id) de um dos livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];
    Deve-se apresentar na saída de console uma consulta por autor em que 2 livros sejam do mesmo autor [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];
    Deve-se apresentar na saída de console uma remoção de um dos livros seguida de uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];
"""

ID_GLOBAL = 0


class Livro:
    def __init__(self, nome, autor, editora, _id):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self._id = _id

class DBLivros:
    def __init__(self):
        self.livros = []
    
    def cadastrar_livro(self, id_global):
        nome = input("")
    
    def consultar_livro(self, id_global):
        pass
    
    def remover_livro(self, id_global):
        pass


def show_principal_menu():
    print('-' * 40)
    print('-' * 11, ' Menu Principal ', '-' * 11)
    print("Escolha a opção desejada: ")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livros")
    print("3 - Remover Livro")
    print("4 - Sair")


def main():
    db = DBLivros()
    print("Bem-vindo a Livraria do Wellington Almeida")
    show_principal_menu()
    opcao = int(input())
    
    if opcao == 1:
        db.cadastrar_livros(ID_GLOBAL + 1)


if __name__ == '__main__':
    main()
