
# numpy 자료형(data type)

# int, float , boolean(True, False)

# 정수형(integer)
# int8, int16, int32, int64 (부호가 있는 정수형 )
# uint8, uint16, uint32, uint64

# 실수형(float)
# float16, float32, float64

# 복소수형(complex)
# 두개의 32 or 64 비트의 부동소수점으로 표시되는 복소수
# complex64, complex128

# 데이터의 type을 알아보기 위한 dtype

import numpy as np

x = np.float32(1.0)
print(x)
print(type(x))
print(np.dtype(x))
print(x.dtype)

z = np.arange(5, dtype='complex64')
print(z)
aa = np.array([1,2,3], dtype='f')
print(aa)
print(aa.dtype)

xx = np.int8(aa)
print(xx)
print(xx.dtype)

bb = np.arange(10)
print(bb)
print(bb.dtype)

cc = np.arange(3,10, dtype=np.float)
print(cc)
print(cc.dtype)

dd = np.arange(2, 3, 0.1)
print(dd)
