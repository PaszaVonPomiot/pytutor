"""
Open/Closed Principle
Software entities(Classes, modules, functions) should be open for extension, not modification.

Example 1 - using just class inheritance
"""

# New discounts will require changes to Discount class - bad
class ConditionalDiscount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4

# New discounts will require new class that inherits Discount and sets new discount - good

class BaseDiscount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
    def get_discount(self):
        return self.price * 0.2 # 20%

class VIPDiscount(BaseDiscount):
    def get_discount(self):
        return super().get_discount() * 2 # 40%

class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 1.5 # 60%

# Example 2 - using abstract class and method
#
# New payment methods will require extending a class

class MultiMethodPaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

# Using abstract class (ABC) and abstract method (abstractmethod) create separate class for new payment methods
#
# Abstract class cannot be instantiated directly, only via subclass. 
# Abstract class can be blueprint for other classes.
#
# Abstract method is declared but has no implementation. Must be implemented by subclass. Subclass without implemented abstractmethod from parent class cannot be instantiated.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

# Example 3 - base class via subclassing with `raise NotImplementedError`
#
# Subclass can be instantiated but cannot use the method unless it's implemented.

class Animal:
    def feed(self):
        raise NotImplementedError("Method not implemented")

class Cat(Animal):
    def feed(self):
        do_something()

# Use abc.ABC and abc.abstractmethod to ENFORCE implementation of abstract methods on ALL subclasses.
# Use inheritance with NotImplementedError to NOT ENFORCE implementation of abstract methods.
#
# Always name abstract classes by convention BaseSomething.
#
# Example 4 - base class can have both abstract and concrete methods

class R(ABC):
    def rk(self):
        print("Abstract Base Class")

class K(R):
    def rk(self):
        super().rk()
        print("subclass ")
