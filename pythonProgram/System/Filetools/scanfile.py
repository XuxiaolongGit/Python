def scanner(name, function):
    for line in open(name):
        function(line)
# for环境迭代
def scanner2(name,function):
    list(map(function, open(name,'r')))
# map函数迭代
def scanner3(name,function):
    [function(line) for line in open(name)]
# 列表解析
def scanner4(name,function):
    list(function(line) for line in open(name))
# 生成器再列表化