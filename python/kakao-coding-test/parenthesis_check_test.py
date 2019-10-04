import pytest

def test_fix():
    assert fix_parenthesis('(()())()') == '(()())()'
    assert fix_parenthesis(')(') == '()'
    assert fix_parenthesis("()))((()") == "()(())()"


def test_is_balanced():
    assert is_balanced(')(') == True
    

def test_is_correct():
    assert is_correct('()') == True
    assert is_correct(')(') == False
    assert is_correct('(()))(') == False

def is_balanced(string):
    count_left = 0
    count_right = 0

    for s in string:
        if s == '(':
            count_left += 1
        elif s == ')':
            count_right += 1

    return count_left == count_right

def is_correct(string):
    count = 0

    for s in string:
        if s == '(':
            count += 1
        elif s == ')':
            if count > 0:
                count -= 1
            else:
                return False

    return True

def test_result():
    assert reverse(')(') == '()'
    assert reverse('))((') == '(())'
 
def reverse(string):
    result = ''
    for s in string:
        if s == '(':
            result += ')'
        elif s == ')':
            result += '('
    return result

def fix_parenthesis(string):
    if len(string) == 0:
        return string

    # find u
    index = 0
    u = ''
    while index < len(string):
        if is_balanced(string[:index+1]):
            u = string[:index+1]
            break
        index += 1

    if is_correct(u):
        return u + fix_parenthesis(string[index+1:])
    else:
        return '(' + fix_parenthesis(string[index+1:]) + ')' + reverse(u[1:-1])

    return string
