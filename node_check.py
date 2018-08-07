import nodes
import requests
from api_key import API_KEY, adress

def send(nodes: dict) -> str:
    """ Sends a request with <dict> of nodes and node states to flask app.
    """
    data = dict()
    data["api_key"] = api_key # adds required api_key to the data <dict>
    for node in nodes: # adds all nodes and their states to the data <dict>
        data[node] = node
    r = requests.post(adress, data=data) # adress == flask app adress
    print(r.text) # response

def check() -> dict:
    """ Checks all the nodes from nodes.list_of_nodes and returns <dict> of nodes and their states
    """
    resp = dict()
    for node in nodes.list_of_nodes:
        state = node.check_state(node.path)
        resp[node.name] = state
    return resp