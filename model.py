
class ComplexNumber(complex):
    """
    In the past, I've had classes write their own complex number class, but seeing as we're a little
    pressed for time, and that you hvae done just a little more with objects than they did in the past,
    we will just inherit from Python's built in complex number class.
    """

    def in_mandelbrot(self, maxDepth = 10):
        """
        Returns True if this complex number is a member of the Mandelbrot Set. The Mandelbrot Set is the
        set of complex numbers that does not diverge when the number is repeatedly multiplied by itself
        and then increased by the original number.
        :param maxDepth: How many times to iterate before deciding membership
        :return: Boolean
        """
        inSet = False
        currentDepth = 0
        point = ComplexNumber(self.real, self.imag)
        while (currentDepth < maxDepth) and (abs(point) < 2):
            currentDepth += 1
            point = (point * point) + self
        if currentDepth == maxDepth:
            inSet = True
        return inSet

class ComplexPlane(object):

    def __init__(self, corner1, corner2, xResolution, yResolution):
        """
        Define a complex plane
        :param corner1: A ComplexNumber representing any corner of the bounding box of the plane.
        :param corner2: A ComplexNumber representing the opposite corner of the bounding box of the plane.
        :param xResolution: The number of pixels between the low and high real values on the plane.
        :param yResolution: The number of pixels between the low and high complex values on the plane.
        """
        self.corner1 = corner1
        self.corner2 = corner2
        self.xResolution = xResolution
        self.yResolution = yResolution
        #
        # From the given (opposite) corners, compute the minimums & maximums
        # for the real and imaginary values. We have to do this because we don't
        # know if the user passed in the lowerLeft and upperRight corners, the
        # the upperRight and lowerLeft corners, the lowerRight and upper Left
        # corners or the upperLeft, lowerRight corners.
        #
        minReal = min(corner1.real,corner2.real)
        minImag = min(corner1.imag,corner2.imag)
        maxReal = max(corner1.real,corner2.real)
        maxImag = max(corner1.imag,corner2.imag)
        self.min = ComplexNumber(minReal,minImag)
        self.max = ComplexNumber(maxReal,maxImag)
        #
        # pre-compute the distance between the imaginary numbers given
        # the resolution of the graphics window.
        #
        self.realDistance = (self.max.real - self.min.real) / self.xResolution
        self.imagDistance = (self.max.imag - self.min.imag) / self.yResolution
        #
        # A potential problem with this implementation is if the user gives
        # corners and resolutions that don't match up, like this:
        #
        #   #######C       ..................
        #   #      #       ..................
        #   #      #       ..................
        #   #      #
        #   #      #
        #   C#######
        #
        # Anything that we display based on those corners onto that set of
        # pixels will be very distorted. There are times where you will
        # want to check for that and change the corners to match what you
        # can actually display. But you can ignore that for now.

    def point(self,x,y):
        """given x,y coordinates, return the associated complex number."""
        complexNumber = ComplexNumber(self.min.real+(x*self.realDistance),
                                      self.min.imag+(y*self.imagDistance))
        return complexNumber

    def pixel(self,complexNumber):
        """
        Given a complex number, return the x,y coordinates of the associated pixel. See if you
        can implement this.
        """
        pass

    def all_points(self):
        """
        Allow someone to iterate through all of the pixels that make up this complex plane. Note that we can't
        iterate over the points, because there are an infinite number of them.

        usage:
                for complexNumber, x, y in myComplexPlane:
                    if complexNumber.in_mandelbrot():
                        draw_dot_at(x,y)                 <---- not a real function!

        """
        for x in range(1,self.xResolution):
            for y in range(1,self.yResolution):
                yield self.point(x,y), x, y

def main():
    upperLeft = ComplexNumber(-2, 2)
    lowerRight = ComplexNumber(2, -2)
    xResolution = 10
    yResolution = 10
    plane = ComplexPlane(upperLeft, lowerRight, xResolution, yResolution)
    print(plane.min)
    print(plane.max)
    print(plane.point(1,1))
    for complexNumber, x, y in plane.all_points():
       print(f'({x},{y}) = {complexNumber}')


if __name__ == '__main__':
    main()

