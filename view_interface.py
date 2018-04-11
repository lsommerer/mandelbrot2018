import sys
from PyQt5 import QtGui, QtCore, QtWidgets

from view_display import MandelbrotWidget
from controller import MandelbrotController


class MyApplication(QtWidgets.QMainWindow):
    def __init__(self, app):
        #
        # MainWindow is, as you might expect, the main window
        # of an application. It supports menus, statusbars,
        # toolbars and probably other stuff.
        #
        # Call __init__ for the parent class to initialize things.
        super(MyApplication, self).__init__()

        #
        # Keep a reference to the app so we can explicitly call self.app.processEvents().
        # You won't have to worry about this for a while. You'll know when you need it.
        #
        self.app = app

        #
        # Setup the main display window.
        #
        self.setup_window()

        #
        # The Controller is where the code will live that serves an an interface between
        # our View (all the PyQt UI code) and our Model (the Mandelbrot set code).
        #
        self.controller = MandelbrotController(self.geometry().width(), self.geometry().height())

        #
        # Initialize the widget that will act as the display.
        #
        self.display = MandelbrotWidget(self.controller)
        self.setCentralWidget(self.display)
        self.display.show()

        #
        # Create actions, menus, toolbars and statusbar
        #
        self.create_actions()
        self.create_menus()
        self.create_tool_bars()
        self.create_status_bar()

        #
        # This example only has one item in the main window. If you write
        # a program where you have multiple items in the main window then
        # you can control the layout of those items. Layout here means
        # the relationship between the items on the screen. This can
        # become complicated as users resize things, so "layouts" really
        # help with that.
        #
        # There are: Vertical Box Layouts (QVBoxLayout), Horizontal Box
        # Layouts (QHBoxLayout) and Grid Layouts (QGridLayout).
        #
        # Try it without these lines commented out. It is a subtle difference.
        # See the layouts examples for, well, examples.
        #
        #mainLayout = QtWidgets.QVBoxLayout()
        #mainLayout.addWidget(self.display)
        #self.setLayout(mainLayout)

    def setup_window(self):
        """
        Just putting a bunch of loosely related window setup stuff together here. This could
        have gone in __init__(), but it was getting long.
        """
        #
        # Starting size of window. I don't think this is required.
        #
        xSize = 500
        ySize = 400
        self.resize(xSize, ySize)

        #
        # Starting coordinates of the window. This centers it on the desktop. Optional.
        #
        desktop = QtWidgets.QDesktopWidget().screenGeometry()
        myWindow = self.geometry()
        xLocation = (desktop.width() - myWindow.width()) / 2
        yLocation = (desktop.height() - myWindow.height()) / 2
        self.move(xLocation, yLocation)

        #
        # Misc window settings that you can use.
        #
        self.setWindowTitle("Title of my program")
        self.setWindowIcon(QtGui.QIcon('./icons/hexagon.png'))
        self.statusBar().showMessage('Ready')

    def create_actions(self):
        """
        Setup an action that can be associated with menus, buttons, shortcuts and taskbars.
        Anything action that is initiated by interacting with the user interface (as opposed
        to clicking directly in a window is setup here.
        """
        #
        # Root is where the application exists in the directory structure.
        #
        root = QtCore.QFileInfo(__file__).absolutePath()

        self.exitAction = QtWidgets.QAction("E&xit", self,
                                            shortcut="Ctrl+Q",
                                            statusTip="Exit the application",
                                            triggered=self.quit)

        self.newAction = QtWidgets.QAction(QtGui.QIcon(root + '/icons/new.png'),   # Note that icon is optional.
                                           "&New", self,
                                           shortcut=QtGui.QKeySequence.New,  #Some shortcuts are defined by the OS.
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
                                             statusTip="More information about the Mandelbrot Set",
                                             triggered=self.about)

        #
        # Not all actions are available at all times. This is how you set that.
        #
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
        self.depthSlider = QtWidgets.QSlider()
        self.depthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.depthSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.depthSlider.setTickInterval(100)
        self.depthSlider.setMinimum(0)
        self.depthSlider.setMaximum(1000)
        self.depthSlider.setValue(50)
        self.depthSlider.setMaximumWidth(300)
        self.depthSlider.setMinimumWidth(150)
        self.fileToolBar.addWidget(self.depthSlider)

        #
        # Connect the slider to a method. Note that the value of the slider is
        # automatically sent to the method as the first parameter. Wouldn't it
        # be nice if it only updated when the user was finished moving it?
        #
        self.depthSlider.valueChanged.connect(self.display.set_lines)

    def create_status_bar(self):
        self.statusBar().showMessage("Ready")
        #
        # You can also add widgets to the statusBar
        #
        # self.progressBar = QtWidgets.QProgressBar(self.statusBar())
        # self.progressBar.hide()
        # self.statusBar().addPermanentWidget(self.progressBar)

    def new(self):
        self.controller.new()
        self.update()

    def open(self):
        self.controller.open()

    def save(self):
        self.controller.save()

    def save_as(self):
        self.controller.save_as()

    def quit(self):
        self.controller.quit()
        self.close()

    def about(self):
        self.controller.about()
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
