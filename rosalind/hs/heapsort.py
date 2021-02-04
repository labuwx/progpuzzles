class Heap:
    # def __init__(self, l=[]):
    # self.d = []
    # for x in l:
    # self.insert(x)

    def __init__(self, l=[]):
        self.d = list(l)
        for i in range(len(l) - 1, -1, -1):
            self.__sift_down(i)

    def insert(self, x):
        self.d.append(x)
        new_idx = len(self.d) - 1
        self.__sift_up(new_idx)

    def mindel(self):
        x = self.d.pop()
        if self.d:
            x, self.d[0] = self.d[0], x
            self.__sift_down(0)
        return x

    @staticmethod
    def __p(i):
        if i:
            return (i - 1) // 2
        else:
            return None

    def __c(self, i):
        c1, c2 = 2 * i + 1, 2 * i + 2
        if c1 >= len(self.d):
            c1 = None
        if c2 >= len(self.d):
            c2 = None
        if c2 != None and self.d[c1] > self.d[c2]:
            c1, c2 = c2, c1
        return c1, c2

    def __sift_up(self, i):
        p = self.__p(i)
        if p == None:
            return
        if self.d[i] < self.d[p]:
            self.d[i], self.d[p] = self.d[p], self.d[i]
            self.__sift_up(p)

    def __sift_down(self, i):
        c, _ = self.__c(i)
        if c == None:
            return
        if self.d[c] < self.d[i]:
            self.d[i], self.d[c] = self.d[c], self.d[i]
            self.__sift_down(c)


def sort(l):
    h = Heap(l)
    l1 = [h.mindel() for _ in l]
    return l1
