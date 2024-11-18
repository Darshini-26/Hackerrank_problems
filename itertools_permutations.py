from itertools import permutations
word,length=input().split()
for i in sorted(permutations(word,int(length))):
    print(''.join(i))
