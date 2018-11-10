elements = []

""" Range excludes last element"""
for i in range(0, 6):
    elements.append(str(i))

print(elements)

for i in elements:
    print(i)

print(' '.join(elements))

"""pop woluld remove element from list"""
top = elements.pop(0)
print(top)


""" By default pop would give you last element in list"""
popElement = elements.pop()
print(popElement)

print(elements)