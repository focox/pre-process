from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from mainwindow import Ui_MainWindow
import os
import pandas as pd
import copy
import pypinyin
import time
import xlsxwriter


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.loadSingleButton.clicked.connect(self.click_load_single_button)
        # self.loadBatchButton.clicked.connect(self.click_load_batch_button)
        self.single_file_path = ''
        self.batch_files_path = ''
        self.save_path = ''
        self.error_counter = 0
        self.legal_counter = 0
        self.bar_counter_base = 0
        self.bar_value = 0
        # self.error_container = []

    def click_load_single_button(self):
        if self.n_split.value() == 0:
            QMessageBox.about(self, "错误", self.tr('单文件条数不能为0！'))
            return
        else:
            self.get_single_file_path()
            self.read_excel_file()


    def get_single_file_path(self):
        single_file_path = QFileDialog.getOpenFileName(self, "打开文件", os.path.abspath(os.curdir), "excel files(*.xls *.xlsx)")
        self.single_file_path = single_file_path[0]
        self.get_save_path()
        print(self.single_file_path)

    def read_excel_file(self):
        self.error_counter = 0
        self.legal_counter = 0
        self.bar_counter_base = 0
        self.bar_value = 0
        if not os.path.exists(self.single_file_path):
            QMessageBox.about(self, "错误", self.tr('文件不存在于', self.single_file_path))
            # QMessageBox.text(self, '错误：录音文件不存在于', self.single_file_path)
            # self.label.setText("About MessageBox")
            return
        else:
            try:
                self.progressBar.setValue(self.bar_value)
                self.process_data(self.single_file_path, self.save_path)
                self.progressBar.setValue(100)
                QMessageBox.about(self, "成功", self.tr('总合法号码：%d条，总非法号码：%d条！' % (self.legal_counter, self.error_counter)))
            except:
                QMessageBox.about(self, '出错！', self.tr('文件命名规则与linux的不兼容！'))

    def process_data(self, df_path, save_path):
        df = pd.read_excel(df_path, sheet_name=None, header=None)
        # print(df)
        sheet_name = [i for i in df if not df.get(i).empty]
        n_total = len(sheet_name)
        if n_total == 0:
            QMessageBox.about(self, '出错！', self.tr('导入的Excel文件为空！'))
            return
        self.bar_counter_base = 100 / n_total
        for idx, key in enumerate(sheet_name):
            df_sub = df.get(key)
            self.bar_value = idx/n_total * 100
            self.progressBar.setValue(self.bar_value)
            print(key)
            df_sub = df.get(key)
            self.split_singe_sheet(df_sub, save_path, key)

    def split_singe_sheet(self, df_original, save_path, sheet_name):
        save_name = ''.join(pypinyin.lazy_pinyin(sheet_name))
        save_name = save_path + '/' + save_name
        data = df_original[0].tolist()
        counter = 0
        length = len(data)
        counter_bias = self.bar_counter_base / length
        container = ['phone']
        previous = 0
        for idx, i in enumerate(data):
            self.bar_value += counter_bias
            self.progressBar.setValue(self.bar_value)
            print(idx + 1)
            if not self.check_phone_number(sheet_name, idx, i):
                continue
            counter += 1
            self.legal_counter += 1
            container.append(i)
            if (idx + 1) % self.n_split.value() == 0 or idx + 1 == length:
                filename = save_name + '_(' + str(previous + 1) + '-' + str(idx + 1) + ')_(' + str(counter) + ')' + '.xls'
                with pd.ExcelWriter(filename) as writer:
                    pd.DataFrame(container).to_excel(
                        writer,
                        header=None, index=False, encoding='utf-8')
                previous = copy.deepcopy(idx + 1)
                counter = 0
                container = ['phone']

    def check_phone_number(self, sheet_name, phone_idx, phone):
        if isinstance(phone, int):
            if len(str(phone)) != 11:
                self.error_counter += 1
                error = '%d 表名: %s, 第%d行, 号码:%s' % (self.error_counter, sheet_name, phone_idx, str(phone))
                print(error)
                self.errorDisplay.append(error)
                return False
            else:
                return True
        else:
            try:
                int(phone)
                return True
            except:
                self.error_counter += 1
                error = '%d 表名: %s, 第%d行, 号码:%s' % (self.error_counter, sheet_name, phone_idx, str(phone))
                print(error)
                self.errorDisplay.append(error)
                return False

    def get_save_path(self):
        self.save_path = QFileDialog.getExistingDirectory(self, "选择保存目录", os.path.abspath(os.path.split(self.single_file_path)[0]))
        QMessageBox.about(self, '提醒：', self.tr('生成文件所在目录：%s' % self.save_path))
        # QFileDialog.close(self)
        # time.sleep(4)
