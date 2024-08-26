#1.

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is: {self.i}, {self.j}")
class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def showw(self):
        print(f"The vector is: {self.i}, {self.j}, {self.k}")

TwoD = TwoDVector(2,3)
TwoD.show()

ThreeD = ThreeDVector(2,3,4)
ThreeD.showw()
