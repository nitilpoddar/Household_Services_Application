from flask import Flask,  render_template, url_for, request
import os
from models import db
from controllers.create_customer import create_customer


cur_directory = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(cur_directory,"testdb.sqlite3")

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(create_customer, url_prefix='/create')

@app.route('/', methods=['GET'])
def test():
    return render_template('createCustomer.html')

if __name__ == '__main__':
    app.run(debug=True)