import os
import time
# from opgg.opgg import OPGG
# from opgg.summoner import Summoner

account_list = {}
path = ""


def main():
    load_accounts()
    print("------Welcome to Leauge Acoount Manager------")
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

    # for i in account_list:
    #     print(i)
    #     print(account_list[i])


def load_accounts():
    with open(path) as f:
        for linea in f:
            partes = linea.strip().split(':')
            if len(partes) == 3:
                usuario, clave, otro = partes
                account_list[usuario] = {'username': clave, 'password': otro}
    f.close()


def print_account_list(i):
    if i == 1:
        print("\n\nAccount List: ")
        count = 1
        for account in account_list:
            print(str(count) + ") " + account)
            count += 1
    elif i == 2:
        os.system('cls')
        print("\n\nAccount List: ")
        count = 1
        for account in account_list:
            print(str(count) + ") " + account)
            count += 1
        print("Esperando...")
        time.sleep(3)
        os.system('cls')
        main()


def select_account():
    print_account_list(1)
    opt = int(input("[!] Enter your choice: "))
    count = 1
    for account in account_list:
        if count == opt:
            print("\nSelected Account: " + account)
            print("Username: " + account_list[account]['username'] +
                  "\nPassword: " + account_list[account]['password'])
            return account
        count += 1


def add_account():
    print("Add Account")
    usuario = input("Enter ingame name: ")
    clave = input("Enter username: ")
    otro = input("Enter password: ")

    # add to the file
    with open(path, "a") as f:
        f.write("\n")
        f.write(usuario + ":" + clave + ":" + otro + "\n")
        f.close()


def delete_account():
    print_account_list(1)
    print("Delete Account")
    opt = int(input("Enter your choice: "))
    count = 1
    for account in account_list:
        if count == opt:
            print("\nSelected Account: " + account)
            print("Username: " + account_list[account]['username'] +
                  "\nPassword: " + account_list[account]['password'])
            with open(path, "r") as f:
                lines = f.readlines()
                f.close()
            with open(path, "w") as f:
                for line in lines:
                    if line.strip("\n") != account + ":" + account_list[account]['username'] + ":" + account_list[account]['password']:
                        f.write(line)
                f.close()
            del account_list[account]
            print("Account deleted")
            time.sleep(3)
            os.system('cls')
            main()
        count += 1


os.system('cls')
main()
