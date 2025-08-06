import sqlite3
import os
from models.user import User
from models.account import Conta
from models.transaction import Transacao
from database.db_transaction_manager import (
    criar_tabela_transacoes,
    salvar_transacao,
    carregar_transacoes
)

def conectar():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect("data/db.sqlite")

def criar_tabelas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contas (
                num_conta TEXT PRIMARY KEY,
                nome TEXT,
                cpf TEXT,
                saldo REAL
            )
        """)
        conn.commit()
    criar_tabela_transacoes()  # cria também a tabela de transações

def salvar_conta(conta):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO contas (num_conta, nome, cpf, saldo)
            VALUES (?, ?, ?, ?)
        """, (conta.num_conta, conta.proprietario.nome, conta.proprietario.cpf, conta.saldo))
        conn.commit()

    # Salvar todas as transações novas (as que ainda não estão salvas)
    # Neste caso, salvamos tudo para simplificar
    #for transacao in conta.historico:
    #    salvar_transacao(conta.num_conta, transacao)

def carregar_conta(num_conta):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT num_conta, nome, cpf, saldo FROM contas WHERE num_conta = ?", (num_conta,))
        row = cursor.fetchone()
        if row:
            user = User(row[1], row[2])
            conta = Conta(row[0], user, row[3])
            conta.historico = carregar_transacoes(row[0])
            return conta
    return None
