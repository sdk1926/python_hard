class VectorP(object):
    
    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return(i for i in (self.__x,self.__y)) # Generator 

    @property
    def x(self):
        print('Called Property X Getter')
        return self.__x 

    @x.setter
    def x(self, v):
        print('Called Property X Setter')
        self.__x = v 

    @property
    def y(self):
        print('Called Property Y Getter')
        return self.__y 

    @y.setter
    def y(self, v):
        print('Called Property Y Setter')
        self.__y = v 

v = VectorP(20,40)
print('*'* 40)
v.x = 'abcd'
print('*'* 40)
print(v.x)
print('*'* 40)
for val in v:
    print('EX1-2 -', val)
print(v.__dict__)
v = VectorP(20,40)
for val in v:
    print('EX1-4 -', val)

class VectorPs(object):
    
    def __init__(self,x,y):
        self._x = float(x)
        self._y = float(y)

    def __iter__(self):
        return(i for i in (self._x,self._y)) # Generator 

v = VectorP(30,50)
print('*'* 40)
v._x = 'abcd'
print('*'* 40)
print(v._x)
print('*'* 40)
for val in v:
    print('EX1-5 -', val)
print(v.__dict__)
