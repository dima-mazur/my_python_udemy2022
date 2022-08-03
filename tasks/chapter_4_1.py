# def calc_dice_scores(lst):
#     x = 0
#     for v, k in lst:
#         if v == k:
#             x = 0
#             return x
#         else:
#             x += v+k
#     return x
#
#
# calc_dice_scores([(1, 1), (3, 4), (5, 6)])


def any_duplicates(square):
    concat_list = []
    for i in square:
        for x in i:
            concat_list.append(x)
    for v in concat_list:
        if concat_list.count(v) > 1:
            return False
    return True

any_duplicates([[1, 3, 2], [9, 7, 8], [4, 5, 6]])
