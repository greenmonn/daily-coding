import pytest
import collections

def rectangle(points):
    x_list = []
    y_list = []

    for x, y in points:
        x_list.append(x)
        y_list.append(y)

    print(collections.Counter(x_list))



def test_rectangle():
    assert rectangle([[1, 4], [3, 4], [3, 10]]) == [1, 10]
