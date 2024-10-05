class EmailService:
    def send_email(self, message):
        print(f"Enviando email: {message}")

class Notification:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service

    def notify(self, message):
        self.email_service.send_email(message)

email_service = EmailService()
notification = Notification(email_service)
notification.notify("Hola, esto es una notificación.")

'''
SOLUCION:
Notification depende de la abstracción EmailService, no de una implementación concreta.
Esto permite cambiar la forma de notificación sin modificar la clase Notification.
'''