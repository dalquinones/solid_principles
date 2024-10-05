class Bird:
    def fly(self):
        return "Volando..."

class Sparrow(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        raise Exception("Los pingüinos no pueden volar")

def let_bird_fly(bird: Bird):
    return bird.fly()

sparrow = Sparrow()
print(let_bird_fly(sparrow))  # Funciona

penguin = Penguin()
# let_bird_fly(penguin)  # Esto causaría una excepción

'''
PROBLEMA:
La clase Penguin no cumple con la expectativa de que todos los Birds pueden volar, 
lo que causa errores al intentar usar la función con un Penguin.
'''