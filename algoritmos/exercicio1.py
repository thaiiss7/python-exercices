lata = 0.35
garrafa_p = 0.6
garrafa_m = 2

continuar = 1

while (continuar == 1):
    print("Opcões de produtos: \n1.Lata de 350ml\n2.Garrafa de 600ml\n3.Garrafa de 2L")
    opcao = int(input("Digite a opção desejada: "))
    quant = int(input("Digite a quantidade do produto: "))

    if (opcao == 1):
        print(f"litros: {lata * quant}L")
    elif (opcao == 2):
        print(f"litros: {garrafa_p * quant}L")
    elif (opcao == 3):
        print(f"litros: {garrafa_m * quant}L")
    else:
        print("Opção inválida")
        
    continuar = int(input("Deseja continuar comprando?\n 1.Sim\n 0.Não"))
