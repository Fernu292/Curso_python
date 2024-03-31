class Sujeto:
    def __init__(self):
        self.observers = []
    def attach(self, observer):
        # Adjuntamos un observador a la lista de 
        # observadores
        if observer not in self.observers:
            self.observers.append(observer)
    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
        
# Definimos la clase Observer (Observador)
class Observer:
    def update(self, message):
        pass

# Implementamos una clase concreta de observador

class EmailSubscriber(Observer):
    def update(self, message):
        print("Email recibido: ", message)

class SMSSubscriber(Observer):
    def update(self, message):
        print("SMS recibido: ", message)

def main():
    notificador = Sujeto()

    email_observer = EmailSubscriber()
    sms_observer = SMSSubscriber()

    # Adjuntamos a los observadores al sujeto

    notificador.attach(email_observer)
    notificador.attach(sms_observer)

    notificador.notify("Nuevo mensaje: Reunion mañana a las 10 AM")
    notificador.detach(email_observer)

    notificador.notify("Segundo mensaje: Cambio de lugar")

if __name__=='__main__':
    main()