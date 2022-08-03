greeting = 'global scope'
#
# def greet():
#     greeting = 'enclosing scope'
#
#
#     def nested():
#         greeting = 'local scope'
#         print(greeting)
#     nested()
#
#
# greet()
# print(greeting)


def greet():
    global greeting
    print(f'Greet in func:{greeting}')

    greeting = 'enclosing scope'

    print(f'Greet in func:{greeting}')


greet()
print(greeting)