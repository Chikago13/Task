# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def func(l):
    res = []
    count = 0
    for i in l:
        if i == 0:
            count += 1
            continue
        res.append(i)
        # res.remove(i)
    for j in range(count):
        res.append(0)
    return res
    



print(func([1, 2, 0, 3, 0, 4]))
print(func([0, 0, 2]))
