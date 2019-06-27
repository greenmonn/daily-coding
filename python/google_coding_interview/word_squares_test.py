import pytest

def test_is_word_square():
    assert True == is_word_square(['BALL', 'AREA', 'LEAD', 'LADY'])
    assert False == is_word_square(['AREA', 'BALL', 'DEAR', 'YARD'])

def test_is_word_square(): 
    assert find_word_squares(['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD']) == [
        ['BALL', 'AREA', 'LEAD', 'LADY'], ['LADY', 'AREA', 'DEAR', 'YARD']]

def find_word_squares(words_list):
    K = len(words_list[0])
    possible_word_squares = []
    for i, word in enumerate(words_list): # 이 word가 첫번째 단어가 될 때
        word_dict = {0: [word]}
        
        remaining_words = words_list[:]
        remaining_words.remove(word)
        for index in range(1, len(word)):
            letter = word[index]

            possible_words = []
            
            for w in remaining_words:
                if w[0] == letter:
                    possible_words.append(w)
            
            word_dict[index] = possible_words

        candidates = list(map(lambda x: [x], word_dict[0]))
        for i in range(1, K):
            new_candidates = []
            possible_words = word_dict[i]
            for candidate in candidates:
                for word in possible_words:
                    if word not in candidate:
                        new_candidates.append(candidate + [word])
            candidates = new_candidates


        for candidate in candidates:
            if is_word_square(candidate):
                possible_word_squares.append(candidate)

        




    return possible_word_squares

def is_word_square(sequence):
    K = len(sequence)

    for index, word in enumerate(sequence):
        if len(word) != K:
            return False
        
        for i in range(K):
            if word[i] != sequence[i][index]:
                return False
    
    return True
