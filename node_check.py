import nodes
import requests

def send(response):
    pass

def check():
    resp = dict()
    for node in nodes.list_of_nodes:
        state = node.check_state(node.path)
        print("node: " + str(node.name) + "\nstate: " + state)
        resp[node.name] = state
    return resp