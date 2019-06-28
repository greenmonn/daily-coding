import pytest

# TODO: Dijkstra, or O(N) solution


def test_volume_of_rainwater():
    assert volume_of_rainwater(
        [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]) == 15
    assert volume_of_rainwater(
        [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 3]) == 16
    assert volume_of_rainwater(
        [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0


def is_all_heights_identical(heights):
    height = heights[0]
    for h in heights:
        if h != height:
            return False
    return True


def volume_of_rainwater(heights):
    previous_bar = 0
    previous_bar_index = -1
    passed_heights = []
    total_volume = 0
    body_volumes = []
    for index, height in enumerate(heights):
        if height >= previous_bar:
            current_body_volume = (
                index - previous_bar_index - 1) * previous_bar - sum(passed_heights)
            total_volume += current_body_volume
            body_volumes.append(current_body_volume)
            previous_bar_index, previous_bar = index, height
            passed_heights = []
        else:
            passed_heights.append(height)

    if len(passed_heights) != 0:
        while len(passed_heights) > 1:
            if is_all_heights_identical(passed_heights):
                break

            max_height = max(passed_heights)
            max_index = passed_heights.index(max_height)
            current_body_volume = max_height * \
                max_index - sum(passed_heights[:max_index])
            passed_heights = passed_heights[max_index + 1:]

            body_volumes.append(current_body_volume)
            total_volume += current_body_volume

    return total_volume
