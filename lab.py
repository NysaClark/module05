"""
    Nysa Clark
    Module 05 Lab Assignment

    This program ...
"""

class Item:
    def __init__(self, name, quantity, price):
        self.__name__ = name
        self.__quantity__ = quantity
        self.__price__ = price

    def get_name(self):
        return self.__name__
    
    def get_quantity(self):
        return self.__quantity__
    
    def get_price(self):
        return self.__price__
    
    def set_price(self, new_price):
        if new_price >= 0.01:
            price_difference = new_price - self.__price__
            percent_change = (price_difference / self.__price__ ) * 100

            if percent_change <= 50 and percent_change >= -50:
                self.__price__ = new_price
            else:
                print("Prices can not be changed by more than 50%.")
        else:
            print("Prices must be 1 cent or more.")
            
    def adding_stock(self, amount):
        self.__quantity__ += amount

    def removing_stock(self, amount):
        if self.__quantity__ - amount >= 0:
            self.__quantity__ -= amount
        else:
            print("The quantity can not be decreased below 0.")

    def clearance(self, reduction_amount):
        if self.__price__ - reduction_amount >= 0.01:
            self.__price__ -= reduction_amount
        else:
            print("Prices must be 1 cent or more.") 


item1 = Item("notebook", 25, 16.00)

print(f"Item Name: {item1.get_name()}")
print(f"Item Quantity: {item1.get_quantity()}")
print(f"Item Price: ${item1.get_price():.2f}")

item1.set_price(12.00)
print(f"Item Price: ${item1.get_price():.2f}")

item1.removing_stock(4)
print(f"Item Quantity: {item1.get_quantity()}")

item1.adding_stock(8)
print(f"Item Quantity: {item1.get_quantity()}")

item1.clearance(2.00)
print(f"Item Price: ${item1.get_price():.2f}")

print("-" * 20)


class Perishable(Item):
    def __init__(self, name, quantity, price, refrigerated, expiration_date):
        super().__init__(name, quantity, price)
        self.__refrigerated__ = refrigerated
        self.__expiration_date__ = expiration_date

    def get_refrigerated(self):
        return self.__refrigerated__
    
    def set_refrigerated(self, new_value):
        self.__refrigerated__ = new_value
    
    def get_expiration_date(self):
        return self.__expiration_date__
    
    def set_expiration_date(self, new_date):
        self.__expiration_date__ = new_date

    def clearance(self):
        self.__price__ -= self.__price__ * .9


item2 = Perishable("milk", 9, 5.00, False, "2/29/2024")

print(f"Item Name: {item2.get_name()}")
print(f"Item Quantity: {item2.get_quantity()}")
print(f"Item Price: ${item2.get_price():.2f}")
print(f"Item needs to be refrigerated? {item2.get_refrigerated()}")
print(f"Item Expiration Date: {item2.get_expiration_date()}")

item2.set_refrigerated(True)
print(f"Item needs to be refrigerated? {item2.get_refrigerated()}")

item2.set_expiration_date("2/22/2024")
print(f"Item Expiration Date: {item2.get_expiration_date()}")

item2.clearance()
print(f"Item Price: ${item2.get_price():.2f}")

print("-" * 20)


class Electronic(Item):
    def __init__(self, name, quantity, price, warrenty_period, return_period, serial_number):
        super().__init__(name, quantity, price)
        self.__warrenty_period__ = warrenty_period
        self.__return_period__ = return_period
        self.__serial_number__ = serial_number

    def get_warrenty_period(self):
        return self.__warrenty_period__
    
    def get_return_period(self):
        return self.__return_period__
    
    def set_return_period(self, new_return_period):
        self.__return_period__ = new_return_period

    def get_serial_number(self):
        return self.__serial_number__
    
    def extend_warrenty(self):
        self.__warrenty_period__ += 180


item3 = Electronic("iPad", 6, 650.00, 90, 30, 1234567)

print(f"Item Name: {item3.get_name()}")
print(f"Item Quantity: {item3.get_quantity()}")
print(f"Item Price: ${item3.get_price():.2f}")
print(f"Item Warrenty Period: {item3.get_warrenty_period()} days")
print(f"Item Return Period: {item3.get_return_period()} days")
print(f"Item Serial Number: {item3.get_serial_number()}")

item3.set_return_period(15)
print(f"Item Return Period: {item3.get_return_period()} days")

item3.extend_warrenty()
print(f"Item Warrenty Period: {item3.get_warrenty_period()} days")