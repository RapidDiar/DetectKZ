import os
import glob
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from Change import Ui_Form
import sys
import codecs

KZ_string = []
final_kz = []
final_not = []
path = os.getcwd()
step = 0

class ch_window(QtWidgets.QMainWindow):
    def __init__(self):
        global step
        global final_kz
        global final_not
        super(ch_window,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.YES_button)
        self.ui.pushButton_2.clicked.connect(self.NO_button)
        self.Setting()
        self.Save()
        self.ui.label.setText(KZ_string[step])
        self.ui.label_2.setText("KZ"+str(len(final_kz))+"\t"*2+str(step+1)+' из '+str(len(KZ_string)+1)+"\t\tNOT"+str(len(final_not)))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z:
            self.YES_button()
        elif event.key() == Qt.Key_M:
            self.NO_button()

    def Setting(self):
        global step
        global path
        path = os.getcwd()
        os.chdir(path + '/OutputKZ/')
        for KZ_txt in glob.glob("*.txt"):
            open_txt = codecs.open(path+"/OutputKZ/" + KZ_txt, "r", "utf_8_sig")
            line_txt = open_txt.readlines()
            for x in line_txt:
                KZ_string.append(x)
        os.chdir(path)
        for s_file in glob.glob("Setting.txt"):
            if s_file == "Setting.txt":
                setting_file = codecs.open(path + "/Setting.txt", "r", "utf_8_sig")
                step = int(setting_file.readline())
                print(step)
            else:
                step = 0
                print(step)
        print('Success')

    def Save(self):
        os.chdir(path + "/Final")
        for s_txt_file in glob.glob("*.txt"):
            if s_txt_file == "Final_KZ.txt":
                open_kz = codecs.open(s_txt_file, "r","utf_8_sig")
                line_open_kz = open_kz.readlines()
                for word in line_open_kz:
                    final_kz.append(word)

            elif s_txt_file == "Final_NOT.txt":
                open_not = codecs.open(s_txt_file, "r","utf_8_sig")
                line_open_not = open_not.readlines()
                for word in line_open_not:
                    final_not.append(word)

    def YES_button(self):
        global path
        global step
        global final_kz
        global KZ_string
        global setting_file
        step = step + 1
        if step >len(KZ_string):
            self.ui.label.text("END")
        else:
            final_kz.append(self.ui.label.text())
            setting_file = codecs.open(path+"/Setting.txt","w+","utf_8_sig")
            setting_file.write(str(step))
            setting_file.close()
            final_txt_kz = codecs.open(path+"/Final/Final_KZ.txt","w+","utf_8_sig")
            for x in final_kz:
                final_txt_kz.write(x)
            final_txt_kz.close()
            self.ui.label_2.setText("KZ"+str(len(final_kz))+"\t"*2+str(step+1)+' из '+str(len(KZ_string)+1)+"\t\tNOT"+str(len(final_not)))
            self.ui.label.setText(KZ_string[step])

    def NO_button(self):
        global path
        global step
        global final_not
        global KZ_string
        global setting_file
        step = step + 1
        if step > len(KZ_string):
            self.ui.label.text("END")
        else:
            final_not.append(self.ui.label.text())
            setting_file = codecs.open(path+"/Setting.txt","w+","utf_8_sig")
            setting_file.write(str(step))
            setting_file.close()
            final_txt_not = codecs.open(path+"/Final/Final_NOT.txt","w+","utf_8_sig")
            for x in final_not:
                final_txt_not.write(x)
            final_txt_not.close()
            self.ui.label_2.setText("KZ"+str(len(final_kz))+"\t"*2+str(step+1)+' из '+str(len(KZ_string)+1)+"\t\tNOT"+str(len(final_not)))
            self.ui.label.setText(KZ_string[step])

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = ch_window()
    application.show()
    sys.exit(app.exec())

