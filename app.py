
from flask import Flask, render_template, jsonify,redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///covid19.db'

db = SQLAlchemy(app)

class Covid19Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(255), nullable=False)
    first_case_date = db.Column(db.String(255), nullable=False)
    jan_1 = db.Column(db.Float, nullable=False)
    feb_1 = db.Column(db.Float, nullable=False)
    mar_1 = db.Column(db.Float, nullable=False)
    apr_1 = db.Column(db.Float, nullable=False)
    may_1 = db.Column(db.Float, nullable=False)
    jun_1 = db.Column(db.Float, nullable=False)
    jul_1 = db.Column(db.Float, nullable=False)
    aug_1 = db.Column(db.Float, nullable=False)
    sept_1 = db.Column(db.Float, nullable=False)
    oct_1 = db.Column(db.Float, nullable=False)
    nov_1 = db.Column(db.Float, nullable=False)
    dec_1 = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f"<Covid19 {self.id} {self.country}>"

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/projects", methods=["GET"])
def projects():
    table = Covid19Table.query.all()
    d=[]
    for row in table:
        row_as_dict = {
            "country": row.country,
            "first case date": row.first_case_date,
            "jan 1": row.jan_1,
            "feb 1": row.feb_1,
            "mar 1": row.mar_1,
            "apr 1": row.apr_1,
            "may 1": row.may_1,
            "jun 1": row.jun_1,
            "jul 1": row.jun_1,
            "aug 1": row.aug_1,
            "sept 1": row.sept_1,
            "oct 1": row.oct_1,
            "nov 1": row.nov_1,
            "dec 1": row.dec_1
        }
        d.append(row_as_dict)
    return render_template("projects.html", data=d)


@app.route("/api", methods=["GET"])
def api_route():
    table = Covid19Table.query.all()
    d=[]
    for row in table:
        row_as_dict = {
            "country": row.country,
            "first case date": row.first_case_date,
            "jan 1": row.jan_1,
            "feb 1": row.feb_1,
            "mar 1": row.mar_1,
            "apr 1": row.apr_1,
            "may 1": row.may_1,
            "jun 1": row.jun_1,
            "jul 1": row.jun_1,
            "aug 1": row.aug_1,
            "sept 1": row.sept_1,
            "oct 1": row.oct_1,
            "nov 1": row.nov_1,
            "dec 1": row.dec_1
        }
        d.append(row_as_dict)
    return jsonify(d)

if __name__=='__main__':
    app.run(debug=True)