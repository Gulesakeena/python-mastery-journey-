class Customer:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(f"Customer Name : {self.name}")
        print(f"Email         : {self.email}")


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.name} - ${self.price}")


class Order:

    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer          # Aggregation
        self.products = []                # List of Product objects

    def add_product(self, product):
        self.products.append(product)

    def total_amount(self):
        total = 0

        for product in self.products:
            total += product.price

        return total

    def display_order(self):
        print("=" * 40)
        print(f"Order ID : {self.order_id}")
        print()

        self.customer.display()

        print("\nProducts")
        print("-" * 40)

        for product in self.products:
            product.display()

        print("-" * 40)
        print(f"Total Amount : ${self.total_amount()}")
        print("=" * 40)


# -------------------------
# Create Customer
# -------------------------

customer1 = Customer("Gul", "gul@gmail.com")

# -------------------------
# Create Products
# -------------------------

product1 = Product("Laptop", 900)
product2 = Product("Mouse", 30)
product3 = Product("Keyboard", 70)

# -------------------------
# Create Order
# -------------------------

order1 = Order(101, customer1)

order1.add_product(product1)
order1.add_product(product2)
order1.add_product(product3)

# -------------------------
# Display Order
# -------------------------

order1.display_order()

# -------------------------
# Delete Order
# -------------------------

del order1

print("\nOrder Deleted Successfully!\n")

# -------------------------
# Customer and Products Still Exist
# -------------------------

print("Customer Still Exists")
customer1.display()

print("\nProducts Still Exist")
product1.display()
product2.display()
product3.display()