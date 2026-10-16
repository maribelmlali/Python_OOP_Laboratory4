from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print("Sending Email:", message)

class SMSNotification(Notification):
    def send(self, message):
        print("Sending SMS:", message)

class AppNotification(Notification):
    def send(self, message):
        print("Sending App Notification:", message)

methods = [EmailNotification(), SMSNotification(), AppNotification()]
for m in methods:
    m.send("Enrollment is now open!")