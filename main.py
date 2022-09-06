class FlatIterator:
    def __init__(self, list):
        self.nested_list = list
        self.pointer = 0
        self.ipointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.pointer < len(self.nested_list):
            while self.ipointer < len(nested_list[self.pointer]):
                result = nested_list[self.pointer][self.ipointer]
                self.ipointer += 1
                return result
            self.pointer += 1
            self.ipointer = 0
        raise StopIteration


def flat_generator(nested_list):
    pointer = 0
    ipointer = 0
    while pointer < len(nested_list):
        while ipointer < len(nested_list[pointer]):
            result = nested_list[pointer][ipointer]
            yield result
            ipointer += 1
        pointer += 1
        ipointer = 0


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

for item in FlatIterator(nested_list):
    print(item)
print()
print()
for item in flat_generator(nested_list):
    print(item)
