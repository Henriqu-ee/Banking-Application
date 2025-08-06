from models.transaction import Transacao

def solicitar_emprestimo(conta, valor):
    conta.deposito(valor)
    conta.historico.append(Transacao("Empréstimo", valor))

def aplicar_poupanca(conta, valor, meses):
    taxa = 0.0065
    montante = valor * ((1 + taxa) ** meses)
    if conta.saque(valor):
        conta.historico.append(Transacao("Poupança", valor, descricao=f"Retorno esperado: R${montante:.2f}"))
        return montante
    return None
