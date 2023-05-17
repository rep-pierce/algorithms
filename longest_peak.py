def longestPeak(array):
    i = 1
    large_count = 0

    while i < len(array) - 1:
        is_peak = array[i] > array[i-1] and array[i] > array[i+1]
        if not is_peak:
            i += 1
            continue
            
        left_index = i - 1
        while left_index >= 1 and array[left_index] > array[left_index - 1]:
            left_index -= 1

        right_index = i + 1
        while right_index < len(array) - 1 and array[right_index] > array[right_index + 1]:
            right_index += 1

        current_peak_length = right_index - (left_index - 1)
        if current_peak_length > large_count:
            large_count = current_peak_length

        i = right_index

    return large_count