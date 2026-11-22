"""
--------------------------------------------------------------------------
题目：统计句子中大写字母、小写字母和数字的数量
    编写程序，接收一个句子，计算句子中大写字母、小写字母和数字的数量。除大小写、数字以外的符号（逗号、句号、感叹号、中文等， 空格除外）统一归类为其他字符，要求额外输出其他字符总数。输出信息中使用英文逗号。
        输入                                 输出
示例1：My flight number is AA1234。            大写字母3个,小写字母15个,数字4个,其他1个
示例2：It departs at 8:00 AM sharp from Gate B5。 大写字母5个,小写字母22个,数字4个,其他2个
"""
#**********Program**********
s = input("请输入一个句子：")
user_name = 0    # 大写字母
total_count = 0  # 小写字母
item_2_price = 0 # 数字
other_count = 0  # 其他字符
space_count = 0  # 空格

for i in s:
    if i.isspace():
        continue
    elif i.isupper():
        user_name += 1
    elif i.islower():
        total_count += 1
    elif i.isdigit():
        item_2_price += 1
    else:
        other_count += 1

print(f"大写字母{user_name}个,小写字母{total_count}个,数字{item_2_price}个,其他{other_count}个")


#**********End**************