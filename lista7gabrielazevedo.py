def inserir_filmes():
    novos_filmes = ()
    t = 's'
    while t == 's':
        titulo = input('Digite o titulo do filme: ')
        genero = input('Digite o genero do filme: ')
        atores = ()
        while t == 's':
            ator = input('Digite o nome de um ator do filme: ')
            atores += (ator,)
            t = input('Deseja digitar outro ator?(s/n) ')
        nota = float(input('Digite a nota do filme: '))
        novos_filmes += ((titulo, genero, atores, nota),)
        t = input('Deseja inserir outro filme?(s/n) ')
    return novos_filmes

def imprimir(tupla_de_filmes):
    if tupla_de_filmes == ():
        print('Nao ha filmes cadastrados.')
    for filme in tupla_de_filmes:
        if (filme[3]*100)%10 == 0:
            decimais = '0'
        else:
            decimais = ''
        s = 'Titulo: {}; Genero: {}; Atores: {}; Nota: {}{}'.format(filme[0],filme[1],filme[2],filme[3],decimais)
        print(s)

def imprimir_genero(tupla_de_filmes):
    if tupla_de_filmes == ():
        print('Nao ha filmes cadastrados.')
    else:
        genero = input('Digite o genero que deseja procurar: ')
        t = False
        for filme in tupla_de_filmes:
            if filme[1].upper() == genero.upper():
                t = True
                if (filme[3]*100)%10 == 0:
                    decimais = '0'
                else:
                    decimais = ''
                s = 'Titulo: {}; Genero: {}; Atores: {}; Nota: {}{}'.format(filme[0],filme[1],filme[2],filme[3],decimais)
                print(s)
        if t == False:
            print('Genero nao encontrado.')

def imprimir_ator(tupla_de_filmes):
    if tupla_de_filmes == ():
        print('Nao ha filmes cadastrados.')
    else:
        ator = input('Digite o ator que deseja procurar: ')
        t = False
        for filme in tupla_de_filmes:
            for atores in filme[2]:
                if atores.upper() == ator.upper():
                    t = True
                    if (filme[3]*100)%10 == 0:
                        decimais = '0'
                    else:
                        decimais = ''
                    s = 'Titulo: {}; Genero: {}; Atores: {}; Nota: {}{}'.format(filme[0],filme[1],filme[2],filme[3],decimais)
                    print(s)
        if t == False:
            print('Ator nao encontrado.')

def remover_dados(tupla_de_filmes):
    while True:
        remover = input('Digite o nome do filme: ')
        nova_tupla = ()
        t = False
        for filme in tupla_de_filmes:
            if filme[0].upper() == remover.upper():
                t = filme
                continue
            nova_tupla += (filme,)
        tupla_de_filmes = nova_tupla
        if t == False:
            print('Filme nao encontrado.')
        else:
            print(t)
            print('Filme removido com sucesso.')
        s = input('Deseja remover outro filme?(s/n) ')
        if s != 's':
            break
    return tupla_de_filmes

def main1():
    tupla_de_filmes = ()
    while True:
        print('1 - Inserir um ou mais filmes(s)')
        print('2 - Mostrar a lista de filmes')
        print('3 - Listar filmes de um genero')
        print('4 - Listar filmes de um ator')
        print('5 - Remover um ou mais filmes(s)')
        print('6 - Sair')
        opcao = int(input('Digite uma opcao: '))
        if opcao == 1:
            tupla_de_filmes += inserir_filmes()
        elif opcao == 2:
            imprimir(tupla_de_filmes)
        elif opcao == 3:
            imprimir_genero(tupla_de_filmes)
        elif opcao == 4:
            imprimir_ator(tupla_de_filmes)
        elif opcao == 5:
            tupla_de_filmes = remover_dados(tupla_de_filmes)
        else:
            break
    return tupla_de_filmes

            
    
