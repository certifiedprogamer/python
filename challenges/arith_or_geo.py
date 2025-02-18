def arithgeo(sequence: list):
    for i in sequence:
        if i == 0:
            return -1
    if sequence[0] == sequence[1]:
        return -1
    elif check_arith(sequence) == True:
        return "Arithmetic"
    elif check_geo(sequence) == True:
        return "Geometric"
    else:
        return -1


def check_arith(sequence: list):
    arith_num = sequence[1] - sequence[0]
    for i in range(len(sequence)):
        g = i + 1
        try:
            if sequence[g] - sequence[i] != arith_num:
                return False
        except:
            pass
    return True


def check_geo(sequence: list):
    geo_num = sequence[1] / sequence[0]
    for i in range(len(sequence)):
        g = i + 1
        try:
            if sequence[g] / sequence[i] != geo_num:
                return False
        except:
            pass
    return True


arith_sequence = [-2, -4, -6, -8]
geo_sequence = [2, 6, 18, 54, 162]
nums = [2, 2, 2, 2, 2, 2]

print(arithgeo(arith_sequence))
print(arithgeo(geo_sequence))
print(arithgeo(nums))
