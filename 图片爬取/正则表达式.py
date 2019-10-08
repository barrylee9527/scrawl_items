import re


# re.match 尝试从起始位置开始匹配，如果不是起始位置返回none
result = re.match(pattern='^sa\s.*?', string='sadfa', flags=0)
print(result)
# result.group()显示匹配到的括号里的字符串。result.span()输出匹配范围
# 转义 反斜杠\加通配符
# re.search() 扫描整个字符串并返回第一个成功的匹配
# re.findall() 搜索字符串，以列表形式返回全部能匹配的子串  re.S换行多行匹配 提起需要for循环遍历
# re.sub('正则表达式', content) 替换字符串中每一个匹配的子串后返回替换后的字符串
# re.compile() 将正则字符串编译为正则表达式对象 ，以便于服用该匹配模式

