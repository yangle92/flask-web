# L=['a','b','c']
# for i,item in enumerate(L):
#     print(i,item   )

#断言 ：打断说话

L = ['a', 'b', 'c']
# L = ['a', 'b']
# if len(L) !=3:
#     raise TypeError('列表长度必须为3，这是我的规则')

assert len(L) == 3
print('---->')

'''
迭代器一定是可迭代的对象，而可迭代对象不一定是迭代器对象

可迭代对象最需要有__iter__()
迭代器对象 __iter__()   __next__()
文件对象本身就是一个迭代器

'''