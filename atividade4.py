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

# variavel para armazenar o menu principal
MENU = f"""
    {'-' * 26}
    {'-' * 5} Menu Principal {'-' * 5}
    1 - Cadastrar Livro
    2 - Consultar Livro
    3 - Remover Livro
    4 - Encerrar Programa
"""

# variavel definida no escopo global com ajuda da keyword
global ID_GLOBAL


# classe responsável por gerenciar os livros
class Livraria:
    def __init__(self):
        self.lista_livro = []  # lista de dicionários para armazenar livros

    # função para cadastrar um livro
    def cadastrar_livro(self, id):
        print('-' * 32)
        print(f"{'-' * 5} MENU CADASTRAR LIVRO {'-' * 5}")
        print(f"Id do livro: {id}")
        nome = input("Por favor entre com o nome do livro: ")
        autor = input("Por favor entre com o autor do livro: ")
        editora = input("Por favor entre com a editora do livro: ")

        livro = {
            "id": id,
            "nome": nome,
            "autor": autor,
            "editora": editora
        }
        self.lista_livro.append(livro)
        print('-' * 32)

    # função para consultar livros
    def consultar_livro(self):
        while True:
            print('-' * 32)
            print(f"{'-' * 5} MENU CADASTRAR LIVRO {'-' * 5}")
            print("1 - Consultar Todos os Livros")
            print("2 - Consultar Livro por Id")
            print("3 - Consultar Livro(s) por Autor")
            print("4 - Retornar")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                print(f"{'-' * 5} Livros Cadastrados {'-' * 5}")
                for livro in self.lista_livro:
                    print('\n')
                    print(f'id: {livro["id"]}')
                    print(f'nome: {livro["nome"]}')
                    print(f'autor: {livro["autor"]}')
                    print(f'editora: {livro["editora"]}')
            elif opcao == "2":
                try:
                    id_busca = int(input("Digite o ID do livro: "))
                    encontrado = False
                    for livro in self.lista_livro:
                        if livro["id"] == id_busca:
                            print('\n')
                            print(f'id: {livro["id"]}')
                            print(f'nome: {livro["nome"]}')
                            print(f'autor: {livro["autor"]}')
                            print(f'editora: {livro["editora"]}')
                            encontrado = True
                            break
                    if not encontrado:
                        print("Livro não encontrado.")
                except ValueError:
                    print("ID inválido.")
            elif opcao == "3":
                autor_busca = input("Digite o nome do autor: ")
                # cria uma lista com list comprehension para os livros encontrados
                encontrados = [livro for livro in self.lista_livro if livro["autor"].lower() == autor_busca.lower()]
                if encontrados:
                    for livro in encontrados:
                        print('\n')
                        print(f'id: {livro["id"]}')
                        print(f'nome: {livro["nome"]}')
                        print(f'autor: {livro["autor"]}')
                        print(f'editora: {livro["editora"]}')
                else:
                    print("Nenhum livro encontrado para este autor.")
            elif opcao == "4":
                break
            else:
                print("Opção inválida.")

    # função para remover livro
    def remover_livro(self):
        while True:
            # uso do try/except para capturar os erros
            try:
                id_remover = int(input("Digite o ID do livro a remover: "))
                # para cada livro na lista de livros, ha uma verificação se o id é igual ao que deve ser removido
                for livro in self.lista_livro:
                    if livro["id"] == id_remover:
                        self.lista_livro.remove(livro)
                        print(f"Livro ID {id_remover} removido com sucesso!")
                        return
                print("Id inválido.")
            except ValueError:
                print("ID inválido, tente novamente.")


def main():
    livraria = Livraria()
    ID_GLOBAL = 0

    print("Bem-vindo a Livraria do Wellington Almeida")
    while True:
        print(MENU)

        opcao = input("Escolha a opção desejada: ")
        # validação das opções do usuário
        if opcao == "1":
            ID_GLOBAL += 1
            livraria.cadastrar_livro(ID_GLOBAL)
        elif opcao == "2":
            livraria.consultar_livro()
        elif opcao == "3":
            livraria.remover_livro()
        elif opcao == "4":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()
