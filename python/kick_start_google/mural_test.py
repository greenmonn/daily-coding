import pytest

# Compute maximum total beauty score

def max_total_score(scores, total_length):
  length = (total_length + 1) // 2

  max_sum = prev_sum = sum_of_digits_in_subsequence(scores, 0, length)

  for i in range(1, total_length - length + 1):
    current_sum = prev_sum - int(scores[i - 1]) + int(scores[i + length - 1])
    prev_sum = current_sum
    if (current_sum > max_sum):
      max_sum = current_sum

  return max_sum

def sum_of_digits_in_subsequence(scores, start, length):
  sum = 0;
  for i in range(start, start + length):
    sum += int(scores[i])
  return sum;

def test_sum_of_digits():
  assert 10 == sum_of_digits_in_subsequence('1234', 0, 4)

def test_max_total_score():
  s1 = '1332'
  s2 = '4321'
  
  assert 6 == max_total_score(s1, 4)
  assert 7 == max_total_score(s2, 4)


if __name__ == "__main__":
  T = int(input())

  for i in range(T):
    N = int(input())
    scores = input()

    print('Case #{n}: {score}'.format(n=i+1, score=max_total_score(scores, N)))
