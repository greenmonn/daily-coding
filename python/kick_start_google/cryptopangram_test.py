import pytest


def test_find_used_primes():
    used_primes, single_prime_sequence = find_used_primes(103, [217, 1891], 2)
    assert [7, 31, 61] == single_prime_sequence
    assert [7, 31, 61] == used_primes

    used_primes, single_prime_sequence = find_used_primes(103, [217, 1891, 427], 3)
    assert [7, 31, 61, 7] == single_prime_sequence
    assert [7, 31, 61] == used_primes

    used_primes, single_prime_sequence = find_used_primes(
        103, [217, 1891, 1891], 3)
    assert [7, 31, 61, 31] == single_prime_sequence
    assert [7, 31, 61] == used_primes


def test_get_primes():
  assert [2, 3, 5, 7, 11, 13, 17, 19] == get_primes(19)

def get_primes(N):
  primes = [2]

  for number in range(3, N+1):
    isPrime = True
    for divisor in primes:
      if number % divisor == 0:
        isPrime = False
        break
    if isPrime:
      primes.append(number)
  
  return primes
      
def test_get_common_divisor():
  assert 31 == get_common_divisor(217, 1891, [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
  assert 1973 == get_common_divisor(3292937, 175597, get_primes(10000))

def get_common_divisor(A, B, candidates):
  for number in candidates:
    if A % number == 0 and B % number == 0:
      return number

  return 0

def find_used_primes(N, ciphertexts, length):
  primes_candidates = get_primes(N)

  single_prime_sequence = [0] * (length+1)

  found_index = -1
  for i in range(length - 1):
    if ciphertexts[i] != ciphertexts[i+1]:
      divisor = get_common_divisor(ciphertexts[i], ciphertexts[i+1], primes_candidates)
      found_index = i+1
      single_prime_sequence[found_index] = divisor
      break
  
  for i in range(found_index + 1, length + 1):
    single_prime_sequence[i] = ciphertexts[i-1] // single_prime_sequence[i-1]

  for i in range(found_index - 1, -1, -1):
    single_prime_sequence[i] = ciphertexts[i] // single_prime_sequence[i+1]


  used_primes = list(set(single_prime_sequence))
  used_primes.sort()

  return used_primes, single_prime_sequence

def decrypt(single_prime_sequence, used_primes):
  alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

  string_map = dict((used_primes[i], alphabets[i]) for i in range(len(used_primes)))

  plaintext = []

  for prime in single_prime_sequence:
    plaintext.append(string_map[prime])
  
  return ''.join(plaintext)

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        N, L = map(int, input().split(' '))

        ciphertexts = list(map(int, input().split(' ')))

        used_primes, single_prime_sequence = find_used_primes(N, ciphertexts, L)

        plaintext = decrypt(single_prime_sequence, used_primes)

        print("Case #{}: {}".format(i+1, plaintext))
