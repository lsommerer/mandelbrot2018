
from PyQt5 import QtWidgets
import sys
from view-interface import MainWindow

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