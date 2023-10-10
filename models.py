from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
import datetime

db = SQLAlchemy()


def get_uuid():
    return uuid4().hex

def now():
    return datetime.datetime.now()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    email = db.Column(db.String(345), unique=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.Text, nullable=False)


# Model for Products
class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    url = db.Column(db.Text, nullable=False, unique=True)
    user_id = db.Column(db.String(32), nullable=False)
    title = db.Column(db.String(345), nullable=False, unique=True)
    latest_price = db.Column(db.Integer, nullable=False, default=0)
    image = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=now)

    @staticmethod
    def get_fields() -> list:
        """
        Returns all of the fields used in here
        """
        return ['id', 'url', 'user_id', 'title', 'latest_price', 'image', 'date_added']


# Model to store all the products price history
class PriceHistory(db.Model):
    __tablename__ = "priceHistory"
    history_id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    product_id = db.Column(db.String(32), nullable=False)
    date = db.Column(db.DateTime, default=now)
    price = db.Column(db.Integer, nullable=True, default=0)

    @staticmethod
    def get_fields() -> list:
        """
        Returns all of the fields used in here
        """
        return ['history_id', 'product_id', 'date', 'price']
