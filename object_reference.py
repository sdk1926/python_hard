# 객체 참조 중요한 특징들 
# Python Object Reference 

print('EX1-1 -')
print(dir())

# id vs __eq__ (==) 증명 
x = {'name': 'seo', 'age': 26, 'city': 'Incheon'}
y = x 

print('EX2-1 -', id(x), id(y))
print('EX2-2 -', x == y)
print('EX2-3 -', x is y)
print('EX2-4 -', x, y)

x['class'] = 10 
print('EX2-5 -', x, y)  # x값을 수정하면 y값도 변경이 된다. 

print()
print()

z = {'name': 'seo', 'age': 26, 'city': 'Incheon', 'class': 10}
print('EX2-6 -', x,z)
print('EX2-7 -', x is z) # 같은 객체 
print('EX2-8 -', x is not z)
print('EX2-9 -', x == z) # 값이 같다 

# 객체 생성 후 완전 불변 -> 즉,id는 객체 주소(정체성 비교), ==(__eq__) 는 값 비교 

print()
print()

# 튜플 불변형 비교 
tuple1 = (10,15,[100,1000])
tuple2 = (10,15,[100,1000])

print('EX3-1 -', id(tuple1), id(tuple2))  # 튜플은 불변형이라서 값이 같아도 id가 절대 같을 수 없음
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-3 -', tuple1.__eq__(tuple2))

xa = {'exo': 'sehun'}
xb = {'exo': 'sehun'}

print(id(xa),id(xb))

# Copy, Deepcopy(깊은복사, 얕은 복사)
tl1 = [10,[100,105], (5,10,15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-4 -', tl1 is tl3)

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('ES4-5 -', tl1)
print('ES4-5 -', tl2)
print('ES4-5 -', tl3)

print()

print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2)
print('EX4-10 -', tl3)
print(id(tl1[2]))  # 튜플은 변경해버리면 id가 바뀐다.

# Deep copy 
# 장바구니 
class Basket:
    def __init__(self,products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self,prod_name):
        self._products.remove(prod_name)

import copy 

basket1 = Basket(['Apple', 'Bag', 'Tv', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX5-1 -', id(basket1), id(basket2), id(basket3))
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products))
print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-4 -', basket2._products)  # 인스턴스 안에서 생기는 문제 
print('EX5-5 -', basket3._products)




