from itertools import count


a = int(input("enter numbers"))
for i in a:
    n = count(i)
    avg = sum(i)/n
    print(avg)