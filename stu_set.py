# 元组
# 元组的创建、访问及常用操作
# 两种
# 单元素元组的创建
# 只有字符串"苹果"的元组
# a=("苹果",)
# print("苹果"[1])
# a=tuple("苹果")
# print(a,type(a))



# 元组的运算符、生成器推导式 函数方法
# + * in
# t=(i for i in range(10))
# c=tuple(t)
# a=list(t)
# print(c,a)

# index
# count


# 集合
# t = ["唐僧","沙和尚","孙悟空","沙和尚","唐僧","孙悟空","猪八戒","唐僧"]
# l=[]
# for i in t:
#     if l.count(i)==0:
#         l.append(i)
# print(l)

# t = ["唐僧","沙和尚","孙悟空","沙和尚","唐僧","孙悟空","猪八戒","唐僧"]
# t=set(t)#转化成集合
# print(t)

# 集合是无序  元素唯一
# 集合是一种无序且元素唯一的容器类型


# 集合的创建
# 等号赋值法
# a={1,2,3,1,1,1,6,6,6,8,8,98,413,45}
# print(a,type(a))
# 创建空集合 不能使用{}创建
# 只能使用转化法创建
# b={} #创建字典 dict
# g=set()#创建集合 set
# print(g,type(g))
# print(b,type(b))

# 转化法
# list() tuple() set() 可以接收可迭代对象
# int() float() str() bool()#填写单个数值
# set(字符串，range,列表，元组)
# a=set("苹果")
# print(a)

# 集合的增删改查
# 增加
# add() 向集合中添加一个可哈希元素
# 例如数字、字符串，以及元素均可哈希的元组
# 列表、字典和集合本身不能作为集合元素
# a=set()
# a.add((1,1,1))
# a.add(1)
# a.add((1,))
# print(a)

# update() 更新 添加一个序列 extend()
# a=set()
# a.update([1,2,3])
# a.update((1,2,3))
# print(a)


# 删除
# remove() 删除不存在的元素会报错 in
# a={1,2,3,True,0,False}
# print(a)
# a.remove(4)
# print(a)

# discard() 删除不存在的元素不会报错
# a.discard(4)
# print(a)

# pop() 删除并返回集合中的任意一个元素，不能指定删除哪个
# a={1,2,3,True,0,False}
# a.pop()
# print(a)
# a={121,300,200}
# print(a)
# a.pop()
# print(a)

# 哈希 哈希表法