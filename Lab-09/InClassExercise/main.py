import package
import errors 
import random

class Menu:


    def print_menu(self):
        print("1. Create new user")
        print("2. Create account for user")
        print("3. List users")
        print("4. List account for user")
        print("5. Deposit for user account")
        print("6. Withdrawal for user account")
        print("7. Exit")
    
    def create_user_command(self, name, EGN):
        return package.User(name, EGN)

    def create_account_command(self, balance, currency, acc_type, IBAN):
        return package.Account(balance, currency, acc_type, IBAN)    
                     
    def run(self):

        users = []

        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":
                    name = input("Input new name.")
                    if len(name) < 4:
                        raise errors.InvalidDataFormat("The name must be at least 4 letters.")
                    EGN = int(input("Input new EGN"))
                    if EGN != int or len(EGN) < 10:
                        raise errors.InvalidDataFormat("EGN must be 10 numbers long")

                    accounts = []
                    user = self.create_user_command(name, EGN)
                    users.append(user)
                                               
                elif choice == "2":
                    currency = str(input("Input type of currency"))
                    acc_type = str(input("Input account type (CURRENT/SAVINGS/CREDIT)"))

                    if currency != str:
                        raise errors.InvalidDataFormat("Type of currency contains only letters")
                    if acc_type != str or acc_type != "CURRENT" or acc_type != "SAVINGS" or acc_type != "CREDIT":
                        raise errors.InvalidAccountType("Type of the account must be (CURRENT/SAVINGS/CREDIT)")

                    ibanrnd = random.randint(1111111111, 9999999999)
                    iban = "BG9812" + str(ibanrnd)

                    account = self.create_account_command(currency, acc_type, iban)
                    username = input("Enter the username you want to add this account to: ")

                    exists = False
                    for us in users:
                        if username == us.name:
                            exists = True
                            us.account.append(account)

                    if not exists:
                        raise errors.UserNotFound("User does not exist!")

                elif choice == "3":
                    pass
                elif choice == "4":
                    pass
                elif choice == "5":
                    pass
                elif choice == "6":
                    pass
                elif choice =="7":
                    break
                else:
                    raise errors.InvalidCommand("Invalid input, please try again")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()
    

if __name__ == '__main__':
    menu = Menu()
    menu.run()