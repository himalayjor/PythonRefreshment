""" string to int"""
stuff = {'a': 1, 'b': 2}

print(stuff['a'])

""" adding element"""
stuff['c'] = 3

""" removing element"""
stuff.pop('a')
del stuff['b']

print(stuff.keys())

print(stuff)

"""map of string to string"""
dstos = {'a': 'first', 'b': 'second', 'c': 'third', 'd': 'fourth'}

""" iterating over keys"""
for key in dstos:
    print(key)

for key, val in dstos.items():
    print(key, '->', val)

""" get with default value"""
print(dstos.get('e', 'unkownValue'))
