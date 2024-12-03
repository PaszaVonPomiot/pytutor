import string
import random


class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, catalogue_price, electric) -> None:
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Tax: {self.compute_tax()}")


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, info) -> None:
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"Id: {self.id}")
        print(f"License: {self.license_plate}")
        self.info.print()


class VehicleRegistry:

    vehicle_info = {}

    def add_vehicle_info(self, brand, catalogue_price, electric):
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electric)

    def __init__(self) -> None:
        self.add_vehicle_info("fiat", 1000, False)
        self.add_vehicle_info("tesla", 2300, True)

    def generate_vehicle_id(self, length):
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:
    def register_vehicle(self, brand: string):
        registry = VehicleRegistry()
        return registry.create_vehicle(brand)


app = Application()
vehicle = app.register_vehicle("tesla")
vehicle.print()
