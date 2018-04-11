import sys, random
from time import sleep, clock
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

from model import ComplexNumber


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
        # You can set a background if you'd like:
        #
        self.background = QtGui.QPixmap()
        root = QtCore.QFileInfo(__file__).absolutePath()
        self.background.load(root + '/graphics/background.jpg')

        #
        # This is an example of connecting a widget (slider) to an instance variable.
        #
        self.lines = 50


    def paintEvent(self, event):
        """
        By magic, this event occasionally gets called. Maybe on self.update()? It is where you
        call all of the drawing to the screen that you want to do.
        """
        painter = QtGui.QPainter(self)
        rectangle = self.contentsRect()

        #
        # Set Background
        #
        painter.drawPixmap(rectangle, self.background, rectangle)

        #
        # Do any drawing that you need to do next.
        #
        self.draw_random_lines(painter)

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

    def draw_random_lines(self, painter):
        width = self.width()
        height = self.height()
        for x in range(self.lines):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)

            #
            # Just your normal HTML color codes. Look them up.
            #
            red = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            green = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            blue = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            color = QtGui.QColor('#' + red + green + blue)
            penWidth = 1
            pen = QtGui.QPen(color, penWidth)
            painter.setPen(pen)
            painter.drawLine(x1, y1, x2, y2)

    def set_lines(self, lines):
        self.lines = lines
        self.update()

    def mousePressEvent(self, event):
        print("click (display)")

    def mouseReleaseEvent(self, event):
        print("release (display)")

