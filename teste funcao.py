def checkin_checkout(reservas_gerais, a, b, c, d, e):
    rsrvs_gerais = {
        'quarto' : {
            'numero do quarto' : a
        },
        'checkin' : {
        'dia do checkin' : b,
        'mes do checkin' : c,
        },
        'checkout' : {
        'dia do checkout' : d,
        'mes do checkout' : e,
        }
    }
    reservas_gerais.append(rsrvs_gerais)

def chk_disponivel(reservas_gerais, num_quarto, a, b, c, d):
    for rsrvs_gerais  in reservas_gerais:
        if rsrvs_gerais['quarto']['numero do quarto'] == num_quarto:
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


while True:
    reservas_gerais = []

    numero_quarto = int(input('Numero do quarto: '))
    checkin_dia = int(input('Dia do checkin: '))
    checkin_mes = int(input('Mes do checkin: '))
    checkout_dia = int(input('Dia do checkout: '))
    checkout_mes = int(input('Mes do checkout: '))
    if  chk_disponivel(reservas_gerais, numero_quarto, checkin_dia, checkin_mes, checkout_dia, checkout_mes):  
        checkin_checkout(reservas_gerais, numero_quarto, checkin_dia, checkin_mes, checkout_dia, checkout_mes)
        print('RESERVA CONCLUIDA')
    else:
        print('RESERVA NAO CONCLUIDA')
