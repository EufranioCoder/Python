palavrasSorteadasParaOJogo = None


def telaDeInicio():
    menuInicial = '''-----------------------------------
    |*******-GAME DAS PALAVRAS-*******|
    -----------------------------------
    Niveis:____________________________
    1 >>>>>>>>>>>>>>>> Iniciante      |
    2 >>>>>>>>>>>>>>>> Intermédio     |
    3 >>>>>>>>>>>>>>>> Díficil        |
    -1 >>>>>>>>>>>>>>> Terminar       |
    -----------------------------------'''
    print(menuInicial)
    lerNivelDesejadoPeloUsuario()


def lerNivelDesejadoPeloUsuario():
    nivel = str(input('Qual nível pretende: ')).strip()
    validarONivelInseridoPeloUsuario(nivel)


def validarONivelInseridoPeloUsuario(nivel):
    if not nivel[0] in '123-':
        print('O nível inserido é invalido')
    else:
        selecionarAsListasDePalavrasParaOJogo(nivel)


def selecionarAsListasDePalavrasParaOJogo(nivel):
    '''
    A Lista de Palavras a serem carregadas vai depender do nivel
    '''
    palavrasSorteadas = []

    if(nivel == '1'):
        from ConjuntoDePalavrasParaOJogo import PalavrasCom4Letras, PalavrasCom5Letras
        gerarAListaDePalavrasSorteadas(PalavrasCom4Letras, PalavrasCom5Letras)
    elif(nivel == '2'):
        from ConjuntoDePalavrasParaOJogo import PalavrasCom5Letras, PalavrasCom6Letras
        gerarAListaDePalavrasSorteadas(PalavrasCom5Letras, PalavrasCom6Letras)
    elif(nivel == '3'):
        from ConjuntoDePalavrasParaOJogo import PalavrasCom6Letras, PalavrasCom8Letras
        gerarAListaDePalavrasSorteadas(PalavrasCom6Letras, PalavrasCom8Letras)


def gerarAListaDePalavrasSorteadas(lista1Palavras, lista2Palavras):
    from random import choice
    global palavrasSorteadasParaOJogo
    quantPalavrasSorteadas = 0
    palavrasSorteadas = []

    while quantPalavrasSorteadas < 6:
        if quantPalavrasSorteadas < 3:
            palavraSorteada = choice(lista1Palavras)
            if not palavraSorteada in palavrasSorteadas:
                palavrasSorteadas.append(palavraSorteada)
                quantPalavrasSorteadas += 1
        else:
            palavraSorteada = choice(lista2Palavras)
            if not palavraSorteada in palavrasSorteadas:
                palavrasSorteadas.append(palavraSorteada)
                quantPalavrasSorteadas += 1
    
    palavrasSorteadasParaOJogo = palavrasSorteadas


def carregarNomes(nivel = 1):
    from random import choice
    from ConjuntoDePalavrasParaOJogo import PalavrasCom4Letras, PalavrasCom5Letras, PalavrasCom6Letras, PalavrasCom8Letras

from random import choice

numeroDeDerrotas = 0
numeroDeVitorias = 0
tot = 1
telaDeInicio()

if __name__ == '__main__':
    while True:
        palavraSorteada = choice(palavrasSorteadasParaOJogo)
        print(f'{tot}º Jogada', '-*-'*20)
        print(f'\033[40;35;1mACERTOS: {numeroDeVitorias}\033[m\n\033[31;40;1mFALHAS: {numeroDeDerrotas}\033[m')
        print(f'Palavras: {palavrasSorteadasParaOJogo}')
        print('_'*35)
        print(f'Pista: A palavra sorteado tem \033[31;40;1m{len(palavraSorteada)} letras\033[m')
        print('-'*50)
        palavraInseridaPeloUsuario = input('Palavra: ')
        tot += 1
        if str(palavraInseridaPeloUsuario).strip().lower() == palavraSorteada:
            print('\033[32;40;1mACERTOU')
            numeroDeVitorias += 1
            continue
        if palavraInseridaPeloUsuario == '-1':
            break
        numeroDeDerrotas += 1
        print('\033[31;40;1mERRADO!!!!')
        print(f'Palavra: {palavraSorteada}')

