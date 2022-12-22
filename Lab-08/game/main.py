from entities import Character, Weapon, Item
from errors import InvalidDataFormat, InvalidCommand, CharacterExists, CharacterNotFound, InvalidCharacterClass

class Menu:

    characters = {}

    def print_menu(self):
        print("1. Create new character")
        print("2. Add new weapon to existing character")
        print("3. Add new item to existing character")
        print("4. Print all characters")
        print("5. Delete character")
        print("6. Stop and exit the program")

    def command_create_character(self, name: str, gender: str, characterClassValue: str):
        if name in self.characters.keys():
            raise CharacterExists(name)

        if gender.isalpha() == False:
            raise InvalidDataFormat("Gender must contain alphabetic characters only!")
            
        if len(name) < 4:
            raise InvalidDataFormat("Character name must be at least 4 characters long!")

        if (characterClassValue in ["Warrior", "Mage", "Priest", "Rogue"]) == False:
            raise InvalidCharacterClass("The character class must be one of the followings: Priest, Warrior, Mage, Rogue")
 
        new_character = Character(name, gender, characterClassValue)
        self.characters[name] = new_character
        print(f"Character {name} has been created successfully!")

    def command_create_weapon(self, attack, characterName: str, weaponName: str):

        if (characterName in self.characters.keys()) == False:
            raise CharacterNotFound(characterName)

        if attack < 0:
            raise InvalidDataFormat("New weapon must have possitive attack!")    
        if weaponName.isalpha() == False:
            raise InvalidDataFormat("New weapon name must contain alphabetic characters only!")
        if len(weaponName) < 4:
            raise  InvalidDataFormat("New weapon name must be at least 4 letters long!")   
     
        self.characters[characterName].weapon = Weapon(weaponName, attack)
        print(f"Weapon {weaponName} has been created successfully and added to character {characterName}!")

    def command_create_item(self, characterName, itemName):
        
        if (characterName in self.characters.keys()) == False:
            raise CharacterNotFound(characterName)

        if itemName.isalpha() == False:
            raise InvalidDataFormat("New item name must contain alphabetic characters only!")
        if len(itemName) < 4:
            raise InvalidDataFormat("New item name must be at least 4 letters long!")       
        
        self.characters[characterName].item = Item(itemName)
        print(f"Item {itemName} has been created successfully and added to character {characterName}!")

    def command_print_all_characters(self):
        for c in self.characters.values():
            print(c.command_print_character())

    def command_delete_character(self, name):
        if (name in self.characters.keys()) == False:
            raise CharacterNotFound(name)
        
        del self.characters[name]
        print(f"Character {name} has been deleted successfully!")
                     
    def run(self):

        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":                    
                    name = input("Input new character name. The name must be at least 4 characters long: ")
                    gender = input("Input character gender. The gender must be at least 4 letters long: ")
                    characterClassValue = input("Input character class (Mage, Priest, Rogue, Warrior): ")

                    self.command_create_character(name, gender, characterClassValue)
                elif choice == "2":
                    characterName = input("Input new character name: ")
                    weaponName = input("Input new weapon name. The name must be at least 4 letters long: ")
                    attack = int(input("Input the attack for the new weapon. The attack must be a positive number: "))

                    self.command_create_weapon(attack,characterName, weaponName)
                elif choice == "3":
                    characterName = input("Input new character name: ")
                    itemName = input("Input new item name. The name must be at least 4 letters long: ")

                    self.command_create_item(characterName, itemName)
                elif choice == "4":
                    self.command_print_all_characters()
                elif choice == "5":
                    name = input("Input new character name: ")

                    self.command_delete_character(name)
                elif choice == "6":
                    break
                else:
                    raise InvalidCommand("Error: Invalid menu item selected!")
            except Exception as ex:
                print(f"Error: {str(ex)}")
            
            print()
    

if __name__ == '__main__':
    menu = Menu()
    menu.run()