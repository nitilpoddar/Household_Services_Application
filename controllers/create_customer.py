from models.customer import Customer, db
from sqlalchemy.orm import session
from flask import Blueprint, render_template, url_for, request
#from app import request

create_customer = Blueprint('create_customer', __name__)

@create_customer.route('/createCustomer', methods=['POST'])
def createCustomer():
    return "<h1>customer creation successful</h1>"
