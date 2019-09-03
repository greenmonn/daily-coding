import pytest


def minimum_sugar_content(all_node_num, w1_edge_num, black_edges):
    edges_num = 0
    sugar_content = 0

    node_num = 1

    unconnected = list(map(lambda x: x+1, range(all_node_num)))
    unconnected.remove(node_num)

    while len(unconnected) > 0:
        has_black_edge = False

        for n1, n2 in black_edges:
            if n1 not in unconnected and n2 in unconnected:
                unconnected.remove(n2)
                has_black_edge = True
                break
            if n2 not in unconnected and n1 in unconnected:
                unconnected.remove(n1)
                has_black_edge = True
                break

        if has_black_edge == False:
            unconnected.pop()
            sugar_content += 2
        else:
            sugar_content += 1
            
    return sugar_content

    

def test_minimum_sugar_content():
    assert minimum_sugar_content(2, 1, [(1, 2)]) == 1

    assert minimum_sugar_content(3, 1, [(2, 3)]) == 3

    assert minimum_sugar_content(4, 3, [(1, 2), (1, 3), (1, 4)]) == 3

    assert minimum_sugar_content(5, 3, [(1, 2), (1, 3), (1, 4)]) == 5

    assert minimum_sugar_content(5, 2, [(2, 3), (1, 5)]) == 6

    assert minimum_sugar_content(5, 3, [(1, 2), (3, 4), (4, 5)]) == 5

    assert minimum_sugar_content(7, 6, [(1, 2), (2, 3), (3, 4), (2, 4), (5, 6), (6, 7)]) == 7

    assert minimum_sugar_content(5, 0, []) == 8






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
