def check(n):
    if(n<2):
        return (n%2==0)
    return (check(n-2))

n=int (input("enter a num = "))
if (check(n)==True):
    print("num is even ")
else:
    print("num is odd")
