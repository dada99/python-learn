#collections_defaultdict.py
import collections

def default_factory():
    return 'default value'
new_dict = {'e': 3, 'd': 2, 'f': 2, 'a': 1, 'b': 1, 'c': 1, 'r': 1}

#d = collections.defaultdict(default_factory, foo='bar')
d = collections.defaultdict(default_factory, new_dict)
print('d:', d)
print('foo =>', d['e'])
print('bar =>', d['bar'])