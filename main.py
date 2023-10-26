import os
import time
import pyperclip

account_list = {}
PATH = ""

class Account:
    def __init__(self, ingame_name, username, password):
        self.ingame_name = ingame_name
        self.username = username
        self.password = password

def main():
    load_accounts()
    print("------Welcome to League Account Manager------")
    print("1) Print Account List")
    print("2) Select Account")
    print("3) Add Account to the List")
    print("4) Delete Account from the List")
    print("5) Exit")

    choice = input("[!] Enter your choice: ")

    if choice == "1":
        print_account_list(2)
    elif choice == "2":
        select_account()
    elif choice == "3":
        add_account()
    elif choice == "4":
        delete_account()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")
        main()

def load_accounts():
    with open(PATH) as f:
        for linea in f:
            partes = linea.strip().split(':')
            if len(partes) == 3:
                usuario, clave, otro = partes
                account_list[usuario] = Account(usuario, clave, otro)
    f.close()

def print_account_list(i):
    if i == 1:
        print("\nAccount List:")
        count = 1
        for account in account_list:
            print(f"{count}) {account_list[account].ingame_name}")
            count += 1
    elif i == 2:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen (Windows or Unix)
        print("\nAccount List:")
        count = 1
        for account in account_list:
            print(f"{count}) Ingame Name: {account_list[account].ingame_name}, Username: {account_list[account].username}")
            count += 1
        print("Esperando...")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen (Windows or Unix)
        main()

def select_account():
    print_account_list(1)
    opt = int(input("[!] Enter your choice: "))
    count = 1
    for account in account_list:
        if count == opt:
            print("\nSelected Account: " + account_list[account].ingame_name)
            pyperclip.copy(account_list[account].username)
            print(f"Username: {account_list[account].username}\nPassword: {account_list[account].password}")
            print("\nUsername copied to clipboard!")
            input("\nPress enter to continue...")

        count += 1

def add_account():
    print("Add Account")
    ingame_name = input("Enter ingame name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    new_account = Account(ingame_name, username, password)
    account_list[ingame_name] = new_account

    with open(PATH, "a") as f:
        f.write(f"\n{ingame_name}:{username}:{password}\n")
    
def delete_account():
    print_account_list(1)
    print("Delete Account")
    opt = int(input("Enter your choice: "))
    count = 1
    to_delete = None
    for account in account_list:
        if count == opt:
            print("\nSelected Account: " + account_list[account].ingame_name)
            print(f"Username: {account_list[account].username}\nPassword: {account_list[account].password}")
            to_delete = account
        count += 1

    if to_delete:
        del account_list[to_delete]
        with open(PATH, "r") as f:
            lines = f.readlines()
            f.close()
        with open(PATH, "w") as f:
            for line in lines:
                if line.strip("\n") != f"{to_delete}:{account_list[to_delete].username}:{account_list[to_delete].password}":
                    f.write(line)
            f.close()
        print("Account deleted")
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen (Windows or Unix)
        main()

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen (Windows or Unix)
    main()
