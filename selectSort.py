# -*-coding: utf-8 -*-
__auth__ = "wade"
__date__ = '2017/12/23 10:40'


'''
基本思路：
选择排序比较好理解，好像是在一堆大小不一的球中进行选择（以从小到大，先选最小球为例）：
　　1. 选择一个基准球
　　2. 将基准球和余下的球进行一一比较，如果比基准球小，则进行交换
　　3. 第一轮过后获得最小的球
　　4. 在挑一个基准球，执行相同的动作得到次小的球
　　5. 继续执行4，直到排序好
时间复杂度：O(n^2).  需要进行的比较次数为第一轮 n-1，n-2....1, 总的比较次数为 n*(n-1)/2
参考：https://www.cnblogs.com/AlwinXu/p/5424510.html
'''


def selectSort(alist):
    alist_len = len(alist)
    for i in xrange(alist_len):
        for j in xrange(i+1, alist_len):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
        #print  "Round ",i,": ",alist
    return alist

if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    print selectSort(alist)