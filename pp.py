b = 'Title@name'
a = b.replace('@',' ')
print(a)
s = a.split()[::-1]
print(s)
l = [ ]
for i in s:
    l.append(i)
    print(i)
print(" ".join(l))

