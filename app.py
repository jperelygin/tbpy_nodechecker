from flask import Flask, abort, request, jsonify
from api_key import API_KEY

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check() -> dict:
    """ Main method of the app. Gets a request and data from it
    """
    if not request.json or 'api_key' not in request.json: # BAD REQUEST if request is not json or missing api_key
        abort(400)
    if request.json['api_key'] != API_KEY: # api_key check
        abort(401)
    resp = reader(request.json)
    return jsonify(resp) # nodes dict in json

def reader(r: dict) -> dict:
    """ Request parser. Gets reed of the api_key in response dictionary
    """
    response = dict()
    for text in r:
        if text == "api_key":
            pass
        else :
            response[text] = text
    return response # a dict without api_key


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
