class Stack:
    SIZE = 6

    def __init__(self):
        self.x = []

    def _is_emmpty(self):
        if len(self.x) == 0:
            return True

    def _is_full(self):
        if len(self.x) == self.SIZE:
            return True

    def pushItem(self, ele):
        if not self.is_full():
            self.x.append(ele)
        else:
            raise Exception("Stack Limit Exceeded")

    def popItem(self):
        if not self.is_emmpty():
            popedItem = self.x.pop()
            return popedItem
        else:
            raise Exception("Stack is empty")
            
    def get_topItem(self):
        if not self.is_emmpty():
            return self.x[-1]
        else:
            raise Exception("Stack is empty")

    def __str__(self):
        return str(self.x)

if __name__ == "__main__":
    s1 = Stack()
    s1.pushItem(10)
    s1.pushItem(30)
    print(s1.popItem())
    s1.pushItem(100)
    s1.pushItem(300)
    s1.pushItem(1000)
    s1.pushItem(3000)
    s1.pushItem(100000)
    print(s1)
    s1.pushItem(300000)
