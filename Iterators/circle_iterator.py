class CircleIter:
    def __init__(self, list_, times):
        self.list = list_
        self.times = times

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter >= self.times:
            raise StopIteration
        self.counter += 1
        return self.list[(self.counter - 1) % len(self.list)]


for x in CircleIter([1,2],5):
    print(x, end=" ")

print()


for x in CircleIter([1,2,3],4):
    print(x, end=" ")
    for y in CircleIter([5,6],3):
        print(y, end=" ")
    print()


