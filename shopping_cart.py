def display_cart(cart):
    if not cart:
        print("your cart is empty")
    else:
        print("shopping cart:")
    total_price= 0
    total_quantity=0
    for item in cart:
        print(f"{item['name']}:,₹{item['price']}:,{item['quantity']}:")  
        total_price += item['price']
        total_quantity += item['quantity']     
    print(f"total:₹{total_price:},total:{total_quantity}")
def main():
    cart = []
    while True:
        print("\n shopping cart Application")
        print("1. Add item to the cart")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Exit")
        choice= input("enter your choice: ")
        if choice == '1':
            item_name=input("Enter item name: ")
            item_price=float(input("Enter item price: "))
            item_quantity=int(input("enter item quantity: "))
            item={"name":item_name,"price":item_price,"quantity":item_quantity}
            cart.append(item)
            print('item added to cart')
        elif choice == '2':
            display_cart(cart)
    
        elif choice == '3':
            if not cart:
              print("your cart is already empty")
            else:
              display_cart(cart)
              item.index = int(input("enter the item number to remove:"))
              if 0<=item.index<len(cart):
                removed_item = cart.pop(item.index)
                print(f"removed item{removed_item['name']}")
              else:
                print("Invalid item number")
        elif choice == '4':
          print("Exit the Application")
         
        else:
          print("Invalid choice please select a valid option")
if __name__ == "__main__":
        main()                           

        
         








