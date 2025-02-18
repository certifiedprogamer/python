def isThreeOfAKind(num_list: list):
    unique_nums = set(num_list)
    req_count = 3
    for i in unique_nums:
        num = num_list.count(i)
        if num >= req_count:
            return True
    return False


def isNumOfAKind(num_list: list, times: int):
    unique_nums = set(num_list)
    req_count = times
    for i in unique_nums:
        num = num_list.count(i)
        if num >= req_count:
            return True
    return False


def isFourInARow(num_list: list):
    num_list.sort()
    numb_in_a_row = num_list[0]
    numb_in_a_row2 = numb_in_a_row + 1
    times = 4
    count = 1
    for i in num_list:
        if i == numb_in_a_row:
            pass
        elif i == numb_in_a_row2:
            numb_in_a_row = i
            numb_in_a_row2 = numb_in_a_row + 1
            count += 1
            if count == times:
                return True
        else:
            numb_in_a_row = i
            numb_in_a_row2 = numb_in_a_row + 1
            count = 1
    return False


def isNumInARow(num_list: list, times: int):
    num_list.sort()
    numb_in_a_row = num_list[0]
    numb_in_a_row2 = numb_in_a_row + 1
    count = 1
    for i in num_list:
        if i == numb_in_a_row:
            pass
        elif i == numb_in_a_row2:
            numb_in_a_row = i
            numb_in_a_row2 = numb_in_a_row + 1
            count += 1
            if count == times:
                return True
        else:
            numb_in_a_row = i
            numb_in_a_row2 = numb_in_a_row + 1
            count = 1
    return False


g = isThreeOfAKind([3, 3, 4, 6, 7, 8, 8, 8])
print(g)
g = isNumOfAKind([3, 3, 4, 6, 7, 8, 8, 8], 2)
print(g)
g = isFourInARow([3, 3, 3, 3, 4, 5, 6, 7, 8, 8, 8])
print(g)
g = isNumInARow([3, 3, 4, 8, 6, 7, 8, 8], 4)
print(g)
