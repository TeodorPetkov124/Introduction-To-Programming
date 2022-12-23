import package
import errors
from random import randint 

class Menu:


    def print_menu(self):
        print("1. Create new user")
        print("2. Create account for user")
        print("3. List users")
        print("4. List account for user")
        print("5. Deposit for user account")
        print("6. Withdrawal for user account")
        print("7. Exit")
    
    def create_user_command(self, name, EGN, accounts):
        if len(name) < 4:
            raise errors.InvalidDataFormat("Name must contain at least 4 letters!")
        elif any(chr.isdigit() for chr in name):
            raise errors.InvalidDataFormat("The name must contain only letters!")
        if len(EGN) < 10:
            raise errors.InvalidDataFormat("The EGN must be at least 10 characters!")
        elif any(chr.isalpha() for chr in EGN):
            raise errors.InvalidDataFormat("The EGN must contain only numbers!")
          
        user = package.User(name, EGN, accounts)
        return user

    def create_account_command(self, currency, acc_type, IBAN):
        if currency != "BGN" and currency != "USD" and currency != "EUR" and currency != "JPY":
            raise errors.InvalidAccountCurrency("The currency must be BGN/USD/EUR/JPY!")
        if acc_type != "CURRENT" and acc_type != "SAVINGS" and acc_type != "CREDIT":
            raise errors.InvalidAccountType("Account type must be CURRENT/SAVINGS/CREDIT!")   
        IBAN = "BG9812"
        for i in range(0, 10):
            IBAN += str(randint(0, 9))    

        account = package.Account(currency, acc_type, IBAN)
        return account   

    def user_exists_check(self, users, username):
        exists = False
        for x in users:
            if username == x.name:
                exists = True
        return exists

    def money_action(self, users, money, username, acc_type, acc_curr, operation):    
        if any(num.isalpha() for num in money):
            raise errors.InvalidDataFormat("Invalid data format!")  

        acc_exists = False
        if self.user_exists_check(users, username):
            for x in users:
                if username == x.name:
                    for a in x.accounts:
                        if a.acc_type == acc_type and a.currency == acc_curr:
                            acc_exists = True
                            if operation == "deposit":
                                 a.balance += float(money)
                            else:
                                if a.balance < money:
                                    raise errors.NotEnoughMoney("You don't have enough money!")
                                else:
                                    a.balance -= float(money) 
                                                          
        if not acc_exists:
            raise errors.AccountNotFound("Account doesn't exist!")

    def run(self):
        
        users = []
        bank = package.Bank(users)
        
        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":

                    username = input("Enter your name: ")
                    egn = input("Enter your EGN: ")
                    accounts = []
                    bank.add_user(self.create_user_command(username, egn, accounts))    

                elif choice == "2":
                    username = input("Enter your username: ")

                    if self.user_exists_check(bank.users, username):                   
                        currency = input("Enter currency: ")
                        acc_type = input("Enter account type: ") 
                        iban = ""
                        for x in bank.users:
                            if username == x.name:
                                 x.accounts.append(self.create_account_command(currency, acc_type, iban))    
                    else:
                        raise errors.UserNotFound("User not found!")    

                elif choice == "3":
                    for x in bank.users:
                        print(x.print_user())

                elif choice == "4":
                    username = input("Enter your username: ")
                    if self.user_exists_check(bank.users, username):
                        for x in bank.users:
                            if username == x.name:
                                for a in x.accounts:
                                    print(a.print_account())
                    else:
                        raise errors.UserNotFound("User not found!")

                elif choice == "5":
                    operation = "deposit"
                    username = input("Enter your username: ")
                    money = input("Enter ammount to deposit: ")
                    acc_type = input("Enter the account's type you want to deposit the money to: ")
                    acc_curr = input("Enter the account's currency you want to deposit the money to: ")

                    self.money_action(bank.users, money, username, acc_type, acc_curr, operation)

                elif choice == "6":
                    operation = "withdraw"
                    username = input("Enter your username: ")
                    money = input("Enter ammount to withdraw: ")
                    acc_type = input("Enter the account's type you want to withdraw the money from: ")
                    acc_curr = input("Enter the account's currency you want to withdraw the money from: ")

                    self.money_action(bank.users, money, username, acc_type, acc_curr, operation)

                elif choice == "7":
                    break
                else:
                    raise errors.InvalidCommand("Invalid input, please try again")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()
    

if __name__ == '__main__':
    menu = Menu()
    menu.run()




