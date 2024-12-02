
n=int(input())
x=list(map(int,input().split()))  
n=int(input())
y=list(map(int,input().split()))

x=set(x)
y=set(y)
print(len(x&y))
