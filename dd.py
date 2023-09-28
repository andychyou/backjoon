def foo(x):
    x = 1
def loo(li):
    li[0] = 1

a = 1000
li = [1]
foo(a)
loo(li)
print(li)