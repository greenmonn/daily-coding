import pytest
import sys

def read_two_integers(input):
  numbers = list(map(int, input.split(' ')))
  return numbers[0], numbers[1]

class Guesser:
  def __init__(self, a, b):
    self.range = (a+1, b+1)  # a <= p < b
    self.currentGuess = 0

  def guess(self):
    guess = sum(self.range) // 2
    self.currentGuess = guess
    return guess

  def getFeedback(self, message):
    if (message == 'TOO_SMALL'):
      self.range = (self.currentGuess+1, self.range[1])

    elif (message == 'TOO_BIG'):
      self.range = (self.range[0], self.currentGuess)

if __name__ == "__main__":
  t = int(input())

  for i in range(t):
      a, b = read_two_integers(input())
      n = int(input())

      guesser = Guesser(a, b)

      for j in range(n):
          guess = guesser.guess()
          print(guess)

          sys.stdout.flush()

          feedback = input()

          if (feedback == 'CORRECT'):
            break

          guesser.getFeedback(feedback)


def test_read_two_integers():
  a = 1
  b = 2
  i1, i2 = read_two_integers(str(a) + ' ' + str(b))
  assert (a, b) == (i1, i2)

def test_initial_guess():
  guesser = Guesser(2, 3)
  assert 3 == guesser.guess()

def test_guess_after_hint():
  guesser = Guesser(2, 5)
  initialGuess = guesser.guess()
  if (initialGuess == 4):
    guesser.getFeedback('TOO_BIG')
    assert 3 == guesser.guess()
