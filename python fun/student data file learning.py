f = open("student data.txt", "r")

for i in f:
    items = i.split()
    if len(items[1:]) > 6:
        print(items[0])

    print(items[0], "max is", max(items[1::]), "min is", min(items[1::]))



f.close()
