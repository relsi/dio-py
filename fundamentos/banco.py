menu = """
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [4] Sair
  """
saldo = 0
extrato = []
qtd_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)
  
  if opcao == "1":
    valor = input()
    
    try:
      valor = float(valor.replace(",", "."))
    except:
      valor = 0

    if valor > 0:
      saldo += valor
      extrato.append(("Depósito", f"{valor:.2f}"))
    else:
      print("Valor de depósito inválido")

  elif opcao == "2":
    valor = input()

    try:
      valor = float(valor.replace(",", "."))
    except:
      valor = 0

    if valor > 0:
      if valor > saldo:
        print("Saldo insuficiente para essa operação")

      elif qtd_saques >= LIMITE_SAQUES:
        print("Você já efetuou o limite de saques hoje.")

      elif int(valor) > LIMITE:
        print("Limite de saque de R$ 500.00")

      else:
        saldo -= valor
        qtd_saques += 1
        extrato.append(("Saque", f"{valor:.2f}"))

    else:
      print("Valor de saque inválido")

  elif opcao == "3":
    print("======== Extrato ========")

    if len(extrato):
      for operacao in extrato:
        print(f"{operacao[0]}: R$ {operacao[1]}")

    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========    *    ========")
    
  elif opcao == "4":
    break

  else:
    print("opção inválida")