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
    print(f'Produto {nome} foi adicionado com sucesso! Id do produto é {id_produto}')
    return id_produto

def rmv_produto():
    pass

def att_produto():
    pass

def lst_produto(estoque_geral):
    for estoque in estoque_geral:
        print(f"ID: {estoque['id']}, Nome: {estoque['nome']}, Quantidade: {estoque['quantidade']}, Preço: {estoque['preco']}")

def bsc_produto(estoque_geral, nome):
    a = False
    for estoque in estoque_geral:
        if estoque['nome'] == nome:
            print(f"ID: {estoque['id']}, Nome: {estoque['nome']}, Quantidade: {estoque['quantidade']}, Preço: {estoque['preco']}")
            a = True
    if not a:
        print('Reserva não encontrada.')
    pass

def flt_produto(estoque_geral, quantidade=None, preco=None):

    pass

def gerar_relatorio():
    pass

def main():
    while True:
        id_ant = 0
        estoque_geral = []
        print('Bem-vindo ao sistema!\nO que deseja fazer hoje?')
        print('[1]-Adicionar produto\n[2]-Remover produto\n[3]-Atualizar produto\n[4]-Buscar produto\n[5]-Filtrar produtos\n[6]-Listar todos os produtos do estoque\n[7]-Gerar relatório')
        esc = input('')

        if esc == '1':
            print('Adicionar produto: ')
            nome = input('Nome: ')
            quant = int(input('Quantidade: '))
            preco = int(input('Preço(unitário): ')) #preço por unidade, nao pela quantidade
            id_ant = adc_produto(estoque_geral, id_ant, nome, quant, preco)
            pass

        elif esc == '2':
            print('Remover produto: ')
            pass

        elif esc == '3':
            print('Atualizar produto: ') #atualizar por id tambem
            pass

        elif esc == '4':
            print('Buscar produto: ') #buscar por nome
            pass

        elif esc == '5':
            print('Filtrar produtos: ')
            opcao = input('[1]-Filtrar quantidade. [2]-Filtrar preço')
            if opcao == '1':
                quant = input('Filtre por quantidade: ')

            if opcao == '2':
                preco = input('Filtrando por preço: ')

            pass

        elif esc == '6':
            print('Listar produtos do estoque: ')
            lst_produto(estoque_geral)
            pass

        elif esc == '7': #vc pega o numero de quantidade e multiplica por preço 
            print('Gerar relatório: ')
            pass

if __name__ == "__main__":
    main()
