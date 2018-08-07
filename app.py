from flask import Flask, abort, request, jsonify
from api_key import API_KEY
import node_check

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check():
    if not request.json or 'api_key' not in request.json:
        abort(400)
    if request.json['api_key'] != API_KEY:
        abort(401)
    #print('\n'+str(request.json)+'\n')
    resp = reader(request.json)
    return jsonify(resp)

def reader(r):
    response = dict()
    for text in r:
        if text == "api_key":
            pass
        else :
            response[text] = text
    return response


if __name__ == '__main__':
    app.run()
