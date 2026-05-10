"""
Single Responsibility Principle

- the SRP is about limiting the impact of change
- gather together the things that change for the same reasons (to prevent class atomization), separate those things that change for different reasons (to prevent coupling)
- a class should have one, and only one, reason to change


The Single Responsibility Principle requires that module, class or function should have only one responsibility (reason to change).
So if a class has more than one responsibility, it becomes coupled. A change to one responsibility results to modification of the other responsibility.

The single responsibility principle states that every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility.

Eg. class to manage address book - add, remove, change, lookup entries but not save to file or database.
"""

# Violated SRP
class AnimalWithPersistence:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def save(self):
        print(f"Saving {self.name} to DB")

srp_violation_horse = AnimalWithPersistence()
srp_violation_horse.set_name('konik')
srp_violation_horse.save()

# No Violation
# Separated conerns of manipulating Animal properties and storing Animal properties
# Further fragmenting Animal class WILL NOT reduce impact of changes
class Animal:
    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

class AnimalDB:
    def save(self, animal: Animal):
        print(f"Saving {animal.name} to DB")

srp_compliant_horse = Animal()
srp_compliant_horse.set_name('konik')

db = AnimalDB()
db.save(srp_compliant_horse)
