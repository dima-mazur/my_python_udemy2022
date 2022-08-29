def to_arabian(string: str):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000
             }

    result = []
    result2 = []

    for i in string:
        if i in roman:
            result.append(roman[i])

    if len(result) % 2 != 0:
        result.append(0)

    i = 0
    while i <= len(result):
        try:
            if result[i] >= result[i + 1]:
                result2.append(result[i])
                i += 1
            elif result[i] < result[i+1]:
                result2.append(result[i+1] - result[i])
                i += 2

        except IndexError:
            result2.append(result[i])
            break

    return sum(result2)


print(to_arabian('MCMXCV'))