def count_substring(string, sub_string):
    ans=0
    for i in range(len(string)-len(sub_string)+1):
        if sub_string in string[i:i+len(sub_string)]:
            ans=ans+1
    return ans