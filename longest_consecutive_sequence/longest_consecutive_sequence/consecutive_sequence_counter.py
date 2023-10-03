def count_sequences(array: list[int]):
    max_length = 0
    array_set = set(array)
    for element in array_set:
        sequence_length = 0
        if (element-1) not in array_set:
            sequence_length = 1
        while (element:= (element+1)) in array_set: 
            sequence_length += 1
        max_length = max(sequence_length, max_length)

    return max_length
    