def number_of_titles(titles):
    alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    occurrences = dict((key, False) for key in alphabets)

    for title in titles:
        occurrences[title[0]] = True

    count = 0
    for alphabet in occurrences:
        occurrence = occurrences[alphabet]
        if not occurrence:
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

