"""
Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou
com a parte de desenvolver a interface com o funcionário.

A copiadora opera da seguinte maneira:
    • Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;

    • Serviço de Impressão Colorida (ICO) o custo por página é de um real;

    • Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos;

    • Serviço de Fotocópia (FOT) o custo por página é de vinte centavos;

    • Se número de páginas for menor que 20 retornar o número de página sem desconto;

    • Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o
    desconto é de 15%;

    • Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com
    o desconto é de 20%;

    • Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas
    com o desconto é de 25%;

    • Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;

    • Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;

    • Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;

    • Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;

O valor final da conta é calculado da seguinte maneira:

total = (servico * num_pagina) + extra

Elabore um programa em Python que:
    A. Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 7];

    B. Deve-se implementar a função escolha_servico() em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
        a. Pergunta o servico desejado;
        b. Retorna o valor servico com base na escolha do usuário;
        c. Repete a pergunta do item B.a se digitar uma opção diferente de: dig/ico/ipb/fot;

    C. Deve-se implementar a função num_pagina() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
        a. Pergunta o número de páginas;

        b. Retorna o número de páginas com desconto seguindo a regra do enunciado (desconto
        calculado em cima do número de páginas);

        c. Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não numérico
        (use try/except para não numérico)

    D. Deve-se implementar a função servico_extra() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
        a. Pergunta pelo serviço adicional;
        b. Retornar o valor de apenas uma das opções de adicional
        c. Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;

    E. Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função,
    conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7];

    F. Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7];

    G. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7];

    H. Deve-se apresentar na saída de console uma mensagem de boas-vindas com
    seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];

    I. Deve-se apresentar na saída de console um pedido no qual o usuário errou a
    opção de serviço [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];

    J. Deve-se apresentar na saída de console um pedido no qual o usuário digitou
    ultrapassou no número de páginas [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];

    K. Deve-se apresentar na saída de console um pedido com opção de serviço, número
    de páginas e serviço extra válidos [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];
"""

# contante para o menu
MENU = """
    DIG: Digitalição
    ICO: Impressão Colorida
    IPB: Impressão Preto e Branco
    FOT: Fotocópia
"""
# contante para o menu de adicionais
ADICIONAL = """
    1 - Encadernaçao simples: R$ 14.00
    2 - Encadernaçao Capa Dura: R$ 40.00
    0 - Não desejo mais nada
"""

# mapping para facilitar a relação entre tipo de serviço (string) e valor de serviço (float)
servico_map = {
    'DIG': 1.10,
    'ICO': 1.00,
    'IPB': 0.40,
    'FOT': 0.20
}


# função auxiliar para obter desconto
def obtem_desconto(num_paginas, valor_servico_escolhido):
    # calculo do valor total
    total = num_paginas * valor_servico_escolhido

    # verificações dos casos de desconto
    if 20 <= num_paginas < 200:
        return total - (0.15 * total)
    elif 200 <= num_paginas < 2000:
        return total - (0.20 * total)
    elif 2000 <= num_paginas < 20000:
        return total - (0.25 * total)
    elif num_paginas >= 20000:
        raise Exception("Não aceitamos pedidos com essa quantidade de páginas.")
    else:
        # quantidade de páginas insuficiente para desconto
        return total


# função requisitada pela questao, para escolha de serviço
def escolha_servico(servico):
    while True:
        # verificação se o serviço que o usuário escolheu é válido
        if servico in ['DIG', 'ICO', 'IPB', 'FOT']:
            # uso do 'try' para capturar alguma exception no processo de escolher serviços
            try:
                num_paginas = int(input("Entre com o número de páginas: "))
                valor_servico_escolhido = servico_map[servico]
                total_pagar = obtem_desconto(num_paginas, valor_servico_escolhido)
            except Exception:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.")
            else:
                return total_pagar, valor_servico_escolhido, num_paginas
        else:
            continue


def main():
    print("Bem-vindo a Copiadora de Wellington Almeida")

    while True:
        print(MENU)
        # obtendo dados do usuário
        servico = input("Entre com o tipo de serviço desejado: ").upper()
        # verificação se seviço é válido
        if servico not in ['DIG', 'ICO', 'IPB', 'FOT']:
            print("Escolha inválida entre com o tipo de serviço novamente.")
            continue
        else:
            # retorno dos valores calculados pela função escolha_servico
            total_servico, valor_servico_escolhido, num_paginas = escolha_servico(servico)
            print(ADICIONAL)
            # verificacao de servico extra
            servico_extra = int(input("Deseja adicionar mais um serviço? "))
            if servico_extra == 1:
                extra = 14
            elif servico_extra == 2:
                extra = 40
            else:
                extra = 0
            total = (total_servico) + extra
            # saída final
            print(f'Total: R$ {total:.2f} (serviço: {valor_servico_escolhido:.2f} * páginas: {num_paginas:.2f} + extra: {extra:.2f})')
            break


if __name__ == '__main__':
    main()
