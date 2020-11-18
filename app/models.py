from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, app

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<Agent {}>'.format(self.first_name + " " + self.last_name)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    phone_numbers = db.relationship('CustomerPhone', backref='customer', lazy='dynamic')
    addresses = db.relationship('CustomerAddress', backref='customer', lazy='dynamic')
    loans = db.relationship('CustomerLoan', backref='customer', lazy='dynamic')
    payments = db.relationship('CustomerPayment', backref='customer', lazy='dynamic')

    def __repr__(self):
        return '<Customer {}>'.format(self.first_name + " " + self.last_name)

class CustomerPhone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
        return '<Number {}>'.format(self.number)

class CustomerAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(64))
    city = db.Column(db.String(64))
    location = db.Column(db.String(64))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))


class CustomerLoan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    amount = db.Column(db.Numeric(5))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

class CustomerPayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(5))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer_loan_id = db.Column(db.Integer, db.ForeignKey('customer_loan.id'))
    payment_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)



@app.cli.command('db_seed')
def db_seed():
    s = db.session()
    objects = [
        Agent(first_name="Kofi", last_name="Ankah", email="kankah@gmail.com",password=generate_password_hash("kankah123")),
        Agent(first_name="Susan", last_name="Lay", email="sussielay@gmail.com",password=generate_password_hash("slay123")),
        Agent(first_name="Joe", last_name="Black", email="joe_black@gmail.com",password=generate_password_hash("j_black123")),
        Customer(first_name="Daniel", middle_name="Kojo", last_name="Dadson"),
        Customer(first_name="David", middle_name="Kojo", last_name="Appiah"),
        Customer(first_name="Isaac", middle_name="Kwesi", last_name="Ampong"),
        Customer(first_name="Richard", middle_name="Kwame", last_name="Manu"),
        Customer(first_name="Goldy", middle_name="Frances", last_name="Dadson"),
        Customer(first_name="Gabby", middle_name="Ofei", last_name="Addo"),
        Customer(first_name="Paulina", middle_name="Adwoa", last_name="Brooke"),
        Customer(first_name="Nana", middle_name="Akosua", last_name="Thompson"),
        CustomerPhone(number="+233201233323", customer_id=1),
        CustomerPhone(number="+233201233324", customer_id=1),
        CustomerPhone(number="+233201233325", customer_id=1),
        CustomerPhone(number="+233201233326", customer_id=2),
        CustomerPhone(number="+233265233327", customer_id=3),
        CustomerPhone(number="+233201212128", customer_id=4),
        CustomerPhone(number="+233201265429", customer_id=5),
        CustomerPhone(number="+233201232420", customer_id=6),
        CustomerPhone(number="+233203233321", customer_id=7),
        CustomerPhone(number="+233265285327", customer_id=8),
        CustomerAddress(region="Greater Accra", city="Accra", location="Coca-Cola Roundabout", customer_id=1),
        CustomerAddress(region="Central", city="Cape-Coast", location="Kakumdo", customer_id=2),
        CustomerAddress(region="Greater Accra", city="Accra", location="Accra Mall", customer_id=3),
        CustomerAddress(region="Greater Accra", city="Adenta", location="Adenta Bus Stop", customer_id=4),
        CustomerAddress(region="Northern", city="Accra", location="Coca-Cola Roundabout", customer_id=5),
        CustomerAddress(region="Greater Accra", city="Accra", location="East-Legon", customer_id=6),
        CustomerAddress(region="Greater Accra", city="Accra", location="Coca-Cola Roundabout", customer_id=7),
        CustomerAddress(region="Greater Accra", city="Accra", location="Coca-Cola Roundabout", customer_id=8),
        CustomerLoan(amount=1000, loan_date="2020-01-01", customer_id=1),
        CustomerLoan(amount=10000, loan_date="2020-01-01", customer_id=2),
        CustomerLoan(amount=2000, loan_date="2020-01-01", customer_id=3),
        CustomerLoan(amount=3000, loan_date="2020-01-01", customer_id=4),
        CustomerLoan(amount=100, loan_date="2020-01-01", customer_id=5),
        CustomerLoan(amount=120, loan_date="2020-01-01", customer_id=6),
        CustomerLoan(amount=120, loan_date="2020-01-01", customer_id=7),
        CustomerLoan(amount=120, loan_date="2020-01-01", customer_id=8),
        CustomerPayment(amount=120, customer_id=1, customer_loan_id=1, payment_date= "2020-02-01"),
        CustomerPayment(amount=120, customer_id=1, customer_loan_id=1, payment_date= "2020-03-01"),
        CustomerPayment(amount=120, customer_id=1, customer_loan_id=1, payment_date= "2020-03-12"),
        CustomerPayment(amount=120, customer_id=1, customer_loan_id=1, payment_date= "2020-04-01"),
        CustomerPayment(amount=120, customer_id=1, customer_loan_id=1, payment_date= "2020-05-01"),
        CustomerPayment(amount=120, customer_id=1, customer_loan_id=1, payment_date= "2020-06-01"),
        CustomerPayment(amount=100, customer_id=1, customer_loan_id=1, payment_date= "2020-07-01"),
        CustomerPayment(amount=120, customer_id=1, customer_loan_id=1, payment_date= "2020-08-01"),
        CustomerPayment(amount=60, customer_id=1, customer_loan_id=1, payment_date= "2020-09-01"),
        CustomerPayment(amount=120, customer_id=2, customer_loan_id=2, payment_date= "2020-02-01"),
        CustomerPayment(amount=120, customer_id=2, customer_loan_id=2, payment_date= "2020-03-01"),
        CustomerPayment(amount=120, customer_id=2, customer_loan_id=2, payment_date= "2020-04-01"),
        CustomerPayment(amount=120, customer_id=3, customer_loan_id=3, payment_date= "2020-05-01"),
        CustomerPayment(amount=120, customer_id=3, customer_loan_id=3, payment_date= "2020-06-01"),
        CustomerPayment(amount=120, customer_id=4, customer_loan_id=4, payment_date= "2020-07-01"),
        CustomerPayment(amount=100, customer_id=5, customer_loan_id=5, payment_date= "2020-08-01"),
        CustomerPayment(amount=120, customer_id=6, customer_loan_id=6, payment_date= "2020-09-01"),
        CustomerPayment(amount=60, customer_id=6, customer_loan_id=6, payment_date= "2020-10-01"),
    ]
    s.bulk_save_objects(objects)
    s.commit()