
class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        lastitem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastitem

    def delete(self, index):
        deleteditem = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        del self.data[self.length - 1]
        self.length -= 1
        return deleteditem


array = Array()
array.push(3)
array.push('hi')
array.push(34)
array.push(20)
array.push('hey')
array.push('welcome')
array.delete(3)
print(array)
