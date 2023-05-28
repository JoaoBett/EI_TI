num=10
game = False

print("Adivinhe o número de 1 a 10!\n")
while not game:
    try:
        guess = int(input("Qual é o número certo? \n"))
        if guess == num:
            print("Parabéns acertou!")
            game = True
        else:
            print("Errou!")
    except KeyboardInterrupt:
        #captura excecao CTRL + C
        print("\n O jogo foi interrompido pelo jogador.")
        break
    except Exception as e:
        #captura todos os erros
        print("Erro inesperado: ", e)
        print("Tente outra vez.")
input("")