import nodes

def check():
    for node in nodes.list_of_nodes:
        state = node.check_state(node.path)
        print("node: " + str(node.name) + "\nstate: " + state)

if __name__ == '__main__':
    check()