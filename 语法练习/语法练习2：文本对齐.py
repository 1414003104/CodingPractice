#文本对齐方法
poem=["登黄雀楼",
      "王之涣",
      "白日依山尽",
      "黄河入海流",
      "欲穷千里目",
      "更上一层楼"]
#居中对齐
for poem_str in poem:
    print("|%s|" % poem_str.center(10," "))
#左对齐
for poem_str in poem:
    print("|%s|" % poem_str.ljust(10," "))
#右对齐
for poem_str in poem:
    print("|%s|" % poem_str.rjust(10," "))


