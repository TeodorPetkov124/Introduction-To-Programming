class InvalidParameterError(Exception):
    pass

class NutrientError(Exception):
    pass

class InvalidFoodError(Exception):
    pass

class Food:
    def __init__(self, carbs, protein, fats, salt):
        try: 
            self.carbs = carbs
            self.protein = protein
            self.fats = fats
            self.salt = salt
            self.name = __class__.__name__

            if type(carbs) != float:
                raise InvalidParameterError
            elif type(protein) != float:
                raise InvalidParameterError
            elif type(fats) != float:
                raise InvalidParameterError
            elif type(salt) != float:
                raise InvalidParameterError   

            if  sum([carbs, protein, fats, salt]) > 100:
                raise NutrientError 

            if sum([carbs, protein, fats, salt]) == 0:
                raise InvalidFoodError

        except InvalidParameterError:
            print("Numbers should be float")
        except NutrientError:
            print("NutrientError")
        except InvalidFoodError:
            print("Nutrients can't be zero")    


    def print_label(self):
        print(f"{self.name}, ({self.carbs}), ({self.protein}), ({self.fats}), ({self.salt})")



for i in range(0, 120, 10):
      food = Food(i+0.1, i+0.1, i+0.1, i+0.2)  
      food.print_label()
      
    
             

    


        