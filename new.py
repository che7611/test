from htisec import htisec_web as ht
from win_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
import time
import json
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.timer=QTimer(self)
        self.b_autostop.setEnabled(True)
        self.b_pause.setEnabled(False)
        self.setWindowTitle("海通期货交易助手V1.1")
        self.l_user.setText("")
        self.l_pwd.setText("")

        self.timer.timeout.connect(self.t_autodo)
        # Login
        self.b_login.clicked.connect(self.c_login)
        self.b_autostop.clicked.connect(self.c_autostop)
        self.b_pause.clicked.connect(self.c_pause)
        self.b_checkstop.clicked.connect(self.c_checkstop)
        self.b_buy.clicked.connect(self.c_buy)
        self.b_sell.clicked.connect(self.c_sell)
        self.b_stopbuy.clicked.connect(self.c_stopbuy)
        self.b_stopsell.clicked.connect(self.c_stopsell)
        self.b_orderlist.clicked.connect(self.c_orderlist)
        self.b_test.clicked.connect(self.c_test)
        self.b_delStop.clicked.connect(self.c_delStop)
        self.b_delAll.clicked.connect(self.c_delAll)
        self.b_delStopB.clicked.connect(self.c_delStopB)
        self.b_delStopS.clicked.connect(self.c_delStopS)
        self.b_info.clicked.connect(self.c_info)
        # commbox box_product
        self.box_product.currentTextChanged.connect(self.prod_change)
        self.box_stop_type.currentTextChanged.connect(self.stop_change)
        self.load_info()


    #save person info
    def c_info(self):
        user = self.l_user.text()
        add = self.box_add.value()
        diff = self.box_diff.value()
        nostop = self.box_nostop.value()
        time = self.box_time.value()
        add2 = self.box_add2.value()
        qty = self.box_qty.value()
        info = {
            "user": user,
            "add": add,
            "diff": diff,
            "nostop": nostop,
            "time": time,
            "add2": add2,
            "qty": qty,
        }
        print(info)
        jsObj = json.dumps(info)
        fileObject = open('info.dll', 'w')
        fileObject.write(jsObj)

    def c_pause(self):
        print("auto exec Pause:")
        self.timer.stop()
        self.b_autostop.setEnabled(True)
        self.b_pause.setEnabled(False)

    def t_autodo(self):
        self.stopNO+=1
        print("autodo_Time%s,No:%d" %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),self.stopNO))
        self.c_checkstop()
        self.c_delStop()
        if web_trade.status==999:
            web_trade.login_a()

    #to auto check stop order
    def c_autostop(self):
        if not web_trade.status:
            w.statusBar().showMessage('没有登陆!')
            return
        print("atuo exec Bgin:")
        diff=self.box_time.value()*1000
        self.timer.start(diff)
        self.b_autostop.setEnabled(False)
        self.b_pause.setEnabled(True)
        self.stopNO=0

    #delete stop B all
    def c_delStopB(self):
        if self.check_login(): return
        hh = web_trade.get_orderlist()
        web_trade.del_stopAll('B',hh)
        self.c_orderlist()

    #delete stop B all
    def c_delStopS(self):
        if self.check_login(): return
        hh = web_trade.get_orderlist()
        web_trade.del_stopAll('S',hh)
        self.c_orderlist()

    # delete all
    def c_delAll(self):
        if self.check_login(): return
        web_trade.order_delAll()
        self.c_orderlist()

    # delete stop
    def c_delStop(self):
        if self.check_login(): return
        web_trade.nostop=self.box_nostop.value()
        web_trade.del_stop()
        self.c_orderlist()

    #check not login
    def check_login(self):
        if not web_trade.status:
            w.statusBar().showMessage('没有登陆!')
            return True
        else:
            timediff=time.time()-web_trade.login_time
            print("time diff:",timediff)
            if  timediff>600:
                web_trade.login_a()
            return False
    #Test button
    def c_test(self):
        pass

    #load info
    def load_info(self):
        try:
            if os.path.exists("info.dll"):
                ff = open("info.dll", encoding='utf-8')
                txt = ff.read()
                info=eval(txt)
                self.l_user.setText(info["user"])
                self.box_add.setValue(info["add"])
                self.box_diff.setValue(info["diff"])
                self.box_nostop.setValue(info["nostop"])
                self.box_time.setValue(info["time"])
                self.box_qty.setValue(info["qty"])
                self.box_add2.setValue(info["add2"])
        except Exception as e:
            print("Error:load_info",e)

    def show_table(self,rows,table):
        ll = [i for i in rows.columns]
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setColumnCount(len(ll))
        table.setRowCount(len(rows))
        table.setHorizontalHeaderLabels(ll)
        for x in range(len(ll)):
            headItem = table.horizontalHeaderItem(x)  # 获得水平方向表头的Item对象
            #headItem.setFont("新宋体")  # 设置字体
            headItem.setBackground(QColor(0x8f, 0x8f, 0x8f))  # 设置单元格背景颜色
        row_index = 0
        for index, row in rows.iterrows():
            i = 0
            for vv in row:
                self.newItem = QtWidgets.QTableWidgetItem(str(vv))
                if row_index % 2:
                    self.newItem.setBackground(QColor(0xcf,0xcf,0xcf))
                table.setItem(row_index, i, self.newItem)
                i = i + 1
            row_index += 1
        table.resizeColumnsToContents()
        table.resizeColumnsToContents()

    #get orderlist
    def c_orderlist(self):
        if self.check_login():return
        #get orderlist
        hh = web_trade.get_orderlist()
        if web_trade.status==999:
            print("get_orderlist没有返回数据[c_orderlist]")
            return -1
        tradelist=web_trade.get_tradelist(hh)
        hold = web_trade.get_hold(hh)
        cols = ['refno', 'product', 'trade_price','trade_qty','trade_time','price', 'filled_qty','r_qty', 'initiator', 'order_time', 'status']
        rows = tradelist[ cols].copy()
        self.show_table(rows, self.table_his)
        cols = ['refno', 'product', 'price', 'filled_qty','r_qty','cond', 'initiator', 'order_time', 'status']
        rows = hh.loc[hh.status.isin(['等待中','工作中']) , cols].copy()
        self.show_table(rows, self.table_wait)
        cols = ['refno', 'product','trade_price','trade_qty','trade_time', 'price', 'filled_qty','r_qty', 'initiator', 'order_time', 'status']
        rows=hold[cols].copy()
        self.show_table(rows, self.table_hold)

    #触发多单
    def c_stopbuy(self):
        self.c_stop("B")

    #触发空单
    def c_stopsell(self):
        self.c_stop("S")

    #止损触发
    def c_stop(self,buy_sell):
        if self.check_login(): return
        prod = self.box_product.currentText()[0:3]
        prodM = self.box_month.currentText()[0:2]
        qty=self.box_qty.value()
        stop_price=self.box_stop_price.value()
        stop_type = self.box_stop_type.currentText()[0:1]
        addon=self.box_add2.value()
        if stop_type=='U' or  (stop_type=='L' and  buy_sell=='B'): 
            price=stop_price+addon
        else:
            price=stop_price-addon
        web_trade.orderdata['buy_sell']=buy_sell
        web_trade.orderdata['prod_code'] = prod
        web_trade.orderdata['contract_mth'] = prodM
        web_trade.orderdata['price']=price
        web_trade.orderdata['qty']=qty
        web_trade.orderdata['stop_type']=stop_type
        web_trade.orderdata['stop_price']=stop_price
        web_trade._post_order()
        if web_trade.status == 2:
            w.statusBar().showMessage(web_trade.error)
        self.c_orderlist()

    def c_order(self, buy_sell):
        '''click buy button'''
        if self.check_login(): return
        prod = self.box_product.currentText()[0:3]
        prodM = self.box_month.currentText()[0:2]
        price = self.box_price.value()
        qty = self.box_qty.value()
        web_trade.orderdata['prod_code'] = prod
        web_trade.orderdata['contract_mth'] = prodM
        if self.c_t1.isChecked():
            web_trade.orderdata['ahfs'] = "on"
        else:
            web_trade.orderdata['ahfs'] = ""
        if buy_sell == 'B':
            web_trade.order_buy(price, qty, prod_code=prod)
            print("%s%s %d@%d" % (prod, prodM, qty, price))
        else:
            web_trade.order_sell(price, qty, prod_code=prod)
            print("%s%s -%d@%d" % (prod, prodM, qty, price))

        if web_trade.status == 2:
            w.statusBar().showMessage(web_trade.error)
        self.c_orderlist()

    def c_sell(self):
        '''Click Sell Button'''
        self.c_order('S')

    def c_buy(self):
        '''Click Buy Button'''
        self.c_order('B')

    # login
    def c_login(self):
        user = self.l_user.text()
        pwd = self.l_pwd.text()
        login = web_trade.login(user, pwd)
        if not web_trade.status:
            w.statusBar().showMessage(web_trade.error)
            return
        w.statusBar().showMessage("登陆成功!")
        web_trade.error=1
        #get trade product
        txt = web_trade.get_orderpage()
        web_trade.get_prod(txt)
        self.box_product.clear()
        self.box_month.clear()
        for prod in web_trade.prodNameF:
            self.box_product.addItem(web_trade.prodNameF[prod])
        # set stop_type
        stop_type = ["L-限价止损", "U-升市触发", "D-跌市触发"]
        for ll in stop_type:
            self.box_stop_type.addItem(ll)
        #show orderlist
        self.c_orderlist()

    #check stop order
    def c_checkstop(self):
        if self.check_login(): return
        web_trade.stop_point = self.box_diff.value()
        web_trade.nostop = self.box_nostop.value()
        web_trade.gostop()
        self.c_orderlist()
        if web_trade.status == 2:
            w.statusBar().showMessage(web_trade.error)

    def stop_change(self):
        curtext = self.box_stop_type.currentText()[0:1]
        if curtext == 'L':
            self.gr_stop.setTitle("限价触发: >=[触发价] 触发多单  ｜ <=[触发价] 触发空单")
        elif curtext == 'U':
            self.gr_stop.setTitle("升市触发：>=[触发价] 触发多单  ｜ >=[触发价] 触发空单")
        else:
            self.gr_stop.setTitle("跌市触发：<=[触发价] 触发多单  ｜ <=[触发价] 触发空单")

    # commbox prod_change
    def prod_change(self):
        try:
            self.box_month.clear()
            self.box_month.setCurrentText("a")
            prod = self.box_product.currentText()[0:3]
            # w.statusBar().showMessage(self.box_product.currentText())
            month = web_trade.prodMonthF[prod]
            #print(month)
            for mm in month:
                self.box_month.addItem("%s-%s" % (mm, month[mm]))
        except Exception as e:
            print("prod_change Try_Error:",e)

if __name__ == "__main__":
    import sys

    web_trade = ht()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    style='''
    QWidget
    {
    color:#8B6914;
       background-color:qlineargradient(spread:pad, x1: 0, y1: 0, x2: 1, y2: 1,
                                      stop: 0 #EFEFFD, stop: 1 #D6C3A0 );
    }
    QStatusBar {
    background: #E5E5E5;
    color:red;
    border: 1px solid #5465E7;
    font-size:12px;
    }
    QPushButton
    {
    color:#0000FF;    
    }
    QPushButton:hover 
    {Color:red}
    QPushButton#b_autostop,QPushButton#b_pause
    {
    background-color: none ;
    }
    QComboBox:hover{ color:red; }
    QComboBox::drop-down:hover
    {color:red;}
    '''
    w.setStyleSheet(style)
    w.show()
    sys.exit(app.exec_())