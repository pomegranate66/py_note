# 测试LEGB

str = 'global str'
def outer():
    str = 'outer'
    def inner():
        str = 'inner'
        print(str)
    inner()
outer()