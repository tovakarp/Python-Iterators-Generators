def  my_enumerate(iterable, start=0):
    count = start
    for elem in iterable:
        yield count, elem
        count += 1


for index, elem in my_enumerate([10, 20, 30, 40], 10):
    print(index, elem)