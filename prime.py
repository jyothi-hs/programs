num = 2
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print("no")
            print(i)
            break
    else:
            print("yes")
# else:
#     print("not a prime")