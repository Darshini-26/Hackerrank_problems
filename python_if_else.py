n=int(input())
if n%2!=0:
    print("Weird")
if n%2==0:
    if (n>=2 and n<=5) or n>20:
        print("Not Weird")
    elif n>=6 and n<21:
        print("Weird")
    