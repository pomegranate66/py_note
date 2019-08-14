'''
原码反码补码：

1-1 = 0

1 + -1 = 0
# 1
0000 0001
# -1
1000 0001
-------------
1000 0010

正数：
    原码 = 反码 = 补码
    +1 的补码 0000 0001
负数：
    最高位为符号位
    原码：1000 0001
    反码：1111 1110（原码，除符号位之外，所有位数反数）
    补码：1111 1111（反码+1）

    补码->反码
    继续取反+1


'''