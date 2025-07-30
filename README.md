# Banking-Application


A complete banking system developed in Python with support for multiple features such as account creation, transfers, transaction history, loan management, bill payments, currency exchange, and more.

## Summary

- [Features](#features)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Possible Improvements](#possible-improvements)
- [License](#license)

## Features

- [x] Bank account creation and management
- [x] Account transfers
- [x] Transaction history
- [x] Loan application and submission
- [x] Bill payments
- [x] Account activity alerts
- [x] Checkbook requests
- [x] Currency conversion with updated rates
- [x] Investment simulation
- [x] Customer support via ticket system

## Prerequisites

- Python 3.8 or higher

---

## How to run

```bash
# Clone the repository
git clone https://github.com/luizleite/banking-app.git
cd banking-app

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows

# Install dependencies (if any)
pip install -r requirements.txt

# Run the system
python main.py
Enviar feedback
Resultados de tradução disponíveis
```

## Estrutura do projeto

```bash
banking-app/
│
├── main.py                  # Ponto de entrada da aplicação
├── models/                  # Classes principais (User, Account, etc.)
│   ├── user.py
│   └── account.py
│
├── services/                # Regras de negócio (transferência, empréstimo, etc.)
│   ├── transfer_service.py
│   ├── loan_service.py
│   └── notification_service.py
│
├── utils/                   # Funções auxiliares (como conversão de moedas)
│   └── currency_api.py
│
├── database/                # Gerenciamento do banco de dados
│   └── db_manager.py
│
├── data/                    # Arquivos de exemplo ou base local
│   └── db.sqlite
│
├── README.md                # Documentação do projeto
├── LICENSE                  # Licença de uso
└── requirements.txt         # Dependências do projeto


