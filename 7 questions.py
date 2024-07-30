def mul(n):
    for i in range(1,11):
        print(n,"x",i,"=",n*i)
a=5
mul(a)


def flt(n):
    n=float(n)
    return n
b=7
print("float: ",flt(b))


def integr(n):
    n=int(n)
    return n
c=6
print("integer: ",integr(c))


def tupl(n):
    n=tuple(n)
    return n
d=["hello",12.1,100,"welcome"]
print("tuple: ",tupl(d))


def lis(n):
    n=list(n)
    return n
d=("hello",12.1,100,"welcome")
print("list: ",lis(d))


def sumn(n):
  total=0
  for i in range (1,n+1):
    total+=i
  return total
n=10
print(sumn(n))
