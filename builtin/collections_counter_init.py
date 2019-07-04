#collections_counter_init.py
import collections
print(collections.Counter('abcdedereff')) #strin
print(collections.Counter(('a','b','c','a'))) #tuple
print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])) #list
print(collections.Counter({'a': 2, 'b': 3, 'c': 1})) #dict
print(collections.Counter(a=2, b=3, c=1))#keyword args