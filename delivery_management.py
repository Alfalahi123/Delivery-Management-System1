from enum import Enum

# Enum for Order Status
class OrderStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    DELIVERED = "Delivered"

class Customer:
    def __init__(self, customer_id, name, contact, address):
        self.__customer_id = customer_id
        self.__name = name
        self.__contact = contact
        self.__address = address

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def display(self):
        print(f"Customer: {self.__name}, Contact: {self.__contact}, Address: {self.__address}")

class Item:
    def __init__(self, code, description, quantity, price):
        self.__code = code
        self.__description = description
        self.__quantity = quantity
        self.__price = price

    def total_price(self):
        return self.__quantity * self.__price

    def display(self):
        print(f"{self.__description} (x{self.__quantity}) - {self.total_price()} AED")

class Order:
    def __init__(self, order_id, customer, delivery_address, status, delivery_date):
        self.__order_id = order_id
        self.__customer = customer
        self.__delivery_address = delivery_address
        self.__status = OrderStatus(status)
        self.__delivery_date = delivery_date
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def total_amt(self):
        return sum(item.total_price() for item in self.__items)

    def display(self):
        print(f"Order ID: {self.__order_id}, Status: {self.__status.value}, Total: {self.total_amt()} AED")
        print("Items:")
        for item in self.__items:
            item.display()

class DeliveryNote:
    def __init__(self, order):
        self.__order = order
        self.__customer = order._Order__customer
        self.__items = order._Order__items
        self.__total_charges = order.total_amt() + 13.50

    def generate(self):
        print("Delivery Note")
        print("----------------------")
        self.__customer.display()
        print(f"Order ID: {self.__order._Order__order_id}, Address: {self.__order._Order__delivery_address}")
        print("Items:")
        for item in self.__items:
            item.display()
        print(f"Total: {self.__total_charges} AED")

class DeliverySystem:
    def __init__(self):
        self.__orders = []

    def add_order(self, order):
        self.__orders.append(order)

    def display_orders(self):
        for order in self.__orders:
            order.display()

# Example Usage
customer1 = Customer(1, "Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Ave, Dubai, UAE")
customer2 = Customer(2, "John Doe", "john.doe@example.com", "23 Market Street, Dubai, UAE")

order1 = Order(123456789, customer1, "45 Knowledge Ave, Dubai, UAE", "Confirmed", "2025-01-25")
order2 = Order(987654321, customer2, "23 Market Street, Dubai, UAE", "Pending", "2025-02-01")

order1.add_item(Item("ITM001", "Wireless Keyboard", 1, 100.00))
order1.add_item(Item("ITM002", "Wireless Mouse & Pad Set", 1, 75.00))
order2.add_item(Item("ITM003", "Laptop Cooling Pad", 1, 120.00))
order2.add_item(Item("ITM004", "Camera Lock", 3, 15.00))

delivery_system = DeliverySystem()
delivery_system.add_order(order1)
delivery_system.add_order(order2)

delivery_note1 = DeliveryNote(order1)
delivery_note2 = DeliveryNote(order2)

delivery_note1.generate()
delivery_note2.generate()

delivery_system.display_orders()

pass  # Placeholder to ensure script runs without error
