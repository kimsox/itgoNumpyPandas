
# numpy 슬라이싱

import numpy as np

list = [[1,2,3],
        [4,5,6],
        [7,8,9]]

arr = np.array(list)

a = arr[0:2, 0:2]
print("matrix a : \n", a)

b = arr[1:, 1:]
print("matrix b : \n", b)

# numpy 정수 인덱싱(integer indexing)

# numpy배열 a에 대해서 a[[row1, row2], [col1, col2]]는 
# a[row1, col1]과 a[row2, col2] 라는 두 개의 배열 요소 집합으 의미한다.

list2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
    ]
a = np.array(list2)

# 정수 인덱싱
res = a[[0, 2], [1, 3]]
print("matrix res : \n", res)

# 부울린 인덱싱(boolean indexing)
list3 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
aa = np.array(list3)
b_arr = np.array([
    [False, True, False],
    [True, False, True],
    [False, True, False]
    ])
n = aa[b_arr].reshape((2,2))
print("matrix n : \n", n)

# 부울린 인덱싱 배열을 생성할 때 표현식으로 이용하기
# 배열 a에 대해서 짝수인 배열 요소만 True로 지정하겠다 하면
# b_arr = ((a % 2) == 0)

list4 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

arr = np.array(list4)

# 배열 arr에 대해서 짝수면 True, 홀수면 False
b_arr = ((arr % 2) == 0)
print(b_arr)
print(arr[b_arr])

n = arr[arr%2 == 0]
print(n)