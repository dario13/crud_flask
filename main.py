from flask import Flask, request, jsonify, make_response, request
#from person import addPerson, getPeople
from person import addPerson, getPeople

app = Flask(__name__)

@app.route('/person', methods=['GET', 'POST'])
def index():

    if(request.method == 'POST'):
        body_request = request.json
        addPerson(name = body_request['name'], age= body_request['age'])
        return make_response(jsonify({'Respond':'Created'}), 200)
    
    if(request.method == 'GET'):
        people = getPeople()
        return make_response(jsonify(people), 200)

if __name__ == "__main__":
    app.run(debug=True)