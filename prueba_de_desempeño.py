import re

inventory = [
    {"name": "tomato", "price": 10.0, "quantity": 30},
    {"name": "banana", "price": 15.0, "quantity": 50},
    {"name": "ham", "price": 20.0, "quantity": 30},
    {"name": "cheese", "price": 25.0, "quantity": 10},
    {"name": "soda", "price": 30.0, "quantity": 20}
]

def validate_letters():
    pattern = r"^[\wÁÉÍÓÚÜÑáéíóúüñ\s.,@#!$%&()\-]+$"
    while True:
        text = input()
        if re.fullmatch(pattern, text):
            return text


# Validation of positive integer
def ValidationNumINT():
    while True:
        number = input()
        try:
            number = int(number)
            if number > 0:
                return number
            else:
                print("The value must be greater than 0. Try again.")
        except ValueError:
            print("Invalid entry. Please enter a positive valid number.")

# Positive floating number validation
def ValidatioNumFLOAT():
    while True:
        number = input()
        try:
            number = float(number)
            if number > 0:
                return number
            else:
                print("The value must be greater than 0. Try again.")
        except ValueError:
            print("Invalid entry. Please enter a positive valid number.")

#Validate answer yes/no
def Validationsn():
    while True:
        answer = input().strip().lower()
        if answer in ('s', 'n'):
            return answer
        else:
            print("Invalid response. Please enter 's' or 'n'.")

# Check if the product already exists
def exists_product(name):
    return any(product['name'].lower() == name.lower() for product in inventory)

# Funtion to add names to the inventory 
def Addname(name,price,quality):
    product={"name": name, "price": price, "quantity": quality}
    inventory.append(product)

# Consult names
def consultnames_list():
    if not inventory:
        print("There are no products in stock.")
        return
    for product in inventory:
        print("\nThe product you are interested in is:\n")
        print(f"name: {product['name']}, Price: ${product['price']}, quantity: {product['quantity']}")
        print("-" * 50)

def consultnames_search(name):
    
    for product in inventory:
        if exists_product(name):
            print("\nThe product you are interested in is:\n")
            if product['name'].lower() == name.lower():
                print("-" * 50)
                print(f"name: {product['name']}, Price: ${product['price']}, quantity: {product['quantity']}")
                print("-" * 50)
            return  
    print(f"The name({name}) was not found")

#Update Price
def UpdatePrice(name,price):
    for product in inventory:
        if product["name"].lower()==name.lower():
            product["price"]=price
            print(f"The name with the name {name}, the price has been update({price}).")
            return
    print(f"The name({name}) was not found")

#Delete names
def nameDelete(name):
    for product in inventory:
        if product["name"].lower()==name.lower():
            print(f"Are you sure to delete this name?({name})(s/n)");Confirmation=Validationsn()
            if Confirmation=="s":
                inventory.remove(product)
                print("The name is delete.")
                return
            elif Confirmation=="n":
                print("Okay......")
                return
    print(f"The name({name}) was not found")

#Calculate total
def CalculateTotal():
    value_total = sum(product['price'] * product['quantity'] for product in inventory)
    print("-" * 50)
    print(f"\nTotal value of the inventory: ${value_total:.2f}")
    print("-" * 50)

#menu
def menu():
    while True:
        print("""
            list of funtions
            
            1. Add names to inventory
            2. Consult names in inventory
            3. Update price list
            4. remove names from inventory
            5. Calculate the total value of the inventory
            6. Exit
            """)
        print("\nenter one option(1-6): "); option=ValidationNumINT()
        
        if option==1:
            while True:
                print("Enter the product name: "); name=validate_letters()
                if not exists_product(name):
                    print("Enter the product price: "); price=ValidatioNumFLOAT()
                    print("Enter the quality of product: "); quality=ValidationNumINT()
                    Addname(name,price,quality)
                    print("\nDo you want to do something else? (s/n):")
                    if Validationsn() == 'n':
                        break
                else:
                    print("The product already exists.")
        elif option==2:
            while True:
                print("Search by name(s) or display list(n): "); consult=validate_letters()
                if consult=="s":
                    print("product name: ");name=validate_letters()
                    consultnames_search(name)
                    print("\nDo you want to do something else? (s/n):")
                    if Validationsn() == 'n':
                        break
                elif consult=="n":
                    consultnames_list()
                    print("\nDo you want to do something else? (s/n):")
                    if Validationsn() == 'n':
                        break
                else:
                    print("Invalid option")
        elif option==3:
            while True:
                print("Entry the name name: "); name=validate_letters()
                if exists_product(name):
                    print("Entry the new price: "); price=ValidatioNumFLOAT()
                    UpdatePrice(name,price)
                    print("\nDo you want to do something else? (s/n): ")
                    if Validationsn() == 'n':
                            break
                else:
                    print("the product does not exist\n")
        elif option==4:
            while True:
                print("Entry the name of the name you want to delete: ");name=validate_letters()
                nameDelete(name)
                print("\nDo you want to do something else? (s/n): ")
                if Validationsn() == 'n':
                        break
        elif option==5:
            CalculateTotal()
        elif option==6:
            print("GoodBye.....")
            break
        else:
            print("Please use a correct option, thx.")
            
menu()