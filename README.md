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

## Project Structure

```bash
banking-app/
│
├── main.py # Application entry point
├── models/ # Main classes (User, Account, etc.)
│ ├── user.py
│ └── account.py
│
├── services/ # Business rules (transfer, loan, etc.)
│ ├── transfer_service.py
│ ├── loan_service.py
│ └── notification_service.py
│
├── utils/ # Helper functions (such as currency conversion)
│ └── currency_api.py
│
├── database/ # Database management
│ └── db_manager.py
│
├── data/ # Sample files or local database
│ └── db.sqlite
│
├── README.md # Project documentation
├── LICENSE # Usage license
└── requirements.txt # Project dependencies
```

## Technologies used

- [x] Python 3.x

- [x] SQLite (or other relational database)

- [x] (Optional) Flask or Tkinter, if available

- [x] Exchange API (simulated or real)

