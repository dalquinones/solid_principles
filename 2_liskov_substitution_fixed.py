class Bird:
    def fly(self):
        return "Volando..."

class Sparrow(Bird):
    def fly(self):
        return "El gorrión vuela alto."

class Duck(Bird):
    def fly(self):
        return "El pato también puede volar."

class Ostrich(Bird):
    def fly(self):
        return "Los avestruces no vuelan, pero corren rápido."

def let_bird_fly(bird: Bird):
    return bird.fly()

sparrow = Sparrow()
duck = Duck()
ostrich = Ostrich()

print(let_bird_fly(sparrow))  # "El gorrión vuela alto."
print(let_bird_fly(duck))     # "El pato también puede volar."
print(let_bird_fly(ostrich))  # "Los avestruces no vuelan, pero corren rápido."

'''
SOLUCION:
Todas las clases que heredan de Bird tienen su propia implementación del método fly. 
Esto permite que cada clase cumpla con su comportamiento esperado, 
asegurando que el código que utiliza el tipo base (Bird) funcione sin problemas.
'''