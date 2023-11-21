class RestaurantMenu:
    def __init__(self):
        self.menu = {}

    def add_item(self, item_name, price):
        self.menu[item_name] = price

    def display_menu(self):
        print("----- Menu -----")
        for item, price in self.menu.items():
            print(f"{item}: {price:.2f}")
        print("-----------------")

# Example usage
if __name__ == "__main__":
    restaurant = RestaurantMenu()

    # Adding items to the menu
    restaurant.add_item("pizza", 199)
    restaurant.add_item("Burger", 80)
    restaurant.add_item("pasta", 120)
    restaurant.add_item("kunafa", 150)

    # Displaying the menu
    restaurant.display_menu()
