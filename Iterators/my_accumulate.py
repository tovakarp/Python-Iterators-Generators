def my_accumulate(iterable):
    count = 0
    for elem in iterable:
        count += elem
        yield count



for elem in my_accumulate([1,2,3,4,5]):
    print(elem)