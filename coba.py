a = [9,8,6,5,7,4,1,2,3]

end = len(a) - 1

while end != 0:

    for i in range(end):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

    end = end - 1

print(a)