users = []
contas = []

class User:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, num_conta, proprietario, saldo = 0.0):
        self.num_conta = num_conta
        self.proprietario = proprietario
        self.saldo = saldo

    def deposito(self, quantidade):
        if quantidade > 0.0:
            self.saldo += quantidade

def procurar_conta(num_conta):
    for conta in contas:
        if conta.num_conta == num_conta:
            return conta
    return None

def criando_user():
    nome = input("Nome do titular: ")
    cpf = input("CPF: ")
    num_conta = input("Número da conta: ")

    user = User(nome, cpf)
    conta = Conta(num_conta, user)

    users.append(user)
    contas.append(conta)

    print(f"\nConta criada com sucesso para {user.nome}!\n")

def depositar():
    acc_num = input("Número da conta: ")
    conta = procurar_conta(acc_num)

    if acc_num:
        quantidade = float(input("Valor para depósito: "))
        conta.deposito(quantidade)
        print(f"Depósito de R${quantidade:.2f} realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def menu():
    while True:
        print("-----Sistema Bancário Alagoas-----")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Ver saldo")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criando_user()
        elif opcao == "2":
            depositar()
        #elif opcao == "3":

        #elif opcao == "4":

        #elif opcao == "5":

        elif opcao == "6":
            print("Encerrando o sistema. Obrigado!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
