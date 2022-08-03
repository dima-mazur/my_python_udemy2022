class StaticTest:
    x = 1


t1 = StaticTest()
print(StaticTest.x)
print(t1.x)

t1.x = 2
print(t1.x)
print(StaticTest.x)

StaticTest.x = 3
print(t1.x)
print(StaticTest.x)
