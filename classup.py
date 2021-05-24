# class 선언 

class VectorP(object):
    
    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return(i for i in (self.__x,self.__y)) # Generator 

    @property
    def x(self):
        return self.__x 

    @x.setter
    def x(self, v):
        print('Called Property X Setter')
        self.__x = v 

    @property
    def y(self):
        return self.__y 

    @y.setter
    def y(self, v):
        print('Called Property X Setter')
        self.__y = v 

# 객체 선언 
v = VectorP(20,40)

# print('EX1-1 -', v.__x, v.__y)

# Getter, Setter
print('EX1-2 -', dir(v), v.__dict__)
print('EX1-3 -', v.x, v.y)

# Iter 확인   
for val in v:
    print('EX1-2 -', val)

# __slot__
# 파이썬 인터프리터에게 통보 
# 해당 클래스가 가지는 속성을 제한 
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용 공간 대폭 감소 
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 set 형태를 사용 

class TestA(object):
    __slots__ = ('a',)

class TestB(object):
    pass 

use_slot = TestA()
no_slot = TestB()

print('EX2-1 -', use_slot)
# print('EX2-2 -', use_slot.__dict__)
print('EX2-3 -', no_slot)
print('EX2-4 -', no_slot.__dict__)

# 메모리 사용량 비교 
import timeit 

# 측정을 위한 함수 선언 
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner

print(min(timeit.repeat(repeat_outer(use_slot), number=1000000)))
print(min(timeit.repeat(repeat_outer(no_slot), number=1000000)))#