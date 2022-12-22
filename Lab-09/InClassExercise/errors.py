class AccountNotFound(Exception):
    def __init__(self, message):
        self.message = message

class UserNotFound(Exception):
    def __init__(self, message):
        self.message = message

class InvalidAccountType(Exception):
    def __init__(self, message):
        self.message = message

class InvalidAccountCurrency(Exception):
    def __init__(self, message):
        self.message = message

class InvalidDataFormat(Exception):
    def __init__(self, message):
        self.message = message

class InvalidCommand(Exception):
    def __init__(self, message):
        self.message = message