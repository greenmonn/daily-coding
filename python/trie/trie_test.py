import unittest


class Node:
    def find(self, key):
        pass


class BranchNode(Node):
    def __init__(self, value = 0):
        self.value = value
        self.children = [None] * 16

    def put(self, key, value):
       newNode = BranchNode()
       newNode.children = self.children

       if not key:
           return newNode.setValue(value)

       newNode.children[key[0]] = BranchNode().put(key[1:], value)

       return newNode.setValue(self.value)

    def find(self, key):
        if not key:
            return self

        if self.children[key[0]] is not None:
            return self.children[key[0]].find(key[1:])

    def setValue(self, value):
        self.value = value

        for i in self.children:
            if i != None:
                return self

        if value is not 0:
            return LeafNode(value)

        return None


class LeafNode(Node):
    def __init__(self, value = 0):
        self.value = value

    def find(self, key):
        if not key:
            return self


class State:
    def __init__(self):
        self.trieRoot = BranchNode()

    def get(self, key):
        if len(key) == 0:
            return 0

        node = self.trieRoot.find(key)
        
        if node is None:
            return 0
        
        return node.value

    def set(self, key, value):
        newState = State()

        newState.trieRoot = self.trieRoot.put(key, value)
        
        return newState
    
class NodeTest(unittest.TestCase):
    keys = [[0xa], [0xb]]
    values = [1, 2]

    def test_find_not_existing_node(self):
        node = BranchNode()
        
        self.assertEqual(None, node.find(self.keys[0]))

    def test_find_self_node(self):
        node = BranchNode()
        node.value = 1

        receivedNode = node.find([])

        self.assertEqual(node.value, receivedNode.value)

    def test_find_child_node(self):
        node = BranchNode()
        node.value = 1

        childNode = BranchNode()
        childNode.value = 2

        node.children[0xa] = childNode

        receivedNode = node.find([0xa])

        self.assertEqual(childNode.value, receivedNode.value)

    def test_put_and_find(self):
        node = BranchNode()

        key = self.keys[0]
        value = self.values[0]

        newNode = node.put(key, value)

        self.assertEqual(value, newNode.find(key).value)

    def test_put_multiple_keys(self):
        node = BranchNode()
        node = node.put(self.keys[0], self.values[0])
        node = node.put(self.keys[1], self.values[1])

        self.assertEqual(self.values[0], node.find(self.keys[0]).value)
        self.assertEqual(self.values[1], node.find(self.keys[1]).value)

    def test_find_child_from_parent(self):
        childValue = 1
        
        key = [0xa, 0xb]

        node = BranchNode()
        
        node.children[key[1]] = BranchNode(childValue)

        parent = BranchNode()
        parent.children[key[0]] = node

        self.assertEqual(childValue, parent.find(key).value)

    def test_put_longer_key(self):
        node = BranchNode()

        key = [0x1, 0x2]
        value = 1

        newNode = node.put(key, value)

        self.assertEqual(value, node.find(key).value)

    def test_never_put_node_of_value_0(self):
        node = BranchNode()

        key = self.keys[0]

        node = node.put(key, 0)

        self.assertEqual(None, node)
    
    def test_exclude_only_leaf_node(self):
        node = BranchNode(1)

        key = self.keys[0]

        node = node.put(key, 0)

        self.assertEqual(None, node.find(key))

    def test_type_of_node_at_the_end(self):
        node = BranchNode()
        
        key = self.keys[0]
        node = node.put(key, 1)

        self.assertEqual(LeafNode, type(node.find(key)))


class StateTest(unittest.TestCase):
    keys = [[0xa], [0xb]]
    values = [1, 2]

    def test_state_set_and_get(self):
        state0 = State()
        
        key = self.keys[0]
        value = self.values[0]

        state1 = state0.set(key, value)
        
        self.assertEqual(value, state1.get(key))

    def test_get_empty_key(self):
        self.assertEqual(0, State().get([]))

    def test_get_unexisting_state(self):
        self.assertEqual(0, State().get([0xc]))

    def test_state_with_multiple_keys(self):
        state0 = State()

        state1 = state0.set(self.keys[0], self.values[0])
        state2 = state1.set(self.keys[1], self.values[1])

        self.assertEqual(self.values[0], state2.get(self.keys[0]))
        self.assertEqual(self.values[1], state2.get(self.keys[1]))
