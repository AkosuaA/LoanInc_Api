from app import app
from app.models import Agent, Customer, CustomerPhone, CustomerAddress, CustomerLoan, CustomerPayment
from flask import request

@app.route('/login', methods=['POST'])
def login(force = True):
    data = request.get_json()
    print(data)
    agent = Agent.query.filter_by(email=data.get('Email')).first()
    if agent is None:
        return {"message": "Email provided does not exist", "field": "Email", "status": "invalid"}
    if not agent.check_password(data.get('Password')):
        return {"message": "Invalid password provided", "field": "Password", "status": "invalid"}
    return {"status": "success"}

@app.route('/customers')
def customers():
    customers = Customer.query.all()
    results = [
        {
            "id": customer.id,
            "first_name": customer.first_name,
            "middle_name": customer.middle_name,
            "last_name": customer.last_name
        } for customer in customers]

    return {"count": len(results), "customers": results}

@app.route('/customer/<customer_id>')
def customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    response = {
        "id": customer.id,
        "first_name": customer.first_name,
        "middle_name": customer.middle_name,
        "last_name": customer.last_name,
        "phone_numbers": [dict(id=number.id, number=number.number) for number in customer.phone_numbers],
        "addresses": [dict(id=address.id, region=address.region, city=address.city, location=address.location) for address in customer.addresses],
        "loans": [dict(amount=str(loan.amount), loan_date=loan.loan_date) for loan in customer.loans],
        "payments": [dict(amount=str(payment.amount), payment_date=payment.payment_date) for payment in customer.payments]
    }
    return {"message": "success", "customer": response}