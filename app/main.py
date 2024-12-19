from config import *

#-----> I'm starting with registration and login functions so that a user can either sign up when they don't have an account and login after they have created one.

#-----> I'm making a global variable so that when I declare it inside a function, it will refer to the global user not locally
current_user = None

#-----> Function to register
def register(): 
    username = input("Enter username: ")
    password = input("Enter password: ")

#-----> Creating a new user and commit the changes
    new_user = User(username=username, password=password)
    session.add(new_user)
    session.commit()
    print(f"User '{username}' registered successfully")

#-----> Function to login
def login(): 
    # -----> This will check the global user outside the functions
    global current_user

    username = input("Enter username: ")
    password = input("Enter password: ")

    #-----> Fetching the user created by querying the database which will check if the username is available and allow the user to log in
    user = session.query(User).filter_by(username=username).first()
    #-----> If the user and the actual password matches the stored password, then it will allow the user to login
    if user and user.password == password: 
        current_user = user
        print(f"Welcome {user.username}.")
    else:
        print("Invalid username and password")

#-----> CREATING THE CUD FUNCTIONS -- Create, Update and Delete

#-----> Creating or adding an item
def create_item(): 

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))

    new_product = Product(name=name, price=price, stock=stock)
    session.add(new_product)
    session.commit()
    print(f"Product {name} created successfully")

#-----> Updating an item
def update_item(): 
    #-----> Using the product id to get the specific product I want to update
    product_id = int(input("Enter product ID to update: "))

    product = session.query(Product).get(product_id)
    #-----> Updating the old product details with new details
    if product:
        new_name = input("Enter new product name: ")
        new_price = float(input("Enter new product price: "))
        new_stock = float(input("Enter new product stock: "))

    # -----> Update the old product details with the new one.
        if new_name:
            product.name = new_name
        if new_price:
            product.price = new_price
        if new_stock:
            product.stock = new_stock

        session.commit()
        print(f"Product {product_id} successfully updated.")

    else: 
        print("Product unavailable.")

#-----> Placing an order and passed my global variable as an argument
def place_order(current_user):
    if current_user is None:
        print("No user is logged in")
        return

    product_id = int(input("Enter product ID to order: "))
    quantity = int(input("Enter quantity: "))

    #-----> Retrieving the product from the database
    product = session.query(Product).get(product_id)

    # -----> Check if the product is available according to the available stock
    if product and product.stock >= quantity:
        #-----> Create a new order with the current user's ID, choose the product, quantity and automatically, it will calculate the total price with the quantity the user has chosen. 
        new_order = Order(user_id=current_user.id, product_id=product_id, quantity=quantity, total_price=product.price * quantity)
        
        #-----> When a user places an order, the stock will decrease
        product.stock -= quantity

        #-----> Add and commit the new order to the session
        session.add(new_order)
        session.commit()

        print(f"Order placed for {quantity} of {product.name}")
    else:
        print("Product unavailable")

#-----> Delete an item / product
def delete_item():
    product_id = int(input("Enter product ID to delete: "))

    #----> Fetch the product and related orders
    product = session.query(Product).get(product_id)

    if product:
        #-----> Delete all related orders first
        session.query(Order).filter_by(product_id=product_id).delete()

        #-----> And lastly, deleting the product then commit the changes
        session.delete(product)
        session.commit()

        print(f"Product {product_id} and its associated orders have been deleted.")
    else:
        print("Product not found.")

    
def main(): 
    while True: 
        print("\nPharmacy Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Place Order")
        print("6. Delete Product")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            create_item()
        elif choice == '4':
            update_item()
        elif choice == '5':
            place_order(current_user)
        elif choice == '6':
            delete_item()
        elif choice == '7':
            break
        else: 
            print("Invalid choice.")

if __name__ == "__main__":
    main()