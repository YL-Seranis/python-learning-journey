# 求前十项之和
# 运行结果：6.619091

a = 1
b = 1
sm = 0

for _ in range(10):
    sm += a / b
    a = a + b
    b = a + b

print(sm)