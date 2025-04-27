"""
Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja
que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:

    • Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
    • Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
    • Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;

Elabore um programa em Python que:
    A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e
    sobrenome [EXIGÊNCIA DE CÓDIGO 1 de 8];

    B. Deve-se implementar o input do sabor (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entra
    com valor diferente de CP e AC [EXIGÊNCIA DE CÓDIGO 2 de 8];

    C. Deve-se implementar o input do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário
    com entra valor diferente de P, M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];

    D. Deve-se implementar if, elif e/ou else, utilizando o modelo aninhado (aula 3 – Tema 4) com cada uma das
    combinações de sabor e tamanho [EXIGÊNCIA DE CÓDIGO 4 de 8];

    E. Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];

    F. Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do
    item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];

    G. Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];

    H. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];

    I. Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE
    SAÍDA DE CONSOLE 1 de 4];
    J. Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE
    CONSOLE 2 de 4];

    K. Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE
    CONSOLE 3 de 4];

    L. Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos
    diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];
"""

CARDAPIO = f"""
    {'-' * 14} Cardápio {'-' * 13}
    {'-' * 37}
    ---| Tamanho | Cupuaçu (CP)|  Açaí (AC)|---
    ---|    P    |   R$09.00   | R$11.00   |---
    ---|    M    |   R$14.00   | R$16.00   |---
    ---|    G    |   R$18.00   | R$20.00   |---
    {'-' * 37}
"""


def main():
    print("Bem-vindo à loja de Wellington Almeida")
    print(CARDAPIO)
    total = 0

    while True:
        sabor = input("Digite o sabor desejado (CP/AC): ").upper()

        if sabor not in ["CP", "AC"]:
            print("Sabor inválido. Tente novamente.")
            continue

        tamanho = input("Digite o tamanho desejado (P/M/G): ").upper()

        if tamanho not in ['P', 'M', 'G']:
            print("Tamanho inválido. Tente novamente.")
            continue

        if sabor == "CP":
            _sabor_aux = 'Cupuaçu'
            if tamanho == "P":
                preco = 9
            elif tamanho == "M":
                preco = 14
            else:
                preco = 18
        elif sabor == "AC":
            _sabor_aux = 'Açaí'
            if tamanho == "P":
                preco = 11
            elif tamanho == "M":
                preco = 16
            else:
                preco = 20
        print(f"Você pediu {_sabor_aux} no tamanho {tamanho}: R$ {preco:.2f}")
        total += preco

        mais = input("\nDeseja mais alguma coisa? (S/N): ").upper()

        if mais == "S":
            continue
        elif mais == "N":
            break
        else:
            print("Resposta inválida, encerrando o pedido.")
            break

    print(f"\nValor total a ser pago: R$ {total:.2f}")


if __name__ == '__main__':
    main()
