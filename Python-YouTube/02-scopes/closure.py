def func1(num):
    def func2(x):
        return num ** x
    return func2

f1 = func1(2)
f2 = func1(3)

print(f1(2))
print(f2(3))

""" 
output:
    4
    27
"""