
print("                        ")
print("                        ")
print("BEM VINDO AO SEU BANCO")
print("Pra criar conta digite '0'.")

dicionario = {}
conta = (input("digite '0' para comecar a criar conta"))
cont = 0

while cont == 0:
   print("BEM VINDO AO SEU BANCO")
   print("                        ")
   print('opcao0 = criar conta')
   print("opcao1 = saldo")
   print("opcao2 = deposito")
   print("opcao3 = saque")
   print("opcao4 = encerrar_atendimento")
   print("                        ")
  
   opcao = str(input("DIGITE UMA OPCAO"))

   print("                        ")

   if opcao == "opcao0":
      nome = str(input("nome"))
      cpf = float(input("cpf"))
      numero = float(input("numero"))
      print ("conta criada")

      import random
      conta = random.randint(1000, 90000)#me da numeros aleatorios
      print("Sua conta é:", conta, "nome:", nome, "cpf:", cpf, "numero:", numero)

      saldo = 0
   
      dicionario["nome"] = nome
      dicionario["cpf"] = cpf
      dicionario["numero"] = numero
      dicionario["conta"] = conta
      print("                        ")
   elif(opcao == "opcao2"): #DEPOSITO
     deposito = float(input("digite o valor do deposito"))
     saldo = deposito + saldo
     print("VALOR DEPOSITADO:", saldo)
     dicionario["saldo"] = saldo
   
     print("                        ")
   elif(opcao == "opcao3"): #SAQUE
      saque = float(input("valor para saque"))
      saldo = saque - saldo
      print("SAQUE DE", saldo, "REALIZADO")
      dicionario["saldo"] = saldo
      print("                        ")
   elif(opcao == "opcao1"): #verificar saldo
      print("seu saldo é", saldo)
      dicionario["saldo"] = saldo

   else:
       print("                        ")
       print("atendimento encerrado")



   










