def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    
    print("\nShopping Cart:")
    total_price = 0
    total_quantity = 0
    
    for index, (item, details) in enumerate(cart.items(), start=1):
        print(f"{index}. {item} - ₹{details['price']} x {details['quantity']}")
        total_price += details['price'] * details['quantity']
        total_quantity += details['quantity']
    
    print(f"Total Price: ₹{total_price}")
    print(f"Total Items: {total_quantity}")

def main():
    items = {
        "Apple": 20,
        "Banana": 10,
        "Orange": 15,
        "Grapes": 30,
        "Mango": 50
    }
    cart = {}
    
    while True:
        print("\n*_____Shopping Cart Application_____*")
        print("1. Add item to the cart")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Available items:")
            for item, price in items.items():
                print(f"{item} - ₹{price}")
            
            item_name = input("Enter item name to add: ").strip()
            if item_name in items:
                item_quantity = int(input("Enter quantity: "))
                if item_name in cart:
                    cart[item_name]['quantity'] += item_quantity
                else:
                    cart[item_name] = {"price": items[item_name], "quantity": item_quantity}
                print(f"{item_name} added to the cart.")
            else:
                print("Item not available.")
        
        elif choice == '2':
            display_cart(cart)
        
        elif choice == '3':
            if not cart:
                print("Your cart is already empty.")
            else:
                display_cart(cart)
                item_name = input("Enter the item name to remove: ").strip()
                if item_name in cart:
                    del cart[item_name]
                    print(f"{item_name} removed from cart.")
                else:
                    print("Item not found in the cart.")
        
        elif choice == '4':
            print("Exiting the Application.")
            break
        
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
