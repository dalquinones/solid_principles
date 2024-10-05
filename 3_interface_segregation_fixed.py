class Printer:
    def print(self, document):
        pass

class Scanner:
    def scan(self):
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print(self, document):
        print(f"Imprimiendo: {document}")
    
    def scan(self):
        print("Escaneando...")

mfd = MultiFunctionDevice()
mfd.print("Documento")
mfd.scan()

'''
SOLUCION:
Printer y Scanner son interfaces separadas, lo que permite que 
las clases que implementan estas interfaces sean específicas a sus responsabilidades.
'''