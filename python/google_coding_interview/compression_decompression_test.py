import pytest


def test_decompress():
    assert 'a' * 10 == decompress('10[a]')

    assert ('abc' * 3) + (4 * 'ab') + 'c' == decompress('3[abc]4[ab]c')

    assert 'aaabaaab' == decompress('2[3[a]b]')


def test_find_most_outer_brackets():
    assert [1, 7] == find_most_outer_brackets('2[3[a]b]')
    assert [2, 4] == find_most_outer_brackets('10[a]')


def find_most_outer_brackets(string):
    stack = []
    for index, char in enumerate(string):
        if char == '[':
            stack.append(index)
        if char == ']':
            if len(stack) > 1:
                stack.pop()
            else:
                stack.append(index)
    return stack


def decompress(string):
    indexes = find_most_outer_brackets(string)
    if len(indexes) != 2:
        return string

    before, after = indexes

    repeat_string = string[before+1:after]
    count = int(string[:before])

    return decompress(repeat_string) * count + decompress(string[after+1:])
