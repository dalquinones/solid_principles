class EmailService:
    def send_email(self, message):
        print(f"Enviando email: {message}")

class Notification:
    def __init__(self):
        self.email_service = EmailService()  # Dependencia directa

    def notify(self, message):
        self.email_service.send_email(message)

notification = Notification()
notification.notify("Hola, esto es una notificación.")

'''
PROBLEMA:
Notification depende directamente de EmailService, 
lo que hace que sea difícil cambiar la forma de notificación sin modificar el código de la clase Notification.
'''