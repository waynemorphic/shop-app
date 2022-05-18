from app import db
from flask_login import UserMixin

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

def __repr__(self):
    return f'User' ({self.username}, {self.email})
    
class Products(db.Modle):
    '''
    defines teh products class
    Args
        id, product_name, product_unit, product_price    
    '''
    
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.Text)
    product_unit = db.Column(db.Integer)
    product_price = db.Column(db.Integer)
    
def __repr__(self):
    return f'User' ({self.username}, {self.email})