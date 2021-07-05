# 파이썬 클래스 만들기 

class Idol_member(object):

    def __init__(self, name, group, gender, age, agency):
        self._name = name
        self._group = group
        self._gender = gender 
        self._age = age
        self._agency = agency 
    
    def __str__(self):
        return f'이름: {self._name}'

    def __repr__(self):
        return f'그룹명 : {self._group}'

idol_member1 = Idol_member('시우민', '엑소', '남자', 32, 'SM엔터테인먼트')
idol_member2 = Idol_member('카이', '엑소', '남자', 28, 'SM엔터테인먼트')
idol_member3 = Idol_member('세훈', '엑소', '남자', 28, 'SM엔터테인먼트')

print(idol_member1.__dict__)

# 리스트 선언 
idol_member_list = []
idol_member_list.append(idol_member1)
idol_member_list.append(idol_member2)
idol_member_list.append(idol_member3)

print(idol_member_list)


# (__str__)
for x in idol_member_list:
    print(x)
    print(repr(x))

