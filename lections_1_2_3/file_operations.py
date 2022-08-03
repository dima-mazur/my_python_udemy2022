# import pwd
# pwd
# import shutil
import os
print('my directory is', os.getcwd())

b = open('sample.txt', 'w')
b.write('hello world'
        '\n dima mazur')
b.close()

file = open('sample.txt', 'r')
print(file.read())
file.read()
# курсор дошел до конца файла
print(file.read())
file.seek(0)
# курсор установлен на начало файла
print(file.read())



lines = file.readline()
print(lines)
print(len(lines))

print(file.closed)
# проверка закрытия файла
file.close()

with open('sample.txt', mode='r+') as sample_file:
    sample_file.seek(0, 2)
    sample_file.write('\n Mashulya Mazur')
    sample_file.seek(0)
    print(sample_file.read())

with open('abracadabra.txt', mode='w+') as spell_file:
    spell_file.write('abra-abra-cadabra')
    spell_file.seek(0)
    print(spell_file.read())
