import pytest

# TODO: How to interprete this as Dijkstra?


def test_volume_of_rainwater():
    assert volume_of_rainwater(
        [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]) == 15
    assert volume_of_rainwater(
        [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 3]) == 16
    assert volume_of_rainwater(
        [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0

def volume_of_rainwater(heights):
    total_volume = 0
    leftmax = {}
    rightmax = {}
    for index in range(len(heights)):
        r_index = len(heights) - 1 - index
        if index == 0:
            leftmax[index] = heights[index]
            rightmax[r_index] = heights[r_index]
        else:
            leftmax[index] = max(leftmax[index - 1], heights[index])
            rightmax[r_index] = max(rightmax[r_index + 1], heights[r_index])
    
    for index in range(len(heights)):
        water_height = min(leftmax[index], rightmax[index])
        if water_height > 0:
            total_volume += water_height - heights[index]
    
    return total_volume
