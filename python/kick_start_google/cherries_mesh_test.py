import pytest


def minimum_sugar_content(all_node_num, w1_edge_num, pairs):
    edges_num = 0
    sugar_content = 0

    node_num = 1

    if len(pairs) > 0:
        node_num = pairs[0][0]

    unconnected = list(map(lambda x: x+1, range(all_node_num)))
    unconnected.remove(node_num)

    while len(unconnected) > 0:
        index = -1
        for i, (n1, n2) in enumerate(pairs):
            if n1 not in unconnected and n2 in unconnected:
                node_num = n2
                index = i
                break
            if n2 not in unconnected and n2 in unconnected:
                node_num = n1
                index = i
                break

        if index == -1:
            node_num = unconnected[0]

            sugar_content += 2
        else:
            sugar_content += 1
            
        unconnected.remove(node_num)

        edges_num += 1

    return sugar_content

    

def test_minimum_sugar_content():
    assert minimum_sugar_content(2, 1, [(1, 2)]) == 1

    assert minimum_sugar_content(3, 1, [(2, 3)]) == 3

    assert minimum_sugar_content(4, 3, [(1, 2), (1, 3), (1, 4)]) == 3

    assert minimum_sugar_content(5, 3, [(1, 2), (1, 3), (1, 4)]) == 5

    assert minimum_sugar_content(5, 2, [(2, 3), (1, 5)]) == 6

    assert minimum_sugar_content(5, 3, [(1, 2), (3, 4), (4, 5)]) == 5

    assert minimum_sugar_content(7, 6, [(1, 2), (2, 3), (3, 4), (2, 4), (5, 6), (6, 7)]) == 7





if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        N, M = map(int, input().split())

        pairs = []
        for j in range(M):
            n1, n2 = map(int, input().split())
            pairs.append((n1, n2))

        answer = minimum_sugar_content(N, M, pairs)
        
        print('Case #{}: {}'.format(i+1, answer))
