#Você é responsavel por criar um sistema simples para gerenciar as reservas de quartos de um hotel.
#o hospede precisa entrar com o nome, check-in, check-out e numero do quarto

def adc_reserva(reservas, numero, id_ant, nome, checkin_dia, checkin_mes, checkout_dia, checkout_mes):
    id_reserva = id_ant + 1
    reserva = {
        'id' : id_reserva, 
        'nome' : nome,
        'numero do quarto' : numero,
        'checkin' : {
        'dia do checkin' : checkin_dia,
        'mes do checkin' : checkin_mes
        },
        'checkout' : {
        'dia do checkout' : checkout_dia,
        'mes do checkout' : checkout_mes
        }
    }
    reservas.append(reserva)
    print(f'Reserva adicionada com sucesso! Seu ID é {id_reserva}')
    return id_reserva 

def cncl_reserva(reservas, id_reserva):
    for reserva in reservas:
        if reserva['id'] == id_reserva:
            reservas.remove(reserva)
            print('Reserva cancelada com sucesso!')
        else:
            print('Reserva não foi encontrada.')


def bsc_reserva(reservas, nome):
    a = False
    for reserva in reservas:
        if reserva['nome'] == nome:
            print(f"ID: {reserva['id']}, Nome: {reserva['nome']}, Quarto: {reserva['numero do quarto']}, Check-in: {reserva['checkin']}, Check-out: {reserva['checkout']}")
            a = True
    if not a:
        print('Reserva não encontrada.')

def menu_edt():
    print('O que você deseja editar?')
    print('[1]-Nome\n[2]-Numero do quarto\n[3]-Dia do check in\n[4]-Mês do checkin\n[5]-Dia do checkout\n[6]-Mês do checkout.')
    esc = int(input(''))
    return esc



def edt_reserva(reservas, id_reserva):
        for reserva in reservas:
            if reserva['id'] == id_reserva:
                opcao = menu_edt()
                if opcao == 1:
                    nome = input('Digite o novo nome: ')
                    reserva['nome'] = nome
                    print(f'nome alterado com sucesso.')
                elif opcao == 2:
                    num = input('Digite o novo numero do qaurto: ')
                    reserva['numero do quarto'] = num
                    print(f'numero alterado com sucesso.')
                elif opcao == 3:
                    dia_checkin = input('Atualize a data do dia do checkin: ')
                    reserva['checkin']['dia do checkin'] = dia_checkin
                    print(f'dia alterado com sucesso.')
                elif opcao == 4:
                    checkin_mes = input('Atualize a data do mês do checkin: ')
                    reserva['checkin']['mes do checkin'] = checkin_mes 
                    print(f'mês alterado com sucesso.')
                elif opcao == 5:
                    checkout_dia = input('Atualize o dia do checkout: ')
                    reserva['checkout']['dia do checkout'] = checkout_dia 
                    print(f'dia alterado com sucesso.')
                elif opcao == 6:
                    checkout_mes = input('Atualize o mês do checkout: ')
                    reserva['checkout']['mes do checkout'] = checkout_mes
                    print(f'mês alterado com sucesso.')
   

def lst_reserva(reservas):
        for reserva in reservas:
            print(f"ID: {reserva['id']}, Nome: {reserva['nome']}, Quarto: {reserva['numero do quarto']}, Check-in: {reserva['checkin']['dia do checkin']} / {reserva['checkin']['mes do checkin']}, Check-out: {reserva['checkout']['dia do checkout']} / {reserva['checkout']['mes do checkout']}")

def chk_disponivel(reservas, num_quarto, a, b, c, d):
    for rsrvs_gerais in reservas:
        if rsrvs_gerais['numero do quarto'] == num_quarto:
            mes_chkin_res = rsrvs_gerais['checkin']['mes do checkin']
            mes_chkout_res = rsrvs_gerais['checkout']['mes do checkout']
            dia_chkin_res = rsrvs_gerais['checkin']['dia do checkin']
            dia_chkout_res = rsrvs_gerais['checkout']['dia do checkout']
             
            if b == mes_chkin_res and d == mes_chkout_res:
                if (a >= dia_chkin_res and a <= dia_chkout_res) or (c >= dia_chkin_res and c <= dia_chkout_res):
                    return False
            elif b >= mes_chkin_res and d <= mes_chkout_res:
                return False
    else:       
        return True
def main():
    id_ant = 0
    reservas = []
    while True:
        print('Bem-vindo ao Hazbin Hotel!')
        print('[1]-Criar reserva\n[2]-Remover reserva\n[3]-Buscar reserva\n[4]-Listar todas as reservas\n[5]-Editar reserva')
        esc = int(input(''))

        if esc == 1:
            print('Adicionar reserva:\nTenha em mãos seus documentos!')
            nome = input('Digite seu nome completo: ')
            checkin_dia = int(input('Dia do check-in: '))
            checkin_mes = int(input('Mês do check-in: '))
            checkout_dia = int(input('Dia de saída: '))
            checkout_mes = int(input('Mês de saída: '))
            numero = int(input('Numero do quarto desejado: '))
            if chk_disponivel(reservas, numero, checkin_dia, checkin_mes, checkout_dia, checkout_mes):
                id_ant = adc_reserva(reservas, numero, id_ant, nome, checkin_dia, checkin_mes, checkout_dia, checkout_mes)
            else:
                print('RESERVA NÃO PODE SER CONCLUIDA. Data ou quarto indisponivel.')

        elif esc == 2:
            print('Remover reserva: ')
            id = int(input('digite o id que deseja cancelar: '))
            cncl_reserva(reservas, id)


        elif esc == 3:
            print('Buscar reserva: ')
            nome = input('Deseja buscar reservas no nome de quem? ')
            bsc_reserva(reservas, nome)

        elif esc == 4:
            print('Listar reservas: ')
            lst_reserva(reservas)

        elif esc == 5:
            print('EDITANDO RESERVAS: ')
            id = int(input('digite o id cujo você deseja editar as informações: '))
            edt_reserva(reservas, id)
if __name__ == "__main__":
    main()

