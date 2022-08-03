def check_sequence(lst):
    if len(lst) < 2:
        print('try again')
    else:
        result = []
        for position, i in enumerate(lst):
            try:
                if i < lst[position+1]:
                    result.append(1)
                elif i > lst[position+1]:
                    result.append(-1)
                else:
                    result.append(0)
            except IndexError:
                break

        if len(set(result)) == 1:
            return result[0]
        else:
            return 0

# check_sequence([1, 2, 3])
check_sequence([1, 2, 1])