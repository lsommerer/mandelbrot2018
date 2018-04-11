from model import ComplexNumber, ComplexPlane


class MandelbrotController(object):

    def __init__(self, xResolution, yResolution):
        self.xResolution = xResolution
        self.yResolution = yResolution
        self.upperLeft = ComplexNumber(-3, 3)
        self.lowerRight = ComplexNumber(3, -3)
        self.depth = 10

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