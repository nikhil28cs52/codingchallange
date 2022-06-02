class demo:
    def __init__(self):
        self.x = 10

    def print_str(self):
        print('hello world')


class demo1(demo):
    def value(self):
        pass

c2 = demo1()

c2.print_str()