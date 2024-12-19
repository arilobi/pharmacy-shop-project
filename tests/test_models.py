# Importing
from app.models.user import User
from app.models.product import Product
from app.models.order import Order

class TestModels:
    def test_user(self):
        # -----> Id and name
        user = User(1, "John Dutton")
        assert user.username == "John Dutton"

    def test_product(self):
        # ------> Id, name of the product, price and stock
        product = Product(1, "Panadol Advanced", 100, 10)
        assert product.name == "Panadol Advanced"
        assert product.price == 100
        assert product.quantity == 10

    def test_order(self):
        # -----> Id, user_id, quantity and price
        order = Order(1, 1, 5, 50)
        assert order.product_id == 1
        assert order.quantity == 5
        assert order.price == 50
