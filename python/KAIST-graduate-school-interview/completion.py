def solution(participant, completion):
    completion.sort()
    participant.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


if __name__ == '__main__':
    print(solution(['leo', 'kiki', 'leo'], ['kiki', 'leo']))
