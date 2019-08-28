def test_decompress():
    assert decompress('3[abc]') == 'abcabcabc'
    assert decompress('3[2[a]]') == 'aaaaaa'
    assert decompress('3[abc]4[ab]c') == 'abcabcabcababababc'
    assert decompress('2[3[a]b]') == 'aaabaaab'
    assert decompress('10[a]') == 'a' * 10

def decompress(compressed):
    if '[' not in compressed:
        return compressed

    open_index = compressed.index('[')
    number = int(compressed[:open_index])
    start_index = open_index + 1
    end_index = find_closing_paranthesis(compressed[start_index:], start_index)

    remaining_string = compressed[end_index + 1:]

    string = compressed[start_index:end_index]
    return number * decompress(string) + decompress(remaining_string)

def test_find_closing_paranthesis():
    assert find_closing_paranthesis('2[a]]', 2) == 4 + 2

def find_closing_paranthesis(string, start_index):
    count = 0
    index = -1
    for i in range(len(string)):
        if string[i] == '[':
            count += 1
        if string[i] == ']':
            count -= 1
            if count == -1: # find the first close bracket make the count negative value
                index = i
                break

    return index + start_index