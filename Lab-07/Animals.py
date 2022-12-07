class InvalidParameterError:
    pass

class InvalidAgeError(InvalidParameterError):
    pass

class InvalidSoundError(InvalidParameterError):
    pass

class JungleAnimal:
    
    def __init__(self, name, age, sound):
        try: 
            self.name = name
            self.age = age
            self.sound = sound

            if type(name) != str:
                raise InvalidParameterError
        
            if type(age) != int:
                raise InvalidAgeError
            if type(sound) != str:
                raise InvalidSoundError

        except InvalidParameterError():
            print("Name")
        except InvalidAgeError():
            print("Age")
        except InvalidSoundError():
            print("Sound")    

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

    def print(self):   
        pass

    def daily_task(self):
        pass     

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        try:
            if age > 15:
                raise InvalidAgeError
            if sound.count("r") != 2:
                raise  InvalidSoundError

        except InvalidAgeError():
            print("Age")      
        except InvalidSoundError():
            print("Sound")      

        print(f"Jaguar {self.name}, {self.age}, {self.sound}")   

    def daily_task(self):
        return  

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        try:
            if age > 10:
                raise InvalidAgeError
            if sound.count("e") != 1:
                raise  InvalidSoundError

        except InvalidAgeError():
            print("Age")      
        except InvalidSoundError():
            print("Sound")      

        print(f"Lemur {self.name}, {self.age}, {self.sound}")

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        try:
            if age > 10:
                raise InvalidAgeError
            if sound.count("e") != 1:
                raise  InvalidSoundError

        except InvalidAgeError():
            print("Age")      
        except InvalidSoundError():
            print("Sound")      

        print(f"Human {self.name}, {self.age}, {self.sound}")

class Buildings:
    def __str__(self, type):
        self.type = type

        
fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

