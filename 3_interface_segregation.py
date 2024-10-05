class MultiFunctionDevice:
    def print(self, document):
        print(f"Imprimiendo: {document}")

    def scan(self):
        print("Escaneando...")

    def fax(self):
        print("Enviando fax...")

mfd = MultiFunctionDevice()
mfd.print("Documento")
mfd.scan()
mfd.fax()

'''
PROBLEMA:
MultiFunctionDevice implementa múltiples funciones en una sola interfaz, 
forzando a los clientes a depender de métodos que no necesitan (por ejemplo, fax), 
lo que viola el principio ISP.
'''