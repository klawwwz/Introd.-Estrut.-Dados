#implementação de lista
class lista():
    def __init__(self):
        self.elementos=[]

    def inserir(self, elemento):
        self.elementos.append(elemento)
    
    def remover(self, elemento):
        self.elementos.pop()
    
    def busca(self, elemento):
        if elemento in self.elementos:
            print(f'aqui esta o {elemento}')
        else:
            print('esse elemento nao esta na lista')

    def imprimir(self):
        if not self.elementos:
            print('lista vazia.')
        else:
            print('elementos:')
            for elemento in self.elementos:
                print(elemento)
                
     def inverter_lista(self):#REVERSÃO DE LISTA!!!!!!!!!!
        tam=len(self.elementos)
        for i in range(tam//2):#iterar metade da lista, serve para que nao tenha duplicação
            self.elementos[i], self.elementos[tam-i-1]=self.elementos[tam-i-1], self.elementos[i]





