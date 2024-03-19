# ============ Inventory Management ============ #

# Import the tabulate module

from tabulate import tabulate

# Define class shoe

class Shoe:
    # Intialise the class with all the associated variables
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Define class functions that:
    # Return cost, return quantity
    def get_cost(self):
        return self.cost
    
    def get_quantity(self):
        return self.quantity
    
    # Return shoe object as a tuple for tabulate function
    def return_tuple(self):
        return (self.country, self.code, self.product, self.cost, self.quantity)
    
    # Define the __str__ class that returns all the variables associated with the class as an f-string
    def __str__(self):
        return f"Product: {self.product}, Country: {self.country}, Code: {self.code}, Cost: {self.cost}, Quantity: {self.quantity}"

# Declare an empty list to store shoe data
    
shoes_list = []

# Define a userfunction to read all the data from a prespecified file into the shoe data list

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                try:
                    cost = float(cost)
                    quantity = int(quantity)
                except ValueError:
                    print("Invalid format in file")
                shoes_list.append(Shoe(country, code, product, cost, quantity))
    except FileNotFoundError:
        print("Error: 'inventory.txt' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Define a user function to capture shoe data to enter into the list
# prompting a user for all the data associated with the particular shoe

def capture_shoes():
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    try:
        cost = float(input("Cost: "))
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Please provide a valid input")
    shoes_list.append(Shoe(country, code, product, cost, quantity))

# Define a user function to view the data of all the shoes in a table



def view_all():
    shoe_tuples = [shoes.return_tuple() for shoes in shoes_list]
    table = tabulate(shoe_tuples, headers=["Country", "Code", "Product", "Cost", "Quantity"])
    print(table)

# Added a get_quantity method for max and min methods to use
def get_quantity(shoe):
    return shoe.quantity

# Define a user function to return the shoe with the lowest quantify,
# and the prompt the user to restock a particular quantity

def re_stock():
    if not shoes_list:
        print("Shoe not available.")
        return

    min_quantity_shoe = min(shoes_list, key=get_quantity)
    print(f"Lowest quantity shoe: {min_quantity_shoe}")
    try:
        add_quantity = int(input("Add quantity: "))
    except ValueError:
        print("Please provide a valid input.")
    min_quantity_shoe.quantity += add_quantity
    print(f"Product restocked with {add_quantity}")

# Define a user function to search the shoe list for a particular shoe code,
# if the shoe is found, return the shoe object

def search_shoe():
    if not shoes_list:
        print("Shoe not available.")
        return

    code = input("Enter the shoe code to search: ")
    found_shoe = None
    for shoe in shoes_list:
        if shoe.code == code:
            found_shoe = shoe
            break

    if found_shoe:
        print("Shoe found:")
        print(found_shoe)
    else:
        print("Shoe not found.")

# For each shoe in the shoe list, calculate the total value in stock
# by multiplying the quantity in stock, and the shoe price

def value_per_item():
    print("Value per item:")
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: {value}")

# Search the list for the shoe with the highest quantity in stock.
# make the suggestion to put the shoe on sale.

def highest_qty():
    if not shoes_list:
        print("No shoes available.")
        return

    max_quantity_shoe = max(shoes_list, key=get_quantity)
    print(f"Shoe {max_quantity_shoe.code} to be put on Sale")
    print(max_quantity_shoe)

# Declare the main function that presents a menu, 
# and each menu item calls a function (user or class) defined above

def main():
    while True:
        print("\nMENU:")
        print("1. Read shoes data from file")
        print("2. Capture new shoes data")
        print("3. View all shoes")
        print("4. Re-stock shoes")
        print("5. Search shoe by code")
        print("6. Calculate value per item")
        print("7. Show highest quantity shoe for sale")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")

# Call the main function

main()

# ============ Inventory Management ============ #


# ============ Emd of Code ============ #
