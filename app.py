from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
import scrapey


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ds_course_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@dataclass
class Covid19(db.Model):
    id: int
    country: str
    first_case_date: str
    jan_1: int
    feb_1: int
    mar_1: int
    apr_1: int
    may_1: int
    jun_1: int
    jul_1: int
    aug_1:int
    sept_1: int
    oct_1: int
    nov_1: int

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(255), nullable=False)
    first_case_date = db.Column(db.String(255), nullable=False)
    jan_1 = db.Column(db.Integer, nullable=False)
    feb_1 = db.Column(db.Integer, nullable=False)
    mar_1 = db.Column(db.Integer, nullable=False)
    apr_1 = db.Column(db.Integer, nullable=False)
    may_1 = db.Column(db.Integer, nullable=False)
    jun_1 = db.Column(db.Integer, nullable=False)
    jul_1 = db.Column(db.Integer, nullable=False)
    aug_1 = db.Column(db.Integer, nullable=False)
    sept_1 = db.Column(db.Integer, nullable=False)
    oct_1 = db.Column(db.Integer, nullable=False)
    nov_1 = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<Covid19 {self.id} {self.country}>"

@app.route('/')
def home():
    data = scrapey.scrape()
    # country = Covid19.query.all()  
    return render_template("base.html", items = data)

# @app.route('/', methods=['GET'])
# def home():
#     return render_template('base.html')

@app.route('/api', methods=['GET'])
def get_data():
    table = Covid19.query.all()
    # table = [x.json() for x in table]
    # return jsonify(table)
    return jsonify(table)

if __name__=='__main__':
    app.run(debug=True)