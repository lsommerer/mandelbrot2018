import sys, random
from time import sleep, clock
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

from mandelbrot_model import Complex


class MandelbrotWidget(QtWidgets.QWidget):

    def __init__(self, mainWindow, parent=None):
        super(MandelbrotWidget, self).__init__(parent)

        self.mainWindow = mainWindow
        #
        # If you are going to use a timer, create one.
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
        # This next section is code specific to our application.
        #
        self.upperLeft = Complex(-3, 3)
        self.lowerRight = Complex(3, -3)
        self.depth = 10
        self.rectangle = 0  # arbitrary initial value to check changes against

    def paintEvent(self, event):
        """By magic, this event occasionally gets called. Maybe on self.update()?"""
        painter = QtGui.QPainter(self)
        rectangle = self.contentsRect()
        #
        # Redraw everything if the screen size changes (or on first run)
        #
        if rectangle != self.rectangle:
            print('Need to update background.')
            self.background = self.background.copy()
            backgroundPainter = QtGui.QPainter(self.background)
            #
            # Put anything you need to redraw the same each time in here.
            #
            pass
        #
        # Set Background
        #
        painter.drawPixmap(rectangle, self.background, rectangle)
        #
        # Do any drawing that you need to do next.
        #
        width = self.width()
        height = self.height()
        self.complexPlane =
        for x in range(500):
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            red = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            green = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            blue = random.choice(['ff', 'dd', '99', '66', '33', '00'])
            color = QtGui.QColor('#' + red + green + blue)
            penWidth = 1
            pen = QtGui.QPen(color, penWidth)
            painter.setPen(pen)
            painter.drawLine(x1, y1, x2, y2)
        #
        # Store the current screen size, to check for changes later.
        #
        self.rectangle = rectangle

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

    def draw_head(self, painter, worm):
        """Draw a little head on each worm."""
        x, y = self.world_location_to_screen_coord(worm.location.x, worm.location.y)
        center = QtCore.QPoint(x, y)
        color = QtGui.QColor(worm.color).lighter()
        for width, radius, alpha in [(7, 12, 4), (6, 10, 8), (5, 8, 16), (4, 6, 32), (3, 4, 64), (2, 2, 128),
                                     (1, 1, 255)]:
            color.setAlpha(alpha)
            pen = QtGui.QPen(color, width)
            painter.setPen(pen)
            painter.drawEllipse(center, radius, radius)

    def draw_all_segments(self, painter):
        """Draw the paths taken by the worms so far."""
        allWorms = self.world.worms + self.world.deadWorms
        for worm in allWorms:
            if worm.is_alive():
                color = QtGui.QColor(worm.color)
            else:
                color = QtGui.QColor(worm.color).darker(150)
            for segment in worm.segments:
                #
                # I can't draw across the screen correctly yet, so this is the
                # temporary fix to just not draw the literal edge case.
                #
                if (abs(segment.xStart - segment.xEnd) <= 2) and (abs(segment.yStart - segment.yEnd) <= 2):
                    x1, y1 = self.world_location_to_screen_coord(segment.xStart, segment.yStart)
                    x2, y2 = self.world_location_to_screen_coord(segment.xEnd, segment.yEnd)
                    for width, alpha in [(11, 4), (9, 8), (7, 16), (5, 32), (3, 64), (1, 255)]:
                        color.setAlpha(alpha)
                        pen = QtGui.QPen(color, width)
                        painter.setPen(pen)
                        painter.drawLine(x1, y1, x2, y2)
                else:
                    pass

        # width = self.width()
        # height = self.height()
        # for x in range(100):
        #     x1 = random.randint(0,width)
        #     y1 = random.randint(0,height)
        #     x2 = random.randint(0,width)
        #     y2 = random.randint(0,height)
        #     red = random.choice(['ff','cc','99','66','33','00'])
        #     green = random.choice(['ff','cc','99','66','33','00'])
        #     blue = random.choice(['ff','cc','99','66','33','00'])
        #     color = QtGui.QColor('#'+red+green+blue)
        #     pen = QtGui.QPen(color, 2)
        #     painter.setPen(pen)
        #     #painter.drawLine(x1,y1,x2,y2)
        #     center = QtCore.QPoint(x1,y1)
        #     radius = x2
        #     painter.drawEllipse(center,radius,radius)
