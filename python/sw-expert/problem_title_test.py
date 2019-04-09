import pytest

def test_number_of_titles():
  assert 2 == number_of_titles(['Air', 'Dad', 'Ear', 'Blue', 'Ace'])

  assert 1 == number_of_titles(['Snow_White', 'A_Problem', 'Another_Problem'])

def number_of_titles(titles):
  alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  occurences = dict((key, False) for key in alphabets)
  
  for title in titles:
    occurences[title[0]] = True

  count = 0
  for alphabet in occurences:
    occurence = occurences[alphabet]
    if occurence == False:
      break
    count += 1

  return count


if __name__ == "__main__":
  T = int(input())
  for i in range(T):
    N = int(input())

    titles = []
    for i in range(N):
      title = input()
      titles.append(title)

