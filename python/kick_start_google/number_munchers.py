import pytest
import itertools


def is_in_ascending_order(number):
    digits = str(number)

    prev = -1
    for d in digits:
        if int(d) <= prev:
            return False
        prev = int(d)
    
    return True

def test_ascending():
    assert is_in_ascending_order(1456) == True
    assert is_in_ascending_order(25) == True
    assert is_in_ascending_order(1000) == False


count = 0

pairs = []

for i in range(1, 1000):
    for j in range(1, 1000):
        pairs.append((i, j))

# print(pairs)

for n1, n2 in pairs:
    result = n1 * n2
    if result >= 1000:
        continue

    if is_in_ascending_order(result):
        if n1 == n2:
            count += 2
        else:
            count += 1


print(count/2)
