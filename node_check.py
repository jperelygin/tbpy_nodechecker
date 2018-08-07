import nodes
import requests
from api_key import API_KEY, adress

def send(nodes):
    data = dict()
    data["api_key"] = api_key
    for node in nodes:
        data[node] = node
    r = requests.post(adress, data=data)
    print(r.text)

def check():
    resp = dict()
    for node in nodes.list_of_nodes:
        state = node.check_state(node.path)
        print("node: " + str(node.name) + "\nstate: " + state)
        resp[node.name] = state
    return resp