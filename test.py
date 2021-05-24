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

