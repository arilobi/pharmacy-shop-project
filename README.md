# Pharmacy Management System (CLI)
## By Marion Okondo

My project is a Command-Line Interface (CLI) based Pharmacy Management System. It allows users to register and log in, create, update, and delete products, and place and view orders.

## Features
- User Authentication:
     - Users can register with a username and password.
     - Users can log in with their credentials.
     - Users can add, update products and even place orders.
- Product Management:
     - Create new products with name, price, and stock quantity.
     - Update existing products by modifying the name, price, and stock quantity.
     - Delete products
- Order Management:
    - Place orders for available products.
    - Orders automatically decrease stock from the inventory.
    - Orders track user information, product details and quantity
- View Orders
     - Users can view all orders placed.

## Technology Stack
- Python
- SQLAlchemy: Object-Relational Mapping (ORM) for interacting woth the SQLite database.
- SQLite: For local database management.

## Installation process
1. Clone the repository to your terminal.
2. Navigate to the project directory 
3. Set up a virtual environment
4. Install the needed dependecies:
   - pipenv install sqlalchemy
   - pipenv shell
5. Lastly run the Pharmacy CLI application:
   - python3 main.py

## Usage
1. Run the Pharmacy CLI application in the app directory
   - python3 main.py
2. Pharmacy Menu Options:
   1. Register
   2. Login
   3. Add Product
   4. Update Product
   5. Place Order
   6. Delete Product
   7. Exit

## Future Improvements
- Implement all these using FastAPI.
- Enhance order history for consumers to track past orders in more detail.
- Add support for more detailed user roles and permissions.
- Enable a more secured password for the users registering and logging in.

## Links
Google slides - https://docs.google.com/presentation/d/1vdgUCr85BlPhlN7zV9Q6DeuVk1eyIfnBM9l-rAazudU/edit?usp=sharing

## Support and contact details
Email:: arinabulobi@gmail.com

## License
Licensed under the MT-license

Copyright (c) 2024 Marion Okondo
