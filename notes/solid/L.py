"""
Liskov Substitution Principle
Child class (derived class, subclass) objects should be able to replace parent class objects without breaking the integrity of the application.

Any code calling methods on objects of a specific type should continue to work when those objects get replaced with instances of a subtype.  A subtype is either a class extending another class or a class implementing an interface.

LSP Smells
- when subclass does not have some methods implemented from base class
- when subclass implementation of a method raises exception
- unexpected behaviour...

LSP not violated ??????????????????
"""

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class Email(Notification):
    def __init__(self, email):
        self.email = email

    def notify(self, message):
        print(f'Send "{message}" to {self.email}')

class SMS(Notification):
    def __init__(self, phone):
        self.phone = phone

    def notify(self, message):
        print(f'Send "{message}" to {self.phone}')

class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class NotificationManager:
    def __init__(self, notification):
        self.notification = notification

    def send(self, message):
        self.notification.notify(message)

if __name__ == '__main__':
    contact = Contact('John Doe', 'john@test.com', '(408)-888-9999')

    sms_notification = SMS(contact.phone)
    email_notification = Email(contact.email)

    notification_manager = NotificationManager(sms_notification)
    notification_manager.send('Hello John')

    notification_manager.notification = email_notification
    notification_manager.send('Hi John')
