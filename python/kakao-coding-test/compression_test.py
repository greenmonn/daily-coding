import pytest

def compress(string, unit):
    compressed = ''
    current_unit = string[:unit]
    current_number = 1

    index = unit
    while index < len(string):
        s = string[index:index+unit]
        if s == current_unit:
            current_number += 1
        
        else:
            if current_number == 1:
                compressed += current_unit
            else:
                compressed += str(current_number) + current_unit
            
            current_unit = s
            current_number = 1
        
        index += unit
    
    if current_number == 1:
        compressed += current_unit
    else:
        compressed += str(current_number) + current_unit
    
    return compressed

def find_shortest_compression(string):
    max_unit = len(string)

    min_length = 10000
    for unit in range(1, max_unit+1):
        length = len(compress(string, unit))
        if length < min_length:
            min_length = length

    return min_length

def test_compress():
    assert compress('aabbaccc', 1) == '2a2ba3c'
    assert compress('abcabcdede', 3) == '2abcdede'
    assert len(compress("abcabcabcabcdededededede", 6)) == 14

def test_shortest_compression():
    assert find_shortest_compression("aabbaccc") == 7
    assert find_shortest_compression("ababcdcdababcdcd") == 9
    assert find_shortest_compression("abcabcdede") == 8
    assert find_shortest_compression("abcabcabcabcdededededede") == 14
    assert find_shortest_compression("xababcdcdababcdcd") == 17
