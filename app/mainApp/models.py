from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from app.mainApp import  app,db

class Category(db.Model):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    image = Column(String(1000), nullable=True, default='https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/1/_/1_251_1.jpg')

if __name__ == '__main__':
    with app.app_context():
        c1 = Category(name='Iphone')
        c2 = Category(name="Samsung")

        db.session.add(c1)
        db.session.add(c2)

        ip14 = Product(name = 'Iphone14', price = 1324532, category_id = 1,image = 'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/1/_/1_251_1.jpg')
        ip11 = Product(name = 'Iphone11', price = 8374, category_id = 1, image = 'https://cdn2.cellphones.com.vn/insecure/rs:fill:0:358/q:80/plain/https://cellphones.com.vn/media/catalog/product/1/_/1_251_1.jpg')


        db.session.add_all([ip11, ip14])



        db.session.commit()

        # db.create_all()