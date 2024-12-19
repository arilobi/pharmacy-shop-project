from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Product, Order

engine = create_engine("sqlite:///../pharmacy.sqlite")

Session = sessionmaker(bind=engine)
session = Session()