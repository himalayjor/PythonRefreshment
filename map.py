la = [1,2,3]

lb = map(lambda x: x*2, la)

print(list(lb))


def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)