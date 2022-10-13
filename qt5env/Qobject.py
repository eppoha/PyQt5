import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        # create label object
        label = QLabel("First QLabel", self)
        
        # set location and width heighth.
        label.setGeometry(100, 100, 200, 50)
        # set style 
        # 设置样式 边框样式：2px 实线 红色
        label.setStyleSheet("""border: 2px solid red""")
        # 水平+垂直居中
        label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        # 打印标签文本内容
        print(label.text())

        self.setGeometry(300, 300, 400, 320)
        self.setWindowTitle('Label')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
