from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget
import sys
import qtmodern.styles
import qtmodern.windows

class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Center the app')
        self.center()
        mw = qtmodern.windows.ModernWindow(self)
        mw.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()

        qr.moveCenter(cp)

        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qtmodern.styles.dark(app)
    demo = Demo()
    sys.exit(app.exec_())
