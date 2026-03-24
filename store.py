from catalog import catalog # import your catalog list

# Global shopping cart
cart = []

# Helper Functions (store name/ menu)
def print_header(text):
    print("----------------------")
    print(text)
    print("----------------------")


def print_menu():
    print("Menu")
    print("1.- View Catalog")
    print("2.- Search Product")
    print("3.- View Cart")
    # add more options if needed
    print("4.- Clear Cart")
    print("Q.- Quit")


# Catalog and Cart Function
def print_catalog():
    print_header("- Our Catalog -")
    for prod in catalog:  # Ljust means justify left. 15 spaces to the right
        print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")

    answer = input("Type ID to add (N to close): ")
    if answer.lower() == "n":
        return
    else:
        add_product_to_cart(answer)
    print("----------------------")
     

def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod) # add product to the cart (bag)
            print(f"{prod["title"]} added to your cart") 
            break
    
    if not found:
        print("Item dose not exist")

def search_product():
    text = input("Search text: ").lower()
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")
            choice = input("Do you want to add this item to your cart? (y/n): ")
            if choice.lower() == "y":
                add_product_to_cart(prod["id"])
            break # stops after first match
    
    if not found:
        print("Sorry, this items dosen't exist.")
    print("----------------------")

def view_cart():
    print_header("Your Cart")
    if not cart:
        print("Your cart is empty.")
    else:
        for prod in cart:
            print(f"| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}")
        cart_total() # shows total price

def cart_total():
    total = 0 # start from 0 and add prices up
    for prod in cart:
        total += prod["price"] # add product price to total
    print(f"Total is: ${total}")
    # for loop- total += prod"price"
    # print("total")


# create a function called clear_cart()
# code- it should clear the cart
# print a message saying "cart is cleared"
# add it to the menu up top and the main program loop
def clear_cart():
    cart.clear()
    print("Your cart has been cleared")


# Main Program Loop
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to STORE")
    print_menu()

    option = input("Choose an option: ")

    if option == "1":
        print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "4":
        clear_cart()
    elif option == "q" or option == "Q":
        print("Good Bye!")
        break
    else:
        print("** Error: invalid option")
        print("----------------------")