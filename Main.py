from PyQt5 import QtWidgets
from QMain import Ui_MainWindow
import sys
import shutil

import re
from googletrans import Translator
import os
from google.cloud import translate_v2 as translate

file_txt = 'AAA'
path = os.getcwd()
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.file_button_open)
        self.ui.pushButton_2.clicked.connect(self.run_filter)

    def file_button_open(self):
        global path
        global file_txt
        files_name = ['/Input','/Output','/OutputKZ','/OutputNot','/Final']
        for x in files_name:
            if path+x == path+x:
                print("none")
            else:
                os.mkdir(path + x)
            #os.mkdir(path + x)
        QF = QtWidgets.QFileDialog()
        txt_file = QF.getOpenFileName(self, "Open File", path)[0]
        result = re.sub(r'[/\[\]\']','',str(re.findall(r'[/\]['']\w+.\w+$',txt_file)))
        file_txt = ''.join(result)
        print(txt_file)
        shutil.move(str(txt_file), str(path + '/Input/' + file_txt))
        print(file_txt)



    def run_filter(self):
        global path
        global file_txt
        print(file_txt)
        # ---------------------------------------------------GOOGLE TRANSLATE API-----------------------------------------------------
        os.environ[
            'GOOGLE_APPLICATION_CREDENTIALS'] = r" Google Translate API File "
        translate_client = translate.Client()

        # ----------------------------------------------------------------------------------------------------------------------------
        read_file = open(path+'/Input/' + file_txt, "r")
        line = read_file.readlines()

        string = []
        before_google_string = []

        for x in line:
            string.append(x)

        for x in range(len(string)):
            string[x] = re.sub(
                r"[~`!@#$%^&*)(_+=,.\"/№';}<>\{|\]\[¬:⌘«»‹›‘’“”„‚❝ ❞£¥€$¢¬¶@§®©™°×π±√‰Ω∞≈÷~≠¹²³½¼¾|⁄\ \[\]{}†‡…·•●⌥⌃⇧↩¡¿‽⁂∴∵◊※←→↑↓☜☞☝☟✔★☆♺☼☂☺☹☃✉✿✄✈✌✎♠♦♣♥♪♫♯♀♂αßÁáÀàÅåÄäÆæÇçÉéÈèÊêÍíÌìÎîÑñÓóÒòÔôÖöØøÚúÙùÜüŽž\"\"0123456789QqRrWwYUuSsDdGgJjLlZzVvNnmETtyPfhkXxBb]",
                '', string[x])
            string[x] = re.sub(r'[F]', 'Ғ', string[x])
            string[x] = re.sub('r[I]', 'І', string[x])
            string[x] = re.sub('r[i]', 'і', string[x])
            string[x] = re.sub('r[e]', 'е', string[x])
            string[x] = re.sub('r[O]', 'О', string[x])
            string[x] = re.sub('r[o]', 'о', string[x])
            string[x] = re.sub('r[P]', 'Р', string[x])
            string[x] = re.sub('r[p]', 'р', string[x])
            string[x] = re.sub('r[A]', 'А', string[x])
            string[x] = re.sub('r[a]', 'а', string[x])
            string[x] = re.sub('r[H]', 'Н', string[x])
            string[x] = re.sub('r[C]', 'С', string[x])
            string[x] = re.sub('r[c]', 'с', string[x])
            string[x] = re.sub('r[M]', 'М', string[x])

        for x in string:
            if re.findall(r"[qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM]", x):
                if all(ord(char) < 128 for char in x):
                    string.remove(x)

        for x in range(len(string)):
            if len(string) <= x:
                continue
            else:
                if len(string[x]) <= 4:
                    string.remove(string[x])

        for y in range(4):
            for x in string:
                if len(x) <= 4:
                    string.remove(x)

        patter = re.compile(
            r"(шалық|шелік|даған|деген|таған|теген|лаған|леген|дайын|дейін|тайын|тейін|ңдар|ңдер|дікі|тікі|нікі|атын|етін|йтын|йтін|гелі|қалы|келі|ғалы|шама|шеме|"
            r"мын|мін|бын|бін|пын|пін|мыз|міз|быз|біз|пыз|піз|сың|сің|сыз|сіз|ңыз|ңіз|дан|ден|тан|тен|нан|нен|нда|нде|дың|дің|тың|тің|ның|нің|дар|дер|тар|тер|лар|"
            r"лер|бен|пен|мен|дай|дей|тай|тей|дық|дік|тық|тік|лық|лік|паз|ғыш|гіш|қыш|кіш|шек|шақ|шыл|шіл|нші|ншы|дап|деп|тап|теп|лап|леп|даc|деc|таc|теc|лаc|леc|"
            r"ғар|гер|қар|кер|дыр|дір|тыр|тір|ғыз|гіз|қыз|кіз|ған|ген|қан|кен|ушы|уші|лай|лей|сын|сін|бақ|бек|пақ|пек|мақ|мек|йын|йін|йық|йік|сы|сі|да|де|та|те|ға|"
            r"ге|қа|ке|на|не|ді|ты|ті|ны|ні|ды|ба|бе|па|пе|ма|ме|лы|лі|ғы|гі|қы|кі|ау|еу|ла|ле|ар|ер|ып|іп|ша|ше|са|се|лақ|лық|н|р|п|й|ы|і)$")
        for x in range(len(string)):
            if patter.findall(string[x]):
                before_google_string.append(string[x])

        self.ui.label.setText(str(len(string)))
        self.ui.label_2.setText(str(len(before_google_string)))

        if len(before_google_string) % 1000 == 0:
            size = int(len(before_google_string) / 1000)
        else:
            size = int(len(before_google_string) / 1000) + 1

        for x in range(size):
            start_line = x * 1000;
            stop_line = start_line + 1000;
            write_file = open("Output/Output" + str(x) + ".txt", "w+")
            for y in range(start_line, stop_line):
                try:
                    if before_google_string[y]:
                        write_file.write(before_google_string[y])
                except IndexError:
                    break
        write_file.close()

        # --------------------------------------------GOOGLE TRANSLATE-----------------------------------------------------------

        for x in range(size):
            google_read_file = open("Output/Output" + str(x) + ".txt", "r")
            google_output_file_KZ = open("OutputKZ/OutputKZ" + str(x) + ".txt", "w+")
            google_output_file_NOT = open("OutputNot/OutputNot" + str(x) + ".txt", "w+")

            google_read_line = google_read_file.readlines()

            google_input_text = []
            google_output_text_KZ = []
            google_output_text_NOT = []
            tr = Translator()

            for y in google_read_line:
                google_input_text.append(y)

            for y in range(len(google_input_text)):
                translation = translate_client.detect_language(google_input_text[y])
                if str(translation['language']) == 'kk':
                    google_output_text_KZ.append(google_input_text[y])
                    self.ui.PlainText.insertPlainText('KK:'+ google_input_text[y])
                    app.processEvents()
                else:
                    google_output_text_NOT.append(google_input_text[y])
                    self.ui.PlainText.insertPlainText('NOT:'+google_input_text[y])
                    app.processEvents()
            for y in range(len(google_output_text_KZ)):
                try:
                    if google_output_text_KZ[y]:
                        google_output_file_KZ.write(google_output_text_KZ[y])
                except IndexError:
                    break
            google_output_file_KZ.close()

            for y in range(len(google_output_text_NOT)):
                try:
                    if google_output_text_NOT[y]:
                        google_output_file_NOT.write(google_output_text_NOT[y])
                except IndexError:
                    break
            google_output_file_NOT.close()

            google_input_text.clear()
            google_output_text_KZ.clear()
            google_output_text_NOT.clear()

            self.ui.PlainText.insertPlainText('-' * 20 + 'END'+ str(x) + '-' * 20)
            app.processEvents()

            # --------------------------------------------GOOGLE TRANSLATE-----------------------------------------------------------


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())