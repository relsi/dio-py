menu = """
  [1] Depositar
  [2] Sacar
  [3] Extrato
  [4] Cadastrar Correntista
  [5] Listar Correntistas
  [6] Criar Conta
  [7] Listar Contas
  [8] sair
  """

def depositar(saldo, valor, extrato, /):
    saldo += valor
    extrato.append(("Depósito", f"{valor:.2f}"))
    print("Depósito efetuado com sucesso!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, limite_saques, qtd_saques):
    if valor > saldo:
        print("Saldo insuficiente para essa operação")
    elif qtd_saques >= limite_saques:
        print("Você já efetuou o limite de saques hoje.")
    elif int(valor) > limite:
        print("Limite de saque de R$ 500.00")
    else:
        saldo -= valor
        qtd_saques += 1
        extrato.append(("Saque", f"{valor:.2f}"))
    return saldo, extrato

def imprime_extrato(saldo, /, *, extrato):
    print("======== Extrato ========")
    if len(extrato):
        for operacao in extrato:
            print(f"{operacao[0]}: R$ {operacao[1]}")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========    *    ========")

def criar_conta(numeros_conta, contas, correntistas, numero_agencia):
    numero = numeros_conta + 1
    agencia = numero_agencia
    cpf = input("Informe o número do CPF: ")
    correntista = next((i for i in correntistas if i['cpf'] == cpf), False)
    if correntista:
        contas.append({"numero":numero, "correntista":correntista, "agencia":agencia})
        print("conta cadastrada com sucesso.")
    else:
        print("Esse CPF já não pertence a nenhum correntista!")
        return numeros_conta, contas
    return numero, contas

def listar_contas(contas):
    for i in contas:
        dados = f"Nº: {i['numero']}, Agencia: {i['agencia']}, Correntista: {i['correntista']['nome']}"
        print(dados)

def cadastrar_correntista(correntistas):
    cpf = input("Informe o número do CPF: ")
    if next((i for i in correntistas if i['cpf'] == cpf), False):
        print("Esse CPF já esta cadastrado!")
        return
    else:
        nome = input("Informe o nome do correntista: ")
        nascimento = input("Informe a data de nascimento do correntista: ")
        endereco = input("Informe o endereço completo: ")
        correntistas.append({"nome":nome, "nascimento":nascimento, "endereco":endereco, "cpf":cpf})
        print("correntista cadastrado com sucesso")

def listar_correntistas(correntistas):
    for i in correntistas:
        dados = f"Nome: {i['nome']}, CPF: {i['cpf']}, Data de Nascimento: {i['nascimento']}, Endereço: {i['endereco']}"
        print(dados)


def main():
    AGENCIA = "0001"
    LIMITE = 500
    LIMITE_SAQUES = 3
    saldo = 0
    qtd_saques = 0
    numeros_conta = 0
    extrato = []
    correntistas = []
    contas = []

    while True:
        opcao = input(menu)
  
        if opcao == "1":
            valor = input("Informe o valor do depósito: ")
            try:
                valor = float(valor.replace(",", "."))
            except:
                valor = 0

            if valor > 0:
                saldo, extrato = depositar(saldo, valor, extrato)
            else:
                print("Valor de depósito inválido")
        elif opcao == "2":
            valor = input("Informe o valor do saque: ")
            try:
                valor = float(valor.replace(",", "."))
            except:
                valor = 0

            if valor > 0:
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=LIMITE,
                    limite_saques=LIMITE_SAQUES,
                    qtd_saques=qtd_saques
                )
            else:
                print("Valor de saque inválido")
        elif opcao == "3":
            imprime_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            cadastrar_correntista(correntistas)
        elif opcao == "5":
            listar_correntistas(correntistas)
        elif opcao == "6":
           numeros_conta, contas = criar_conta(numeros_conta, contas, correntistas, AGENCIA)
        elif opcao == "7":
            listar_contas(contas)
        elif opcao == "8":
            break
        else:
            print("opção inválida")

main()