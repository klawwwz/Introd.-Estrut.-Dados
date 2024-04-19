#Considere um cenário em que uma empresa de consultoria possui uma pilha de relatórios pendentes e uma fila de atendentes disponíveis. Cada atendente deve pegar o relatório no topo da pilha e processá-lo.

class Pilha:
    def __init__(self):
        self.pilha=[]
    
    def adicionar(self, elemento):
        self.pilha.append(elemento)

    def remover(self):
        return self.pilha.pop()

    def topo(self):
        print (self.pilha[-1])

    def isEmpty(self):
        if not self.pilha:
            return True
        else:
            return False
        
    def mostrar(self):
        return self.pilha
    
    def tamanho(self):
        taman=len(self.pilha)
        return taman
        
class Fila:
    def __init__(self):
        self.fila=[]

    def adicionar(self, pessoa):
        self.fila.append(pessoa)

    def remover(self):
        return self.fila.pop(0)

    def topo(self):
        return self.fila[0]
    
    def isEmpty(self):
        if not self.fila:
            return True
        else:
            return False
        
    def mostrar(self):
        for i in self.fila:
            print(f'-{i}')

    def tamanho(self):
        taman=len(self.fila)
        return taman

fila_atnd=Fila()
pilha_prcss=Pilha()
fila_quant=Fila()

def processar(fila_atnd, pilha_prcss):
    if pilha_prcss.isEmpty() or fila_atnd.isEmpty():
        print("Operação não pode ser realizada.")
    else:
        print(f'O atendente {fila_atnd.remover()} atendeu o processo {pilha_prcss.remover()}')
        print('Processo realizado.')

while True:
    print ('='*33)
    print('SETOR DE ATENDIMENTO DE PROCESSOS')
    print ('='*33)

    esc=int(input('Seja bem-vindo!\nDesejo operar com:\n[1]-Atendentes\n[2]-Processos\n[3]-Mostrar quantos processos foram realizados\n[4]-Encerrar programa\n'))

    if esc==1:
        print('-='*17)
        escf=int(input('Operações com atendentes:\n[1]-Adicionar\n[2]-Mostrar fila\n'))
        if escf==1:
            nome=input('Quem você deseja adicionar?\n')
            fila_atnd.adicionar(nome)
            print(f'{nome} adicionado à fila!')

        elif escf==2:
            if fila_atnd.isEmpty():
                print('Sem atendentes.')
            else:
                print('FILA DOS ATENDENTES:')
                fila_atnd.mostrar()

    elif esc==2:
        print('-='*17)
        escp=int(input('Operações com processos:\n[1]-Adicionar\n[2]-Mostrar próximo\n[3]-Processar\n'))
        if escp==1:
            num=int(input('Número do processo a ser adicionado:\n'))
            pilha_prcss.adicionar(num)
            print(f'-{num}- adicionado à pilha de processos')

        elif escp==2:
            if pilha_prcss.isEmpty():
                print('Pilha vazia.')
            else:
                print('O PRÓXIMO PROCESSO NA PILHA É:')
                pilha_prcss.topo()
                
        elif escp==3:
                print('processando...')
                processar(fila_atnd, pilha_prcss)
                fila_quant.adicionar(+1)

    
    elif esc==3:
        if pilha_prcss.isEmpty():
            tam=fila_quant.tamanho()
            print(f'{tam} processos realizados.')
            print('Nenhum processo pendente.')
        else:
            tam=fila_quant.tamanho()
            tam2=pilha_prcss.tamanho()
            print(f'{tam} processos realizados.')
            print(f'{tam2} processos pendentes.')

    elif esc==4:
        print('Até breve!\nEncerrando programa...')
        break 

    else:
        print('Escolha Inválida.')

