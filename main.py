from PySide import QtCore, QtGui
import sys, json, math, xlsxwriter, datetime
from window import Ui_Auto_Flange_Selection
from Data import window_data,Pipe,table_index



count = 0 # start of counter
type_mix = None

# create application
app = QtGui.QApplication(sys.argv)

# Create form and unit
Auto_Flange_Selection = QtGui.QDialog()
ui = Ui_Auto_Flange_Selection()
ui.setupUi(Auto_Flange_Selection)
Auto_Flange_Selection.show()


# add data in window elements
start_data = window_data.send_data_on_the_window(ui)

# add pipe diameter in edit line when you change Dy in combobox


def get_and_set():
    ui.lineEdit_Pipe.setText(Pipe.get(ui.comboBox_Dy.currentText()))

ui.comboBox_Dy.activated[int].connect(get_and_set)


# OPEN JSON FILE FOR READ

with open("Flange_data.json", "r", encoding='utf-8-sig') as gost_data:
    data = json.load(gost_data)

# hook logic

# FUNCTION CREATE NEW NAME FOR TYPE, RETURN NAME IN TYPE_MIX  ----------------OK---------------


def type_select():
    tupe = ui.comboBox_4.currentText()
    otvet = ui.comboBox_3.currentText()
    global type_mix
    if otvet == 'Ответный':
        if tupe == "1":
            type_mix = tupe + '/' + tupe
        elif tupe == "2":
            type_mix = tupe + '/' + '3'
        else:
            type_mix = tupe + '/' + '2'
    elif otvet == 'Нет':
        type_mix = tupe
    elif otvet == "Заглушка":
        if tupe == "1":
            type_mix = tupe + '/' + '1(З)'
        elif tupe == "2":
            type_mix = tupe + '/' + '3(З)'
        else:
            type_mix = tupe + '/' + '2(З)'

# FUNCTION FOR SELECT MASS AND THICKNESS ------------------OK ----------------


def mass_select_and_thickness():
# SPLIN TYPE FOR SEPARATOR /
    a= type_mix.split("/")
    final_mass = []
    trickness=[]
#ADD VARIABLES FOR EACH ELEMENT IN LIST a
    try:
        b=a[0]
        c=a[1]
    except IndexError:
        pass
# SELECT GOST FOR DATA BASE
    if ui.comboBox_GOST.currentText() == "12820-80 (плоские)":
        l='20_'
        k='20_b'
        h =data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]['h']
        h1 =data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]['h1']
    else:
        l='21_'
        k='h4'
        h = data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]['h']
        h1 = data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]['h1']

# SELECT MASS ; TRY WORK WHEN NUMBER OF VARIABLES = 2, IF = 1 WORK EXCEPT
    try:
        if b==c :
            ui.tableWidget.setItem(count, 5, QtGui.QTableWidgetItem(data[ui.comboBox_Py.currentText()]
                                          [table_index[ui.comboBox_Dy.currentText()]][(l+"m_1")]))
            trick=(int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]][k])+int(h))
            ui.tableWidget.setItem(count, 6, QtGui.QTableWidgetItem(str(trick)))
            return
        else:
            for i in a:
                if i == "2":
                    final_mass.append(data[ui.comboBox_Py.currentText()]
                                          [table_index[ui.comboBox_Dy.currentText()]][(l+"m_2")])
                    trick=(int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]][k])+int(h1))
                    trickness.append(trick)
                elif i == "3":
                    final_mass.append(data[ui.comboBox_Py.currentText()]
                                      [table_index[ui.comboBox_Dy.currentText()]][(l + "m_3")])
                    trick = (
                    int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]][k]) + int(h))
                    trickness.append(trick)

                elif i == '1(З)' or i == '2(З)' or i == '3(З)':
                    final_mass.append(data[ui.comboBox_Py.currentText()]
                                      [table_index[ui.comboBox_Dy.currentText()]]["Z_m"])
                    trickness.append(data[ui.comboBox_Py.currentText()]
                                      [table_index[ui.comboBox_Dy.currentText()]]["Z_b"])

                else:
                    final_mass.append(data[ui.comboBox_Py.currentText()]
                                      [table_index[ui.comboBox_Dy.currentText()]][(l + "m_3")])
                    trick = (
                    int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]][k]) + int(h))
                    trickness.append(trick)

    except UnboundLocalError:
        if b == "2":
            final_mass.append(data[ui.comboBox_Py.currentText()]
                              [table_index[ui.comboBox_Dy.currentText()]][(l + "m_2")])
            trick = (int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]][k]) + int(h1))
            trickness.append(trick)

        elif b == "3":
            final_mass.append(data[ui.comboBox_Py.currentText()]
                              [table_index[ui.comboBox_Dy.currentText()]][(l + "m_3")])
            trick = (int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]][k]) + int(h))
            trickness.append(trick)
        elif b == "1":
            final_mass.append(data[ui.comboBox_Py.currentText()]
                              [table_index[ui.comboBox_Dy.currentText()]][(l + "m_1")])
            trick = (int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]][k]) + int(h))
            trickness.append(trick)

    try:
        ui.tableWidget.setItem(count, 5, QtGui.QTableWidgetItem(final_mass[0]+'/'+final_mass[1]))
        ui.tableWidget.setItem(count, 6, QtGui.QTableWidgetItem(str(trickness[0]) + '/' + str(trickness[1])))
    except IndexError:
        ui.tableWidget.setItem(count, 5, QtGui.QTableWidgetItem(final_mass[0]))
        ui.tableWidget.setItem(count, 6, QtGui.QTableWidgetItem(str(trickness[0])))

# FUNCTION PLOTS PIN LENGHT --------------Ok-------------


def lenght_pin():
# SELECT GOST FOR DATA BASE
    if ui.comboBox_GOST.currentText() == "12820-80 (плоские)":
        b = '20_b'
    else:
        b = '21_b'
# VARIABLES
    b_f=int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]][b])
    h=int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]["h"])
    h1=int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]["h1"])
    h2=int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]["h2"])
    b_Z=int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]["Z_b"])
    prok = 3
    h_scha =float(data["Шайба"][0][data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]["Bolt"]])
    h_Gai =float(data["Гайка"][0][data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]["Bolt"]])
    otstup = 6
# FUNCTION
    if type_mix == "1/1":
        l=(h+b_f)*2+prok+(h_scha+h_Gai)*2+otstup
    elif type_mix == '1/1(З)':
        l=h*2+b_f+b_Z+prok+(h_scha+h_Gai)*2+otstup
    elif type_mix == '2/3' or type_mix=='3/2':
        l = h1 + prok - h2 + h + b_f * 2 + (h_scha + h_Gai) * 2 + otstup
    elif type_mix == "2/3(З)" or type_mix=='3/2(З)':
        l=h1+prok-h2+h+b_f+b_Z+(h_scha+h_Gai)*2+otstup
    elif type_mix== "1" or type_mix=='2'or type_mix=="3":
        l="---"
        ui.tableWidget.setItem(count, 8, QtGui.QTableWidgetItem(l))
        return
    k= str(math.ceil(l/5.0)*5)+' '+'('+str(l)+")"
    ui.tableWidget.setItem(count, 8, QtGui.QTableWidgetItem(k))


def set_prok():
    prok_A = {"0,1;0,25 МПа":"A_0.1-0.63", "0.6 МПа":'A_0.1-0.63', "1.0 МПа":"A_1", "1.6 МПа":"A_1.6", "2.5 МПа":'A_2.5'}
    prok_B = {"0,1;0,25 МПа":"B_0.1-0.63", "0.6 МПа":'B_0.1-0.63', "1.0 МПа":"B_1-2.5", "1.6 МПа":"B_1-2.5", "2.5 МПа":'B_1-2.5'}
    if type_mix== "1/1" or type_mix=="1/1(З)":
        A = prok_A[ui.comboBox_Py.currentText()]
        ui.tableWidget.setItem(count, 14, QtGui.QTableWidgetItem(data["Прокладка"][table_index[ui.comboBox_Dy.currentText()]][A]))
    elif type_mix=="2/3" or type_mix=="3/2" or type_mix == '2/3(З)' or type_mix == '3/2(З)':
        B = prok_B[ui.comboBox_Py.currentText()]
        ui.tableWidget.setItem(count, 14,QtGui.QTableWidgetItem(data["Прокладка"][table_index[ui.comboBox_Dy.currentText()]][B]))


def quantity_Pin_and_Sihm():
    if ui.comboBox_3.currentText()=="Нет":
        ui.tableWidget.setItem(count, 7,  QtGui.QTableWidgetItem("-----"))               # Шпилька
        ui.tableWidget.setItem(count, 9,  QtGui.QTableWidgetItem('------'))  # Кголичество шпилек (9)
        ui.tableWidget.setItem(count, 10, QtGui.QTableWidgetItem('------'))  # Гайка (10)
        ui.tableWidget.setItem(count, 11, QtGui.QTableWidgetItem('------'))  # Кголичество гаек(11)
        ui.tableWidget.setItem(count, 12, QtGui.QTableWidgetItem('------'))  # Шайба(12)
        ui.tableWidget.setItem(count, 13, QtGui.QTableWidgetItem('------'))  # Кголичество шайб (13)
        ui.tableWidget.setItem(count, 14, QtGui.QTableWidgetItem('------'))  # Прокладка (14)
        ui.tableWidget.setItem(count, 15, QtGui.QTableWidgetItem('------'))  # Кголичество прокладок (15)



    else :
        ui.tableWidget.setItem(count, 7, QtGui.QTableWidgetItem(data[ui.comboBox_Py.currentText()]
                            [table_index[ui.comboBox_Dy.currentText()]]["Bolt"]))                       # Шпилька
        kol_1 = int(data[ui.comboBox_Py.currentText()][table_index[ui.comboBox_Dy.currentText()]]["n"]) * int(
            ui.spinBox_number.text())
        ui.tableWidget.setItem(count, 9, QtGui.QTableWidgetItem(str(kol_1)))                            # Кголичество шпилек (9)
        ui.tableWidget.setItem(count, 10, QtGui.QTableWidgetItem(data[ui.comboBox_Py.currentText()]
                                [table_index[ui.comboBox_Dy.currentText()]]["Bolt"]))                   # Гайка (10)
        ui.tableWidget.setItem(count, 11, QtGui.QTableWidgetItem(str(kol_1*2)))                         # Кголичество гаек(11)
        ui.tableWidget.setItem(count, 12, QtGui.QTableWidgetItem(data[ui.comboBox_Py.currentText()]
                                [table_index[ui.comboBox_Dy.currentText()]]["Bolt"]))                   # Шайба(12)
        ui.tableWidget.setItem(count, 13, QtGui.QTableWidgetItem(str(kol_1 * 2)))                       # Кголичество гаек(13)
        set_prok()
        ui.tableWidget.setItem(count, 15, QtGui.QTableWidgetItem(ui.spinBox_number.text()))      # Кголичество прокладок (15)


# FUNCTION FOR ADDED SELECT DATA IN TABLET, WORKING AFTER CLICKED BOTTOM   -------OK--------


def add_data():
    global count

    ui.tableWidget.setItem(count, 0,QtGui.QTableWidgetItem(data[ui.comboBox_Py.currentText()]
                            [table_index[ui.comboBox_Dy.currentText()]]["Ду"]))                     # Ду
    ui.tableWidget.setItem(count, 1, QtGui.QTableWidgetItem(type_mix))                              # Тип
    ui.tableWidget.setItem(count, 2, QtGui.QTableWidgetItem(ui.comboBox_3.currentText()))           # Ответный
    ui.tableWidget.setItem(count, 3, QtGui.QTableWidgetItem(ui.spinBox_number.text()))              # количество
    ui.tableWidget.setItem(count, 4, QtGui.QTableWidgetItem(data[ui.comboBox_Py.currentText()]
                              [table_index[ui.comboBox_Dy.currentText()]]["D"]))                    # диаметр наружний
    mass_select_and_thickness()                                                                     # масса и толщина (5,6)
    lenght_pin()                                                                                    # Длина шпилек (8)
    quantity_Pin_and_Sihm()
    ui.tableWidget.setItem(count, 16, QtGui.QTableWidgetItem(ui.lineEdit_Pipe.text()))
    ui.tableWidget.setItem(count, 17, QtGui.QTableWidgetItem(ui.lineEdit_Lenght_pipe.text()))
    count+=1                # GO TO THE NEXT ROW


ui.pushButton_add.clicked.connect(type_select)
ui.pushButton_add.clicked.connect(add_data)



#   FUNCTION DELETE DATA FROM TABL, WORKING AFTER CLICKED BOTTOME  --------------OK----------------




def delete_data():
    global count
    indices = ui.tableWidget.selectionModel().selectedRows()
    if indices == []:
        count += 1
#    print(indices)
    for index in sorted(indices):
        ui.tableWidget.removeRow(index.row())
    count-=1
    ui.tableWidget.insertRow(19)
ui.pushButton_delete.clicked.connect(delete_data)
#############################################################################################################
def save_to_Exel():
    date=datetime.datetime.now().strftime("(%Y_%m_%d__%H.%M.%S)")
    print(date)
    workbook = xlsxwriter.Workbook('фланцы_'+str(date)+'.xlsx')
    worksheet = workbook.add_worksheet()

    table_Horiz_Lable = (
        'Фланец Ду', " Тип  ", 'Ответный', "кол.", ' диаметр', "   масса   ", "толщина ", "Шпилька",
        "Длина шпильки факт(теор)", "кол-во", "Гайка", "кол-во",
        "Шайба", "кол-во", "Прокладка Ду", "кол-во", "труба", "Длина патрубка")
    z=0
    for k in table_Horiz_Lable:
        worksheet.write(0,z,k)
        z+=1
    for i in range(0,count):
        for k in range(0,18):
            a=ui.tableWidget.item(i,k).text()
            worksheet.write(i+1,k,str(a))
    workbook.close()
ui.pushButton_change.clicked.connect(save_to_Exel)
##############################################################################################################
# Run main loop
sys.exit(app.exec_())
