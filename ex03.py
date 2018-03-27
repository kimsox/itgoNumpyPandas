
# numpy 연산

# 연산자를 이용할 경우에는 +,-,*,/
# 함수를 사용할 경우에는 add(), subtract(), multiple(), divide()

# 배열 a와 배열 b가 있을 때, a+b,는 a[0]+b[0], a[1]+b[1], ...
# 와 같은 방식으로 결과를 리턴한다.

import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

#c = a + b
c = np.add(a, b)
print("add c : ", c)
#c= a - b
c = np.subtract(a, b)
print("subtract c : ", c)
#c = a * b
c = np.multiply(a, b)
print("multiply c : ", c)
#c = a / b
c = np.divide(a, b)
print("divide c : ", c)

print("----------------------------------")

# numpy에서 vector와 matrix의 product를 구하기 위해서는 dot() 함수를 이용한다.
print("두 matrix에 대한 product 구하기")
list1 = [[1,2], [3,4]]
list2 = [[5,6], [7,8]]
a = np.array(list1)
b = np.array(list2)
c = np.dot(list1, list2)
print(c)

# numpy에서는 배열 간의 연산을 위한 여러 함수들을 제공하는데,
# 각 배열의 요소를 더하는 함수 sum(), 배열의 요소들을 곱하는 prod()함수
# 이 함수들은 옵션이 있다. (axis 옵션) axis 0 이면 컬럼끼리 더함, 1이면 행끼리 더함
print("")
a = np.array([[1,2], [3,4]])
s1 = np.sum(a)
s2 = np.sum(a, axis=0)
s3 = np.sum(a, axis=1)
print("matrix a : \n", a)
print("sum of a : \n", s1)
print("sum of a - axis=0 : \n", s2)
print("sum of a - axis=1 : \n", s3)
print("")
p1 = np.prod(a)
p2 = np.prod(a, axis=0)
p3 = np.prod(a, axis=1)
print("matrix a : \n", a)
print("sum of a : \n", p1)
print("sum of a - axis=0 : \n", p2)
print("sum of a - axis=1 : \n", p3)


