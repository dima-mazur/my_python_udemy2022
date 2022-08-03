# walrus = False
# print(walrus)

print(walrus := True)

# 1111
for i in range(int(rows := input('Enter the numbers '))):
    print('*' * (i+1))
print(f'Number of rows = {rows}')

# 2222
def read_file(file):
    while line := file.readline():
        if not line:
            break

        split_line = line.split(';')
        print(split_line[1])