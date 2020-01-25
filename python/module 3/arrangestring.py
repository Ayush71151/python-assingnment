s=input("enter any string")
s1,s2="",""
for i in range(len(s)):
    if s[i].islower():s1=s1+s[i]
    if s[i].isupper():s2=s2+s[i]
print (s1+s2)
