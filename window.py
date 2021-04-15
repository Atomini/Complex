# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui

class Ui_Auto_Flange_Selection(object):



    def setupUi(self, Auto_Flange_Selection):
        Auto_Flange_Selection.setObjectName("Auto_Flange_Selection")
        Auto_Flange_Selection.setWindowModality(QtCore.Qt.NonModal)
        Auto_Flange_Selection.resize(615, 702)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Auto_Flange_Selection.sizePolicy().hasHeightForWidth())
        Auto_Flange_Selection.setSizePolicy(sizePolicy)
        Auto_Flange_Selection.setMaximumSize(QtCore.QSize(16777215, 702))
        Auto_Flange_Selection.setAutoFillBackground(True)
        Auto_Flange_Selection.setStyleSheet("Auto ")
        Auto_Flange_Selection.setSizeGripEnabled(True)
        Auto_Flange_Selection.setModal(False)

        self.horizontalLayoutWidget = QtGui.QWidget(Auto_Flange_Selection)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 301, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)
        self.comboBox_GOST = QtGui.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_GOST.setSizeIncrement(QtCore.QSize(0, 0))
        self.comboBox_GOST.setObjectName("comboBox_GOST")

        self.horizontalLayout.addWidget(self.comboBox_GOST)
        self.gridLayoutWidget = QtGui.QWidget(Auto_Flange_Selection)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 50, 571, 51))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label_type = QtGui.QLabel(self.gridLayoutWidget)
        self.label_type.setObjectName("label_type")

        self.gridLayout.addWidget(self.label_type, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_Add = QtGui.QLabel(self.gridLayoutWidget)
        self.label_Add.setObjectName("label_Add")

        self.gridLayout.addWidget(self.label_Add, 0, 2, 1, 1)
        self.comboBox_Dy = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_Dy.setObjectName("comboBox_Dy")

        self.gridLayout.addWidget(self.comboBox_Dy, 1, 0, 1, 1)
        self.comboBox_4 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")

        self.gridLayout.addWidget(self.comboBox_4, 1, 1, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 1, 2, 1, 1)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Auto_Flange_Selection)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 150, 301, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEdit_Lenght_pipe = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_Lenght_pipe.setObjectName("lineEdit_Lenght_pipe")

        self.horizontalLayout_2.addWidget(self.lineEdit_Lenght_pipe)
        self.label_6 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_2.addWidget(self.label_6)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Auto_Flange_Selection)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(370, 150, 160, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")

        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_7 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName("label_7")

        self.horizontalLayout_3.addWidget(self.label_7)
        self.lineEdit_Pipe = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_Pipe.setEnabled(True)
        self.lineEdit_Pipe.setObjectName("lineEdit_Pipe")

        self.horizontalLayout_3.addWidget(self.lineEdit_Pipe)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(Auto_Flange_Selection)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(340, 10, 251, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")

        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_8 = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.label_8.setObjectName("label_8")

        self.horizontalLayout_4.addWidget(self.label_8)
        self.comboBox_Py = QtGui.QComboBox(self.horizontalLayoutWidget_4)
        self.comboBox_Py.setObjectName("comboBox_Py")

        self.horizontalLayout_4.addWidget(self.comboBox_Py)
        self.horizontalLayoutWidget_5 = QtGui.QWidget(Auto_Flange_Selection)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(20, 110, 160, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")

        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.label_9 = QtGui.QLabel(self.horizontalLayoutWidget_5)
        self.label_9.setObjectName("label_9")

        self.horizontalLayout_5.addWidget(self.label_9)
        self.spinBox_number = QtGui.QSpinBox(self.horizontalLayoutWidget_5)
        self.spinBox_number.setObjectName("spinBox_number")

        self.horizontalLayout_5.addWidget(self.spinBox_number)
        self.pushButton_add = QtGui.QPushButton(Auto_Flange_Selection)
        self.pushButton_add.setGeometry(QtCore.QRect(20, 190, 161, 31))
        self.pushButton_add.setObjectName("pushButton_add")

        self.pushButton_delete = QtGui.QPushButton(Auto_Flange_Selection)
        self.pushButton_delete.setGeometry(QtCore.QRect(390, 190, 181, 31))
        self.pushButton_delete.setObjectName("pushButton_delete")

        self.pushButton_change = QtGui.QPushButton(Auto_Flange_Selection)
        self.pushButton_change.setGeometry(QtCore.QRect(200, 190, 171, 31))
        self.pushButton_change.setObjectName("pushButton_change")

        self.tableWidget = QtGui.QTableWidget(20,18,Auto_Flange_Selection)
        self.tableWidget.setGeometry(QtCore.QRect(20, 230, 580, 450))
        self.tableWidget.setObjectName("tableWidget")

        self.retranslateUi(Auto_Flange_Selection)
        QtCore.QMetaObject.connectSlotsByName(Auto_Flange_Selection)
        Auto_Flange_Selection.setTabOrder(self.comboBox_GOST, self.comboBox_Py)
        Auto_Flange_Selection.setTabOrder(self.comboBox_Py, self.comboBox_Dy)
        Auto_Flange_Selection.setTabOrder(self.comboBox_Dy, self.comboBox_4)
        Auto_Flange_Selection.setTabOrder(self.comboBox_4, self.comboBox_3)
        Auto_Flange_Selection.setTabOrder(self.comboBox_3, self.spinBox_number)
        Auto_Flange_Selection.setTabOrder(self.spinBox_number, self.lineEdit_Lenght_pipe)
        Auto_Flange_Selection.setTabOrder(self.lineEdit_Lenght_pipe, self.lineEdit_Pipe)
        Auto_Flange_Selection.setTabOrder(self.lineEdit_Pipe, self.pushButton_add)
        Auto_Flange_Selection.setTabOrder(self.pushButton_add, self.pushButton_change)
        Auto_Flange_Selection.setTabOrder(self.pushButton_change, self.pushButton_delete)



    def retranslateUi(self, Auto_Flange_Selection):
        Auto_Flange_Selection.setWindowTitle(QtGui.QApplication.translate("Auto_Flange_Selection",
                                                    "Авто подбор фланцев v 1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Фланец ГОСТ</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_type.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Тип фланца</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Условный проход Ду</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_Add.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ответный/Заглушка/Нет</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Длина патрубка</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">мм</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Труба</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Условное давление</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "<html><head/><body><p><span style=\" font-weight:600;\">Количество</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton_add.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "Добавить", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "Удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_change.setText(QtGui.QApplication.translate("Auto_Flange_Selection", "Сохранить", None, QtGui.QApplication.UnicodeUTF8))

        table_Horiz_Lable = (
            'Фланец \n Ду'," Тип  ", 'Ответный', "кол.",' диаметр',"   масса   ", "толщина " ,"Шпилька",
            "Длина \n шпильки\n факт(теор)", "кол-во", "Гайка", "кол-во",
            "Шайба", "кол-во", "Прокладка \n Ду", "кол-во", "труба", "Длина \n патрубка")

        self.tableWidget.setHorizontalHeaderLabels(table_Horiz_Lable)
        self.tableWidget.resizeColumnsToContents()
        self.lineEdit_Pipe.setText("20x2.5")
        self.lineEdit_Lenght_pipe.setText("0")