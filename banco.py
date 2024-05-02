

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Saird

=> """


def main():
    saldo= 0
    lista = []
    LIMITE = 3
    while True:
        opcao = input(menu)
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            operacao = deposito(valor, lista)
            if(operacao):
                saldo+= valor
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            operacao = saque(valor, saldo, lista, LIMITE)
            if(operacao):
                saldo-= valor
                LIMITE -=1
            
        elif opcao == "e":
            extrato(lista)
            print(f"Saldo atual: R${saldo}")
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def saque(valor,saldo, lista, LIMITE):
    if saldo ==0:
        print("Não há saldo na conta")
        return
    
    if LIMITE ==0:
        print("Limite diario atingido")
        return
    
    if valor >500:
        print("Valor ultrapassa limite de saque")
        return
    
    if valor > saldo:
        print("Valor ultrapassa saldo")
        return
    valor
    lista.append(f'Saque: R${valor:.2f}')
    print("Saque Realizado")
    return True
    

    
def deposito(valor, lista:list):
    if valor > 0:
        lista.append(f'Depósito: R${valor:.2f}')
        print("Valor depositado!")
        return True
    else: 
        print("Valor deve ser maior que zero") 
        return 

def extrato(lista):
    print("\n================ EXTRATO ================")
    if lista:
        for item in lista:
            print(item)
    else: print("Não houve operações")   
    print("==========================================")
 
    
main()