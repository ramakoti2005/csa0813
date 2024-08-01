def anagram(a,b):
    n=sorted(a)
    m=sorted(b)
    if(m==n):
        return "it is anagram"
    else:
        return "not anagram"
a="silent"
b="listen"
print(anagram(a,b))
