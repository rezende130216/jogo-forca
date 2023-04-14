from palavras import palavras
import random


def escolher_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()


def Jogar(palavra):
    palavraSecreta = "_" * len(palavra)
    acertou = False
    letrasErradas = []
    palavrasUsadas = []
    tentativas = 6

    print("Vamos jogar Forca!")
    print(forca(tentativas))
    print("Está é a palavra : %s" % palavraSecreta)

    while not acertou and tentativas > 0:
        tentativa = (input("Tentativa: ")).upper()
        print(tentativa)

        if len(tentativa) == 1 and tentativa.isalpha():
            if tentativa in palavrasUsadas:
                print("Você já tentou essa letra: %s" % tentativa)
            elif tentativa not in palavra:
                print("Letra errada: %s" % tentativa)
                tentativas -= 1
                letrasErradas.append(tentativa)
            else:
                print("Letra correta: %s" % tentativa)
                palavrasUsadas.append(tentativa)
                palavraLista = list(palavraSecreta)
                indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
                for indice in indices:
                    palavraLista[indice] = tentativa
                palavraSecreta = "".join(palavraLista)
                if "_" not in palavraSecreta:
                    acertou = True
        elif len(tentativa) == len(palavra) and tentativa.isalpha():
            if tentativa in palavrasUsadas:
                print("Você já tentou essa palavra: %s" % tentativa)
            elif tentativa != palavra:
                print("Palavra errada: %s" % tentativa)
                tentativas -= 1
                letrasErradas.append(tentativa)
            else:
                acertou = True
                palavraSecreta = palavra

        else:
            print("Invalido!")
        
        print(forca(tentativas))
        print(palavraSecreta)
    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("A palavra era %s" % palavra)

def forca(tentativas):
    estagios = [  # Fim de jogo
        """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
        # Falta 1 tentativa
        """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
        # Faltam 2 tentativas
        """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
        # Faltam 3 tentativas
        """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
        # Faltam 4 tentativas
        """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
        # Faltam 5 tentativas
        """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
        # Estado inicial
        """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
    ]

    return estagios[tentativas]


def Iniciar():
    palavra = escolher_palavra()
    Jogar(palavra)


Iniciar()
