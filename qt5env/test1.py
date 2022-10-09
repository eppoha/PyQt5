# 1.导包
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 2.创建窗口类
# 继承 QWidge ，实例化 Example 就相当于实例化 QWidge。QWidge 控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口。
class Example(QWidget):
    # 4.调用 initUI 方法
    def __init__(self):

    # 继承并调用 QWidge 的 `__init__()` 方法。
        super().__init__()

        self.initUI()

    # 3.自定义 initUI 方法，功能：对窗口做以下列的操作
    # 比如设置窗口的位置、大小、图标、标题等等
    def initUI(self):

        # 设置窗口大小、位置坐标
        self.setGeometry(400, 300, 400, 300)

        # 设置窗口标题
        self.setWindowTitle('Hello 我的第一个qt应用')

        # 展示 UI 界面。
        self.show()


# 5.实例化 Example 类，同学们可以当作此为一个固定写法
if __name__ == '__main__':

    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
