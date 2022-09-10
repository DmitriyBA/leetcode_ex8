array_number = [1, 1, 2, 2]


def array_number_plus(array_number: list) -> list:
    dict_number = {}
    iter_k = 0

    for iter_i in range(len(array_number)):
        for iter_j in range(len(array_number)):
            if array_number[iter_i] == array_number[iter_j]:
                iter_k += 1
        dict_number[array_number[iter_i]] = iter_k
        iter_k = 0

    new_array_number = []

    for key_number in dict_number:
        if dict_number[key_number] >= 2:
            new_array_number.append(key_number)

    new_array_number.sort()

    if (len(new_array_number) < len(array_number)):
        iter_len_array_number = len(array_number) - len(new_array_number)
        count = 0
        while count != iter_len_array_number:
            new_array_number.append('_')
            count += 1

    return new_array_number


print(array_number_plus(array_number))
