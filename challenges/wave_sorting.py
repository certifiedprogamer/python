arr_ = [2, 0, 4, 1, 4, 1]


def WaveSorting(arr: list):
    alternator = False
    for i in range(len(arr) - 1):
        if alternator == False:
            if arr[i] > arr[i+1]:
                alternator = True
                pass
            else:
                return False
        elif alternator == True:
            if arr[i] < arr[i+1]:
                alternator = False
                pass
            else:
                return False
    return True


print(WaveSorting(arr_))
