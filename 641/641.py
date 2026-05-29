class CustomListIterator:
    def __init__(self, data):
        self._odds = []
        self._evens = []
        for x in data:
            if x % 2 != 0:
                self._odds.append(x)
            else:
                self._evens.append(x)
        self._odds.sort()
        self._evens.sort(reverse=True)

        self._index = 0
        self._combined = self._odds + self._evens
    def __iter__(self):
        return self
    def __next__(self):
        if self._index<len(self._combined):
            value= self._combined[self._index]
            self._index+=1
            return value
        raise StopIteration

class CustomList:
    def __init__(self, data=None):
        self._data=[]
        if data is None:
            return
        if isinstance(data, CustomList):
            data=data._data
        for x in data:
            if type(x)!=int:
                raise TypeError("CustomList може містити лише цілі числа")
            self._data.append(x)
    def __iter__(self):
        return CustomListIterator(self._data)
    def __str__(self):
        return f"CustomList({self._data}), size={len(self._data)}"
    def __len__(self):
        return len(self._data)
    def __getitem__(self, index):
        return self._data[index]
    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("Тільки int")
        self._data[index] = value
    def __contains__(self, item):
        return item in self._data
    def __iadd__(self, other):
        if isinstance(other, CustomList):
            self._data.extend(other._data)
        elif isinstance(other, int):
            self._data.append(other)
        else:
            return NotImplemented
        return self
cl = CustomList()
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        for part in line.split():
            if part.lstrip("-").isdigit():
                cl += int(part)
print("Елементи у спеціальному порядку:")
for x in cl:
    print(x)
