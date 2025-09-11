class LegendArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self):
        return self.size == self.capacity

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
        else:
            print("리스트 overflow 또는 유효하지 않은 삽입 위치")
            exit()

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos < self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            print("리스트 overflow 또는 유효하지 않은 삭제 위치")
            exit()

    def getEntry(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else:
            return None

if __name__ == "__main__":
    legend_array = LegendArray(100)
    print("최초  ", legend_array.array[0:legend_array.size])
    legend_array.insert(0, 10)
    legend_array.insert(0, 20)
    legend_array.insert(1, 30)
    legend_array.insert(legend_array.size, 40)
    legend_array.insert(2, 50)
    print("삽입x5", legend_array.array[0:legend_array.size])
    legend_array.delete(2)
    print("삭제(2)", legend_array.array[0:legend_array.size])
    legend_array.delete(legend_array.size-1)
    print("삭제(E)", legend_array.array[0:legend_array.size])
    legend_array.delete(0)
    print("삭제(0)", legend_array.array[0:legend_array.size])
