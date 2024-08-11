#sistema de gerenciamento de um estoque
#o sistema deve permitir ao usuario adicionar, remover, atualizar, visualizar, listar, filtrar produtos e gerar relatorios dos produtos no estoque

def adc_produto(estoque_geral, id_ant, nome, quantidade, preco):
    id_produto = id_ant + 1
    estoque = {
        'id' : id_produto,
        'nome' : nome,
        'quantidade' : quantidade,
        'preco' : preco
    }
    estoque_geral.append(estoque)
    print(f"Produto '{nome}' foi adicionado com sucesso! Id do produto é '{id_produto}'")
    return id_produto

def rmv_produto(estoque_geral, id_produto):
    for estoque in estoque_geral:
        if estoque['id'] == id_produto:
            nome_prod = estoque['nome']
            estoque_geral.remove(estoque)
            print(f'{nome_prod} foi removido.')
        return True

def menu_att():
    print('O que você deseja atualizar?')
    print('[1]-Nome\n[2]-Preço\n[3]-Quantidade')
    esc = input('')
    return esc

def att_produto(estoque_geral, id_produto):
    for estoque in estoque_geral:
        if estoque['id'] == id_produto:
            opcao = menu_att()
            if opcao == '1':
                nome = input('Atualize o nome: ')
                estoque['nome'] = nome
                print(f'Nome atualizado para {nome}')
            if opcao == '2':
                preco = float(input('Atualize o preço: '))
                estoque['preco'] = preco
                print(f'Preço atualizado para {preco}')
            if opcao == '3':
                quant = int(input('Atualize a quantidade: '))
                quant_ant = estoque['quantidade']
                estoque['quantidade'] = quant
                print(f'Quantidade atualizada de {quant_ant} para {quant}')

def lst_produto(estoque_geral):
    for estoque in estoque_geral:
        print(f"ID: {estoque['id']}, Nome: {estoque['nome']}, Quantidade: {estoque['quantidade']}, Preço: {estoque['preco']}")

def bsc_produto(estoque_geral, nome):
    for estoque in estoque_geral:
        if estoque['nome'].lower() == nome.lower():
            print(f"ID: {estoque['id']}, Nome: {estoque['nome']}, Quantidade: {estoque['quantidade']}, Preço: {estoque['preco']}")
        return True

def flt_produto(estoque_geral, quantidade=None, preco=None):
    if quantidade:
        print(f'Filtrando produtos com quantidade inferior a {quantidade}')
        for estoque in estoque_geral:
            if quantidade >= estoque['quantidade']:
                print(f"QUANTIDADE: {estoque['quantidade']}, ID: {estoque['id']}, Nome: {estoque['nome']}, Preço: {estoque['preco']}")
    if preco:
        print(f'Filtrando produtos com preço menor a {preco}')
        for estoque in estoque_geral:
            if preco >= estoque['preco']:
                print(f"PREÇO: {estoque['preco']}, ID: {estoque['id']}, Nome: {estoque['nome']}, Quantidade: {estoque['quantidade']}")

def gerar_relatorio(estoque_geral):
    soma_produto = 0
    soma_valor = 0
    print('PRODUTO | QUANTIDADE | PREÇO(UNITÁRIO) | PREÇO TOTAL.')
    for estoque in estoque_geral:
         print(f"{estoque['nome']} | {estoque['quantidade']} | R${estoque['preco']} = R${estoque['quantidade'] * estoque['preco']} ")
         soma_produto = soma_produto + estoque['quantidade']
         soma_valor = soma_valor + estoque['quantidade'] * estoque['preco']
    print('-----------------------------------------------------------------')
    print(f'Quantidade de produtos: {soma_produto} produtos.')
    print(f'Valor total no estoque: R${soma_valor}')

def main():
    id_ant = 0
    estoque_geral = []
    while True:
        print('===============================================')
        print('Bem-vindo ao sistema!\nO que deseja fazer hoje?')
        print('[1]-Adicionar produto\n[2]-Remover produto\n[3]-Atualizar produto\n[4]-Buscar produto\n[5]-Filtrar produtos\n[6]-Listar todos os produtos do estoque\n[7]-Gerar relatório')
        esc = input('')
        print('===============================================')

        if esc == '1':
            print('Adicionar produto: ')
            nome = input('Nome: ')
            quant = int(input('Quantidade: '))
            preco = float(input('Preço(unitário): '))
            id_ant = adc_produto(estoque_geral, id_ant, nome, quant, preco)

        elif esc == '2':
            print('Remover produto: ')
            id_produto = int(input('Qual o id do produto você deseja remover? '))
            cond = rmv_produto(estoque_geral, id_produto)
            if not cond:
                print('Produto não foi encontrado.')

        elif esc == '3':
            print('Atualizar produto: ')
            id_produto = int(input('Qual o id do produto você deseja atualizar? '))
            att_produto(estoque_geral, id_produto)

        elif esc == '4':
            print('Buscar produto: ')
            nome = input('Digite o nome do produto: ')
            cond = bsc_produto(estoque_geral, nome)
            if not cond:
                print('Produto não encontrado.')

        elif esc == '5':
            print('Filtrar produtos: ')
            print('[1]-Filtrar quantidade. [2]-Filtrar preço')
            opcao = input('')
            if opcao == '1':
                quant = int(input('Filtre por quantidade: '))
                flt_produto(estoque_geral, quantidade=quant)

            if opcao == '2':
                preco = float(input('Filtrando por preço: '))
                flt_produto(estoque_geral, preco=preco)

        elif esc == '6':
            print('Listar produtos do estoque: ')
            lst_produto(estoque_geral)

        elif esc == '7':
            print('Mostrando relatório: ')
            gerar_relatorio(estoque_geral)

if __name__ == "__main__":
    main()