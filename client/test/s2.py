

#### 将s1文件中所有的内容打印出来

#
# import s1
#
#
# # print(dir(s1))
# for k in dir(s1):
#     if k.isupper():
#         v = getattr(s1, k)
#         print(k, v)

'''
Traceback (most recent call last):
  File "/Users/shangzekai/PycharmProjects/client/test/s2.py", line 23, in <module>
    test()
  File "/Users/shangzekai/PycharmProjects/client/test/s2.py", line 19, in test
    int('xxxx')
ValueError: invalid literal for int() with base 10: 'xxxx'

invalid literal for int() with base 10: 'xxxx'
'''
#
# import traceback
#
# def test():
#     try:
#         int('xxxx')
#     except Exception as e:
#         print(traceback.format_exc())
#
#     print('hello')
#
# test()


import time

from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def test(i):
    time.sleep(2)
    print(i)

p = ThreadPoolExecutor(10)

for i in range(100):

    p.submit(test, i)

















