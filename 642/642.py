class Segment:
    def __init__(self, start, end, include_start=True, include_end=True, empty=False):
        self.empty = empty
        if start>end:
            self.empty = True
        self.start=start
        self.end=end
        self.include_start=include_start
        self.include_end=include_end
    def __str__(self):
        if self.empty:
            return "Порожній інтервал"
        left = "[" if self.include_start else "("
        right = "]" if self.include_end else ")"
        return f"{left}{self.start}; {self.end}{right}"

class SegmentSetIterator:
    def __init__(self, segments):
        def get_start(segment):
            return segment.start
        self._segments = list(segments)
        self._segments.sort(key=get_start)
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index<len(self._segments):
            current=self._segments[self._index]
            self._index+= 1
            return current
        raise StopIteration

class SegmentSet:
    def __init__(self):
        self._segments = []
    def add(self, segment):
        if not isinstance(segment, Segment):
            raise TypeError("Можна додавати лише Segment")
        if not segment.empty:
            self._segments.append(segment)
    def __iter__(self):
        return SegmentSetIterator(self._segments)
    def __str__(self):
        if len(self._segments) == 0:
            return "Порожня множина"
        result = ""
        for seg in self:
            result += str(seg) + " U "
        return result[:-3]

def main():
    s1 = Segment(-3, 1)
    s2 = Segment(1, 5, True, False)
    s3 = Segment(10, 20, False, True)
    s4 = Segment(7, 8)
    segment_set = SegmentSet()
    segment_set.add(s2)
    segment_set.add(s1)
    segment_set.add(s4)
    segment_set.add(s3)

    print("Всі інтервали:")
    print(segment_set)
    print("\nІтерація по SegmentSet:")
    for seg in segment_set:
        print(seg)
if __name__ == "__main__":
    main()
