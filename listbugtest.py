#!/usr/bin/env python3


def compute(base, value):
    base_copy = base.copy()#创建一个临时的base
   # base_copy = base[:]
    base_copy.append(value)
    result = sum(base_copy)
    print(result)#打印后释放

if __name__ == '__main__':
    testlist =[10, 20, 30]
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)
