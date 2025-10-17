# 从键盘读取一行输入
s = input()

# 初始化四个计数器
letters = 0
digits = 0
spaces = 0
others = 0

# 逐个字符判断类型
for c in s:
    if c.isalpha():  # 英文字母
        letters += 1
    elif c.isdigit():  # 数字
        digits += 1
    elif c.isspace():  # 空格
        spaces += 1
    else:  # 其他字符
        others += 1

# 按格式输出
print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
