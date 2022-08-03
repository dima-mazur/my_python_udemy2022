# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as ex:
#         print(f'error occured: {ex}')
#     except:
#         print('unknown error')
#
#
# divide(4, 0)


# file = None
# try:
#     file = open(r'abra.txt')
#     data = file.read()
# finally:
#     print('there')
#     if file:
#         file.close()

def get_int():
    while True:
        try:
            reply = int(input('enter a number - '))
            print(reply)
            return reply
        except:
            print('Not a number')
            continue

number = get_int()
