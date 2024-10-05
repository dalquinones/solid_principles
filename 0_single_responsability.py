class Report:
    def generate_report(self):
        return "Generando reporte..."

    def print_report(self):
        print(self.generate_report())
        
    def save_report(self, file_name):
        with open(file_name, 'w') as file:
            file.write(self.generate_report())

report = Report()
report.print_report()
report.save_report("reporte.txt")

'''
PROBLEMA:
La clase Report tiene múltiples responsabilidades: 
generar, imprimir y guardar el reporte, lo que hace que sea difícil de mantener y probar.
'''