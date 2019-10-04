import pytest

class Node():
    def __init__(self):
        self.value = None
        self.children = [None] * 26
    
    def put(self, s):
        if len(s) == 0:
            self.value = True
        else:
            index = ord(s[0]) - ord('a')
            if self.children[index] == None:
                child = Node()
            else:
                child = self.children[index]
            
            child.put(s[1:])
            self.children[index] = child

    def find(self, s):
        if len(s) == 0:
            return self

        else:
            index = ord(s[0]) - ord('a')
            if self.children[index] == None:
                return None
            else:
                return self.children[index].find(s[1:])

    def find_all_children(self, depth):
        count = 0
        for child in self.children:
            if child == None:
                continue
            if depth == 1:
                if child.value == True:
                    count += 1
            else:
                count += child.find_all_children(depth-1)
        return count



def find(words, queries) -> list:
    words_tree = Node()
    reverse_words_tree = Node()

    for word in words:
        words_tree.put(word)
        word = word[::-1]
        reverse_words_tree.put(word)
        
    result = []
    for query in queries:
        if query[0] == '?':
            reverse_query = query[::-1]
            result.append(find_query(reverse_words_tree, reverse_query))
        else:
            result.append(find_query(words_tree, query))
    
    return result

def find_query(words_tree, query):
    prefix = query[:query.index('?')]
    unknown_count = len(query) - len(prefix)

    node = words_tree.find(prefix)

    if node == None:
        return 0
    
    return node.find_all_children(unknown_count)


def test_find_children():
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    words_tree = Node()

    for word in words:
        words_tree.put(word)

    assert words_tree.find_all_children(5) == 5


def test_node():
    node = Node()
    node.put('fro')
    node.put('frodo')

    assert node.find('fro').value == True
    assert node.find('fr') != None
    assert node.find('fr').value == None


def test_find_query():
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    words_tree = Node()

    for word in words:
        words_tree.put(word)

    assert find_query(words_tree, '?????') == 5


def test_find():
    assert find(["frodo", "front", "frost", "frozen", "frame", "kakao"], [
           "fro??", "????o", "fr???", "fro???", "pro?"]) == [3, 2, 4, 1, 0]
