import pytest

# Compute maximum total beauty score

def max_total_score(scores):
  length = (len(scores) + 1) // 2
  max_sum = 0

  for i in range(len(scores) - length + 1):
    subsequence = scores[i:i+length]
    current_sum = sum(subsequence)
    if (current_sum > max_sum):
      max_sum = current_sum

  return max_sum


def test_max_total_score():
  scores = [1, 3, 3, 2]
  
  assert 6 == max_total_score(scores)


if __name__ == "__main__":
  T = int(input())

  for i in range(T):
    N = int(input())
    numbers = list(input())
    scores = [int(number) for number in numbers]

    print('Case #{n}: {score}'.format(n=i+1, score=max_total_score(scores)))
