from htisec import htisec_web as ht
from jy import HS
from win_ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
import time
import json
import os
import math

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.timer=QTimer(self)
        #self.b_autostop.setEnabled(True)
        #self.b_pause.setEnabled(False)
        self.setWindowTitle("海通期货交易助手V2.1")
        self.l_user.setText("")
        self.l_pwd.setText("")

        #self.timer.timeout.connect(self.t_autodo)
        # Login
        self.b_login.clicked.connect(self.c_login)
        #self.b_autostop.clicked.connect(self.c_autostop)
        #self.b_pause.clicked.connect(self.c_pause)
        self.b_checkstop.clicked.connect(self.c_checkstop)
        self.b_buy.clicked.connect(self.c_buy)
        self.b_sell.clicked.connect(self.c_sell)
        self.b_stopbuy.clicked.connect(self.c_stopbuy)
        self.b_stopsell.clicked.connect(self.c_stopsell)
        self.b_orderlist.clicked.connect(self.c_orderlist)
        self.b_test.clicked.connect(self.c_test)
        self.b_test1.clicked.connect(self.c_test1)
        self.b_gostop.clicked.connect(self.c_gostop)
        self.b_delStop.clicked.connect(self.c_delStop)
        self.b_delAll.clicked.connect(self.c_delAll)
        self.b_delStopB.clicked.connect(self.c_delStopB)
        self.b_delStopS.clicked.connect(self.c_delStopS)
        self.b_info.clicked.connect(self.c_info)
        self.rStop1.clicked.connect(self.chg_radio)
        self.rStop2.clicked.connect(self.chg_radio)
        self.rStop3.clicked.connect(self.chg_radio)
        self.rClose1.clicked.connect(self.chg_close)
        self.rClose2.clicked.connect(self.chg_close)
        self.rClose3.clicked.connect(self.chg_close)
        # commbox box_product
        self.box_product.currentTextChanged.connect(self.prod_change)
        self.box_stop_type.currentTextChanged.connect(self.stop_change)
        self.box_diff.valueChanged.connect(self.chg_radio)
        self.box_nostop.valueChanged.connect(self.chg_radio)
        self.box_add.valueChanged.connect(self.chg_radio)
        self.box_c1.valueChanged.connect(self.boxc1_chg)
        self.box_c2.valueChanged.connect(self.boxc2_chg)
        self.box_c3.valueChanged.connect(self.chg_close)
        self.b_close1.clicked.connect(self.cb_close1)

        self.load_info()

    #save person info
    def c_info(self):
        user = self.l_user.text()
        add = self.box_add.value()
        diff = self.box_diff.value()
        nostop = self.box_nostop.value()
        #time = self.box_time.value()
        add2 = self.box_add2.value()
        qty = self.box_qty.value()
        info = {
            "user": user,
            "add": add,
            "diff": diff,
            "nostop": nostop,
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
        #diff=self.box_time.value()*1000
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
            if web_trade.verify_out1():
                w.statusBar().showMessage('Session Timeout!')
                return True
            else:
                return False
    #Test button
    def c_test(self):
        if self.check_login(): return
        self.show_stop()

    def show_stop(self):
        set1=self.set1
        hold=set1['持仓']
        h_cost=math.ceil(set1['原始成本'])
        h_costA = set1['净会话成本']
        h_costB = set1['净持仓成本']
        #print("参考开仓成本  %d@%f" %(hold,h_cost))
        self.txt1.setText("%d@%f" %(hold,h_cost))
        self.txt2.setText ( "%d@%f" % (hold, h_costA))
        self.txt3.setText ( "%d@%f" % (hold, h_costB))
        self.txt_c1.setText("%d@%f" %(hold,h_cost))
        self.txt_c2.setText("%d@%f" % (hold, h_costA))
        self.txt_c3.setText("%d@%f" % (hold, h_costB))
        self.calc_close()
        self.calc_stop()
    #test1 button
    def c_test1(self):
        if self.check_login(): return

        # get orderlist
        hh = web_trade.get_orderlist()
        if web_trade.status == 999:
            print("get_orderlist没有返回数据[c_orderlist]")
            return -1
        tradelist = web_trade.get_tradelist(hh)
        self.get_comm(tradelist)

    #取得会话记录
    def get_comm(self,tradelist):
        list1 = tradelist
        df1 = list1[['trade_qty', 'trade_price', 'trade_time','product']]
        df2 = df1.fillna(0)
        df2.columns = ['bs', 'price', 'time','product']
        h = HS()
        df2 = h.ray(df2)

        cols = ['refno', 'product', 'trade_price', 'trade_qty', 'trade_time', 'price', 'filled_qty', 'r_qty',
                'initiator', 'order_time', 'status']
        rows = df2.copy()

        self.set1=df2.iloc[-1]
        self.show_table(rows, self.table_comm)
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
                #self.box_time.setValue(info["time"])
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
        self.get_comm(tradelist)
        self.show_stop()
        w.statusBar().showMessage("交易刷新成功!")

    #触发空单
    #触发空单
    def c_gostop(self):
        if self.check_login(): return
        Lots,StopPrice=self.calc_stop()
        print(Lots,StopPrice)
        if Lots==0:
            return
        addon=self.box_add.value()
        prod = self.set1['合约']
        if Lots>0:
            web_trade.order_stopS(StopPrice,Lots,prod,addon)
        else:
            web_trade.order_stopB(StopPrice,-Lots, prod,addon)


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
        login = web_trade.login_1(user, pwd)
        pos=login.find(web_trade.url['sms'])
        if pos==-1:
            w.statusBar().showMessage("登陆不成功!")
            return
        w.statusBar().showMessage("短信验证!")
        sms, ok = QInputDialog.getText(self, '短信验证', '请填写短信验证码：')
        if ok:
            res=web_trade.login_2(login,sms)
            if res==0:
                w.statusBar().showMessage("登陆不成功!")
                return
        else:
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

    #radio button rStop1
    def c_rStop1(self):
        self.gr_stop.setTitle("止损选项--radio 1")

    #box_c1 change
    def boxc1_chg(self):
        if not hasattr(self,'set1'):
            print('Not Set1')
            return

        hold=self.set1['持仓']
        if hold==0:
            return

        if self.rClose1.isChecked():
            cost=self.set1['原始成本']
        elif self.rClose2.isChecked():
            cost = self.set1['净会话成本']
        elif self.rClose3.isChecked():
            cost = self.set1['净持仓成本']

        prod=self.set1['合约']
        if prod[0:3]=='HSI':
            point=50
        elif prod[0:3]=='MHI':
            point=10

        win = self.box_c1.value()
        profit = abs(hold) * point * win
        self.box_c2.setValue(profit)
        self.calc_close()

    #box_c2 change
    def boxc2_chg(self):
        if not hasattr(self,'set1'):
            print('Not Set1')
            return

        hold=self.set1['持仓']
        if hold==0:
            return

        if self.rClose1.isChecked():
            cost=self.set1['原始成本']
        elif self.rClose2.isChecked():
            cost = self.set1['净会话成本']
        elif self.rClose3.isChecked():
            cost = self.set1['净持仓成本']

        prod=self.set1['合约']
        if prod[0:3]=='HSI':
            point=50
        elif prod[0:3]=='MHI':
            point=10

        profit = self.box_c2.value()
        win=math.ceil(profit/point/abs(hold))
        self.box_c1.setValue(win)
        self.calc_close()

    #close radio change
    def chg_close(self):
        self.calc_close()


    #calc close Price
    def calc_close(self):
        if not hasattr(self,'set1'):
            print('Not Set1')
            return

        hold=self.set1['持仓']
        if hold==0:
            return

        prod=self.set1['合约']
        if prod[0:3]=='HSI':
            point=50
            charg=33.54
        elif prod[0:3]=='MHI':
            point=10
            charg=13.6

        win = self.box_c1.value()
        profit=self.box_c2.value()
        lock=self.box_c3.value()


        if self.rClose1.isChecked():
            cost=math.ceil(self.set1['原始成本'])
            preProfit=self.set1['净利润']
            Charges = self.set1['手续费']
            Charg1=charg*abs(hold)
            win=math.ceil(win+charg*2/point)
        elif self.rClose2.isChecked():
            cost = self.set1['净会话成本']
            comHold=self.set1['会话盈利']/self.set1['会话平均盈利'] if self.set1['会话平均盈利']!=0 else 0
            closeHold = self.set1['已平仓']
            Charges = (closeHold-comHold)*charg*2
            preProfit = self.set1['利润']-self.set1['会话盈利']*point-Charges
            Charg1=comHold*charg*2+abs(hold)*charg*2
            win=math.ceil(Charg1/point/abs(hold)+win)
        elif self.rClose3.isChecked():
            cost = self.set1['净持仓成本']
            Charges = self.set1['手续费']
            preProfit=-Charges
            Charg1 = charg * abs(hold)
            closeHold=self.set1['已平仓']
            win=math.ceil((Charges+Charg1)/point/abs(hold)+win)

        #hold buy
        if hold>0:
            ClosePrice=cost+win
            lots=-hold+lock if lock<=hold else 0
        #hold sell
        else:
            ClosePrice = cost -win
            lots=-hold-lock if lock<=-hold else 0

        curProfit=preProfit+win*abs(hold)*point-Charg1
        curCharges=Charges+abs(hold)*charg

        inf="止盈单:%d@%d|Pre:%.2f + %.2f|Cur:%.2f + %.2f" \
            %(lots,ClosePrice,preProfit,Charges,curProfit,curCharges)
        self.grClose.setTitle(inf)
        return lots,ClosePrice

    #click 止盈
    def cb_close1(self):
        if self.check_login(): return

        prod = self.set1['合约']

        if self.c_close1.isChecked():
            web_trade.orderdata['ahfs'] = "on"
        else:
            web_trade.orderdata['ahfs'] = ""

        Lots,Price=self.calc_close()

        prod_code=prod[0:3]
        prod_month=prod[3:5]
        web_trade.orderdata['prod_code'] = prod_code
        web_trade.orderdata['contract_mth'] = prod_month

        if Lots >0:
            web_trade.order_buy(Price, Lots, prod_code=prod_code)
            print("%s %d@%d" % (prod,  Lots, Price))
        else:
            web_trade.order_sell(Price, -Lots, prod_code=prod_code)
            print("%s -%d@%d" % (prod, Lots, Price))

    #chg radio
    def chg_radio(self):
        self.calc_stop()

    def calc_stop(self):
        if not hasattr(self,'set1'):
            print('Not Set1')
            return
        hold=self.set1['持仓']
        if hold==0:
            return

        prod=self.set1['合约']
        if prod[0:3]=='HSI':
            point=50
            charg=33.54
        elif prod[0:3]=='MHI':
            point=10
            charg=13.6

        stop_point = self.box_diff.value()
        nostop = self.box_nostop.value()
        addon=self.box_add.value()

        if self.rStop1.isChecked():
            cost=math.ceil(self.set1['原始成本'])
            preProfit=self.set1['净利润']
            Charges = self.set1['手续费']
            Charg1=charg*abs(hold)
        elif self.rStop2.isChecked():
            cost = self.set1['净会话成本']
            comHold=self.set1['会话盈利']/self.set1['会话平均盈利']
            closeHold = self.set1['已平仓']
            Charges = (closeHold-comHold)*charg*2
            preProfit = self.set1['利润']-self.set1['会话盈利']*point-Charges
            Charg1=comHold*charg*2+abs(hold)*charg*2
        elif self.rStop3.isChecked():
            cost = self.set1['净持仓成本']
            Charges = self.set1['手续费']
            preProfit=-Charges
            closeHold=self.set1['已平仓']
            Charg1=charg*abs(hold)

        if hold>0:
            lots=nostop-hold if hold>=nostop else 0
            StopPrice=cost-stop_point
            sign='SL<'
        elif hold<0:
            lots=-hold-nostop if -hold>=nostop else 0
            StopPrice=cost+stop_point
            sign='SL>'
        else:
            lots=0
            StopPrice=0
            sign='L>'

        curProfit=preProfit-point*abs(hold)*(stop_point+addon)-Charg1
        curCharges=Charges+Charg1

        inf="止损单:%d@%s%f+%d|Pre:%.2f + %.2f|Cur:%.2f + %.2f" \
            %(lots,sign,StopPrice,addon,preProfit,Charges,curProfit,curCharges)
        #inf="上损:%d@%s%f+%d" %(lots,sign,StopPrice,addon)
        self.grStop.setTitle(inf)
        return lots,StopPrice

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
    #grClose::title,#grStop::title{
    color:red;
    }
    #txt1,#txt2,#txt3{
    color:green;
    }
    #txt_c1,#txt_c2,#txt_c3{
    color:red;
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
