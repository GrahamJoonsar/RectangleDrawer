class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.topAndBottom = ""
        self.mid = ""

    def draw(self):
        self.topAndBottom += "* "
        for i in range(self.width - 2):
            self.topAndBottom += "* "
        self.topAndBottom += "*"
        print(self.topAndBottom)
        self.mid += "*"
        for i in range(len(self.topAndBottom)-2):
            self.mid += " "
        self.mid += "*"
        for i in range(self.height-2):
            print(self.mid)
        print(self.topAndBottom)

newRectangle = rectangle(5, 5)
newRectangle.draw()
