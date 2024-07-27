#crie um sistema de biblioteca utilizando as estruturas apresentadas na aula de IED
#adc=adicionar // rmv=remover // prc=procurar // lst=listar

def adc_livro(biblioteca, livro, autor, genero):
    if livro not in biblioteca:
        biblioteca[livro] = {'autor': autor, 'genero': genero}
        print(f"O livro '{livro}' do autor '{autor}' foi adicionado à coleção na aba de '{genero}'\n")

def rmv_livro(biblioteca, livro):
    if livro in biblioteca:
        del biblioteca[livro]
        print(f"Livro '{livro}' foi removido.")
    else:
        print("Livro não está na coleção.")

def prc_livro(biblioteca, livro):
    if livro in biblioteca:
        titulo = biblioteca[livro]
        print(f"Aqui esta seu livro {livro}: '{titulo}' ")

    else:
        print("Este livro não foi encontrado")

def lst_livro(biblioteca):
    for titulo, info in biblioteca.items():
        autor = info['autor']
        genero = info['genero']
        print(f'Titulo: {titulo}, Autor: {autor}, Gênero: {genero}')


def menu():
    biblioteca = {}
    while True:
        print('Escolha a opção desejada:\n[1]-Adicionar livro a coleção\n[2]-Remover livro da coleção\n[3]-Procurar titulo específico\n[4]-Listar toda a coleção\n[5]-Desligar sistema')
        esc = input('')

        if esc == '1':
            livro = input('Digite o nome do livro: ')
            aut = input('Digite o nome do autor: ')
            gen = input('Digite o gênero do livro: ')
            adc_livro(biblioteca, livro, aut, gen)

        elif esc == '2':
            livro = input('Digite o livro que voce deseja remover: ')
            rmv_livro(biblioteca, livro)

        elif esc == '3':
            livro = input('Escreva o titulo que deseja procurar: ')
            prc_livro(biblioteca, livro)

        elif esc == '4':
            print('Sua lista será mostrada.')
            lst_livro(biblioteca)

def main():
    menu()
    pass

if __name__ == "__main__":
    main()
    pass