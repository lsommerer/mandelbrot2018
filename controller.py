from model import ComplexNumber, ComplexPlane


class MandelbrotController(object):

    def __init__(self, xResolution, yResolution):
        self.xResolution = xResolution
        self.yResolution = yResolution
        self.upperLeft = ComplexNumber(-2, 1.5)
        self.lowerRight = ComplexNumber(1, -1.5)
        self.depth = 10

        self.plane = ComplexPlane(self.upperLeft, self.lowerRight, xResolution, yResolution)

    def quit(self):
        pass

    def new(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass

    def about(self):
        pass