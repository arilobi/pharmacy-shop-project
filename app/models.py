from sqlalchemy import  Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    #-----> Creating a new table called users
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    # Creating a relationship with the order table
    orders = relationship('Order', back_populates = 'user')

class Product(Base): 
     #-----> Creating a new table called products
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

    # -----> Creating a relationship with the order table
    orders = relationship('Order', back_populates = 'product')

class Order(Base): 
     #-----> Creating a new table called orders
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

    # -----> creating a relationship with the user and product table
    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')