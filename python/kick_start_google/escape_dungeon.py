import pytest


def is_escapable(string):
    num_keys = 0
    for s in string:
        if s == '&':
            num_keys += 1
        elif s == '|':
            if num_keys > 0:
                num_keys -= 1
            else:
                return '0'

    return '1'


def test_is_escapable():
    assert is_escapable('&|&|&&|&|||') == '0'
    assert is_escapable('&&|&|') == '1'


r = [0] * 10

r[0] = is_escapable(
    '&|&|&|&&&|&|||&&&|&&|||&||&||&|&&|||||&|&|&&&&||||&&&|&|&&||||&&&|&&|||&&|&&&|||')

r[1] = is_escapable(
    '&&||&&&|&||&&&||&|||&&&|&||&&&|||||||&&&&|&&||&||&&|||&|&&&&&&|&|||&&||&|||&&|&|')

r[2] = is_escapable(
    '&|&|&&&&|&&&|&|||&&&||||||&&|&&&&|&&|&&&|&||&|&&|||&&&|&&&&&|&&&&&&||&|&&||&&|&&')

r[3] = is_escapable(
    '&|&&|||||&&&&||&&&||||&&&&|||||&||&|&|&|&||&|&&|&|&||||||&&||||||&|&&|&&&&&&||||')

r[4] = is_escapable(
    '&||&&||&|&||&|&|&&&&&||&&&&&&&||&&|&&||&|&|&|&&&&|&&|||||&&&||||&||&&&|||&&&|||&')

r[5] = is_escapable(
    '&&&&|&&|&|&&&|||&&&||||&|&|&&|&&&|&&&|||&|&&&|&|&&&|&&|||&|&|&|&|&&|&&&&|&&|||||')

r[6] = is_escapable(
    '&&|&|&||||&||||&&|||&&&|||&&||&|&|||&||&&&||||&|&|&&|&&&|&&&|&&|&||&|&&&|&&&||||')

r[7] = is_escapable(
    '&&&||||&&&&&|&|&&&&||&&|&|||&&&||&&&&|&&&|&&|&||&|&&|&||||&|&|||&|&||&||&|&&&&||')

r[8] = is_escapable(
    '&&&|&&&||&||&||&|&|&||&&&|||||&|&&||&&&|||&|||||||&&|||&&||&|&|&|&|&&&&&&||&|&||')

r[9] = is_escapable(
    ' &&||&&|&&|||||&&&||&|&|&|&|&||&|&||&&&&||||&|&|||||||&|&&&&|&&|||||&|&||&&&||&|&')

result = ''
for s in r:
    result += s

print(result)