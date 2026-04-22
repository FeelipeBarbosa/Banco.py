def AdicionarDinheiro(Saldo):
    Valor = float(input("Digite o valor do deposito desejado: "))
    if Valor > 0:
        Saldo += Valor
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")
    return Saldo
def SacarDinheiro(Saldo):
    valor = float(input("Digite o valor de saque desejado: "))
    if Saldo >= valor:
        Saldo -= valor
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realização de saque.")
    return Saldo
def ConsultraSaldo(Saldo):
    print(f"Saldo em conta: R${Saldo:.2f}")

Saldo = 0
opção = ''

while opção != '0':

    print("=====Bem-vindo ao Banco Citóbank=====")
    print("=====Menu de opções=====")
    print("1.Adicionar dinheiro")
    print("2.Sacar dinheiro")
    print("3.Consultar saldo em conta")
    print("0.Sair")
    print("=========================")

    opção = input( 
        
        
        "Digite a opção desejada: ")

    if opção == '1':
        Saldo = AdicionarDinheiro(Saldo)

    if opção =='2':
        Saldo = SacarDinheiro(Saldo)

    if opção == '3':
        ConsultraSaldo(Saldo)   

    if opção == '0':
        print("Obrigado por usar o Banco Citóbank, volte sempre!")

    else:
        print("Opção inválida, tente novamente.")   