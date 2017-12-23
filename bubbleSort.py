# -*-coding: utf-8 -*-
__auth__ = "wade"
__date__ = '2017/12/23 10:40'

'''
冒泡排序的基本思想是，对相邻的元素进行两两比较，顺序相反则进行交换，这样，每一趟会将最小或最大的元素“浮”到顶端，最终达到完全有序
算法的核心在于每次通过两两比较交换位置，选出剩余无序序列里最大（小）的数据元素放到队尾。
1、比较相邻的元素。如果第一个比第二个大（小），就交换他们两个。
2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大（小）的数。
3、针对所有的元素重复以上的步骤，除了最后已经选出的元素（有序）。
4、持续每次对越来越少的元素（无序元素）重复上面的步骤，直到没有任何一对数字需要比较，则序列最终有序。
参考：https://www.cnblogs.com/chengxiao/p/6103002.html
     http://blog.csdn.net/guoweimelon/article/details/50902597
'''

def bubbleSort(alist):
    alist_len = len(alist)
    for i in xrange(alist_len-1):
        for j in xrange(alist_len-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
        # print  "Round ", i, ": ", alist
    return alist


# 改进的冒泡排序, 加入一个校验, 如果某次循环发现没有发生数值交换, 直接跳出循环
def modiyBubbleSort(alist):
    alist_len = len(alist)
    exchange = True
    while alist_len > 0 and exchange:
        exchange = False # 进入while循环先赋值成False，如果发生了数据交换，则exchange = True，否则，下次执行的时候exchange为False，直接跳出循环
        for j in xrange(alist_len-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
        alist_len -= 1
        # print  "Round ", alist_len, ": ", alist
    return  alist

if __name__ == "__main__":
    alist = [1,2,3,4,5]
    print modiyBubbleSort(alist)