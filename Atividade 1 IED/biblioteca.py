#crie um sistema de biblioteca utilizando as estruturas apresentadas na aula de IED
#adc=adicionar // rmv=remover // prc=procurar // lst=listar

#To com problema em printar umas coisas (linha 27)
#melhorar a forma que ta printando
#quero mudar o jeito que ta listando os livros
#Perguntar dos 'pass' e 'if name'
#
#
biblioteca = {
}
def adc_livro(biblioteca, livro, autor, genero):
    if livro not in biblioteca:
        biblioteca[livro] = {'autor': autor, 'genero': genero}
        print(f"o livro '{livro}' do autor '{autor}' foi adicionado a coleçao na aba de '{genero}'")
        pass

def rmv_livro(biblioteca, livro):
    if livro in biblioteca:
        del biblioteca[livro]
        print(f"livro '{livro}' foi removido.")
    else:
        print("livro não está na coleção.")
    pass

def prc_livro(biblioteca, livro):#aqui é pro usuario procurar um livro especifico
    if livro in biblioteca:
        print("Aqui esta seu livro: '{biblioteca[livro]}' ")

    else:
        print("este livro nao foi encontrado")
    pass

def lst_livro(biblioteca):
    itens = biblioteca.items()
    print('lista dos livros da biblioteca:')
    print(itens) #quero botar algo para quando a lista tiver vazia mande um recado

    pass

def menu():
    biblioteca = {}
    while True:
        print('Escolha a opção desejada:\n[1]-Adicionar livro a coleção\n[2]-Remover livro da coleção\n[3]-Procurar titulo específico\n[4]-Listar toda a coleção')
        esc = input('')

        if esc == '1':
            livro = input('Digite o nome do livro: ')
            aut = input('Digite o nome do autor: ')
            gen = input('Digite o gênero do livro: ')
            adc_livro(biblioteca, livro, aut, gen)

        elif esc == '2':
            livro = input('digite o livro que voce deseja remover: ')
            rmv_livro(biblioteca, livro)

        elif esc == '3':
            livro = input('escreva o titulo que deseja procurar: ')
            prc_livro(biblioteca, livro)

        elif esc == '4':
            print('sua lista será mostrada.')
            lst_livro(biblioteca)


        pass

def main():
    menu()
    pass

if __name__ == "__main__":
    main()
    pass
