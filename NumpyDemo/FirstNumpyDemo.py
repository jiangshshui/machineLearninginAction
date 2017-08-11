from numpy import *
print(random.rand(4,4)) #这产生的是数组,numpy 的数组和矩阵是不同的

randMat=mat(random.rand(4,4,))
print("--mat--")
print(randMat)
print("--mat's inverse--")
invRandMat=randMat.I
print(invRandMat)

print("--invRandMat*randMat--")
myEye=invRandMat*randMat
print(myEye)
print("------误差------")
print(myEye-eye(4))

print(eye(4))


