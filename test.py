
def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


c3 = coroutine2(10)

from inspect import getgeneratorstate

print('EX1-2 -', getgeneratorstate(c3))

print(next(c3))

print('EX1-3 -', getgeneratorstate(c3))

print(c3.send(15))

#print(c3.send(20)) # 예외

print()
print()