numbers = [2, 4, 6, 8, 10]
numbers.append(12)

print(numbers)

numbers.insert (2, 14)

print (numbers)

numbers.insert(-1, 16)

print (numbers)

numbers.insert(100, 18)

print(numbers)

numbers.sort()
print (numbers)

print(numbers.index(2))

numbers = [ 1, 2, 3, 4]

numbers += [6]

print (numbers)


for i in numbers:
    print(i)


for item in [1, [2, 3], 4]:
    print (item)


def print_recursive(alist):
    if alist == []:             #base case
        pass
    elif type (alist) == int:   #base
        print(alist)
    else:                       #general
        for item in alist:
            print_recursive(item)

print_recursive([1, [2, 3], 4])

print([i * 2 for i in numbers])

