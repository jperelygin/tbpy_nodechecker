from flask import Flask, abort, request, jsonify
from api_key import API_KEY, TG_KEY, GROUP
import json

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
    all_online = True # trigger of online nodes
    response = dict()
    for title in r:
        if title == "api_key":
            pass
        elif r[title] == "offline":
            all_online = False
        response[title] = title
    if all_online == False:
        send_mess(response) # sends message to group if any node is offline
    return response # a dict without api_key

def send_mess(resp: dict):
    text = json.JSONEncoder().encode(resp)
    data = {"chat_id":GROUP, "text":text} # GROP from api_key
    request.post('https://api.telegram.org/bot'+TG_KEY+'/sendMessage',data=data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
