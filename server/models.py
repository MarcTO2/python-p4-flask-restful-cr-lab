from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Decimal(10), nullable=False)

    id = db.Column(db.Integer, primary_key=True)
