def rodizio(fila, i):
    for _ in range(i):#o traço serve como variavel descartavel
        cli_frente=fila.pop(0)
        fila.append(cli_frente)

    return fila

fila_inicial=['d', 'i', 'e', 'g', 'o']
num_vezes=3

newfila=rodizio(fila_inicial, num_vezes)

print(newfila)
    
    
    