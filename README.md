# Simple Bank Account Management System

A Python CLI application that allows users to manage bank accounts, perform basic financial transactions (deposit, withdraw, check balance), and save customer data persistently using a CSV file.

## Features

- **Account Management:** Create new accounts and auto-generate unique account indices.
- **Transaction Processing:** Perform deposits, withdrawals, and balance inquiries.
- **Persistent Storage:** Saves account state automatically to `account_DB.csv` across sessions.
- **Standalone Executable Support:** PyInstaller spec included to package the application as a standalone binary executable.

## Project Structure

```text
├── Bank_Account_2.py   # Defines the core BankAccount class and methods
├── accounts.py         # Main execution script handling UI logic and file I/O
├── account_DB.csv      # Local database file for storing account records
├── accounts.spec       # PyInstaller specification file for building an executable
└── notes.txt           # OOP design reference notes
