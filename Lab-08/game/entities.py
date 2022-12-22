class Character:
    def __init__(self, name: str, gender: str, characterClass: str):
        self.name = name
        self.gender = gender
        self.characterClass = characterClass
        self.weapon = None
        self.item = None

    def command_print_character(self):
       return f"Character {self.name} is {self.gender} with character class {self.characterClass}, weapon {self.weapon} and item {self.item}"

class Item:
    def __init__(self,name):
        self.name = name
        self.durability = 100

    def __str__(self) -> str:
        return f"name: {self.name} - durability: {self.durability}"

class Weapon(Item):
    def __init__(self, name, attack):
        super().__init__(name)
        self.attack = attack

    def __str__(self) -> str:
        return f"name: {self.name} - durability: {self.durability} - attack: {self.attack}"