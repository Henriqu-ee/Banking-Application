from database.db_manager import criar_tabelas, salvar_conta, carregar_conta
from database.db_transaction_manager import salvar_transacao, criar_tabela_transacoes, deletar_transacoes
from models.user import User
from models.account import Conta
from services.loan_service import solicitar_emprestimo, aplicar_poupanca
from services.transfer_service import transferir
from services.notification_service import definir_alerta, verificar_alerta
from services.currency_service import cambio 

criar_tabelas()

users = []
contas = []

def procurar_conta(num_conta):
    for conta in contas:
        if conta.num_conta == num_conta:
            return conta
    conta = carregar_conta(num_conta)
    if conta:
        contas.append(conta)
    return conta


def criando_user():
    nome = input("Nome do titular: ")
    cpf = input("CPF: ")
    num_conta = input("Número da conta: ")

    user = User(nome, cpf)
    conta = Conta(num_conta, user)

    salvar_conta(conta)  # grava no banco

    print(f"\nConta criada com sucesso para {user.nome}!\n")


def depositar():
    acc_num = input("Número da conta: ")
    conta = procurar_conta(acc_num)

    if conta:
        quantidade = float(input("Valor para depósito: "))
        conta.deposito(quantidade)
        transacao = conta.historico[-1]
        salvar_transacao(conta.num_conta, transacao)
        salvar_conta(conta)

        print(f"\nDepósito de R${quantidade:.2f} realizado com sucesso!\n")
        verificar_alerta(conta)
    else:
        print("\nConta não encontrada.\n")

def sacar():
    acc_num = input("Número da conta: ")
    conta = procurar_conta(acc_num)

    if conta:
        quantidade = float(input("Valor para saque: "))
        if conta.saque(quantidade):
            salvar_transacao(conta.num_conta, conta.historico[-1])
            salvar_conta(conta)

            print(f"\nSaque de R${quantidade:.2f} realizado com sucesso!\n")
            verificar_alerta(conta)
        else:
            print("\nSaldo insuficiente.\n")
    else:
        print("\nConta não encontrada.\n")

def transferir_entre_contas():
    acc_origem = input("Conta de origem: ")
    acc_destino = input("Conta de destino: ")
    quantidade = float(input("Valor da transferência: "))

    origem = procurar_conta(acc_origem)
    destino = procurar_conta(acc_destino)

    if origem and destino:
        if transferir(origem, destino, quantidade):
            salvar_transacao(origem.num_conta, origem.historico[-1])
            salvar_transacao(destino.num_conta, destino.historico[-1])
            salvar_conta(origem)
            salvar_conta(destino)

            print("\nTransferência realizada com sucesso!\n")
            verificar_alerta(origem)
        else:
            print("\nSaldo insuficiente na conta de origem.\n")
    else:
        print("\nConta(s) não encontrada(s).\n")

def ver_saldo():
    acc_num = input("Número da conta: ")
    conta = procurar_conta(acc_num)
    if conta:
        print(f"\nSaldo atual: R${conta.saldo:.2f}\n")
    else:
        print("\nConta não encontrada.\n")

def ver_historico():
    acc_num = input("Número da conta: ")
    conta = procurar_conta(acc_num)
    if conta:
        print("\\n--- Histórico de Transações ---")
        if not conta.historico:
            print("\nNenhuma transação registrada.\n")
        else:
            for transacao in conta.historico:
                print(f"- {transacao}")
    else:
        print("\nConta não encontrada.\n")

def limpar_historico():
    acc_num = input("Número da conta: ")
    conta = procurar_conta(acc_num)
    if conta:
        confirm = input("Tem certeza que deseja apagar TODO o histórico? (s/n): ").lower()
        if confirm == "s":
            conta.historico.clear()                 # Limpa na memória
            deletar_transacoes(conta.num_conta)     # Limpa no banco
            salvar_conta(conta)                     # Atualiza saldo
            print("\nHistórico apagado com sucesso!\n")
        else:
            print("\nOperação cancelada.\n")
    else:
        print("\nConta não encontrada.\n")

def menu():
    while True:
        print("\\n----- Sistema Bancário Alagoas -----")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Ver saldo")
        print("6 - Ver histórico de transações")
        print("7 - Solicitar empréstimo")
        print("8 - Definir alerta de saldo")
        print("9 - Câmbio de moedas")
        print("10 - Aplicar na poupança")
        print("11 - Sair")
        print("12 - Limpar histórico da conta")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criando_user()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            transferir_entre_contas()
        elif opcao == "5":
            ver_saldo()
        elif opcao == "6":
            ver_historico()
        elif opcao == "7":
            conta = procurar_conta(input("Número da conta: "))
            if conta:
                valor = float(input("Valor do empréstimo: "))
                solicitar_emprestimo(conta, valor)
                salvar_transacao(conta.num_conta, conta.historico[-1])
                salvar_conta(conta)

                print("\nEmpréstimo realizado.\n")
            else:
                print("\nConta não encontrada.\n")
        elif opcao == "8":
            conta = procurar_conta(input("Número da conta: "))
            if conta:
                limite = float(input("Definir alerta se saldo for menor que: R$"))
                print("\n")
                definir_alerta(conta, limite)
            else:
                print("\nConta não encontrada.\n")
        elif opcao == "9":
            conta = procurar_conta(input("Número da conta: "))
            if conta:
                moeda = input("Para qual moeda (USD, EUR, JPY): ").upper()
                valor = float(input("Valor em R$: "))
                valor_convertido = cambio(conta, moeda, valor)
                if valor_convertido is not None:
                    salvar_transacao(conta.num_conta, conta.historico[-1])
                    salvar_conta(conta)
                    print(f"\nOperação realizada com sucesso! Valor convertido: {valor_convertido:.2f} {moeda}\n")
                else:
                    print("\nOperação de câmbio falhou.\n")
            else:
                print("\nConta não encontrada.\n")
        elif opcao == "10":
            conta = procurar_conta(input("Número da conta: "))
            if conta:
                valor = float(input("Valor a aplicar: "))
                meses = int(input("Quantidade de meses: "))
                retorno = aplicar_poupanca(conta, valor, meses)
                if retorno:
                    salvar_transacao(conta.num_conta, conta.historico[-1])  # ⬅️ salva a transação
                    salvar_conta(conta) 
                    print(f"\nAplicação realizada. Retorno esperado: R${retorno:.2f}\n")
            else:
                print("\nConta não encontrada.\n")
        elif opcao == "11":
            print("\nEncerrando o sistema. Obrigado!\n")
            break
        elif opcao == "12":
            limpar_historico()
        else:
            print("\nOpção inválida!\n")

if __name__ == "__main__":
    criar_tabelas()
    criar_tabela_transacoes()
    menu()

