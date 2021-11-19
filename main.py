from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QMainWindow, QApplication
from PyQt5.QtCore import Qt
import sys
import random


hiragana = """
あいうえお
かきくけこ
さしすせそ
たちつてと
なにぬねの
はひふへほ
まみむめも
やゆよ
らりるれろ
わを
"""

katakana = """
アイウエオ
カキクケコ
サシスセソ
タチツテト
ナニヌネノ
ハヒフヘホ
マミムメモ
ヤユヨ
ラリルレロ
ワヲ
"""

hangul = """
아이우에오
카키쿠케코
사시스세소
타치츠테토
나니누네노
하히후헤호
마미무메모
야유요
라리루레로
와오"""

hiragana = "".join(hiragana.split())
katakana = "".join(katakana.split())
hangul = "".join(hangul.split())
kana_to_ko = {}

for hira, kata, han in zip(hiragana, katakana, hangul):
    kana_to_ko[hira] = han
    kana_to_ko[kata] = han

class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def change(self):
        if kana_to_ko[self.kanaLabel.text()] == self.inputTxt.text():
            self.kanaLabel.setText(random.choice(list(kana_to_ko.keys())))
        self.inputTxt.setText("")

    def initUI(self):
        self.kanaLabel = QLabel(self)
        self.kanaLabel.setText(random.choice(list(kana_to_ko.keys())))
        self.kanaLabel.setAlignment(Qt.AlignCenter)

        font1 = self.kanaLabel.font()
        font1.setPointSize(60)


        self.kanaLabel.setFont(font1)

        self.inputTxt = QLineEdit()
        self.inputTxt.returnPressed.connect(self.change)

        layout = QVBoxLayout()
        layout.addWidget(self.kanaLabel)
        layout.addWidget(self.inputTxt)

        self.setLayout(layout)
        self.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Kana Practice')
        self.setGeometry(300, 300, 300, 200)
        self.setCentralWidget(MainWidget())
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
