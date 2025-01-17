from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:7629@localhost:3306/rental_house'
database = SQLAlchemy(app)

# User model
class User(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    first_name = database.Column(database.String(50), nullable=False)
    last_name = database.Column(database.String(50), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(255), nullable=False)
    created_at = database.Column(database.DateTime, default=database.func.now())

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"

# Listing model
class Listing(database.Model):
    __tablename__ = 'listings'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'), nullable=False)
    title = database.Column(database.String(200), nullable=False)
    description = database.Column(database.Text, nullable=False)
    price_per_night = database.Column(database.Float, nullable=False)
    location = database.Column(database.String(100), nullable=False)
    created_at = database.Column(database.DateTime, default=database.func.now())

    user = database.relationship('User', backref=database.backref('listings', lazy=True))

    def __repr__(self):
        return f"<Listing {self.title}>"

# Booking model
class Booking(database.Model):
    __tablename__ = 'bookings'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'), nullable=False)
    listing_id = database.Column(database.Integer, database.ForeignKey('listings.id'), nullable=False)
    start_date = database.Column(database.Date, nullable=False)
    end_date = database.Column(database.Date, nullable=False)
    total_price = database.Column(database.Float, nullable=False)
    created_at = database.Column(database.DateTime, default=database.func.now())

    user = database.relationship('User', backref=database.backref('bookings', lazy=True))
    listing = database.relationship('Listing', backref=database.backref('bookings', lazy=True))

    def __repr__(self):
        return f"<Booking {self.id}>"

# Review model
class Review(database.Model):
    __tablename__ = 'reviews'

    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'), nullable=False)
    listing_id = database.Column(database.Integer, database.ForeignKey('listings.id'), nullable=False)
    rating = database.Column(database.Integer, nullable=False)  # Rating out of 5
    comment = database.Column(database.Text, nullable=True)
    created_at = database.Column(database.DateTime, default=database.func.now())

    user = database.relationship('User', backref=database.backref('reviews', lazy=True))
    listing = database.relationship('Listing', backref=database.backref('reviews', lazy=True))

    def __repr__(self):
        return f"<Review {self.id}>"