from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    '''
    class defines the user/shop keeper
    Args:
        id, username, email, password_hash
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String)
    password_hash = db.Column(db.String(255))

    def save_users(self):
        db.session.add(self)
        db.session.commit()
    
    
    @property 
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.pass_hash = generate_password_hash(password)
        
        
    def verify_password(self, password):
        return check_password_hash(self.pass_hash, password)
    
    @login_manager.user_loader 
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'User {self.username}: {self.email}'
    
class Products(db.Model):
    '''
    defines the products class
    Args
        id, product_name, product_unit, product_price    
    '''
    
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.Text)
    product_unit = db.Column(db.Integer)
    product_price = db.Column(db.Integer)
    
    def save_product(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_product_id(cls, id):
        product_id = Products.query.filter_by(id = id).order_by(Products.id.desc())
        return product_id
    
    def __repr__(self):
        return f'User {self.username} : {self.email}'