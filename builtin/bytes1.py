chinese_str = "你好"
#chinese_str = b"你好" Wrong assignment,bytes only support ACSII
print(chinese_str.encode("utf-8"))
chinese_str_encode = chinese_str.encode()
for i in chinese_str_encode:
    print(i)
