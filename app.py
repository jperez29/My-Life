from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ds_course_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Covid19(db.Model):
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


@app.route('/api', methods=['GET'])
def get_data():
    table = Covid19.query.all()
    return jsonify(table)


if __name__=='__main__':
    app.run(debug=True)