print("Crie um programa que faça o computador jogar Jokenpô com você.")
print(f'''{"JOGO de J0-KEN-PO":-^45}''')
while True:
    while True:
        try:
            usuario = int(input(f"""\nVAMOS JOGAR?\nESCOLHA UMA OPÇÃO!
            {'PEDRA   [1]':<10}
            {'PAPEL   [2]':<10}
            {'TESOURA [3]':<10}\nDIGITE SUA OPÇÃO->"""))
            break
        except ValueError:
            print("ERRO! -> Verifique se você realmente digitiu um número <-")
    while True:
        if usuario > 3 or usuario < 0:
            print("Opção Inválida.")
            usuario = int(input("""ESCOLHA UM NÚMERO VÁLIDO!
            [1] para PEDRA 
            [2] para PAPEL
            [3] para TESOURA."""))
        else:
            break
    elementos = ["PEDRA!", "PAPEL!", "TESOURA!"]
    from random import choice
    maquina = choice(elementos)
    print("\nO usuário escolheu...")
    from time import sleep
    if usuario == 1:
        print("\nPEDRA!")
    if usuario == 2:
        print("\nPAPEL!")
    if usuario == 3:
        print("\nTESOURA!")
    print("\nA ESCOLHA DA MÁQUINA É...")
    sleep(1)
    print(f"{'JO!':=^15}")
    sleep(1)
    print(f"{'KEN!':=^15}")
    sleep(1)
    print(f"{'PO!':=^15}")
    sleep(1)
    print("\n",maquina,"\n")
    sleep(0.5)
    if usuario == 1 and maquina == elementos[1]:
        print("Máquina venceu!")
    elif usuario == 2 and maquina == elementos[2]:
        print("Máquina venceu!")
    elif usuario == 3 and maquina == elementos[0]:
        print("Máquina venceu!")
    elif usuario == 1 and maquina == elementos[0] or usuario == 2 and maquina == elementos[1] or usuario == 3 and maquina == elementos[2]:
        print("Deu empate!")
    else:
        print("Usuário Venceu!")
    while True:
        pergunta = str(input("Quer jogar mais?Digite [S] para SIM e [N] para NÃO.")).strip().upper()
        if pergunta not in "SN":
            print("Resposta inválida...Quer jogar mais?")
        elif pergunta in "SN":
            break
    if pergunta in "S":
        print("Ok.Então vamos lá...")
    elif pergunta in "N":
        print("FIM de JOGO!Até a próxima..")
        break
