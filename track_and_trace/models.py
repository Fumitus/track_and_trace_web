from datetime import datetime
from track_and_trace import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    codes = db.relationship('Codes', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Codes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    new_code = db.Column(db.String(100), unique=True, nullable=True)
    date_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    def __repr__(self):
        return f"Codes('{self.product_id}', '{self.code}', '{self.new_code}', '{self.user_id}')"

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_batch = db.Column(db.String(100), nullable=False)
    expire_date = db.Column(db.String(100), nullable=False)
    date_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Product('{self.product_name}', '{self.product_batch}', '{self.expire_date}', '{self.user_id}')"

class Box_codes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    box_code = db.Column(db.String(100), unique=True, nullable=False)
    code_id = db.Column(db.Integer, db.ForeignKey('codes.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Box_codes('{self.box_code}', '{self.date_stamp}')"

class Pallet_codes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pallet_code = db.Column(db.String(100), unique=True, nullable=False)
    box_code_id = db.Column(db.Integer, db.ForeignKey('box_codes.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_stamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Box_codes('{self.pallet_code}', '{self.date_stamp}')"