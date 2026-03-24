class Coffee:
    def __init__(self, name, description, base_price):
        self.name = name
        self.description = description
        self.base_price = base_price

    def __str__(self):
        return f"{self.name} - {self.description} - ${self.base_price:.2f}"

class Order:
    def __init__(self, coffee, size, quantity=1):
        self.coffee = coffee
        self.size = size
        self.quantity = quantity

    def get_price(self):
        return self.calculate_price()

    def calculate_price(self):
        total_price = self.coffee.base_price
        if self.size == "Medium":
            total_price += 0.50
        elif self.size == "Large":
            total_price += 1.00
        return total_price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.size} {self.coffee.name} - ${self.calculate_price():.2f}"

class Cafe:
    def __init__(self, name, tax_rate=0.08, daily_special="House Blend"):
        self.name = name
        self.menu = []
        self.orders = []
        self.tax_rate = tax_rate
        self.daily_special = daily_special
        self.loyalty_unlocked = False

    def add_to_menu(self, coffee):
        self.menu.append(coffee)

    def display_menu(self):
        print( f'\n===== {self.name.upper()} MENU =====')
        print(f"🌟 Daily Special: {self.daily_special}\n")
        for i, item in enumerate(self.menu, 1):
            print(f"{i}. {item.name} - {item.description}\t${item.base_price:.2f}")

    def display_sizes(self):
        """Print the available sizes."""
        print("""\nAvailable sizes:
    1. Small (+0.00)
    2. Medium (+0.50)
    3. Large (+1.00)
""")


    def add_order(self, coffee, size, quantity):
        """Create a new Order and adds it to the orders list."""
        new_order = Order(coffee, size, quantity)
        self.orders.append(new_order)
        print(f"\n✅ Added: {new_order}")

        remaining = 3 - self.total_items()
        
        if remaining > 0:
            print(f"💡 Add {remaining} more item(s) to unlock a 5% discount!")
        elif not self.loyalty_unlocked:
            print("🎉 Loyalty discount unlocked! 5% off will be applied at checkout.")
            self.loyalty_unlocked = True

    def remove_order(self, order_index):
        if 0 <= order_index < len(self.orders):
            removed = self.orders.pop(order_index)
            print(f"\n🗑️ Removed: {removed}")

            if self.total_items() < 3:
                self.loyalty_unlocked = False

        else:
            print("❌ Invalid order number.")

    def total_items(self):
        return sum(order.quantity for order in self.orders)

    def calculate_subtotal(self):
        """Add up the price of every order and return the total."""
        return sum(order.calculate_price() for order in self.orders)
    
    def generate_bill_text(self, tip_percent):
        subtotal = self.calculate_subtotal()

        discount = 0
        if self.total_items() >= 3:
            discount = subtotal * 0.05

        discounted_subtotal = subtotal - discount
        tax = discounted_subtotal * self.tax_rate
        tip = discounted_subtotal * (tip_percent / 100)
        total = discounted_subtotal + tax + tip

        lines = []
        lines.append("==== BILL ====")
        for order in self.orders:
            lines.append(f"• {order}")
        lines.append(f"Subtotal: ${subtotal:.2f}")

        if discount > 0:
            lines.append(f"Loyalty Discount (5%): -${discount:.2f}")

        lines.append(f"Tax: ${tax:.2f}")
        lines.append(f"Tip: ${tip:.2f}")
        lines.append(f"Total: ${total:.2f}")

        return "\n".join(lines)

    def print_and_save_bill(self, tip_percent, filename="receipt.txt"):
        bill_text = self.generate_bill_text(tip_percent)
        print("\n" + bill_text)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(bill_text)

        print(f"\n💾 Receipt saved to {filename}")

cafe = Cafe("Sunny Bean Café", tax_rate=0.08, daily_special="Mocha Monday - $1 off any Mocha")

cafe.add_to_menu(Coffee("Espresso",    "Strong and bold shot of coffee",           2.50))
cafe.add_to_menu(Coffee("Americano",   "Espresso diluted with hot water",          3.00))
cafe.add_to_menu(Coffee("Cappuccino",  "Equal parts espresso, foam, and milk",     3.75))
cafe.add_to_menu(Coffee("Latte",       "Creamy espresso with lots of steamed milk",3.50))
cafe.add_to_menu(Coffee("Flat White",  "Velvety milk with a double espresso shot", 4.00))
cafe.add_to_menu(Coffee("Macchiato",   "Espresso 'stained' with a touch of foam",  3.25))
cafe.add_to_menu(Coffee("Mocha",       "Espresso with chocolate and steamed milk", 4.25))
cafe.add_to_menu(Coffee("Cold Brew",   "Slow-steeped coffee served cold",          4.00))

SIZES = ["Small", "Medium", "Large"]

print(f"\nWelcome to {cafe.name}! ☕")

while True:
    print("\n" + "=" * 40)
    print("What would you like to do?")
    print("1. View menu and order a drink")
    print("2. View current order")
    print("3. Remove an item from order")
    print("4. Checkout and pay")
    print("=" * 40)

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        cafe.display_menu()

        drink_input = input("\nEnter the number of the drink you want (or 0 to cancel): ").strip()

        if drink_input == "0":
            continue

        if not drink_input.isdigit():
            print("❌ Please enter a number.")
            continue

        drink_index = int(drink_input) - 1

        if drink_index < 0 or drink_index >= len(cafe.menu):
            print("❌ That number is not on the menu. Try again.")
            continue

        selected_coffee = cafe.menu[drink_index]

        cafe.display_sizes()
        size_input = input("Enter the number of the size you want: ").strip()

        if not size_input.isdigit():
            print("❌ Please enter a number.")
            continue

        size_index = int(size_input) - 1

        if size_index < 0 or size_index >= len(SIZES):
            print("❌ Invalid size. Try again.")
            continue

        selected_size = SIZES[size_index]
        
        quantity_input = input("How many would you like? ").strip()
        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("❌ Please enter a valid quantity.")
            continue

        quantity = int(quantity_input)

        cafe.add_order(selected_coffee, selected_size, quantity)

    elif choice == "2":
        if not cafe.orders:
            print("\n🛒 Your order is empty.")
        else:
            print("\n--- Your Current Order ---")
            for i, order in enumerate(cafe.orders, start=1):
                print(f" {i}. {order}")
            print(f"\nTotal items: {cafe.total_items()}")
            print(F"\nSubtotal so far: ${cafe.calculate_subtotal():.2f}")
    
    elif choice == "3":
        if not cafe.orders:
            print("\n🛒 Your order is empty.")
            continue

        print("\n--- Current Order ---")
        for i, order in enumerate(cafe.orders, start=1):
            print(f"{i}. {order}")

        remove_input = input("Enter the number of the item to remove: ").strip()
   
        if not remove_input.isdigit():
            print("❌ Please enter a number.")
            continue

        remove_index = int(remove_input) - 1
        cafe.remove_order(remove_index)

    elif choice == "4":
        if not cafe.orders:
            print("\n❌ You have not ordered anything yet!")
            continue

        print("\nHow much would you like to tip?")
        print("1. 10% 2. 15% 3. 20% 4. No tip")
        tip_choice = input("Enter your choice (1/2/3/4): ").strip()

        tip_map = {"1": 10, "2": 15, "3": 20, "4": 0}
        tip_percent = tip_map.get(tip_choice, 0)

        cafe.print_and_save_bill(tip_percent)
        print("\nThank you for visiting! Have a great day! ☕\n")
        break

    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
