class CustomSetIterator:
    def __init__(self, data):
        self._data = list(data)
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index<len(self._data):
            value = self._data[self._index]
            self._index+=1
            return value
        raise StopIteration

class CustomSet:
    def __init__(self, data=None):
        self._data=[]
        if data is not None:
            for x in data:
                if x not in self._data:
                    self._data.append(x)
    def __iter__(self):
        return CustomSetIterator(self._data)
    def __len__(self):
        return len(self._data)
    def __str__(self):
        return str(self._data)
    def __add__(self, other):
        result = CustomSet(self._data)
        if isinstance(other, CustomSet):
            for x in other:
                if x not in result._data:
                    result._data.append(x)
        else:
            if other not in result._data:
                result._data.append(other)
        return result
    def __mul__(self, other):
        result = CustomSet()
        if isinstance(other, CustomSet):
            for x in self:
                if x in other._data:
                    result._data.append(x)
        else:
            if other in self._data:
                result._data.append(other)
        return result
    def __sub__(self, other):
        result = CustomSet()
        if isinstance(other, CustomSet):
            for x in self:
                if x not in other._data:
                    result._data.append(x)
        else:
            for x in self:
                if x != other:
                    result._data.append(x)
        return result
    def __truediv__(self, other):
        return (self - other) + (other - self)
def read(filename):
    words = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.lower().split():
                word = word.strip(".,!?;:\"'()")
                if word != "":
                    words.append(word)
    return CustomSet(words)

file1 = read("file1.txt")
file2 = read("file2.txt")
file3 = read("file3.txt")

common_words = file1*file2*file3
all_words = file1+file2+file3
only_first = file1-file2-file3

print("Слова у всіх файлах:")
for word in common_words:
    print(word)
print("Кількість:", len(common_words))
print("\nСлова хоча б в одному файлі:")
for word in all_words:
    print(word)
print("Кількість:", len(all_words))
print("\nСлова лише у першому файлі:")
for word in only_first:
    print(word)
print("Кількість:", len(only_first))
