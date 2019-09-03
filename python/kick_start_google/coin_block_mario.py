import pytest

def collect(blocks):
    total = 0
    for i in range(1, blocks+1):
        base = i
        if i % 3 == 0:
            if i % 15 != 0:
                base *= 2
        if i % 5 == 0:
            if i % 15 != 0:
                base *= 3
            elif i % 15 == 0:
                base = i * 10

        total += base

    return total

def test_collect():
    assert collect(15) == 315
    assert collect(1000) == 1
