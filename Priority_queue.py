class PriorityQueue:
    def __init__(self):
        self.queue = [ ]

    def isempty(self):
        return True if len(self.queue) == 0 else False

    def getsize(self):
        return len(self.queue)

    def getmin(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[ 0 ]

    def insert(self, data):
        self.queue.append(data)

        CI = len(self.queue) - 1

        while (CI > 0):
            PI = (CI - 1) // 2
            if self.queue[ CI ] < self.queue[ PI ]:
                self.queue[ CI ], self.queue[ PI ] = self.queue[ PI ], self.queue[ CI ]
            else:
                break

            CI = PI

    def remove_min(self):
        if len(self.queue) == 0:
            return None

        PI = 0
        ans = self.queue[0]
        self.queue[ 0 ], self.queue[ len(self.queue)-1 ] = self.queue[ len(self.queue)-1], self.queue[ 0 ]
        self.queue.pop()
        CI = len(self.queue)
        while True:
            LCI = 2 * PI + 1
            RCI = 2 * PI + 2
            min_idx = PI

            if LCI < len(self.queue)  and self.queue[ LCI ] < self.queue[ min_idx ]:
                min_idx = LCI
            if RCI < len(self.queue) and self.queue[ RCI ] < self.queue[ min_idx ]:
                min_idx = RCI

            if PI == min_idx:
                break

            self.queue[PI],self.queue[min_idx] = self.queue[min_idx], self.queue[PI]

            PI = min_idx
        return ans

    def display(self):
        print(self.queue)




