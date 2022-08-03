# while
x = 0
while x < 3:
    print(f'x = {x}')
    x += 1

while x < 3:
    print(f'x = {x}')
    x += 1
else:
    print('blablabla')

vals = [i for i in range(1, 10)]
print(vals)
sum = 0
for v in vals:
    if v % 2 == 0:
        continue
    else:
        sum += v
    if sum > 10:
        break
print(sum)
