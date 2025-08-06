from utils.currency_api import get_cambio
from models.transaction import Transacao

def cambio(conta, moeda, valor):
    taxa = get_cambio(moeda)
    if not taxa:
        print("Moeda inválida.")
        return
    if conta.saque(valor):
        convertido = valor / taxa
        conta.historico.append(Transacao("Câmbio", valor, descricao=f"{valor} BRL para {convertido:.2f} {moeda}"))
        return convertido
    else:
        print("Saldo insuficiente.")
        return