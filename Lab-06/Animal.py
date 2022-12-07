<<<<<<< HEAD
import random

class Animal():
    def __init__(self, name,year, food):
        self.years = year
        self.food = food
        self.name = name

    def make_sound(self):
        pass
    def eat_food(self,quantity):
        pass

class Cat(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("Meow")

    def eat_food(self,quantity):
        foodNeeded = 10

        if quantity == 0:
            self.make_sound()
            self.make_sound()
            self.make_sound()
            self.make_sound()
            return 0
        elif foodNeeded <= quantity:
            return quantity - foodNeeded
        elif foodNeeded > quantity:
            self.make_sound()
            self.make_sound()
            return 0

class Dog(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("Bark")

    def eat_food(self,quantity, eat_quantity = 5):
        if quantity - eat_quantity < 0:
            return 0
        return quantity - eat_quantity

class Duck(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("quack")

    def eat_food(self,quantity):
        self.make_sound()
        eat_quantity = random.randint(0,9)
        if quantity - eat_quantity < 0:
            return 0
        return quantity - eat_quantity

class Horse(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("horse sound")

    def eat_food(self,quantity):
        eat_quantity = 15
        if quantity < 8:
            return 0, quantity
        if quantity - eat_quantity < 15:
            eat_quantity = 8
            return quantity - eat_quantity, eat_quantity
        else:
            return quantity - eat_quantity, eat_quantity

cat = Cat("ivan", 3, "chicken")
cat1 = Cat("petar", 5, "beef")
dog = Dog("pesho", 6, "pork")
dog1 = Dog("mariqn", 4, "beef")
dog2 = Dog("spas", 7, "chicken")
duck = Duck("gosho", 4, "chicken")
horse = Horse("boiko", 6, "pork")
horse1 = Horse("denis", 5, "grass")
duck1 = Duck("ivailo", 7, "grass")
duck2 = Duck("krasi", 8, "grass")

animals = [cat,cat1,dog,dog1,dog2,duck,horse,horse1,duck1,duck2]
food = {"fish": 9, "dogFoot":10, "duckFood":15, "grass":30}

for i in animals:
    if type(i) == Cat:
        foodQuantity = food["fish"]
        if(foodQuantity < 10):
            print(f"{i.name} the Cat jsut ate {foodQuantity} {list(food.keys())[0]}, there's {i.eat_food(foodQuantity)} left.")
        else:
            print(f"{i.name} the Cat jsut ate 10 {list(food.keys())[0]}, there's {i.eat_food(foodQuantity)} left.")
    elif type(i) == Dog:
        foodQuantity = food["dogFoot"]
        if(foodQuantity < 5):
            print(f"{i.name} the Dog jsut ate {foodQuantity} {list(food.keys())[1]}, there's {i.eat_food(foodQuantity)} left.")
        else:
            print(f"{i.name} the Dog jsut ate 5 {list(food.keys())[1]}, there's {i.eat_food(foodQuantity)} left.")
    elif type(i) == Duck:
        foodQuantity = food["duckFood"]
        print(f"{i.name} the Duck jsut ate 10 {list(food.keys())[2]}, there's {i.eat_food(foodQuantity)} left.")
    elif type(i) == Horse:
        foodQuantity = food["grass"]
        print(f"{i.name} the Horse jsut ate {i.eat_food(foodQuantity)[1]} {list(food.keys())[3]}, there's {i.eat_food(foodQuantity)[0]} left.")               
=======
import random

class Animal():
    def __init__(self, name,year, food):
        self.years = year
        self.food = food
        self.name = name

    def make_sound(self):
        pass
    def eat_food(self,quantity):
        pass

class Cat(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("Meow")

    def eat_food(self,quantity):
        foodNeeded = 10

        if quantity == 0:
            self.make_sound()
            self.make_sound()
            self.make_sound()
            self.make_sound()
            return 0
        elif foodNeeded <= quantity:
            return quantity - foodNeeded
        elif foodNeeded > quantity:
            self.make_sound()
            self.make_sound()
            return 0

class Dog(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("Bark")

    def eat_food(self,quantity, eat_quantity = 5):
        if quantity - eat_quantity < 0:
            return 0
        return quantity - eat_quantity

class Duck(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("quack")

    def eat_food(self,quantity):
        self.make_sound()
        eat_quantity = random.randint(0,9)
        if quantity - eat_quantity < 0:
            return 0
        return quantity - eat_quantity

class Horse(Animal):
    def __init__(self, name, year, food):
        super().__init__(name, year, food)

    def make_sound(self):
        print("horse sound")

    def eat_food(self,quantity):
        eat_quantity = 15
        if quantity < 8:
            return 0, quantity
        if quantity - eat_quantity < 15:
            eat_quantity = 8
            return quantity - eat_quantity, eat_quantity
        else:
            return quantity - eat_quantity, eat_quantity

cat = Cat("ivan", 3, "chicken")
cat1 = Cat("petar", 5, "beef")
dog = Dog("pesho", 6, "pork")
dog1 = Dog("mariqn", 4, "beef")
dog2 = Dog("spas", 7, "chicken")
duck = Duck("gosho", 4, "chicken")
horse = Horse("boiko", 6, "pork")
horse1 = Horse("denis", 5, "grass")
duck1 = Duck("ivailo", 7, "grass")
duck2 = Duck("krasi", 8, "grass")

animals = [cat,cat1,dog,dog1,dog2,duck,horse,horse1,duck1,duck2]
food = {"fish": 9, "dogFoot":10, "duckFood":15, "grass":30}

for i in animals:
    if type(i) == Cat:
        foodQuantity = food["fish"]
        if(foodQuantity < 10):
            print(f"{i.name} the Cat jsut ate {foodQuantity} {list(food.keys())[0]}, there's {i.eat_food(foodQuantity)} left.")
        else:
            print(f"{i.name} the Cat jsut ate 10 {list(food.keys())[0]}, there's {i.eat_food(foodQuantity)} left.")
    elif type(i) == Dog:
        foodQuantity = food["dogFoot"]
        if(foodQuantity < 5):
            print(f"{i.name} the Dog jsut ate {foodQuantity} {list(food.keys())[1]}, there's {i.eat_food(foodQuantity)} left.")
        else:
            print(f"{i.name} the Dog jsut ate 5 {list(food.keys())[1]}, there's {i.eat_food(foodQuantity)} left.")
    elif type(i) == Duck:
        foodQuantity = food["duckFood"]
        print(f"{i.name} the Duck jsut ate 10 {list(food.keys())[2]}, there's {i.eat_food(foodQuantity)} left.")
    elif type(i) == Horse:
        foodQuantity = food["grass"]
        print(f"{i.name} the Horse jsut ate {i.eat_food(foodQuantity)[1]} {list(food.keys())[3]}, there's {i.eat_food(foodQuantity)[0]} left.")               
>>>>>>> a44b987b961262e3601eff34d1462cf05495ee02
