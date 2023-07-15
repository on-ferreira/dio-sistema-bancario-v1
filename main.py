log = []
saldo = 0.00
op = 0
ctSaques = 0

while(op != 4):
    print(''' 
--- Digite a operação que deseja realizar ---

1 - Depósito
2 - Saque
3 - Extrato
4 - Sair
---------------------------------------------
    ''')
    op = int(input())

    if op == 1:
        valor = int(input('Digite o valor do deposito: '))
        if valor > 0:
            saldo += valor
            log.append("Depósito R$ "+str(valor))

    elif op == 2 :
        valor = int(input('Digite o valor do saque: '))
        if valor > saldo:
            print("Saldo insuficiente")
        elif ctSaques >= 3:
            print("Limite de saques atingido")
        elif valor > 500:
            print("O limite por saque é de R$500.00")
        else:
            ctSaques += 1
            saldo -= valor
            log.append("Saque R$ "+str(valor))

    elif op == 3:
        print("Saldo R$ "+str(saldo))
        if len(log)==0:
            print("Não foram realizadas movimentações.")
        else:
            print("Log de Operações")
            for op in log:
                print(op)

    elif op == 4:
        exit()
