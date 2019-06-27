import pytest

# Find longest word in dictionary that is a subsequence of a given string

# TODO: O(N+L) algorithm

def test_find_longest_word():
    string = "abppplee"
    words_set = ["able", "ale", "apple", "bale", "kangaroo"]

    assert "apple" == find_longest_word(string, words_set)

def find_longest_word(string, words_set):
    words_set = sorted(words_set, key=lambda x: -len(x))
    
    for word in words_set:
        string_compare = string[:]
        is_substring = True
        for c in word:
            index = string_compare.find(c)
            if index == -1:
                is_substring = False
                break
            
            string_compare = string_compare[index+1:]
        if is_substring:
            return word
    
    return None
