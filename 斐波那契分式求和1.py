# 求前十项之和
# 运行结果：6.479905

# c = a + b
# a = b
# b = c

a = 1
b = 1
sm = 0

for _ in range(10):
    sm += a / b
    c = a + b
    a = b
    b = c

print(sm)