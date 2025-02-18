arr = [4, 5, 1, 2, 7]


def ElementMerger(arr):
    if len(arr) <= 1:
        return arr
    newarr = []
    for i in range(len(arr) - 1):
        newarr.append(abs(arr[i] - arr[i+1]))
    # print(newarr)
    return ElementMerger(newarr)


print(ElementMerger(arr))
