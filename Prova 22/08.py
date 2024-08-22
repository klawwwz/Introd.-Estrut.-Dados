#Criar uma aplicação simples para simular algumas funcionalidades básicas de uma
#agência bancária chamada Finance Pro, utilizando listas e dicionários para armazenar
#informações sobre clientes e contas.

#Diego Henrique Rodrigues 

def adc_cliente(banco, id_ant, nome, idade, telefone, tipo=None):
    id_cliente = id_ant + 1
    clientes = {
        'id' : id_cliente,
        'nome' : nome,
        'idade' : idade,
        'telefone' : telefone,
        'conta' : {
            'saldo' : 0,
            'tipo' : tipo
        }
    }
    banco.append(clientes)
    print(f'O cliente {nome} foi adicionado. Seu ID é {id_cliente}.')
    return id_cliente

def depositar(banco, id):
    for clientes in banco:
        a = False
        if clientes['id'] == id:
            print('Qual o valor do depósito? ')
            saldo_novo = float(input('R$'))
            saldo_antigo = float(clientes['conta']['saldo'])
            clientes['conta']['saldo'] = (saldo_novo + saldo_antigo)
            print('Saldo adicionado à conta.')
            print(f"Saldo atual = R${clientes['conta']['saldo']}")
            a = True
        return a

def sacar(banco, id):
    for clientes in banco:
        a = False
        if clientes['id'] == id:
            print('Qual o valor do saque?')
            valor = float(input('R$'))
            if clientes['conta']['saldo'] >= valor:
                novo_saldo = clientes['conta']['saldo'] - valor
                clientes['conta']['saldo'] = novo_saldo
                print('Saque realizado.')
                print(f"Saldo atual = R${clientes['conta']['saldo']}")
                a = True
            else: 
                print('Você não possui dinheiro o suficiente.')
                a = True
        else:
            print('Conta não encontrada.')
            a = False 
        return a

def extrato(banco, id):
    for clientes in banco:
        if clientes['id'] == id:
            print(f"Nome: {clientes['nome']} | Nº da conta: {clientes['id']} --> Saldo: R${clientes['conta']['saldo']}")

def clientes_banco(banco):
    print('--- CLIENTES DO BANCO --- ')
    for clientes in banco:
        print(f"Nome: {clientes['nome']} | Nº da conta: {clientes['id']} --> Saldo: R${clientes['conta']['saldo']}")

def menu():
    print('Menu:')
    print('[1]-Adicionar cliente.\n[2]-Depositar.\n[3]-Sacar.\n[4]-Gerar extrato.\n[5]-Listar clientes do banco.')
    esc = input('')
    return esc

def main():
    id_ant = 0
    banco = []
    print('Bem-vindo à agência bancária Finance Pro!')
    while True:
        opcao = menu()
        if opcao == '1':
            print('ADICIONAR CLIENTE: ')
            nome = input('Nome do cliente: ')
            idade = int(input('Digite a idade: '))
            tel = (input('Digite o número de telefone(xxx-xxx): '))
            tipo = input('Qual tipo de conta você deseja?\n[1]-Poupança - Foco no rendimento. | [2]-Corrente - Foco em receber e sacar.\n')
            if tipo == '1':
                id_ant = adc_cliente(banco, id_ant, nome, idade, tel, tipo='Poupança')
            elif tipo == '2':
                id_ant = adc_cliente(banco, id_ant, nome, idade, tel, tipo='Corrente')

        elif opcao == '2':
            print('DEPOSITAR DINHEIRO: ')
            id_cliente = int(input('Qual ID do usuário? '))
            a = depositar(banco, id_cliente)
            if not a:
                print('conta não encontrada')
        elif opcao == '3':
            print('SACAR DINHEIRO: ')
            id_cliente = int(input('Qual o ID de sua conta? '))
            a = sacar(banco, id_cliente)
            if not a:
                print('conta não encontrada')
        elif opcao == '4':
            print('GERAR EXTRATO: ')
            id_cliente = int(input('Qual o ID da conta? '))
            extrato(banco, id_cliente)
        elif opcao == '5':
            clientes_banco(banco)


if __name__ == "__main__":
    main()