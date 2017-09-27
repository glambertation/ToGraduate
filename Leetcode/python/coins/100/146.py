'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''

'''
python collections 模块 deque 双向链表

deque
deque其实是 double-ended queue 的缩写，翻译过来就是双端队列，它最大的好处就是实现了从队列 头部快速增加和取出对象: .popleft(), .appendleft() 。

你可能会说，原生的list也可以从头部添加和取出对象啊？就像这样：

l.insert(0, v)
l.pop(0)
但是值得注意的是，list对象的这两种用法的时间复杂度是 O(n) ，也就是说随着元素数量的增加耗时呈 线性上升。而使用deque对象则是 O(1) 的复杂度，所以当你的代码有这样的需求的时候， 一定要记得使用deque。

作为一个双端队列，deque还提供了一些其他的好用方法，比如 rotate 等。

上述 http://www.zlovezl.cn/articles/collections-in-python/

https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001411031239400f7181f65f33a4623bc42276a605debf6000
https://docs.python.org/2/library/collections.html#collections.deque

dict
https://docs.python.org/2.7/library/stdtypes.html#typesmapping



'''

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key = {}
        self.q = collections.deque([])
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key:
            return -1
        self.q.remove(key)
        self.q.append(key)
        return self.key[key]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key:
            self.q.remove(key) 
        elif len(self.key) == self.capacity:
            v = self.q.popleft()
            self.key.pop(v)
        self.key[key] = value
        self.q.append(key)
        

            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
