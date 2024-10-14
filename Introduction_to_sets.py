def average(array):
    ans=0
    Uarray = set(array)
    length=len(Uarray)
    for item in Uarray:
        ans += item
    
    avg=ans/length
    return avg
        
