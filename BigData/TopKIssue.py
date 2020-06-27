# coding:utf-8

'''
【题目1】
海量日志数据，提取出某日访问百度次数最多TOP K 的IP
'''

'''
算法思路：hash分解 + Hash_map统计 + 只有K个元素的最小堆 + 合并排序

1.IP地址最多有2^32=4G种取值情况，所以不能完全加载到内存中处理；
2.可以考虑采用“分而治之”的思想，按照IP地址的Hash(IP)%1024值，把海量IP日志分别存储到1024个小文件中。这样，每个小文件最多包含4MB个IP地址； 
3.对于每一个小文件，可以构建一个IP为key，出现次数为value的Hash map 统计;
4. 建立只有K个元素的最小堆，若次数小于 堆顶 丢弃，若大于 则替换堆顶，并进行堆调整；
5. 将1024个小文件的topK 结果合并为后，重新使用K个元素的最小堆 得到结果；
'''

'''
【题目2】
搜索引擎会通过日志文件把用户每次检索使用的所有检索串都记录下来，每个查询串的长度为1-255字节。
假设目前有一千万个记录（这些查询串的重复度比较高，虽然总数是1千万，但如果除去重复后，不超过3百万个。
一个查询串的重复度越高，说明查询它的用户越多，也就是越热门。），请你统计最热门的10个查询串，要求使用的内存不能超过1G。
'''

'''
算法思路：hash分解 + Hash_map统计 + 只有K个元素的最小堆 + 合并排序
'''