#WEEK 10, LAB #1

from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}

@app.route('/', methods=['GET'])
def get_records():
    return jsonify(students)

@app.route('/', methods=['POST'])
def create_record():
    added = {}
    for k,v in request.args.items():
        if not k in students.keys():
            added[k] = v
            students[k] = v
    return jsonify({"added": added, "current": students})

@app.route('/', methods=['DELETE'])
def delete_record():
    deleted = {}
    for k,v in request.args.items():
        try:
            students.pop(k)
            deleted[k] = v
        except:
            continue
    return jsonify({"deleted": deleted, "current": students})
                
if __name__ == '__main__':
    app.run(debug=True)
    
    
