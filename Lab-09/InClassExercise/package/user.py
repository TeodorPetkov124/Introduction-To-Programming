class User:
    def __init__(self, account, name, EGN):
        self.account = account
        self.name = name
        self.EGN = EGN

    def print_user(self):
        return print(f"User: {self.account} {self.name} {self.EGN}")
        