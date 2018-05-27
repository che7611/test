import urllib3
import requests
import pandas as pd
import re
import time
from pyquery import PyQuery as pq

class htisec_web(object):
    '''HTISEC to Web Trade'''
    
    def __init__(self):
        urllib3.disable_warnings()
        self.status=0
        self.error=0
        self.url={
        'login_jsp':'https://futures.htisec.com/wf/jsp/login.jsp',
        'login_do':'https://futures.htisec.com/wf/login.do',
        'orderlist':'https://futures.htisec.com/wf/enquiryOrderList.do',
        'account':'https://futures.htisec.com/wf/account.do?method=queryAccount',
        'confirmBS':'https://futures.htisec.com/wf/confirmBS.do',
        'order':'https://futures.htisec.com/wf/placeOrder.do',
        'cancelorder':'https://futures.htisec.com/wf/cancelOrder.do',
        'orderdetail':'https://futures.htisec.com/wf/cancelOrderDetail.do?acc_order_no=%d&has_TS_falg=N',
        'orderpage':'https://futures.htisec.com/wf/orderPage.do',
        'deleteAll':'https://futures.htisec.com/wf/jsp/deleteAll.jsp?acc_order_no=&has_TS_falg=N',
        'cancelAllOrder':"https://futures.htisec.com/wf/cancelAllOrder.do",
        'session':"https://futures.htisec.com/wf/jsp/session.jsp",
        "Eorderdetail":"https://futures.htisec.com/wf/enquiryOrderDetail.do?acc_order_no=%d&has_TS_falg=Y",
        "sms":"https://futures.htisec.com/wf/jsp/check_sms.jsp",
        "login_2":"https://futures.htisec.com/wf/login2fa.do",
        "risk":"https://futures.htisec.com/wf/jsp/risk_disclosure.jsp",
        }
        #返回错误码的正则表达式 
        self.reg={
        'error':"actionMsgs.+?='(.+?)';".encode('utf-8'),
        'prodNameF':"prodNameF=({(.|\n|\r\n)+?})",
        "prodMonthF":"prodMonthF=({(.|\n|\r\n)+?}})",
        }
        self._headers={
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'zh-CN',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Host': 'futures.htisec.com',
        }
        self.orderdata={
        'active_text':'否',
        'buy_sell':'B',
        'buy_sell_text':'买入 ',
        'cond_text':'不適用',
        'contract_mth':'F8',
        'contract_mth_text':'2018/01',
        'exchange':'HKFE',
        'exchange_text':'香港交易所',
        'order_action':'1',
        'order_type_text':'',
        'price':'29505',
        'prod_code':'HSI',
        'product_text':'HSI-恒生指数',
        'product_type':'F',
        'product_type_text':'期貨',
        'qty':'1',
        'side':'',
        'spec_time':'',
        'spec_time_text':'',
        'valid_type':'0',
        'stop_price':'',
        'stop_type':'',
        'strike_price':''
        }
        self.df_cache=pd.DataFrame(columns=['trade_price','trade_qty','trade_time','refno'])
        self.dictHold={}
        #验证是否自动退出的返回页面特征 
        self.logout_sign="goLoginPage()"
        #允许不止损的交易单数 
        self.nostop=0
        #默认止损的点数 
        self.stop_point=50
        self._s=requests.session()
        
    def verify_error(self,html):
        '''检验是否有错误提示 '''
        reg=re.search(self.reg['error'] ,html.encode('utf-8'))
        if reg:
            self.error=reg.group(1).decode('utf-8')
            return 1
        else:
            return 0   

    # auto login
    def login_a(self):
        self.login(self.account['user'],self.account['pwd'])

    #log in
    def login(self,user,pwd):
        '''auto login for htisec'''
        self.account={'user':user,'pwd':pwd}
        self._s.cookies.clear()
        try:
            get1=self._s.get(self.url['login_jsp'] ,verify=False)
            #print('Login Request Status:',get1.status_code)
            jid1=get1.cookies['JSESSIONID']
            self._headers['Cookie']="JSESSIONID="+jid1
            login_data = {'login_id': user, 'pwd': pwd}
            post1 = self._s.post(self.url['login_do'] , data=login_data,verify=False,timeout=5)
            if self.verify_error(post1.text):
                self.status=0
                print("Login Error:",self.error)
                return 0
            self._jid=post1.cookies.values()[0]
            self._headers['Cookie']="JSESSIONID="+self._jid
            print("Login OK,JSESSIONID:" ,self._jid)
            self.status=1
            self.login_time=time.time()
            print("Login Time:",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            return self._jid
        except Exception as e:
            self.status=0
            print("Login Try_Error:",e)

    def login_1(self,user,pwd):
        '''登陆第一步'''
        self.account={'user':user,'pwd':pwd}
        self._s.cookies.clear()
        #login jsp
        get1 = self._s.get(self.url['login_jsp'], verify=False)
        # print('Login Request Status:',get1.status_code)
        jid1 = get1.cookies['JSESSIONID']
        self._headers['Cookie'] = "JSESSIONID=" + jid1
        login_data = {'login_id': user, 'pwd': pwd}
        post1 = self._s.post(self.url['login_do'], data=login_data, verify=False, timeout=20)
        print(post1.status_code)
        self.login1_post=post1.text
        return post1.text

    def login_2(self,text,otp):
        '''手机验证'''
        self.status=1
        forms=self.get_forms(text)
        forms['otp']=otp
        post2 = self._s.post(self.url['login_2'], data=forms, verify=False, timeout=5)
        self.login2_post=post2.text
        self.login_time = time.time()
        pos=post2.text.find(self.url['risk'])
        if pos>-1 :
            return 1
        else:
            return 0
        
    def get_url(self,url):
        '''get url html'''
        try:
            if self.status==0:
                return
            get2=self._s.get(url ,verify=False,timeout=10)
            #print("Get_url %s %s,Re:%s" %(get2.url,get2.status_code,get2.history))
            if  self.verify_out(get2):
                return "ERROR"
            else:
                return get2.text
        except Exception as e:
            print("Get_url Try_Error:",e)
            self.status=999
            self.error="get url Try_error"
            return "ERROR"
            
    def get_orderpage(self):
        html=self.get_url(self.url['orderpage'] )
        return html
        
    def verify_out(self,req):
        '''验证是否已自动退出 '''
        if (req.url == self.url["session"]):
            print("Session Timout...Please login again")
            #self.login_a()
            return True
        else:
            return False

    def verify_out1(self):
        '''验证是否已自动退出 '''
        url=self.url['orderlist']
        get2 = self._s.get(url, verify=False, timeout=10)
        if (get2.url == self.url["session"]):
            print("Session Timout...Please login again")
            return True
        else:
            return False

    def get_orderlist(self):
        try:
            if self.status==0:
                return
            html=self.get_url(self.url['orderlist'])
            if html=="ERROR" :
                return -1
            df1=pd.read_html(html,header=0)
            newdata=df1[5]
            cols=['sel','refno','ex','product','callput','ex_month','bqty','sqty',
                  'price','valid','T+1','cond','status','filled_qty','initiator','order_time']
            newdata.columns=cols
            rep={'bqty':-1,'sqty':-1}
            newdata=newdata.fillna(rep)
            newdata.bqty=newdata.bqty.astype(int)
            newdata.sqty=newdata.sqty.astype(int)
            newdata.refno=newdata.refno.astype(int)
            if not len(newdata):
                self.status = 999
                self.error = "get_orderlist No Data"
                print("get_orderlist NO DATA")
                return newdata
            newdata['filled_qty'] = newdata[['bqty', 'filled_qty']].apply(
                lambda x: -x.filled_qty if x.bqty == -1 else x.filled_qty, axis=1)
            newdata['r_qty'] = newdata[['bqty', 'sqty']].apply(lambda x: -x.sqty if x.bqty == -1 else x.bqty, axis=1)
            cols=['refno','product','r_qty','price','valid','T+1','cond','status','filled_qty','initiator','order_time','bqty','sqty']
            newdata=newdata[cols].copy()
            return newdata.sort_values('refno',ascending=True)
        except Exception as e:
            print("Get_orderlist Try_Error:",e)
            self.status=999
            self.error="get orderlist Try_error"

    #order detail
    def get_orderdetail(self,ref,to_cache=1):
        cols=['trade_price', 'trade_qty', 'trade_time']
        df1=self.df_cache.loc[self.df_cache.refno==ref,cols]
        if len(df1):
            return df1
        else:
            url =self.url["Eorderdetail"] % ref
            html = self.get_url(url)
            dfs = pd.read_html(html, header=1)
            dfs[3].columns=cols
            if to_cache:
                dfs[3]['refno']=ref
                self.df_cache=self.df_cache.append(dfs[3])
            return dfs[3]

    def get_tradelist(self,hh):
        #hh=self.get_orderlist()
        hh.loc[hh.status == '28', 'status'] = '已成交'
        his = hh[hh.status == '已成交'].copy()
        dfHis = pd.DataFrame(columns=['refno','product','trade_price','trade_qty','trade_time','filled_qty','price','order_time'])
        no = 0
        rowindex = []
        for index, rows in his.iterrows():
            if rows.r_qty!=0:
                newdf = self.get_orderdetail(rows.refno,0)
            else:
                newdf = self.get_orderdetail(rows.refno,1)
            for ii, row in newdf.iterrows():
                rowindex.append(no)
                rows['trade_price'] = row.iloc[0]
                if rows.filled_qty < 0:
                    rows['trade_qty'] = -row.iloc[1]
                else:
                    rows['trade_qty'] = row.iloc[1]
                rows['trade_time'] = row.iloc[2]
                dfHis = dfHis.append(rows)
                no += 1
        dfHis.index = rowindex
        return dfHis

    def get_account(self):
        return self.get_url(self.url['account'])
    
    def _post_order(self):
        try:
            orderHtml = self._s.post(self.url['confirmBS'], data=self.orderdata,verify=False,timeout=5)
            if self.verify_out(orderHtml):
                self._post_order()
            #print("_Post_Order  Status:",orderHtml.status_code)
            self.ptext=orderHtml.text
            forms=self.get_forms(orderHtml.text)
            forms['login_pwd']=self.account['pwd']
            #print("taken:",forms['token'])
            orderHtml = self._s.post(self.url['order'], data=forms,verify=False,timeout=5)
            print("Order Request Status:",orderHtml.status_code)
            if self.verify_error(orderHtml.text):
                self.status=2
                print("_Post_order MSG:",self.error)
        except Exception as e:
            print("System Error:",e)
            self.error="There was an error in post_order"
            self.status=2

    def order_buy(self,price,qty=1,prod_code='HSI'):
        if not prod_code:
            prod_code=self.orderdata['prod_code']
        self.orderdata['price']=str(price)
        self.orderdata['qty']=str(qty)
        self.orderdata['prod_code']=prod_code
        self.orderdata['valid_type']='0'
        self.orderdata['buy_sell']='B'
        self.orderdata['stop_type']=''
        self.orderdata['stop_price']=''
        self.orderdata['cond_text']=''
        self._post_order()   
        
    def order_sell(self,price,qty=1,prod_code='HSI'):
        print('prod code:',prod_code)
        if not prod_code:
            prod_code=self.orderdata['prod_code']
        self.orderdata['price']=str(price)
        self.orderdata['qty']=str(qty)
        self.orderdata['prod_code']=prod_code
        self.orderdata['valid_type']='0'
        self.orderdata['buy_sell']='S'
        self.orderdata['stop_type']=''
        self.orderdata['stop_price']=''
        self.orderdata['cond_text']=''
        self._post_order()  

        
    def order_stopB(self,stop_price,qty,product,add=0):
        '''限价多单止损，跌破止损价->触发空单'''
        price=stop_price-add
        prod_code=product[0:3]
        prod_month=product[3:5]
        self.orderdata['prod_code']=prod_code
        self.orderdata['contract_mth']=prod_month
        self.orderdata['price']=str(price)
        self.orderdata['qty']=str(qty)       
        self.orderdata['valid_type']='0'
        self.orderdata['buy_sell']='S'
        self.orderdata['stop_type']='L'
        self.orderdata['stop_price']=str(stop_price)
        self.orderdata['cond_text']=''
        self._post_order()
        
    def order_stopS(self,stop_price,qty,product,add=0):
        '''限价空单止损，升破止损价->触发多单'''
        price=stop_price+add
        prod_code=product[0:3]
        prod_month=product[3:5]
        self.orderdata['prod_code']=prod_code
        self.orderdata['contract_mth']=prod_month
        self.orderdata['price']=str(price)
        self.orderdata['qty']=str(qty)       
        self.orderdata['valid_type']='0'
        self.orderdata['buy_sell']='B'
        self.orderdata['stop_type']='L'
        self.orderdata['stop_price']=str(stop_price)
        self.orderdata['cond_text']=''
        self._post_order()    
    
    def get_forms(self,html):
        '''获得提交表单数据'''
        d=pq(html)
        s=d('INPUT')
        para={}
        for i in s.items():     
            if i.attr('type')=='hidden':
                para[i.attr('name')]=i.attr('value')
        return para

    #del all
    def order_delAll(self):
        gethtml = self.get_url(self.url['deleteAll'])
        forms = self.get_forms(gethtml)
        #print("Delete All Status:", gethtml.status_code)
        forms['login_pwd'] = self.account['pwd']
        posthtml = self._s.post(self.url['cancelAllOrder'], data=forms, verify=False, timeout=5)
        print("Cancel Order Status:", posthtml.status_code)
        if self.verify_error(posthtml.text):
            self.status = 2
            print("Oder_delAll MSG:", self.error)

    #del order ref
    def order_del(self,orderid):
        '''del order'''
        try:
            gethtml = self.get_url(self.url['orderdetail']%orderid)
            forms=self.get_forms(gethtml)
            #print("Orderdetail Status:",gethtml.status_code)
            forms['login_pwd']=self.account['pwd']
            posthtml=self._s.post(self.url['cancelorder'],data=forms,verify=False,timeout=5)
            print("Cancel Order Status:",posthtml.status_code)
            if self.verify_error(posthtml.text):
                self.status = 2
                print("Order_del MSG:", self.error)
        except Exception as e:
            print("Order del Try_Error:",e)
        
    def get_hold(self,hh):
        '''得到最新执仓'''
        dfList=self.get_tradelist(hh)
        df2=dfList.groupby('product').trade_qty.sum()
        dictH={x[0]:0 for x in df2.iteritems()}
        dfH=pd.DataFrame(columns=['refno','product','trade_price','trade_qty','order_time','filled_qty','price','trade_time'])
        for index,row in dfList.iterrows():
            product=row['product']
            trade_qty=row.trade_qty
            if (dictH[product]>=0 and trade_qty>0) or (dictH[product]<=0 and trade_qty<0):
                dfH=dfH.append(row)
                dictH[product]+=trade_qty
                #print("go add %d %d" %(row.refno,trade_qty))
            else:
                #print("go calc %d %d" %(row.refno,trade_qty))
                dfH=self.calc_hold(dfH,row,dictH)
            #print("len dfH:",len(dfH),dictH)
        print(dictH)
        self.dictHold=dictH
        return dfH

    def calc_hold(self,dfHold,row1,dict1):
        '''for ge hold'''
        if not len(dfHold):
            return dfHold
        proc = row1['product']
        calc_qty = row1.trade_qty
        # print("func hold record:%d close:%d" %(len(dfHold),calc_qty))
        for index, row in dfHold[dfHold['product'] == proc].sort_index(ascending=False).iterrows():
            hold_qty = row.trade_qty
            if abs(hold_qty) == abs(calc_qty):
                dict1[proc] += calc_qty
                dfHold.drop(row.name, axis=0, inplace=True)
                # print("a Proc:%s Hold: %s %d，Close:%s %d" %(proc,row.refno,hold_qty,row1.refno,calc_qty))
                return dfHold
            elif abs(hold_qty) > abs(calc_qty):
                dict1[proc] += calc_qty
                dfHold.loc[row.name, 'trade_qty'] = hold_qty + calc_qty
                # print("b Proc:%s Hold: %s %d，Close:%s %d" %(proc,row.refno,hold_qty,row1.refno,calc_qty))
                return dfHold
            elif abs(hold_qty) < abs(calc_qty):
                dfHold.drop(row.name, axis=0, inplace=True)
                dict1[proc] += -hold_qty
                calc_qty += hold_qty
                # print("c Proc:%s Hold: %s %d，Close:%s %d | calc:%d,hold:%d"
                #         %(proc,row.refno,hold_qty,row1.refno,-hold_qty,calc_qty,dict1[proc]))
                if abs(calc_qty) > 0 and dict1[proc] == 0:
                    row1.trade_qty = calc_qty
                    dict1[proc] = calc_qty
                    dfHold = dfHold.append(row1)
                    # print("d go add %d %d %d" %(row1.refno,calc_qty,len(dfHold)))
                    return dfHold

    def gostop(self):
        # self.login_a()
        orderlist =self.get_orderlist()
        if self.status==999:
            print("没有正常反回数据！")
            return -1
        #tradelist=self.get_tradelist(orderlist)
        holdlist=self.get_hold(orderlist)
        for hh in self.dictHold:
            self._gostop(orderlist,holdlist,hh)

    def _gostop(self,orderlist, holdlist, proc):
        '''auto stop'''
        nostop = self.nostop
        stop_point = self.stop_point
        hh = orderlist[orderlist['product'] == proc]
        holdlist = holdlist[holdlist['product'] == proc]
        holdlist = holdlist.sort_values("trade_time", ascending=False)
        s_stop = hh.loc[(hh.status == '等待中') & (hh.cond.str.find('SL>=') > -1), 'r_qty'].sum()
        b_stop = hh.loc[(hh.status == '等待中') & (hh.cond.str.find('SL<=') > -1), 'r_qty'].sum()
        holdQty = self.dictHold[proc]
        if holdQty < 0:
            add_lots = -holdQty - s_stop - nostop
        else:
            add_lots = holdQty + b_stop - nostop
        print("%s@%d hold stop:%d@SL>=price,%d@SL<=price,Add Stop---%d@price" % (
                proc, holdQty, s_stop, b_stop, add_lots))
        if holdQty == 0 or add_lots <= 0:
            return
        cnt = 0
        for index, row in holdlist.iterrows():
            qty = row['trade_qty']
            price = row['trade_price']
            if qty < 0 and cnt <= add_lots:
                print("%s:%d@SL>=%d" % (proc, qty, price + stop_point))
                self.order_stopS(price + stop_point, qty=int(-qty), product=proc, add=0)
            elif qty > 0 and cnt <= add_lots:
                print("%s:%d@SL<=%d" % (proc, qty, price - stop_point))
                self.order_stopB(price - stop_point, qty=int(qty), product=proc, add=0)
            cnt += abs(qty)
            if cnt >= add_lots: return
                
    def get_prod(self,txt):
        '''Get the New Product List'''
        r1=re.search(self.reg['prodNameF'],txt)
        #print(r1)
        self.prodNameF=eval(r1.group(1))
        r2=re.search(self.reg['prodMonthF'],txt)
        self.prodMonthF=eval(r2.group(1))
        #print(r2)

    #del 多余的止损
    def  del_stop(self):
        orderlist=self.get_orderlist()
        if self.status==999:
            print("没有正常反回数据！")
            return -1
        #tradelist=self.get_tradelist(orderlist)
        holdlist=self.get_hold(orderlist)
        stoplist = orderlist.loc[(orderlist.cond.str.find("SL") > -1) & (orderlist.status == '等待中')]
        stopgg = stoplist.groupby('product').size()
        if len(stopgg) ==0:
            return
        if not self.dictHold:
            self.del_stopAll('B', stoplist)
            self.del_stopAll('S', stoplist)

        for ii in stopgg.index:
            self._delstop(stoplist, ii)

    # del指定品种多余的止损单
    def _delstop(self,hh,proc):
        nostop = self.nostop
        stoplist = hh.loc[(hh['product'] == proc) & (hh.cond.str.find("SL") > -1) & (hh.status == '等待中')]
        stop_S = stoplist.loc[stoplist.r_qty > 0, 'r_qty'].sum()
        stop_B = stoplist.loc[stoplist.r_qty < 0, 'r_qty'].sum()
        if proc in self.dictHold:
            holdQty = self.dictHold[proc]
            stopQty = holdQty - nostop if holdQty >= nostop else 0
            if holdQty > 0:
                delQty = abs(stop_B) - stopQty
                self.del_stopB(delQty, stoplist)
                self.del_stopAll('S', stoplist)
            elif holdQty < 0:
                delQty = stop_S - stopQty
                self.del_stopS(delQty, stoplist)
                self.del_stopAll('B', stoplist)
            else:
                self.del_stopAll('B', stoplist)
                self.del_stopAll('S', stoplist)
        else:
            self.del_stopAll('B', stoplist)
            self.del_stopAll('S', stoplist)

    #del stop order
    def del_stopB(self,delqty,hh):
        cont = "SL<="
        delpd = hh.loc[(hh.status == '等待中') & (hh.cond.str.find(cont) > -1)].copy()
        if delqty <= 0 or not len(delpd): return
        delpd = delpd.sort_index(ascending=True)
        for index, rows in delpd.iterrows():
            if rows.sqty <= delqty:
                print("del order %s refno:%d %d" %(rows['product'],rows.refno, rows.sqty))
                self.order_del(rows.refno)
            elif rows.sqty > delqty:
                self.order_del(rows.refno)
                print("del order refno:", rows.refno, delqty)
                stop_price = int(rows.cond[4:].replace(',', ''))
                qty = rows.sqty - delqty
                product = rows['product']
                add = stop_price - rows.price
                self.order_stopB(stop_price, qty, product, add=add)
                print('add  stopB:stop_price=%d,qty=%d,product=%s,add=%d' % (stop_price, qty, product, add))
            delqty = delqty - rows.sqty
            if delqty <= 0: break

    #del stop order
    def del_stopS(self,delqty,hh):
        cont = "SL>="
        delpd = hh.loc[(hh.status == '等待中') & (hh.cond.str.find(cont) > -1)].copy()
        if delqty <= 0 or not len(delpd): return
        delpd = delpd.sort_index(ascending=True)
        for index, rows in delpd.iterrows():
            if rows.bqty <= delqty:
                print("del order refno:", rows.refno, rows.bqty)
                self.order_del(rows.refno)
            elif rows.bqty> delqty:
                self.order_del(rows.refno)
                print("del order refno:", rows.refno, delqty)
                stop_price = int(rows.cond[4:].replace(',', ''))
                qty = rows.bqty - delqty
                product = rows['product']
                add =rows.price-stop_price
                self.order_stopS(stop_price, qty, product, add=add)
                print('add  stopB:stop_price=%d,qty=%d,product=%s,add=%d' % (stop_price, qty, product, add))
            delqty = delqty - rows.bqty
            if delqty <= 0: break

    # del stop all
    def del_stopAll(self,buy_sell,hh):
        if buy_sell=='B':
            cont ="SL<="
        else:
            cont = "SL>="
        delpd = hh.loc[(hh.status == '等待中') & (hh.cond.str.find(cont) > -1)].copy()
        if  not len(delpd): return
        delpd = delpd.sort_index(ascending=True)
        for index, rows in delpd.iterrows():
            print("del order refno:", rows.refno, rows.bqty)
            self.order_del(rows.refno)

print("import OK")
