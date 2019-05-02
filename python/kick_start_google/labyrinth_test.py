import pytest

def find_original_path(N, P):
  count_mine = {'S': 0, 'E': 0}
  count_lydia = {'S': 0, 'E': 0}

  path = []

  for i in range(len(P)):
    direction = 'S' if P[i] == 'E' else 'E'

    path.append(direction)
    count_mine[direction] += 1

    count_lydia[P[i]] += 1
  
  return ''.join(path)

def test_find_original_path():
  assert 'ES' == find_original_path(2, 'SE')
  assert 'SSEEESES' == find_original_path(5, 'EESSSESE')
  assert 'SSSSEEEE' == find_original_path(5, 'EEEESSSS')
  assert 'EEEESSSS' == find_original_path(5, 'SSSSEEEE')
  
if __name__ == "__main__":
  T = int(input())

  for i in range(T):
    N = int(input())
    P = input()

    path = find_original_path(N, P)

    print("Case #{}: {}".format(i+1, path))

      
