# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1194, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.t_his = QtWidgets.QTabWidget(self.centralwidget)
        self.t_his.setGeometry(QtCore.QRect(10, 260, 1161, 581))
        self.t_his.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.t_his.setObjectName("t_his")
        self.t_wait = QtWidgets.QWidget()
        self.t_wait.setObjectName("t_wait")
        self.table_wait = QtWidgets.QTableWidget(self.t_wait)
        self.table_wait.setGeometry(QtCore.QRect(10, 10, 1051, 551))
        self.table_wait.setObjectName("table_wait")
        self.table_wait.setColumnCount(0)
        self.table_wait.setRowCount(0)
        self.t_his.addTab(self.t_wait, "")
        self.t_hold = QtWidgets.QWidget()
        self.t_hold.setObjectName("t_hold")
        self.table_hold = QtWidgets.QTableWidget(self.t_hold)
        self.table_hold.setGeometry(QtCore.QRect(10, 10, 1031, 551))
        self.table_hold.setObjectName("table_hold")
        self.table_hold.setColumnCount(0)
        self.table_hold.setRowCount(0)
        self.t_his.addTab(self.t_hold, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.table_his = QtWidgets.QTableWidget(self.tab2)
        self.table_his.setGeometry(QtCore.QRect(15, 11, 1031, 551))
        self.table_his.setObjectName("table_his")
        self.table_his.setColumnCount(0)
        self.table_his.setRowCount(0)
        self.t_his.addTab(self.tab2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table_comm = QtWidgets.QTableWidget(self.tab)
        self.table_comm.setGeometry(QtCore.QRect(10, 10, 1131, 571))
        self.table_comm.setObjectName("table_comm")
        self.table_comm.setColumnCount(0)
        self.table_comm.setRowCount(0)
        self.t_his.addTab(self.tab, "")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 271, 161))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.l_pwd = QtWidgets.QLineEdit(self.groupBox)
        self.l_pwd.setGeometry(QtCore.QRect(110, 60, 131, 20))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.l_pwd.setFont(font)
        self.l_pwd.setText("")
        self.l_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.l_pwd.setObjectName("l_pwd")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 71, 19))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.l_user = QtWidgets.QLineEdit(self.groupBox)
        self.l_user.setGeometry(QtCore.QRect(110, 30, 131, 20))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.l_user.setFont(font)
        self.l_user.setText("")
        self.l_user.setFrame(True)
        self.l_user.setReadOnly(False)
        self.l_user.setObjectName("l_user")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 71, 19))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.b_login = QtWidgets.QPushButton(self.groupBox)
        self.b_login.setGeometry(QtCore.QRect(150, 110, 111, 31))
        self.b_login.setObjectName("b_login")
        self.b_info = QtWidgets.QPushButton(self.groupBox)
        self.b_info.setGeometry(QtCore.QRect(30, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_info.setFont(font)
        self.b_info.setObjectName("b_info")
        self.b_orderlist = QtWidgets.QPushButton(self.centralwidget)
        self.b_orderlist.setGeometry(QtCore.QRect(150, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_orderlist.setFont(font)
        self.b_orderlist.setObjectName("b_orderlist")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(310, 0, 851, 221))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_stop = QtWidgets.QWidget()
        self.tab_stop.setObjectName("tab_stop")
        self.grStop = QtWidgets.QGroupBox(self.tab_stop)
        self.grStop.setGeometry(QtCore.QRect(14, 7, 811, 91))
        self.grStop.setObjectName("grStop")
        self.b_checkstop = QtWidgets.QPushButton(self.grStop)
        self.b_checkstop.setGeometry(QtCore.QRect(630, 50, 81, 24))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_checkstop.setFont(font)
        self.b_checkstop.setObjectName("b_checkstop")
        self.box_nostop = QtWidgets.QSpinBox(self.grStop)
        self.box_nostop.setGeometry(QtCore.QRect(660, 16, 58, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_nostop.setFont(font)
        self.box_nostop.setMaximum(500)
        self.box_nostop.setProperty("value", 2)
        self.box_nostop.setObjectName("box_nostop")
        self.box_add = QtWidgets.QSpinBox(self.grStop)
        self.box_add.setGeometry(QtCore.QRect(355, 16, 49, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_add.setFont(font)
        self.box_add.setMaximum(50)
        self.box_add.setProperty("value", 0)
        self.box_add.setObjectName("box_add")
        self.label_5 = QtWidgets.QLabel(self.grStop)
        self.label_5.setGeometry(QtCore.QRect(580, 18, 71, 19))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.grStop)
        self.label_3.setGeometry(QtCore.QRect(274, 17, 71, 19))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.grStop)
        self.label_4.setGeometry(QtCore.QRect(430, 17, 80, 19))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.box_diff = QtWidgets.QSpinBox(self.grStop)
        self.box_diff.setGeometry(QtCore.QRect(510, 15, 54, 24))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_diff.setFont(font)
        self.box_diff.setMaximum(500)
        self.box_diff.setProperty("value", 50)
        self.box_diff.setObjectName("box_diff")
        self.rStop1 = QtWidgets.QRadioButton(self.grStop)
        self.rStop1.setGeometry(QtCore.QRect(12, 23, 83, 16))
        self.rStop1.setChecked(True)
        self.rStop1.setObjectName("rStop1")
        self.rStop2 = QtWidgets.QRadioButton(self.grStop)
        self.rStop2.setGeometry(QtCore.QRect(11, 43, 101, 16))
        self.rStop2.setObjectName("rStop2")
        self.rStop3 = QtWidgets.QRadioButton(self.grStop)
        self.rStop3.setGeometry(QtCore.QRect(11, 65, 89, 16))
        self.rStop3.setObjectName("rStop3")
        self.txt1 = QtWidgets.QLineEdit(self.grStop)
        self.txt1.setGeometry(QtCore.QRect(119, 24, 101, 16))
        self.txt1.setStyleSheet("")
        self.txt1.setText("")
        self.txt1.setReadOnly(True)
        self.txt1.setObjectName("txt1")
        self.txt2 = QtWidgets.QLineEdit(self.grStop)
        self.txt2.setGeometry(QtCore.QRect(120, 44, 101, 16))
        self.txt2.setReadOnly(True)
        self.txt2.setObjectName("txt2")
        self.txt3 = QtWidgets.QLineEdit(self.grStop)
        self.txt3.setGeometry(QtCore.QRect(120, 65, 101, 16))
        self.txt3.setReadOnly(True)
        self.txt3.setObjectName("txt3")
        self.b_gostop = QtWidgets.QPushButton(self.grStop)
        self.b_gostop.setGeometry(QtCore.QRect(490, 50, 81, 24))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_gostop.setFont(font)
        self.b_gostop.setObjectName("b_gostop")
        self.grClose = QtWidgets.QGroupBox(self.tab_stop)
        self.grClose.setGeometry(QtCore.QRect(10, 100, 811, 91))
        self.grClose.setObjectName("grClose")
        self.b_close2 = QtWidgets.QPushButton(self.grClose)
        self.b_close2.setGeometry(QtCore.QRect(630, 50, 81, 24))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_close2.setFont(font)
        self.b_close2.setObjectName("b_close2")
        self.box_c3 = QtWidgets.QSpinBox(self.grClose)
        self.box_c3.setGeometry(QtCore.QRect(650, 16, 58, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_c3.setFont(font)
        self.box_c3.setMaximum(500)
        self.box_c3.setProperty("value", 2)
        self.box_c3.setObjectName("box_c3")
        self.box_c1 = QtWidgets.QSpinBox(self.grClose)
        self.box_c1.setGeometry(QtCore.QRect(313, 16, 71, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_c1.setFont(font)
        self.box_c1.setMinimum(0)
        self.box_c1.setMaximum(500)
        self.box_c1.setProperty("value", 10)
        self.box_c1.setObjectName("box_c1")
        self.label_16 = QtWidgets.QLabel(self.grClose)
        self.label_16.setGeometry(QtCore.QRect(590, 18, 51, 19))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.grClose)
        self.label_17.setGeometry(QtCore.QRect(240, 17, 61, 19))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.grClose)
        self.label_18.setGeometry(QtCore.QRect(430, 17, 51, 19))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.box_c2 = QtWidgets.QSpinBox(self.grClose)
        self.box_c2.setGeometry(QtCore.QRect(483, 15, 91, 24))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_c2.setFont(font)
        self.box_c2.setMinimum(0)
        self.box_c2.setMaximum(499998)
        self.box_c2.setSingleStep(50)
        self.box_c2.setProperty("value", 1000)
        self.box_c2.setDisplayIntegerBase(10)
        self.box_c2.setObjectName("box_c2")
        self.rClose1 = QtWidgets.QRadioButton(self.grClose)
        self.rClose1.setGeometry(QtCore.QRect(12, 23, 83, 16))
        self.rClose1.setChecked(True)
        self.rClose1.setObjectName("rClose1")
        self.rClose2 = QtWidgets.QRadioButton(self.grClose)
        self.rClose2.setGeometry(QtCore.QRect(11, 43, 101, 16))
        self.rClose2.setObjectName("rClose2")
        self.rClose3 = QtWidgets.QRadioButton(self.grClose)
        self.rClose3.setGeometry(QtCore.QRect(11, 65, 89, 16))
        self.rClose3.setObjectName("rClose3")
        self.txt_c1 = QtWidgets.QLineEdit(self.grClose)
        self.txt_c1.setGeometry(QtCore.QRect(119, 24, 101, 16))
        self.txt_c1.setStyleSheet("")
        self.txt_c1.setText("")
        self.txt_c1.setReadOnly(True)
        self.txt_c1.setObjectName("txt_c1")
        self.txt_c2 = QtWidgets.QLineEdit(self.grClose)
        self.txt_c2.setGeometry(QtCore.QRect(120, 44, 101, 16))
        self.txt_c2.setReadOnly(True)
        self.txt_c2.setObjectName("txt_c2")
        self.txt_c3 = QtWidgets.QLineEdit(self.grClose)
        self.txt_c3.setGeometry(QtCore.QRect(120, 65, 101, 16))
        self.txt_c3.setReadOnly(True)
        self.txt_c3.setObjectName("txt_c3")
        self.b_close1 = QtWidgets.QPushButton(self.grClose)
        self.b_close1.setGeometry(QtCore.QRect(500, 50, 81, 24))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_close1.setFont(font)
        self.b_close1.setObjectName("b_close1")
        self.c_close1 = QtWidgets.QCheckBox(self.grClose)
        self.c_close1.setGeometry(QtCore.QRect(760, 20, 51, 20))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.c_close1.setFont(font)
        self.c_close1.setObjectName("c_close1")
        self.tabWidget.addTab(self.tab_stop, "")
        self.tab_order = QtWidgets.QWidget()
        self.tab_order.setObjectName("tab_order")
        self.box_product = QtWidgets.QComboBox(self.tab_order)
        self.box_product.setGeometry(QtCore.QRect(70, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_product.setFont(font)
        self.box_product.setObjectName("box_product")
        self.label = QtWidgets.QLabel(self.tab_order)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 19))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.box_month = QtWidgets.QComboBox(self.tab_order)
        self.box_month.setGeometry(QtCore.QRect(310, 10, 151, 23))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_month.setFont(font)
        self.box_month.setObjectName("box_month")
        self.label_2 = QtWidgets.QLabel(self.tab_order)
        self.label_2.setGeometry(QtCore.QRect(230, 10, 67, 19))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.c_t1 = QtWidgets.QCheckBox(self.tab_order)
        self.c_t1.setGeometry(QtCore.QRect(486, 14, 71, 16))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.c_t1.setFont(font)
        self.c_t1.setObjectName("c_t1")
        self.gr_stop = QtWidgets.QGroupBox(self.tab_order)
        self.gr_stop.setGeometry(QtCore.QRect(20, 70, 511, 101))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.gr_stop.setFont(font)
        self.gr_stop.setObjectName("gr_stop")
        self.label_11 = QtWidgets.QLabel(self.gr_stop)
        self.label_11.setGeometry(QtCore.QRect(200, 30, 81, 19))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.gr_stop)
        self.label_10.setGeometry(QtCore.QRect(20, 30, 81, 19))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.box_stop_price = QtWidgets.QSpinBox(self.gr_stop)
        self.box_stop_price.setGeometry(QtCore.QRect(90, 30, 91, 22))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_stop_price.setFont(font)
        self.box_stop_price.setMinimum(10000)
        self.box_stop_price.setMaximum(40000)
        self.box_stop_price.setProperty("value", 30600)
        self.box_stop_price.setObjectName("box_stop_price")
        self.box_stop_type = QtWidgets.QComboBox(self.gr_stop)
        self.box_stop_type.setGeometry(QtCore.QRect(280, 30, 151, 23))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.box_stop_type.setFont(font)
        self.box_stop_type.setObjectName("box_stop_type")
        self.b_stopsell = QtWidgets.QPushButton(self.gr_stop)
        self.b_stopsell.setGeometry(QtCore.QRect(390, 60, 101, 30))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_stopsell.setFont(font)
        self.b_stopsell.setObjectName("b_stopsell")
        self.b_stopbuy = QtWidgets.QPushButton(self.gr_stop)
        self.b_stopbuy.setGeometry(QtCore.QRect(280, 60, 101, 30))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_stopbuy.setFont(font)
        self.b_stopbuy.setObjectName("b_stopbuy")
        self.label_12 = QtWidgets.QLabel(self.gr_stop)
        self.label_12.setGeometry(QtCore.QRect(20, 70, 81, 19))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.box_add2 = QtWidgets.QSpinBox(self.gr_stop)
        self.box_add2.setGeometry(QtCore.QRect(110, 70, 71, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_add2.setFont(font)
        self.box_add2.setMaximum(50)
        self.box_add2.setProperty("value", 0)
        self.box_add2.setObjectName("box_add2")
        self.box_price = QtWidgets.QSpinBox(self.tab_order)
        self.box_price.setGeometry(QtCore.QRect(70, 40, 91, 22))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_price.setFont(font)
        self.box_price.setMinimum(10000)
        self.box_price.setMaximum(40000)
        self.box_price.setProperty("value", 30600)
        self.box_price.setObjectName("box_price")
        self.label_8 = QtWidgets.QLabel(self.tab_order)
        self.label_8.setGeometry(QtCore.QRect(10, 40, 51, 20))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_order)
        self.label_9.setGeometry(QtCore.QRect(230, 40, 51, 19))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.box_qty = QtWidgets.QSpinBox(self.tab_order)
        self.box_qty.setGeometry(QtCore.QRect(290, 40, 51, 22))
        font = QtGui.QFont()
        font.setFamily("方正姚体")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.box_qty.setFont(font)
        self.box_qty.setMinimum(1)
        self.box_qty.setMaximum(20)
        self.box_qty.setSingleStep(1)
        self.box_qty.setProperty("value", 1)
        self.box_qty.setObjectName("box_qty")
        self.b_buy = QtWidgets.QPushButton(self.tab_order)
        self.b_buy.setGeometry(QtCore.QRect(370, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_buy.setFont(font)
        self.b_buy.setObjectName("b_buy")
        self.b_sell = QtWidgets.QPushButton(self.tab_order)
        self.b_sell.setGeometry(QtCore.QRect(490, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_sell.setFont(font)
        self.b_sell.setObjectName("b_sell")
        self.tabWidget.addTab(self.tab_order, "")
        self.b_delAll = QtWidgets.QPushButton(self.centralwidget)
        self.b_delAll.setGeometry(QtCore.QRect(330, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_delAll.setFont(font)
        self.b_delAll.setObjectName("b_delAll")
        self.b_delStopB = QtWidgets.QPushButton(self.centralwidget)
        self.b_delStopB.setGeometry(QtCore.QRect(470, 230, 181, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_delStopB.setFont(font)
        self.b_delStopB.setObjectName("b_delStopB")
        self.b_delStopS = QtWidgets.QPushButton(self.centralwidget)
        self.b_delStopS.setGeometry(QtCore.QRect(660, 230, 161, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_delStopS.setFont(font)
        self.b_delStopS.setObjectName("b_delStopS")
        self.b_delStop = QtWidgets.QPushButton(self.centralwidget)
        self.b_delStop.setGeometry(QtCore.QRect(840, 230, 151, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.b_delStop.setFont(font)
        self.b_delStop.setObjectName("b_delStop")
        self.b_test = QtWidgets.QPushButton(self.centralwidget)
        self.b_test.setGeometry(QtCore.QRect(1010, 230, 71, 31))
        self.b_test.setObjectName("b_test")
        self.b_test1 = QtWidgets.QPushButton(self.centralwidget)
        self.b_test1.setGeometry(QtCore.QRect(1100, 230, 71, 31))
        self.b_test1.setObjectName("b_test1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1194, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.t_his.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.t_his.setTabText(self.t_his.indexOf(self.t_wait), _translate("MainWindow", "等待执行 "))
        self.t_his.setTabText(self.t_his.indexOf(self.t_hold), _translate("MainWindow", "当前执有 "))
        self.t_his.setTabText(self.t_his.indexOf(self.tab2), _translate("MainWindow", "成交记录 "))
        self.t_his.setTabText(self.t_his.indexOf(self.tab), _translate("MainWindow", "记录分析"))
        self.groupBox.setTitle(_translate("MainWindow", "用户信息"))
        self.label_6.setText(_translate("MainWindow", "用户名 ："))
        self.label_7.setText(_translate("MainWindow", "密  码 ："))
        self.b_login.setText(_translate("MainWindow", "登陆"))
        self.b_info.setText(_translate("MainWindow", "保存信息"))
        self.b_orderlist.setText(_translate("MainWindow", "更新交易"))
        self.grStop.setTitle(_translate("MainWindow", "止损选项"))
        self.b_checkstop.setText(_translate("MainWindow", "逐单止损 "))
        self.label_5.setText(_translate("MainWindow", "不止损单 ："))
        self.label_3.setText(_translate("MainWindow", "追加点位：  "))
        self.label_4.setText(_translate("MainWindow", "止损点位："))
        self.rStop1.setText(_translate("MainWindow", "参考开仓价"))
        self.rStop2.setText(_translate("MainWindow", "参考会话成本 "))
        self.rStop3.setText(_translate("MainWindow", "参考总成本 "))
        self.b_gostop.setText(_translate("MainWindow", "止  损 "))
        self.grClose.setTitle(_translate("MainWindow", "平仓选项"))
        self.b_close2.setText(_translate("MainWindow", "逐单止损 "))
        self.label_16.setText(_translate("MainWindow", "锁 单："))
        self.label_17.setText(_translate("MainWindow", "盈利点：  "))
        self.label_18.setText(_translate("MainWindow", "盈  利："))
        self.rClose1.setText(_translate("MainWindow", "参考开仓价"))
        self.rClose2.setText(_translate("MainWindow", "参考会话成本 "))
        self.rClose3.setText(_translate("MainWindow", "参考总成本 "))
        self.b_close1.setText(_translate("MainWindow", "止 盈"))
        self.c_close1.setText(_translate("MainWindow", "T+1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stop), _translate("MainWindow", "止损区"))
        self.label.setText(_translate("MainWindow", "产 品："))
        self.label_2.setText(_translate("MainWindow", "到期月份:"))
        self.c_t1.setText(_translate("MainWindow", "T+1"))
        self.gr_stop.setTitle(_translate("MainWindow", "止损选项 "))
        self.label_11.setText(_translate("MainWindow", "止损类型 ："))
        self.label_10.setText(_translate("MainWindow", "触发价 ："))
        self.b_stopsell.setText(_translate("MainWindow", "触发空单 "))
        self.b_stopbuy.setText(_translate("MainWindow", "触发多单 "))
        self.label_12.setText(_translate("MainWindow", "追加点位：  "))
        self.label_8.setText(_translate("MainWindow", "价 格："))
        self.label_9.setText(_translate("MainWindow", "数  量 ："))
        self.b_buy.setText(_translate("MainWindow", "多单"))
        self.b_sell.setText(_translate("MainWindow", "空单 "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_order), _translate("MainWindow", "下单区 "))
        self.b_delAll.setText(_translate("MainWindow", "删除未成交的单"))
        self.b_delStopB.setText(_translate("MainWindow", "删除多单的止损(空)"))
        self.b_delStopS.setText(_translate("MainWindow", "删除空单的止损(多)"))
        self.b_delStop.setText(_translate("MainWindow", "删除多余的止损单"))
        self.b_test.setText(_translate("MainWindow", "Test"))
        self.b_test1.setText(_translate("MainWindow", "Test1"))

