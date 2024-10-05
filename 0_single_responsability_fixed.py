class Report:
    def generate_report(self):
        return "Generando reporte..."

class ReportPrinter:
    def print_report(self, report):
        print(report.generate_report())

# Uso
report = Report()
printer = ReportPrinter()
printer.print_report(report)

'''
SOLUCION:
La clase Report tiene la única responsabilidad de generar un reporte, 
mientras que ReportPrinter se encarga de imprimirlo. 
Esto mantiene las responsabilidades separadas.
'''