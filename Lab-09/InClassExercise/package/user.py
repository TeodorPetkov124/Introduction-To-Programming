class User:
    def __init__(self, name, EGN, accounts = None):
        self.name = name
        self.EGN = EGN
        self.accounts = accounts

    def account_list_print(self):
        result = ""
        for x in self.accounts:
            result += f"{x.print_account()}"
        return result

    def print_user(self):
        return f"User: ({self.name}, {self.EGN}, {self.account_list_print()})"

        