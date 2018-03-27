
# Numpy / Pandas 소개

"""
    Numpy 는 과학 계산을 위한 라이브러리로 다차원 배열을 처리하는데 
    필요한 여러 기능을 제공한다.

    - numpy 배열
        numpy에서 배열은 동일한 타입의 값 들을 갖는다.
        배열의 차원을 rank라고 한다.

    - shape : 각 차원의 크기를 튜플로 표시한 것
        ex) 2행, 3열인 2차원 배열의 rank는 2이고, shape은 (2,3)

    - numpy 배열을 생성
        파이썬의 리스트를 사용하는 방법
        array() 함수의 인자로 리스트를 넣어 생성한다.

        ex) numpy.arrray([1,2,3])

    - numpy에서 제공하는 함수를 사용하는 방법
        1) zeros()   : 배열에 모두 0을 집어넣는다.
        2) ones()    : 모두 1을 집어넣는다.
        3) full()    : 사용자가 지정한 값을 넣는데 사용
        4) eye()     : 대각선으로는 1이고 나머지는 0인 n차원 배열을 생성
        5) reshape() : 다차원으로 변형하는 함수
"""

# -*- coding : utf-8 -*-

import numpy as np

# list 배열 선언
list1 = [1, 2, 3, 4]
# list 배열 array화
a= np.array(list1)
print("배열 a :", a)
print("a의 shape :", a.shape)
b= np.array([[1,2,3], [4,5,6]])
print("배열 b :\n", b)
print("b의 shape :", b.shape)
print("b[1,1] :", b[1,1])
print('\n')

aa = np.zeros((2,2))
print( "배열 aa :\n", aa)
print("type aa :", type(aa))
bb = np.ones((2,3))
print("배열 bb :\n", bb)
cc = np.eye(4)
print("배열 cc :\n", cc)
dd = np.array(range(20)).reshape((5,4))
print("배열 dd :\n", dd)