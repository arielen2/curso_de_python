import random
conta = random.randint(1000, 90000)#me da numeros aleatorios
dicionario = {}
saldo = 0
def banco():
    nome = str(input("nome"))
    cpf = float(input("cpf"))
    numero = float(input("numero"))
    dicionario["nome"] = nome
    dicionario["cpf"] = cpf
    dicionario["numero"] = numero
    dicionario["conta"] = conta
    dicionario["saldo"] = saldo
    print("Sua conta é:", conta, "nome:", nome, "cpf:", cpf, "numero:", numero)
    return("conta criada")

def saldo_conta():
    print("seu saldo é",dicionario["saldo"] )

def deposito():
    deposito = float(input("digite o valor do deposito"))
    ari = saldo + deposito
    dicionario["saldo"] = ari
    print("VALOR DEPOSITADO:", dicionario["saldo"])

def saque():
    saque = float(input("valor para saque"))
    if dicionario["saldo"] >= saque:
       dicionario["saldo"] -= saque
       print(dicionario["saldo"])
    
    else:
        print ("sem saldo suficiente")
   
while True:

    print()
    print()

    print("BEM VINDO AO SEU BANCO")
    print()
    print("1 = criar conta")
    print("2 = saldo")
    print("3 = deposito")
    print("4 = saque")
    print("0 = encerrar atendimento")
    print()
    opcao = input("digite sua opção: ")
    if opcao == '1':
        banco()
    elif opcao == "2":
        saldo_conta()
    elif opcao == "3":
        deposito()
    elif opcao == "4":
        saque()
    else:
        print("atendimento encerrado")
        break




