class heap:
    def __init__(self, toheap, size, i):
        """
        :trype: list
        """
        return self.max_heapify(toheap, size, i)

    def max_heapify(self, toheap, size, i):
        l = 2*i
        r = 2*i + 1

        largest = i

        if l < size and toheap[l] > toheap[i]:
            largest = i

        if r < size and toheap[r] > toheap[largest]:
            largest = r

        if largest != i:
            # swap
            toheap[i], toheap[largest] = toheap[largest], toheap[i]
            self.max_heapify(self, toheap, size, largest)
    