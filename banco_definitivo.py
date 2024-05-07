
import re
pattern = re.compile(r"\d{11}")

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]Nova conta
    [lc]Listar contas
    [nu]Novo usuário
    [q]\tSair
    => """
    return input(menu)

def procurarCPF(usuarios:list, cpf):
    existe = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return existe[0] if existe else None


def criarUsuario(usuarios:list):
    cpf = input("digite seu cpf:")
    #checa se o formato é válido
    if re.match(pattern, cpf):  
        if not procurarCPF(usuarios, cpf):
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
            print("usuario criado com sucesso")
        else: print("Usuario ja existe")
        
        
def criarConta(AGENCIA,numero_conta,usuarios):
    cpf = input("digite cpf do usuario:")
    if re.match(pattern, cpf): 
        user = procurarCPF(usuarios, cpf)
        if user:
            conta:dict = {"Agência": AGENCIA, "Número da conta":numero_conta+1, "Usuário": user}
            return conta
        else: print("Usuário não existe")    
    

    
def main():
    usuarios = []
    contas = []
    saldo= 0
    historico = []
    LIMITE = 3
    numero_conta = 0
    AGENCIA = "0001"
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            operacao = deposito(valor, historico)
            if(operacao):
                saldo+= valor
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            operacao = saque(valor, saldo, historico, LIMITE=LIMITE,)
            if(operacao):
                saldo-= valor
                LIMITE-=1         
        elif opcao == "e":
            extrato(historico)
            print(f"Saldo atual: R${saldo}")
            
        elif opcao == "lc":
            listar_contas(contas)          
        elif opcao == "nc":
            contas.append(criarConta(AGENCIA,numero_conta,usuarios))
            numero_conta+=1
        elif opcao == "nu":
            criarUsuario(usuarios)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def saque(valor,saldo, historico, LIMITE):
    if saldo ==0:
        print("Não há saldo na conta")
        return
    
    if LIMITE==0:
        print("Limite diario atingido")
        return
    
    if valor >500:
        print("Valor ultrapassa limite de saque")
        return
    
    if valor > saldo:
        print("Valor ultrapassa saldo")
        return
    historico.append(f'Saque: R${valor:.2f}')
    print("Saque Realizado")
    return True
    

    
def deposito(valor, historico:list, /):
    if valor > 0:
        historico.append(f'Depósito: R${valor:.2f}')
        print("Valor depositado!")
        return True
    else: 
        print("Valor deve ser maior que zero") 
        return 

def extrato(historico):
    print("\n================ EXTRATO ================")
    if historico:
        for item in historico:
            print(item)
    else: print("Não houve operações")   
    print("==========================================")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['Agência']}
            C/C:\t{conta['Número da conta']}
            Titular:\t{conta['Usuário']['nome']}
        """
        print("=" * 100)
        print(linha)

main()