import pytest
import itertools

def root(number):
    sum = 0
    for s in str(number):
        sum += s
    return sum


pairs = itertools.combinations(range(1, 9), 1)
print(list(pairs))