ACCEPTING = 1
REJECTING = -1
NORMAL = 0

currentNode = None

class Node:
    def __init__(self, name, a):
        self.name = name
        self.links = dict()
        self.state = a

    def getName(self):
        return self.name

    def getNode(self, c):
        return self.links[c]

    # Add a transition to node 'n' using character 'c'.
    def addLink(self, c, n):
        self.links[c] = n

    # Check character 'c' for a transition.
    def hasLink(self, c):
        return c in self.links.keys()

    def accepts(self):
        return self.state == ACCEPTING

    def rejects(self):
        return self.state == REJECTING

    def getState(self):
        if self.accepts():
            print("STATE: Accepting")
        elif self.rejects():
            print("STATE: Rejecting")
        else:
            print("STATE: Normal")


# If a transition exists for the character 'c' on node 'n', transition to that node.
def transition(n, c):
    if n.hasLink(c):
        return n.getNode(c)
