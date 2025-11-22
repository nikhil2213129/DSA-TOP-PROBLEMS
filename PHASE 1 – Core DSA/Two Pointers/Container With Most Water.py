def max_water(heights):
    left_index = 0
    right_index = len(heights) - 1
    max_area = 0
    while left_index < right_index:
        width = right_index - left_index
        left_height = heights[left_index]
        right_height = heights[right_index]
        min_height = min(left_height, right_height)
        area = width * min_height
        max_area = max(area, max_area)
        if left_height <= right_height:
            left_index += 1
        else:
            right_index -= 1
    return max_area
