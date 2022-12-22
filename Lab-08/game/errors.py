class InvalidDataFormat(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()

    def __str__(self) -> str:
        return self.message


class InvalidCommand(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()

    def __str__(self) -> str:
        return self.message

        
class CharacterExists(Exception):
    def __init__(self, characterName):
        self.message = f"Character with name {characterName} already exists!"
        super().__init__()

    def __str__(self) -> str:
        return self.message


class CharacterNotFound(Exception):
    def __init__(self, characterName):
        self.message = f"Character with name {characterName} not found!"
        super().__init__()

    def __str__(self) -> str:
        return self.message


class InvalidCharacterClass(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()

    def __str__(self) -> str:
        return self.message