class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.topAndBottom = ""
        self.mid = ""

    def draw(self):
        if self.width > 1 and self.height > 1:
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
        elif self.width == 1 and self.height > 0:
            for i in range(self.height):
                print("*")
        elif self.height == 1 and self.width > 0:
            self.topAndBottom += "* "
            for i in range(self.width - 2):
                self.topAndBottom += "* "
            self.topAndBottom += "*"
            print(self.topAndBottom)
        else:
            print("Cannot show a rectangle with a side length of Zero or less.")

newRectangle = rectangle(5, 5)
newRectangle.draw()
