"""
    Nysa Clark
    Module 05 Programming Project
    Part A

    This program ...
"""

class Customer:
    def __init__(self, name, birthday):
        self.__name__ = name
        self.__birthday__ = birthday
        self.__num_visits__ = 0
        self.__total_spent__ = 0.00

    def get_name(self):
        return self.__name__
    
    def set_name(self, new_name):
        self.__name__ = new_name
    
    def get_birthday(self):
        return self.__birthday__
    
    def get_num_visits(self):
        return self.__num_visits__
    
    def get_total_spent(self):
        return self.__total_spent__
    
    def visit(self, amount_spent):
        print("Visiting...")
        print(f"Spent ${amount_spent:.2f}")
        self.__num_visits__ += 1
        self.__total_spent__ += amount_spent


customer1 = Customer("John Doe", "01-01-1989")

print(f"Name: {customer1.get_name()}")
print(f"Birthday: {customer1.get_birthday()}")
print(f"# of Visits: {customer1.get_num_visits()}")
print(f"Total Amount Spent: {customer1.get_total_spent()}")

customer1.visit(90.99)

print(f"# of Visits: {customer1.get_num_visits()}")
print(f"Total Amount Spent: {customer1.get_total_spent()}")

print("-" * 20)


class PreferredCustomer(Customer):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)
        self.__discount__ = 10

    def get_discount(self):
        return self.__discount__

    def visit(self, amount_spent):
        Customer.visit(self, amount_spent)
        if self.__num_visits__ >= 20 or self.__total_spent__ >= 500:
            self.__discount__ = 15


customer2 = PreferredCustomer("Jane Doe", "02-02-1995")

print(f"Name: {customer2.get_name()}")
print(f"Birthday: {customer2.get_birthday()}")
print(f"# of Visits: {customer2.get_num_visits()}")
print(f"Total Spent: ${customer2.get_total_spent():.2f}")
print(f"Discount: {customer2.get_discount()}%")

customer2.visit(150.00)

print(f"# of Visits: {customer2.get_num_visits()}")
print(f"Total Spent: ${customer2.get_total_spent():.2f}")
print(f"Discount: {customer2.get_discount()}%")

customer2.visit(350.00)

print(f"# of Visits: {customer2.get_num_visits()}")
print(f"Total Spent: ${customer2.get_total_spent():.2f}")
print(f"Discount: {customer2.get_discount()}%")

print("-" * 20)


class FamilyFriendCustomer(PreferredCustomer):
    def __init__(self, name, birthday):
        super().__init__(name, birthday)

    def visit(self, amount_spent):
        Customer.visit(self, amount_spent)
        if self.__num_visits__ >= 15 or self.__total_spent__ >= 350:
            self.__discount__ = 15


customer3 = FamilyFriendCustomer("Nysa Clark", "05-15-2004")

print(f"Name: {customer3.get_name()}")
print(f"Birthday: {customer3.get_birthday()}")
print(f"# of Visits: {customer3.get_num_visits()}")
print(f"Total Spent: ${customer3.get_total_spent():.2f}")
print(f"Discount: {customer3.get_discount()}%")

customer3.visit(180.00)

print(f"# of Visits: {customer3.get_num_visits()}")
print(f"Total Spent: ${customer3.get_total_spent():.2f}")

customer3.visit(200.00)

print(f"# of Visits: {customer3.get_num_visits()}")
print(f"Total Spent: ${customer3.get_total_spent():.2f}")
print(f"Discount: {customer3.get_discount()}%")