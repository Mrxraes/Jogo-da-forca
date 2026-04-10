def escolherPalavra(arquivo):
    global palavraEscolhida
    try:
        with open('palavras.txt', "r") as arquivo:

            escolha = random.randint(0, 48)
            #print(escolha)

            conteudo = arquivo.readlines()
            palavraEscolhida = conteudo[escolha]

            #print(conteudo)
            print(palavraEscolhida)

            return palavraEscolhida
    except FileNotFoundError:
        print('Arquivo não encontrado')
    else:
        return True
    

def dadosJogador(arquivo2, nome, score):
    try:
        listaAtualizada = []
        usuario_encontrado = False

        with open('usuarios.txt', 'r') as arquivo2:
            linhas = arquivo.readlines()

        for linha in linhas:
            nome_usuario, pontos = linha.strip().split(",")

            if nome_usuario == nome:
                pontos = int(pontos) + score
                usuario_encontrado = True

            listaAtualizada.append(f"{nome_usuario},{pontos}\n")

        if not usuario_encontrado:
            listaAtualizada.append(f"{nome},{score}\n")

        with open('usuarios.txt', 'w') as arquivo2  :
            arquivo2.writelines(listaAtualizada)

    except FileNotFoundError:
         with open('usuarios.txt', 'x') as arquivo2:
            print("O arquivo nao existe, mas acabou de ser criado!")
    except:
        print('Opsss, algo deu errado...')
    else:
        True


    

def esconderFun(palavra):
    global esconder
    tam = len(palavra)
    esconder = '_' * (tam-1)
    print(esconder)

    return esconder

    
def tentativas(palavra, pergunta):
    global chance
    global esconder
    indice = 0 

   

    if len(pergunta) > 1 or len(pergunta) < 1:
        print('Adicione um caracter por vez')
        return None
    
    if pergunta in letrasDigitadas: #amanha verificar essa logica
            print('Você já digitou essa letra!')
            print(esconder)
            #print(letrasDigitadas)
    elif pergunta in palavra:
            for letra in palavra:
                    #print(letra)
                if letra in pergunta:
                    esconder = esconder[:indice] + pergunta + esconder[indice + 1:]

                    print('-' * 15)
                    print('| Você acertou! |')
                    print('-' * 15)

                    print('-' * (len(palavra) + 3))
                    print(f'| {esconder} |')
                    print('-' * (len(palavra) + 3))

                    if chance == 0:
                        print('-' * 33)
                        print('| Sua forca ainda está intacta! |')
                        print('-' * 31)    

                    letrasDigitadas.append(pergunta)
                    indice += 1
                else:
                    #print(letra)
                    #print(f"essa nao, indice dessa = {indice}")
                    indice += 1
            return palavra, esconder
    else:
        espaço = 4
        print('Opsss você errou...')         
        match chance:
            case 0:
                print(f"*{"-" * 7}*")
                print('| CORPO |')
                print(f"*{"-" * 7}*")
                print(f'{espaço * " "}O')
                print('Cabeça criada!')
                print(esconder)
            case 1:
                print(f"*{"-" * 7}*")
                print('| CORPO |')
                print(f"*{"-" * 7}*")
                print(f'{espaço * " "}O')
                print(f'{espaço * " "}|')
                
                print(esconder)
            case 2:
                print(f"*{"-" * 7}*")
                print('| CORPO |')
                print(f"*{"-" * 7}*")
                print(f'{espaço * " "}O')
                print(f'{espaço * " "}|')
                print(f'{espaço * " "}(')
                print(esconder)
            case 3:
                print(f"*{"-" * 7}*")
                print('| CORPO |')
                print(f"*{"-" * 7}*")
                print(f'{espaço * " "}O')
                print(f'{espaço * " "}|')
                print(f'{espaço * " "}()')
                print(esconder)
            case 4:
                print(f"*{"-" * 7}*")
                print('| CORPO |')
                print(f"*{"-" * 7}*")
                print(f'{espaço * " "}O')
                print(f'{espaço * " "}/|')
                print(f'{espaço * " "}()')
                print(esconder)
            case 5:
                print(f"*{"-" * 7}*")
                print('| CORPO |')
                print(f"*{"-" * 7}*")
                print(f'{espaço * " "}O')
                print(f'{espaço * " "}/|\\')
                print(f'{espaço * " "}()')
                print('Forca completa, você perdeu!!')
        letrasDigitadas.append(pergunta)
        chance += 1


#programa       

palavraEscolhida = ''
esconder = ''
score =  0
letrasDigitadas = []
indiceAtualizadas = []

import random

arquivo = 'PROJETOjogoDaForca/palavras.txt'
arquivo2 = 'PROJETOjogoDaForca/usuarios.txt'

chance = 0

decisao = input('Vamos jogar o jogo da forca? (s/n) ').strip().lower()
nome = input('Qual o seu nome? ').strip().lower().title()


if decisao == "s":
    print(f'Obaaaaa, vamos jogar {nome}')
    escolherPalavra(arquivo)
    esconderFun(palavraEscolhida)
    while True:
        tentativas(palavraEscolhida, input('Digite um caracter: '))
        
        if "_" not in esconder:
            #print(f'Esconder agora é -->{esconder}, usuário acertou tudo')
            print(f'{nome}, você venceu!! Ganhou +20 pontos!')
            score += 20
            dadosJogador(arquivo2, nome, score)
            break
        elif chance == 6:
            break
            
#add jogares e score somado
