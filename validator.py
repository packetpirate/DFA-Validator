# This program allows the user to set up a DFA and test strings against it.

from node import *

# Example DFA: Accepts strings following the format "(10)*", or repeating strings of "10".
q0 = Node("q0", ACCEPTING)
q1 = Node("q1", NORMAL)
q2 = Node("q2", ACCEPTING)
q3 = Node("q3", REJECTING)

q0.addLink('0', q3)
q0.addLink('1', q1)

q1.addLink('0', q2)
q1.addLink('1', q3)

q2.addLink('0', q3)
q2.addLink('1', q1)

currentNode = q0

# Example strings to test.
tests = ["",  # accept
         "10",  # accept
         "1010",  # accept
         "101",  # reject
         "11",  # reject
         "101010101010101010",  # accept
         "01010",  # reject
         "101011"]  # reject

for s in tests:
    print("STRING: " + s)
    currentNode = q0
    for c in s:
        currentNode = transition(currentNode, c)
        if currentNode.rejects():
            break
    currentNode.getState()
    print("FINAL NODE: " + str(currentNode.getName()))
    print()
