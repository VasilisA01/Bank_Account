from Bank_Account_2 import BankAccount
import csv
import pandas as pd
import os


accounts = {}

if os.path.exists("account_DB.csv"):
    temp_df = pd.read_csv("account_DB.csv")
    for index, row in temp_df.iterrows():
        account = BankAccount(row['Holder_Name'], row['Account_Number'], row['Balance'])
        accounts[row['Account_Index']] = account
else:
    account_1 = BankAccount("John Doe", "123456789", 1000)
    accounts[1] = account_1
    with open("account_DB.csv", "w" ) as f:
        writer = csv.writer(f)
        writer.writerow(["Account_Index", "Holder_Name", "Account_Number", "Balance"])
        writer.writerow([1, account_1.Holder_Name, account_1.Account_Number, account_1.Balance])

    df = pd.read_csv("account_DB.csv")
    df = df.rename(columns={df.columns[0]: 'Account_Index'})
    df = df.rename(columns={df.columns[1]: 'Holder_Name'})
    df = df.rename(columns={df.columns[2]: 'Account_Number'})
    df = df.rename(columns={df.columns[3]: 'Balance'})


def perform_transaction(account):
    transaction_type = input("Enter transaction type (deposit/withdraw/balance): ")
    amount = float(input("Enter amount: "))
    if transaction_type == "deposit":
        account.deposit(amount)
    elif transaction_type == "withdraw":
        account.withdraw(amount)
    elif transaction_type == "balance":
        account.get_balance()
    else:
        print("Invalid transaction type.")

df = pd.read_csv("account_DB.csv")
acc_list = df['Account_Index'].tolist()

def main():
    choice = input("Do you want to perform a transaction? (yes/no/new): ")
    if choice == "new":
        next_index = len(accounts) + 1
        owner_name = input("Enter owner name: ")
        account_number = input("Enter Account_Number: ")
        balance = float(input("Enter initial balance: "))
        new_account = BankAccount(owner_name, account_number, balance)
        accounts[next_index] = new_account
        print("New account created successfully.")
        acc_list.append(acc_list[-1] + 1)
    if choice == "yes":
        idx = int(input("Enter the Account Index you want to access: "))
        if idx in accounts:
            chosen_account = accounts[idx]
            perform_transaction(chosen_account)
            next_choice = input("Would you like anything else? (yes/no): ")
            if next_choice == "yes":
                main()
    
        else:
            print("Account not found.")
            
    
    else:
        print("Thank you for using our banking system.")

main()

with open("account_DB.csv", "w" ) as f:
    writer = csv.writer(f)
    writer.writerow(["Account_Index", "Holder_Name", "Account_Number", "Balance"])

    index_counter = 1

    for account in accounts.values():    
       writer.writerow([index_counter, account.Holder_Name, account.Account_Number, account.Balance])
       index_counter += 1


df = pd.read_csv("account_DB.csv")
print(df)   
print(acc_list,"    Accounts: ",len(acc_list))