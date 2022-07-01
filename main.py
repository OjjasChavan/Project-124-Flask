from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        'contact': '2824812472',
        'name': 'Kelly',
        'id' : 1,
        'done' : False
    },
    {
        'contact': '1284214211',
        'name': 'Elliot',
        'id': 2,
        'done' : False
    },
    {
        'contact' : '7020874780',   
        'name' : 'Dominika',
        'id' : 3,
        'done' : False
    },
    {
        'contact' : '1240214211',
        'name' : 'Ashley',
        'id' : 4,
        'done' : False
    }
]

@app.route("/add-data", methods=["POST"])

def app_tasks():
    if not request.json:
        return jsonify({
            'status' : 'error',
            'message' : 'please provide the data'
        }, 400)

    contact = {
        'Contact' : request.json.get('Contact', ""),
        'Name': request.json['Name'],
        'id' : tasks[-1]['id'] + 1, 
        'done' : False
    } 
    data.append(contact)
    return jsonify({
        'status' : 'success',
        'message' : 'task added successfully'
    })

if (__name__ == "__main__"):
    app.run(debug=True)