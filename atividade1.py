"""
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de um app de vendas para uma
determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maior
conforme o valor da compra, conforme a listagem abaixo:

- Se valor for menor que 2500 o desconto será de 0%;

- Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%;

- Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;

- Se valor for igual ou maior que 10000 o desconto será de 11%;

Elabore um programa em Python que:

A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e sobrenome
[EXIGÊNCIA DE CÓDIGO 1 de 6];

B. Deve-se implementar o input do valor unitário e da quantidade do produto [EXIGÊNCIA DE CÓDIGO 2 de 6];

C. Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se as condições de menor, igual
e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];

D. Deve-se implementar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 4 de 6];

E. Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];

F. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];

G. Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome
[EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];

H. Deve-se apresentar na saída de console um pedido recebendo desconto (valor total sem desconto maior ou igual
a 2500) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];
"""


# função auxiliar para gerenciar o desconto
def obtem_desconto(valor):
    if valor in range(0, 2499):
        return 0

    elif valor in range(2500, 5999):
        return 0.04

    elif valor in range(6000, 9999):
        return 0.07

    else:
        return 0.11


def main():
    print("Bem-vindo a loja de Wellington Almeida")
    # obter dados do usuário
    valor_produto = int(input("Digite o Valor do produto: "))
    qtd_produto = int(input("Digite a quantidade do produto: "))
    # cálculo do valor toral
    valor_total = valor_produto * qtd_produto
    desconto = obtem_desconto(valor_total)
    # print auxiliar para mostrar o desconto obtido
    print(f"Desconto aplicavel: {int(desconto * 100)}%")
    # cálculo do valor com desconto
    valor_com_desconto = valor_total - (valor_total * desconto)

    # saída dos valores na tela
    print(f"Valor SEM desconto: {valor_total:.2f}")
    print(f"Valor COM desconto: {valor_com_desconto:.2f}")


if __name__ == '__main__':
    # função principal
    main()
