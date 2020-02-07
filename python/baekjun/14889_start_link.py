import pytest

import itertools


def test_solution():
    S = [[0, 1, 2, 3], [4, 0, 5, 6], [7, 1, 0, 2], [3, 4, 5, 0]]
    N = 4
    assert solution(S, N) == 0


def get_sum_abilities(S, N):
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += S[i][j]
    return sum


def solution(S, N):
    num_members = N // 2

    teams = range(N)

    start_teams_candidates = itertools.combinations(range(N), num_members)

    min_ability_diff = 10*10

    def calc_abilities(members):
        sum = 0
        for member in members:
            other_members = list(members[:])
            other_members.remove(member)
            for other in other_members:
                sum += S[member][other]
        return sum
    all_members = set(range(N))
    for start_team_members in start_teams_candidates:

        link_team_members = list(all_members - set(start_team_members))

        start_team_ability = calc_abilities(start_team_members)
        link_team_ability = calc_abilities(link_team_members)

        diff = abs(start_team_ability - link_team_ability)

        if diff < min_ability_diff:
            min_ability_diff = diff

    return min_ability_diff


if __name__ == '__main__':
    N = int(input())

    S = []
    for i in range(N):
        row = list(map(int, input().split(' ')))
        S.append(row)

    print(solution(S, N))
