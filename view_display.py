import sys, random
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

class MandelbrotWidget(QtWidgets.QWidget):

    def __init__(self, controller, parent=None):
        super(MandelbrotWidget, self).__init__(parent)

        #
        # Pass in the controller because we'll need some information from it
        # in order to draw the Mandelbrot Set. In the past I've passed in the
        # whole app, but I don't think I need all that (could be wrong).
        #
        self.controller = controller

        #
        # If you are going to use a timer, create one. Oh, and look up timers.
        #
        self.timer = QtCore.QBasicTimer()
        self.timer.stop()

        #
        # I'm not actually sure why I thought this was a good idea.
        # Someone should really look into this.
        #
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        #
        # You can set a background if you'd like, but we are overriding it next in this case.
        #
        #self.background = QtGui.QPixmap()
        #root = QtCore.QFileInfo(__file__).absolutePath()
        #self.background.load(root + '/graphics/background.jpg')

        #
        # You can have a painter draw directly onto this widget, but you have more
        # options when you draw on an image. We will do that a little later.
        #
        self.image = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_RGB32)
        self.image.fill(0)

    def paintEvent(self, event):
        """
        By magic, this event occasionally gets called. Maybe on self.update()? Certainly on
        a window resize.
        """
        painter = QtGui.QPainter(self)
        rectangle = self.contentsRect()

        #
        # Set Background
        #
        #painter.drawPixmap(rectangle, self.background, rectangle)

        #
        # Note that this isn't quite right, because when we resize we also need to
        # let the controller know that the resolutoin is different so that it can
        # supply the correct points in the future.
        #
        newSize = self.size()
        self.image = self.image.scaled(newSize)
        painter.drawImage(0, 0, self.image)


        #
        # Do any drawing that you need to do next.
        #
        self.mandelbrot_random_walk()

    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_Right, QtCore.Qt.Key_Up]:
            print('up')
        elif event.key() in [QtCore.Qt.Key_Left, QtCore.Qt.Key_Down]:
            print('down')
        elif event.key() in [QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return, QtCore.Qt.Key_Space]:
            print('select')
            self.update()

    def wheelEvent(self, event):
        """should work a lot like keypress..."""
        if event.angleDelta().y() > 0:
            print('up')
        else:
            print('down')

    def mandelbrot_random_walk(self):
        #
        # Get the pixels in random order.
        #
        pixels = []
        for pixel in self.controller.plane.all_points():
            pixels.append(pixel)
        random.shuffle(pixels)

        point = 0
        x = 1
        y = 2

        painter = QtGui.QPainter(self.image)

        for pixel in pixels[:500]:
            if pixel[point].in_mandelbrot(self.controller.depth):
                painter.setPen(QtCore.Qt.white)
                painter.drawPoint(pixel[x], pixel[y])


    def set_depth(self, depth):
        self.controller.depth = depth
        self.update()

    def mousePressEvent(self, event):
        print("click (display)")

    def mouseReleaseEvent(self, event):
        print("release (display)")

