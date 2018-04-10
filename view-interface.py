import sys
from PyQt5 import QtGui, QtCore, QtWidgets

from mandelbrot_view import MandelbrotWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        #
        # MainWindow is, as you might expect, the main window
        # of an application. It supports menus, statusbars,
        # toolbars and probably other stuff.
        #
        # Call __init__ for the parent class to initialize things.
        super(MainWindow, self).__init__()
        #
        # Keep a reference to the app so we can explicitly call self.app.processEvents()
        #
        self.app = app
        #
        # Initialize the widget that will act as the display.
        #
        self.display = MandelbrotWidget(self)
        self.setCentralWidget(self.display)
        #
        # Create actions, menus, toolbars and statusbar
        #
        self.create_actions()
        self.create_menus()
        self.create_tool_bars()
        self.create_status_bar()
        #
        # Setup the main display window.
        #
        self.setup_window()
        #
        # I don't know if we need this stuff or not. Tutorials vary.
        #
        #
        # Create a seperate widget to control the layout of our window.
        # This example shows the Vertical Box Layout (QVBoxLayout). You
        # could also do a horizontal box (QHBoxLayout) or a grid layout
        # (QGridLayout).
        #
        # mainWidget = QtWidgets.QWidget(self)
        # self.setCentralWidget(mainWidget)
        # mainLayout = QtWidgets.QVBoxLayout()
        # mainLayout.addWidget(self.display)
        # self.setLayout(mainLayout)
        self.display.show()

    def setup_window(self):
        """Just putting a bunch of loosely related window setup stuff together here."""
        # Starting size of window. I don't think this is required.
        xSize = 500
        ySize = 400
        self.resize(xSize, ySize)
        # Starting coordinates of the window will be centered.
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        xLocation = (screen.width() - size.width()) / 2
        yLocation = (screen.height() - size.height()) / 2
        self.move(xLocation, yLocation)
        # Get things ready
        self.setWindowTitle("Mandelbrot Set")
        self.setWindowIcon(QtGui.QIcon('./icons/hexagon.png'))
        self.statusBar().showMessage('Ready')

    def create_actions(self):
        """Setup an action that can be associated with menus, buttons,
           shortcuts and taskbars."""
        #
        # Root is where the application exists in the directory structure.
        #
        root = QtCore.QFileInfo(__file__).absolutePath()

        self.exitAction = QtWidgets.QAction("E&xit", self,
                                            shortcut="Ctrl+Q",
                                            statusTip="Exit the application",
                                            triggered=self.quit)

        self.newAction = QtWidgets.QAction(QtGui.QIcon(root + '/icons/new.png'),
                                           "&New", self,
                                           shortcut=QtGui.QKeySequence.New,
                                           statusTip="Start a new fractal",
                                           triggered=self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon(root + '/icons/open.png'),
                                            "&Open", self,
                                            shortcut=QtGui.QKeySequence.Open,
                                            statusTip="Open a previous fractal",
                                            triggered=self.open)

        self.saveAction = QtWidgets.QAction(QtGui.QIcon(root + '/icons/save.png'),
                                            "&Save", self,
                                            shortcut=QtGui.QKeySequence.Save,
                                            statusTip="Save the current fractal",
                                            triggered=self.save)

        self.saveAsAction = QtWidgets.QAction("Save &As", self,
                                              shortcut=QtGui.QKeySequence.SaveAs,
                                              statusTip="Save the current fractal under a new name",
                                              triggered=self.save_as)

        self.aboutAction = QtWidgets.QAction("&About", self,
                                             statusTip="More information about Paterson's Worms",
                                             triggered=self.about)

        self.openAction.setEnabled(False)
        self.saveAction.setEnabled(False)
        self.saveAsAction.setEnabled(False)

    def create_menus(self):
        """Create a menubar and add a menu and an action."""

        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.saveAsAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)

        self.menuBar().addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction(self.aboutAction)

    def create_tool_bars(self):
        """Create a toolbar and add an action to it."""

        self.fileToolBar = self.addToolBar("File")
        self.fileToolBar.addAction(self.newAction)
        self.fileToolBar.addAction(self.openAction)
        self.fileToolBar.addAction(self.saveAction)

        #
        # Lets add an ugly slider to the toolbar.
        #
        self.speedSlider = QtWidgets.QSlider()
        self.speedSlider.setOrientation(QtCore.Qt.Horizontal)
        self.speedSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.speedSlider.setTickInterval(100)
        self.speedSlider.setMinimum(1)
        self.speedSlider.setMaximum(1000)
        self.speedSlider.setValue(500)
        self.speedSlider.setMaximumWidth(300)
        self.speedSlider.setMinimumWidth(150)
        # self.speedSlider.valueChanged.connect(self.display.set_timer_base_speed)
        self.fileToolBar.addWidget(self.speedSlider)

    def create_status_bar(self):
        self.statusBar().showMessage("Ready")
        #
        # You can also add widgets to the statusBar
        #
        # self.progressBar = QtWidgets.QProgressBar(self.statusBar())
        # self.progressBar.hide()
        # self.statusBar().addPermanentWidget(self.progressBar)

    def new(self):
        pass

    def open(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass

    def quit(self):
        self.close()

    def about(self):
        QtWidgets.QMessageBox.about(self, "Mandelbrot Set",
                                    "I should <b>probably</b> put some "
                                    "real text in here.")

    def mousePressEvent(self, event):
        print("click")

    def mouseReleaseEvent(self, event):
        print("release")

    def keyPressEvent(self, event):
        print("key press")

    def keyReleaseEvent(self, event):
        print("key release")


def main():
    #
    # Setup the application and pass it any command line
    # arguments that might be present.
    #
    app = QtWidgets.QApplication(sys.argv)
    #
    # Create a new window and show it to the user. Then
    # start the applications main event loop.
    #
    mainWin = MainWindow(app)
    mainWin.show()
    #
    # Execute the application (and hence the window), enter the application's
    # main event loop, and service user requests until the user terminates the
    # application. Then exit returning and exit conditions.
    #
    exitCondition = app.exec_()
    sys.exit(exitCondition)


if __name__ == '__main__':
    main()
