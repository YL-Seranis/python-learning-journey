# 创建列表 lst = [1, 2, 3, 4, 5]，
# 完成：①删除列表最后一个元素；
# ②在索引1的位置插入元素 99；
# ③在末尾添加元素 6 ；
# ④打印最终列表。

# lst = [1, 2, 3, 4, 5]
# lst.pop()
# lst.insert(1, 99)
# lst.append(6)
#
# print(lst)


# 现有列表 liebiao = [5, 2, 9, 1, 5, 6]。
# ①对列表进行升序排序并打印结果；
# ②对列表进行降序排序并打印结果。
# 输入五个正整数组成列表。
# ①按输入的顺序打印这五个数；
# ②按逆序打印这五个数。

# lst = [5, 2, 9, 1, 5, 6]
# lst.sort()
# print(lst)
#
# lst.sort(reverse = True)
# print(lst)


# lst = input("输入5个整数：").strip().split()
# for i in lst:
#     print(i)
#     lst.reverse()
#
# print(lst)


# 给定列表 data = [1,3,5,7,9,2,4,6,8]，
# 筛选出里面所有大于5的数，存入新列表new。
# data = [1, 3, 5, 7, 9, 2, 4, 6, 8]
# new = [i for i in data if i > 5]
#
# print(new)


# 删除列表 nums = [1, 2, 3, 2, 5, 2] 中所有值为2的元素，
# 打印最终的列表nums。
# nums = [1, 2, 3, 2, 5, 2]
# nums = [i for i in nums if i != 2]
# print(nums)


# 统计列表 msg = ["a", "b", "a", "c", "a", "d"] 中元素 "a" 出现的次数。
# msg = ["a", "b", "a", "c", "a", "d"]
# count = 0
# for i in msg:
#     if i == 'a':
#         count += 1 # 计数
# print(count)


# 清空列表 lst = [11,22,33,44] 里所有元素，但不删除列表lst。
# lst = [11,22,33,44]
# lst.clear()
# print(lst)


# 唐僧取经途中，依次收服了孙悟空、白龙马、猪八戒、沙和尚为徒。
# ①建立一个取经团队名单的空列表names，
# 按上述顺序，依次添加他们五人的名字，并打印最终名单names。
# ②三打白骨精时，唐僧误以为孙悟空滥杀无辜，将孙悟空逐出师门，
# 执行在上面列表中删除孙悟空姓名的操作，并打印新名单。
# ③后来唐僧被妖精抓了后，猪八戒打不过妖精，又去花果山请回了孙悟空。
# 对列表names执行操作：再将孙悟空的名字插入列表names中，变成原始名单。
# names = []
# names.extend(['孙悟空', '白龙马', '猪八戒', '沙和尚'])
# print(names)
#
# names = [i for i in names if i != '孙悟空']
# print(names)
#
# names.insert(0, '孙悟空')
# print(names)


# 在校计算机技能比赛中，
# 李磊、韩梅、小明、小芳依次活动一等奖、二等奖、三等奖、优胜奖。
# 颁奖时，按先较低级别、最后最高级别的顺序发奖。
# ①建个获奖名单的列表winner_list，按上述名次，保存他们四人的名字。
# ②再建立一个列表award，按颁奖顺序保存姓名。
# winner_list = ['李磊', '韩梅', '小明', '小芳']
# award = winner_list[::-1]
# print(award)