class FilaDeBanco:
    def __init__(self):
        self.fila=[]

    def inserir(self, cliente):
        self.fila.append(cliente)
        print(f'o cliente {cliente} foi inserido na fila.')

    def atender(self):
        if self.fila:
            cliente = self.fila.pop(0)
            print(f'o cliente {cliente} foi atendido')
        else:
            print('a fila esta vazia')

    def is_empty(self):
        if not self.fila:
            return True
        else:
            return False
        
    def mostrar(self):
        for pessoa in self.fila:
            print(pessoa)

fila_cliente=FilaDeBanco()
while True:
    print('Escolha a opção:\n1-adicionar cliente\n2-atender cliente\n3-mostrar fila')
    num=int(input())

    if num==1:
        cliente=input('digite o nome do cliente:\n')
        fila_cliente.inserir(cliente)

    elif num==2:
        fila_cliente.atender()

    elif num==3:
        fila_cliente.mostrar()

        alt=fila_cliente.is_empty()
        if alt==True:
            print('sem clientes.')
    else:
        print('PROGRAMA ENCERRADO.')
        break