from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QColor,QPixmap, QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow,  QGraphicsDropShadowEffect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyautogui
import datetime
import random
from barcode import EAN13
import os
import test
import sys
import sqlite3
con=sqlite3.connect("mac.db")
cur=con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS spend(spendname,spendpeice,spendid,spendstate)""")
cur.execute("""CREATE TABLE IF NOT EXISTS parex(parexname,parexprice,parexquantity,parexdate,parexid,parexstate)""")
cur.execute("""CREATE TABLE IF NOT EXISTS parfume(parfumename,parfumeprice,parfumequantity,parfumedate,parfumeid,parfumestate)""")
cur.execute("""CREATE TABLE IF NOT EXISTS extrait(extraitname,extraittype,extraitprice,extraitquantity,extraitbarode,extraituser,extraitid,extraitstate)""")
cur.execute("""CREATE TABLE IF NOT EXISTS bottles(bottlesname,bottlessize,bottlesquantity,bottlesprice,bottlesdate,bottlesuser,bottlesid,bottlesstate)""")
cur.execute("""CREATE TABLE IF NOT EXISTS clientpay(peymentpay,paymentdate,paymentbottles,typename,extraitname,bottlesname,clientuser,clientid,paymentid,paymentstate)""")
cur.execute("""CREATE TABLE IF NOT EXISTS users(username,userphone,userpassword,user,userdate,userid,userstate)""")
cur.execute("""CREATE TABLE IF NOT EXISTS superuser(user,name,password)""")
cur.execute("""CREATE TABLE IF NOT EXISTS extraittype(etypenam,typequantity,typediscount,typedatecreating,typeuser,typeid,state)""")
cur.execute("""CREATE TABLE IF NOT EXISTS clients(clientname,clientdate,clientphone,clientcridit,clientcodepar,clientpenf,clientdiscount,clientuser,clientid,clientstate)""")
cur.execute("""CREATE TABLE IF NOT EXISTS rest(date,price)""")
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow,self).__init__()
        uic.loadUi("ayoub.ui",self)
#///////////////////////////////Events/////////////////////////////////////////////////////
        self.showFullScreen()
#_______________________________tableWidth______________________________#
        self.tableWidget_17.setColumnWidth(0,220)
        self.tableWidget_17.setColumnWidth(1,220)   
        self.tableWidget_17.setColumnWidth(2,220)
        self.tableWidget_17.setColumnWidth(3,220)
        self.tableWidget_17.setColumnWidth(4,60)
        self.tableWidget_17.setColumnWidth(5,50)
        #            ___________                #
        self.tableWidget_18.setColumnWidth(0,220)
        self.tableWidget_18.setColumnWidth(1,220)   
        self.tableWidget_18.setColumnWidth(2,220)
        self.tableWidget_18.setColumnWidth(3,220)
        self.tableWidget_18.setColumnWidth(4,60)
        self.tableWidget_18.setColumnWidth(5,50)
        #             ___________               #
        self.tableWidget_28.setColumnWidth(0,220)
        self.tableWidget_28.setColumnWidth(1,220)   
        self.tableWidget_28.setColumnWidth(2,220)
        self.tableWidget_28.setColumnWidth(3,220)
        self.tableWidget_28.setColumnWidth(4,60)
        self.tableWidget_28.setColumnWidth(5,50)
        #              __________               #
        self.tableWidget_27.setColumnWidth(0,220)
        self.tableWidget_27.setColumnWidth(1,220)   
        self.tableWidget_27.setColumnWidth(2,220)
        self.tableWidget_27.setColumnWidth(3,220)
        self.tableWidget_27.setColumnWidth(4,60)
        self.tableWidget_27.setColumnWidth(5,50)
        #---------------------------------------#
        self.tableWidget_20.setColumnWidth(0,220)
        self.tableWidget_20.setColumnWidth(1,220)   
        self.tableWidget_20.setColumnWidth(2,200)
        self.tableWidget_20.setColumnWidth(3,200)
        self.tableWidget_20.setColumnWidth(4,200)   
        self.tableWidget_20.setColumnWidth(6,60)
        self.tableWidget_20.setColumnWidth(7,50)
        #             ___________               #
        self.tableWidget_19.setColumnWidth(0,220)
        self.tableWidget_19.setColumnWidth(1,220)   
        self.tableWidget_19.setColumnWidth(2,200)
        self.tableWidget_19.setColumnWidth(3,200)
        self.tableWidget_19.setColumnWidth(4,200)   
        self.tableWidget_19.setColumnWidth(6,60)
        self.tableWidget_19.setColumnWidth(7,50)
        #             __________                #
        self.tableWidget_29.setColumnWidth(0,220)
        self.tableWidget_29.setColumnWidth(1,220)   
        self.tableWidget_29.setColumnWidth(2,200)
        self.tableWidget_29.setColumnWidth(3,200)
        self.tableWidget_29.setColumnWidth(4,200)   
        self.tableWidget_29.setColumnWidth(6,60)
        self.tableWidget_29.setColumnWidth(7,50)
        #            ____________               #
        self.tableWidget_30.setColumnWidth(0,220)
        self.tableWidget_30.setColumnWidth(1,220)   
        self.tableWidget_30.setColumnWidth(2,200)
        self.tableWidget_30.setColumnWidth(3,200)
        self.tableWidget_30.setColumnWidth(4,200)   
        self.tableWidget_30.setColumnWidth(6,60)
        self.tableWidget_30.setColumnWidth(7,50)
        #           ___________                 #
        #               ______                  #
        self.tableWidget_19.setColumnWidth(0,220)
        self.tableWidget_19.setColumnWidth(1,220)   
        self.tableWidget_19.setColumnWidth(2,200)
        self.tableWidget_19.setColumnWidth(3,200)
        self.tableWidget_19.setColumnWidth(4,200)   
        

        #---------------------------------------#
        self.tableWidget_12.setColumnWidth(0,220)
        self.tableWidget_12.setColumnWidth(1,220)   
        self.tableWidget_12.setColumnWidth(2,220)
        self.tableWidget_12.setColumnWidth(3,220)
        self.tableWidget_12.setColumnWidth(4,60)   
        self.tableWidget_12.setColumnWidth(5,60)
        #             __________                #
        self.tableWidget_9.setColumnWidth(0,220)
        self.tableWidget_9.setColumnWidth(1,220)   
        self.tableWidget_9.setColumnWidth(2,220)
        self.tableWidget_9.setColumnWidth(3,220)
        self.tableWidget_9.setColumnWidth(4,60)   
        self.tableWidget_9.setColumnWidth(5,60)
        #             __________                #
        self.tableWidget_10.setColumnWidth(0,220)
        self.tableWidget_10.setColumnWidth(1,220)   
        self.tableWidget_10.setColumnWidth(2,220)
        self.tableWidget_10.setColumnWidth(3,220)
        self.tableWidget_10.setColumnWidth(4,60)   
        self.tableWidget_10.setColumnWidth(5,60)
        #             __________                #

        #---------------------------------------#
        self.tableWidget_14.setColumnWidth(0,200)
        self.tableWidget_14.setColumnWidth(1,150)
        self.tableWidget_14.setColumnWidth(2,180)
        self.tableWidget_14.setColumnWidth(3,180)
        self.tableWidget_14.setColumnWidth(4,180)
        self.tableWidget_14.setColumnWidth(5,160)
        self.tableWidget_14.setColumnWidth(6,60)
        #           __________                  #
        self.tableWidget_13.setColumnWidth(0,200)
        self.tableWidget_13.setColumnWidth(1,150)
        self.tableWidget_13.setColumnWidth(2,180)
        self.tableWidget_13.setColumnWidth(3,180)
        self.tableWidget_13.setColumnWidth(4,180)
        self.tableWidget_13.setColumnWidth(5,160)
        self.tableWidget_13.setColumnWidth(6,60)
        #            ___________                #
        self.tableWidget_24.setColumnWidth(0,200)
        self.tableWidget_24.setColumnWidth(1,150)
        self.tableWidget_24.setColumnWidth(2,180)
        self.tableWidget_24.setColumnWidth(3,180)
        self.tableWidget_24.setColumnWidth(4,180)
        self.tableWidget_24.setColumnWidth(5,160)
        self.tableWidget_24.setColumnWidth(6,60)
        #             __________                #
        self.tableWidget_23.setColumnWidth(0,200)
        self.tableWidget_23.setColumnWidth(1,150)
        self.tableWidget_23.setColumnWidth(2,180)
        self.tableWidget_23.setColumnWidth(3,180)
        self.tableWidget_23.setColumnWidth(4,180)
        self.tableWidget_23.setColumnWidth(5,160)
        self.tableWidget_23.setColumnWidth(6,60)
        #---------------------------------------#
        self.tableWidget_21.setColumnWidth(0,200)
        self.tableWidget_21.setColumnWidth(1,150)
        self.tableWidget_21.setColumnWidth(2,180)
        self.tableWidget_21.setColumnWidth(3,180)
        self.tableWidget_21.setColumnWidth(4,180)
        self.tableWidget_21.setColumnWidth(5,160)
        self.tableWidget_21.setColumnWidth(6,100)
        self.tableWidget_21.setColumnWidth(7,60)
        #---------------------------------------#
        self.tableWidget_16.setColumnWidth(0,200)
        self.tableWidget_16.setColumnWidth(1,150)
        self.tableWidget_16.setColumnWidth(2,180)
        self.tableWidget_16.setColumnWidth(3,180)
        self.tableWidget_16.setColumnWidth(4,180)
        self.tableWidget_16.setColumnWidth(5,160)
        self.tableWidget_16.setColumnWidth(6,60)
        self.tableWidget_16.setColumnWidth(7,60)
        #               __________              #
        self.tableWidget_15.setColumnWidth(0,200)
        self.tableWidget_15.setColumnWidth(1,150)
        self.tableWidget_15.setColumnWidth(2,180)
        self.tableWidget_15.setColumnWidth(3,180)
        self.tableWidget_15.setColumnWidth(4,180)
        self.tableWidget_15.setColumnWidth(5,160)
        self.tableWidget_15.setColumnWidth(6,60)
        self.tableWidget_15.setColumnWidth(7,60)
        #               __________              #
        self.tableWidget_26.setColumnWidth(0,200)
        self.tableWidget_26.setColumnWidth(1,150)
        self.tableWidget_26.setColumnWidth(2,180)
        self.tableWidget_26.setColumnWidth(3,180)
        self.tableWidget_26.setColumnWidth(4,180)
        self.tableWidget_26.setColumnWidth(5,160)
        self.tableWidget_26.setColumnWidth(6,60)
        self.tableWidget_26.setColumnWidth(7,60)
        #               _________               #
        self.tableWidget_25.setColumnWidth(0,200)
        self.tableWidget_25.setColumnWidth(1,150)
        self.tableWidget_25.setColumnWidth(2,180)
        self.tableWidget_25.setColumnWidth(3,180)
        self.tableWidget_25.setColumnWidth(4,180)
        self.tableWidget_25.setColumnWidth(5,160)
        self.tableWidget_25.setColumnWidth(6,60)
        self.tableWidget_25.setColumnWidth(7,60)
        #----------------------------------------#
        self.tableWidget.setColumnWidth(0,250)
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,80)
        #               _________               #
        self.tableWidget_28.setColumnWidth(0,200)
        self.tableWidget_28.setColumnWidth(1,150)
        self.tableWidget_28.setColumnWidth(2,180)
        #---------------------------------------#
        self.tableWidget_3.setColumnWidth(0,200)
        self.tableWidget_3.setColumnWidth(1,200)
        self.tableWidget_3.setColumnWidth(2,180)
        self.tableWidget_3.setColumnWidth(3,150)
        self.tableWidget_3.setColumnWidth(4,60)
        #                 _______              #
        self.tableWidget_33.setColumnWidth(0,200)
        self.tableWidget_33.setColumnWidth(1,150)
        self.tableWidget_33.setColumnWidth(2,180)
        self.tableWidget_33.setColumnWidth(3,150)
        self.tableWidget_33.setColumnWidth(4,60)
        #---------------------------------------#
        self.tableWidget_4.setColumnWidth(0,200)
        self.tableWidget_4.setColumnWidth(1,150)
        self.tableWidget_4.setColumnWidth(2,180)
        self.tableWidget_4.setColumnWidth(3,150)
        self.tableWidget_4.setColumnWidth(4,10)
        #         _________                     #
        self.tableWidget_34.setColumnWidth(0,200)
        self.tableWidget_34.setColumnWidth(1,150)
        self.tableWidget_34.setColumnWidth(2,180)
        self.tableWidget_34.setColumnWidth(3,150)
        self.tableWidget_34.setColumnWidth(4,60)        
# ------------------------------tamplates-------------------------------#
        self.extrait_tamplate()
        self.extrait_buttons()
        self.extrait_item()
        self.type_tamplate()
        self.type_buttons() 
        self.type_item_add()            
        self.user_tamplate()
        self.user_buttons()
        self.bottles_tamplate()
        self.bottles_buttons()
        self.bottles_item_add()
        self.client_tamplate()
        self.client_buttons()
        self.parfume_tamplate()
        self.rest_tow()
        self.reset()
        self.type_confirm()
        self.chose_type() 
#-------------------------------HIDES-----------------------------------#
        self.dockWidget_2.hide()
       # self.resize(400,540)
       # self.stackedWidget.setCurrentIndex(2)
        self.table_rest()
#-------------------------------EXTRAIT---------------------------------#
        self.pushButton.clicked.connect(self.extrait_main_page)
        self.pushButton_24.clicked.connect(self.extrait_page)
        self.pushButton_23.clicked.connect(self.extrait_ajoute_page)
        self.ext_confirm_2.clicked.connect(self.extrait_insert_data)
        self.pushButton_27.clicked.connect(self.extrait_trash)
        self.tableWidget_20.doubleClicked.connect(self.extrait_barcode_page)
        self.pushButton_31.clicked.connect(self.extrait_barcode) 
        self.lineEdit_9.textChanged.connect(self.extrait_searsh)  
        self.lineEdit_13.textChanged.connect(self.extrait_searsh)    
#-------------------------------TYPEETRAIT------------------------------#
        self.pushButton_25.clicked.connect(self.extrait_type_page)
        self.pushButton_22.clicked.connect(self.extrait_insert_type_page)
        self.ext_type_confirm_4.clicked.connect(self.type_insert_data)
        self.pushButton_28.clicked.connect(self.type_trash) 
        self.lineEdit_12.textChanged.connect(self.type_searsh)       
#-------------------------------BOTTLES---------------------------------#
        self.pushButton_21.clicked.connect(self.bottles_page)
        self.pushButton_20.clicked.connect(self.bottles_ajoute_page)
        self.user_confirm_4.clicked.connect(self.bottles_insert_data)
        self.pushButton_26.clicked.connect(self.bottles_trash)
        self.lineEdit_10.textChanged.connect(self.bottles_searsh)
#-------------------------------CLIENTS---------------------------------#
        self.pushButton_3.clicked.connect(self.client_page)
        self.pushButton_19.clicked.connect(self.clients_payment_page)
        self.pushButton_18.clicked.connect(self.clients_ajoute_page)
        self.client_confirm_2.clicked.connect(self.clients_insert_data)
        self.ext_type_confirm_3.clicked.connect(self.client_payment)
        self.tableWidget_14.doubleClicked.connect(self.client_payment_table)
       # self.ext_type_cancel_3.clicked.connect(self.client_payment_discount)
        self.pushButton_29.clicked.connect(self.client_trash)
#-------------------------------SETTINGS--------------------------------#
        self.pushButton_4.clicked.connect(self.settings_page)
        self.pushButton_14.clicked.connect(self.utilusateur_page)
        self.pushButton_15.clicked.connect(self.trash_page)
        self.pushButton_17.clicked.connect(self.users_ajoute_page)
        self.user_confirm_3.clicked.connect(self.user_insert_data)
        self.pushButton_16.clicked.connect(self.user_trash)
        self.lineEdit_8.textChanged.connect(self.user_searsh)
#-------------------------------SPEND-----------------------------------#
        self.pushButton_5.clicked.connect(self.spend_page)
        self.pushButton_34.clicked.connect(self.spend_insert_data)
        self.pushButton_32.clicked.connect(self.spend_add_page)
        self.lineEdit_11.textChanged.connect(self.spend_searash)
#-------------------------------PARFUME ORIGINAL------------------------#
        self.pushButton_6.clicked.connect(self.parfume_page)
        self.pushButton_37.clicked.connect(self.parfume_add_page)
        self.ext_confirm_3.clicked.connect(self.parfume_insert_data)  
        self.lineEdit_17.textChanged.connect(self.parfume_searsh)     
#-------------------------------39A9ER----------------------------------#
        self.pushButton_7.clicked.connect(self.parex_page)
        self.pushButton_35.clicked.connect(self.parex_add_page)
        self.ext_confirm_5.clicked.connect(self.parex_insert_data)
        self.lineEdit_16.textChanged.connect(self.parex_searsh)
#-------------------------------type confirm----------------------------#
        self.comboBox_4.currentTextChanged.connect(self.type_confirm)   
        self.comboBox.currentTextChanged.connect(self.chose_type)  
        self.pushButton_8.clicked.connect(self.home_page)     
#///////////////////////////////fonctions/////////////////////////////////////////////////#
    def home_page (self):
        try:
            self.stackedWidget_4.setCurrentIndex(7)
        except Exception as e:
            pyautogui.alert(e)
    def table_rest (self):
        try:
            date=datetime.date.today()
            rest=self.lineEdit_5.text()
            cur.execute(""" select paymentdate from clientpay """)
            bring=cur.fetchall()
            for res in bring:
                tur=res[-1]
                if tur != date :
                    cur.execute(f"""insert into rest values("{tur}","{rest}")""")
                    cur.execute("select * from rest ")
                    row=cur.fetchall()
                    self.tableWidget_36.setRowCount(0)
                    for index,value in enumerate(row):
                        self.tableWidget_36.insertRow(index)
                        for indexs,values in enumerate(value):
                            self.tableWidget_36.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
                    con.commit()
                else:
                    pass 
                          
        except Exception as e:
            pyautogui.alert(e)
    def reset (self):
        try:
            date=datetime.date.today()
            cur.execute(f"""select peymentpay,extraitname,bottlesname from clientpay where paymentdate="{date}" """)
            row=cur.fetchall()
            self.tableWidget_35.setRowCount(0)
            for index,value in enumerate(row):
                self.tableWidget_35.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_35.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))

        except Exception as e:
            pyautogui.alert(e)
    def rest_tow(self):
        try:
            date=datetime.date.today()
            s=0
            cur.execute(f"""select peymentpay from clientpay where paymentdate="{date}" """)
            bring=cur.fetchall()
            for x in bring:
            	for t in x :
            		s=s+int(t)
            		self.lineEdit_5.setText(str(s))
                    
                    
        except Exception as e:
            pyautogui.alert(e)
    def insert_superuser(self):

        try:
            user="Super Admin"
            name=self.lineEdit_35.text()
            password=self.lineEdit_36.text()
            cur.execute(f"""insert into superuser values ("{user}","{name}", "{password}" """)
            con.commit()
            self.stackedWidget.setCurrentIndex(1)

        except Exception as e:
            pyautogui.alert(e)    
#-------------------------------type COnfirm----------------------------#
    def type_confirm(self):
        try:
            name=self.comboBox_4.currentText()
            if name=="Extrait":
                self.comboBox.show()
                self.label_67.show()
                self.chose_type()
                self.extrait_item()
            elif name=="Parfume":
                self.label_67.hide()
                self.comboBox.hide()
                self.comboBox_2.clear()
                cur.execute("""select parfumename from parfume where parfumestate='1'  """)
                bring=cur.fetchall()
                for b in bring:
                    for y in b:
                        self.comboBox_2.addItem(y)
            elif name=="Parex":
                self.label_67.hide()
                self.comboBox.hide()
                self.comboBox_2.clear()
                cur.execute("""select parexname from parex where parexstate='1'  """)
                bring=cur.fetchall()
                for b in bring:
                    for y in b:
                        self.comboBox_2.addItem(y)
        except Exception as e:
            pyautogui.alert(e) 
    def chose_type(self):
        try:
            self.comboBox_2.clear()
            name=self.comboBox.currentText()
            cur.execute(f"""select extraitname from extrait where extraittype="{name}" """)
            bring=cur.fetchall()
            for u in bring:
                for d in u:
                    self.comboBox_2.addItem(d)
                    
        except Exception as e:
            pyautogui.alert(e)               
#-------------------------------login_page------------------------------#
    def login_superuser(self):
        try:
            user=self.comboBox_12.currentText()
            username=self.lineEdit_33.text()
            password=self.lineEdit_34.text()
            cur.execute(f"""select user,name,password from superuser where user="{user}" and name="{username}" and password="{password}" """)
            result=cur.fetchall()
            if result:
                self.stackedWidget.setCurrentIndex(0)
            else:
                pyautogui.alert("username ou password incorrect")    
        except Exception as e:
            pyautogui.alert(e)  
    def login_user(self):
        try:
            user=self.comboBox_12.currentText()
            username=self.lineEdit_33.text()
            password=self.lineEdit_34.text()
            cur.execute(f"""select user,name,password from users where user="{user}" and username="{username}" and userpassword="{password}" """)    
            result=cur.fetchall()
            if result:
                self.stackedWidget.setCurrentIndex(0)
            else:
                pyautogui.alert("username ou password incorrect")  
        except Exception as e:
            pyautogui.alert(e)                    
#-------------------------------EXTRAIT---------------------------------#
    def extrait_barcode_page(self):
        try:
            row=self.tableWidget_20.currentRow()
            item=self.tableWidget_20.item(row,0)
            name=item.text()
            self.ext_type_name_3.setText(name)
            self.dockWidget_2.show()
            self.stackedWidget_8.setCurrentIndex(7)
        except Exception as e:
            pyautogui.alert(e)    
    def extrait_barcode(self):
        try:
            num=random.randrange(1000000000000000000000000000000000000000000000000000000000000000)
            number=str(num)
            code=EAN13(number)
            name=self.ext_type_name_3.text()
            code.save(name)
            

        except Exception as e:
            pyautogui.alert(e)    
    def extrait_main_page(self):
        try:
            self.stackedWidget_4.setCurrentIndex(4)
        except Exception as e:
            pyautogui.alert(e)  
    def extrait_page(self):
        try:
            self.stackedWidget_7.setCurrentIndex(1) 
        except Exception as e:
            pyautogui.alert(e)         
    def extrait_ajoute_page(self):
        try:
            self.dockWidget_2.show()
            self.stackedWidget_8.setCurrentIndex(0) 
        except Exception as e:
            pyautogui.alert(e)
    def extrait_insert_data(self):
        try:
            name=self.ext_name_2.text()
            typee=self.ext_type_2.currentText()
            price=self.spinBox_6.value()
            quantity=self.spinBox_11.value()
            user="" 
            idnumber=random.randrange(1000000000000) 
            state="1"
            barcode=""
            idnumbers=str(idnumber)
            rand=name+idnumbers
            extraitid="".join(random.sample(rand,20))
            cur.execute(f"""insert into extrait values("{name}","{typee}","{price}","{quantity}","{barcode}","{user}","{extraitid}","{state}"   )  """)
            self.extrait_tamplate()
            con.commit()
            self.extrait_buttons()
            self.comboBox_2.addItem(name)
             
        except  Exception as e:
            pyautogui.alert(e)                    
    def extrait_tamplate(self):
        try:
            cur.execute("""select * from extrait where extraitstate='1' """)
            bring=cur.fetchall()
            self.tableWidget_20.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_20.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_20.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alert(e)
    def extrait_buttons(self):
        try:
            row=self.tableWidget_20.rowCount()
            for row in range(int(row)):
                self.delete_button_extrait=QPushButton(self)
                self.update_button_extrait=QPushButton(self)
                icondel=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/icons8-remove-30.png")
                iconup=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/edit.png")
                self.delete_button_extrait.setIcon(QtGui.QIcon(icondel))
                self.update_button_extrait.setIcon(QtGui.QIcon(iconup))
                size= QSize(20, 20)
                self.delete_button_extrait.setIconSize(size)
                self.update_button_extrait.setIconSize(size)
                self.delete_button_extrait.setStyleSheet("""QPushButton{
                background-color: rgb(255, 255, 255)

                }
                QPushButton:pressed{
                    padding-top: 5px;
                    }""")
                self.update_button_extrait.setStyleSheet("""QPushButton{
                    background-color: rgb(0, 0, 0,0);
                    text-align:left;                          
                }
                QPushButton:pressed{
                padding-top: 5px;

                }
                                """)              
                self.tableWidget_20.setCellWidget(row,6,self.delete_button_extrait)
                self.tableWidget_20.setCellWidget(row,7,self.update_button_extrait)
                self.delete_button_extrait.clicked.connect(self.extrait_delete)
                self.update_button_extrait.clicked.connect(self.extrait_update)
        except Exception  as e:
            pyautogui.alert(e)        
    def extrait_delete(self):
        try:
            row=self.tableWidget_20.currentRow()
            item=self.tableWidget_20.item(row,6)
            idnumber=item.text()
            cur.execute(f"""update extrait set extraitstate='0' where extraitid="{idnumber}" """)
            self.extrait_tamplate()
            con.commit()
            self.extrait_buttons()
            self.extrait_item()
        except Exception as e:
            pyautogui.alert(e)
    def extrait_update(self):
        try:
            row=self.tableWidget_20.currentRow()
            item=self.tableWidget_20.item(row,6)
            idnumber=item.text()
            row=self.tableWidget_20.currentRow()
            item=self.tableWidget_20.item(row,0)
            name=item.text()
            row=self.tableWidget_20.currentRow()
            item=self.tableWidget_20.item(row,1)
            type=item.text()
            row=self.tableWidget_20.currentRow()
            item=self.tableWidget_20.item(row,2)
            price=item.text()
            row=self.tableWidget_20.currentRow()
            item=self.tableWidget_20.item(row,3)
            quantity=item.text()
            cur.execute(f"""update extrait set extraitname="{name}" , extraittype="{type}" , extraitprice="{price}" , extraitquantity="{quantity}" where extraitid="{idnumber}" """)
            self.extrait_tamplate()
            con.commit()
            self.extrait_buttons()
            self.extrait_item()
        except Exception as e:
            pyautogui.alert(e)    
    def extrait_item(self):
        try:
            self.comboBox_2.clear()
            cur.execute("""select extraitname from extrait where extraitstate='1'  """)
            bring=cur.fetchall()
            for b in bring:
                for y in b:
                    self.comboBox_2.addItem(y)
        except Exception as e:
            pyautogui.alert(e)  
    def extrait_trash(self):
        try:
            self.stackedWidget_2.setCurrentIndex(4)
            cur.execute(""" select * from extrait where extraitstate = '0' """)
            bring=cur.fetchall() 
            self.tableWidget_29.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_29.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_29.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alett(e)                       
    def extrait_searsh(self):
        try:
            srearsh=self.lineEdit_9.text()    
            cur.execute(f"""select * from extrait where extraitstate='1' and clientname="{searsh}" or clientphone="{searsh}" or clientcodepar="{searsh}" or clientpenf="{searsh}" """)
            bring=cur.fetchall()
            self.tableWidget_20.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_20.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_20.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alert(e)           
    def extrait_searsh (slef):
        try:
            searsh=self.lineEdit_13.text()     
            cur.execute(f"""select * from extrait where extraitstate='1' and extraitname=%"{searsh}"% or extraittype= %"{searsh}"% """)
            bring=cur.fetchall()
            self.tableWidget_20.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_20.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_20.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alert(e)    
#-------------------------------TYPEEXTRAIT-----------------------------#
    def extrait_type_page(self):
        try:
            self.stackedWidget_7.setCurrentIndex(0)   
        except Exception as e:
            pyautogui.alert(e)    
    def extrait_insert_type_page(self):
        try:
            self.dockWidget_2.show()
            self.stackedWidget_8.setCurrentIndex(5)
        except Exception as e:
            pyautogui.alert(e)
    def type_buttons(self):
        try:
            row=self.tableWidget_17.rowCount()
            for row in range(int(row)):
                self.delete_button=QPushButton(self)
                self.update_button=QPushButton(self)
                icondel=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/icons8-remove-30.png")
                iconup=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/edit.png")
                self.delete_button.setIcon(QtGui.QIcon(icondel))
                self.update_button.setIcon(QtGui.QIcon(iconup))
                size= QSize(20, 20)
                self.delete_button.setIconSize(size)
                self.update_button.setIconSize(size)
                self.delete_button.setStyleSheet("""QPushButton{
                background-color: rgb(255, 255, 255)

                }
                QPushButton:pressed{
                    padding-top: 5px;
                    }""")
                self.update_button.setStyleSheet("""QPushButton{
                    background-color: rgb(0, 0, 0,0);
                    text-align:left;                          
                }
                QPushButton:pressed{
                padding-top: 5px;

                }
                                """)                
                self.tableWidget_17.setCellWidget(row,5,self.delete_button)
                self.tableWidget_17.setCellWidget(row,6,self.update_button)
                self.delete_button.clicked.connect(self.type_delete_data)
                self.update_button.clicked.connect(self.type_update_data)
        except Exception as e:
            pyautogui.alert(e)        
    def type_insert_data(self):
        try:
            name=self.ext_type_name_2.text()
            quantity=self.spinBox_10.value()
            discount=self.discount_2.value()
            date=datetime.date.today()
            idnumber=random.randrange(10000000)
            state="1"
            user="" 
            cur.execute(f"""insert into extraittype values("{name}","{quantity}","{discount}","{date}","{user}","{idnumber}","{state}")""")
            self.type_tamplate()
            con.commit()
            self.ext_type_2.addItem(name)
            self.type_buttons() 
        except Exception as e:
            pyautogui.alert(e)     
    def type_delete_data(self):
        try: 
            row=self.tableWidget_17.currentRow()
            item=self.tableWidget_17.item(row,5) 
            idnumber=item.text()
            cur.execute(f"""update extraittype set state="0" where typeid="{idnumber}" """) 
            self.type_tamplate()
            con.commit()
            self.type_item_add()
            self.type_buttons()
        except Exception as e:
            pyautogui.alert(e)    
    def type_update_data(self):
        try:
            row=self.tableWidget_17.currentRow()
            item=self.tableWidget_17.item(row,5) 
            idnumber=item.text()
            row=self.tableWidget_17.currentRow()
            item=self.tableWidget_17.item(row,0)
            name=item.text()
            row=self.tableWidget_17.currentRow()
            item=self.tableWidget_17.item(row,1)
            quantity=item.text()
            row=self.tableWidget_17.currentRow()
            item=self.tableWidget_17.item(row,2)
            discount=item.text()
        
            cur.execute(f"""update extraittype set typename="{name}",typequantity="{quantity}",typediscount="{discount}" where typeid="{idnumber}" """)
            self.type_tamplate()
            con.commit() 
            self.type_buttons() 
            self.type_item_add()
        except Exception as e:
            pyautogui.alert(e)    
    def type_tamplate(self):
        try:
            cur.execute(""" select * from extraittype where state="1" """)
            bring=cur.fetchall()
            self.tableWidget_17.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_17.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_17.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))  
        except Exception as e:
            pyautogui.alert(e)            
    def type_item_add(self):
        try:
            self.ext_type_2.clear()
            self.comboBox.clear()
            self.ext_user_name_3.clear()
            cur.execute(""" select typename from extraittype where state="1" """)
            bring=cur.fetchall()
            for x in bring:
                for y in x:
                    self.ext_user_name_3.addItem(y)
                    self.comboBox.addItem(y)
                    self.ext_type_2.addItem(y)
        except Exception as e:
            pyautogui.alert(e)        
    def type_trash(self):
        try:
            self.stackedWidget_2.setCurrentIndex(3)
            cur.execute(""" select * from extraittype where state = '0' """)
            bring=cur.fetchall() 
            self.tableWidget_28.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_28.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_28.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alett(e)                   
    def type_searsh(self):
        try:
            searsh=self.lineEdit_12.text()    
            cur.execute(f""" select * from extraittype where state="1" and etypenam=%"{searsh}"%  """)
            bring=cur.fetchall()
            self.tableWidget_17.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_17.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_17.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))  
        except Exception as e:
            pyautogui.alert(e)             
#-------------------------------BOTTLES---------------------------------#
    def bottles_page(self):
        try:
            self.stackedWidget_4.setCurrentIndex(3)
        except Exception as e:
            pyautogui.alert(e)    
    def bottles_ajoute_page(self):
        try:
            self.dockWidget_2.show()
            self.stackedWidget_8.setCurrentIndex(4)        
        except Exception as e:
            pyautogui.alert(e)  
    def bottles_insert_data(self):
        try:
            name=self.lineEdit_14.text()
            size=self.spinBox_7.value()
            quantity=self.spinBox_8.value()
            price=self.spinBox_9.value()
            date=datetime.date.today()
            idnumber=random.randrange(1000000)
            state='1'
            user="" 
            cur.execute(f"""insert into bottles values("{name}","{size}","{quantity}","{price}","{date}","{user}","{idnumber}","{state}")""")
            self.bottles_tamplate()
            con.commit()
            self.comboBox_3.addItem(name)
            self.bottles_buttons()
        except Exception as e:
            pyautogui.alert(e)  
    def bottles_tamplate(self):
        try:
            cur.execute("""select * from bottles where bottlesstate='1'  """)
            bring=cur.fetchall()
            self.tableWidget_16.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_16.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_16.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))

        except Exception as e:
            pyautogui.alert(e)      
    def bottles_buttons(self):
        try:
            row=self.tableWidget_16.rowCount()
            for row in range(int(row)):
                self.bottles_delete_button=QPushButton(self)
                self.bottles_update_button=QPushButton(self)
                icondel=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/icons8-remove-30.png")
                iconup=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/edit.png")
                self.bottles_delete_button.setIcon(QtGui.QIcon(icondel))
                self.bottles_update_button.setIcon(QtGui.QIcon(iconup))
                size= QSize(20, 20)
                self.bottles_delete_button.setIconSize(size)
                self.bottles_update_button.setIconSize(size)
                self.bottles_delete_button.setStyleSheet("""QPushButton{
                background-color: rgb(255, 255, 255)

                }
                QPushButton:pressed{
                    padding-top: 5px;
                    }""")
                self.bottles_update_button.setStyleSheet("""QPushButton{
                    background-color: rgb(0, 0, 0,0);
                    text-align:left;                          
                }
                QPushButton:pressed{
                padding-top: 5px;

                }
                                """)                
                self.tableWidget_16.setCellWidget(row,6,self.bottles_delete_button)
                self.tableWidget_16.setCellWidget(row,7,self.bottles_update_button)
                self.bottles_delete_button.clicked.connect(self.bottles_delete)
                self.bottles_update_button.clicked.connect(self.bottles_update)                     
        except Exception as e:
            pyautogui.alert(e)   
    def bottles_delete(self):
        try:
            row=self.tableWidget_16.currentRow()
            item=self.tableWidget_16.item(row,6)
            idnumber=item.text()
            cur.execute(f"""update bottles set bottlesstate='0' where bottlesid="{idnumber}" """)
            self.bottles_tamplate()
            con.commit()
            self.bottles_item_add()
            self.bottles_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def bottles_update(self):
        try:
            row=self.tableWidget_16.currentRow()
            item=self.tableWidget_16.item(row,6)
            idnumber=item.text()
            row=self.tableWidget_16.currentRow()
            item=self.tableWidget_16.item(row,0)
            name=item.text()
            row=self.tableWidget_16.currentRow()
            item=self.tableWidget_16.item(row,1)
            size=item.text()
            row=self.tableWidget_16.currentRow()
            item=self.tableWidget_16.item(row,2)
            quantity=item.text()
            row=self.tableWidget_16.currentRow()
            item=self.tableWidget_16.item(row,3)
            price=item.text()
            cur.execute(f"""update bottles set bottlesname="{name}" ,bottlessize="{size}" ,bottlesquantity="{quantity}" ,bottlesprice="{price}" where bottlesid="{idnumber}" """)
            self.bottles_tamplate()
            con.commit()
            self.bottles_item_add()
            self.bottles_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def bottles_item_add(self):
        try:
            self.comboBox_3.clear()
            cur.execute("""select bottlesname from bottles where bottlesstate='1' """)
            row=cur.fetchall()
            for i in row:
                for h in i:
                    self.comboBox_3.addItem(h)


        except Exception as e:
            pyautogui.alert(e)    
    def bottles_trash(self):
        try:
            self.stackedWidget_2.setCurrentIndex(2)
            cur.execute(""" select * from bottles where bottlesstate = '0' """)
            bring=cur.fetchall() 
            self.tableWidget_26.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_26.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_26.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alett(e)                                                 
    def bottles_searsh(self):
        try:
            searsh=self.lineEdit_10.text()    
            cur.execute(f"""select * from bottles where bottlesstate='1' and bottlesname=%"{searsh}"%  """)
            bring=cur.fetchall()
            self.tableWidget_16.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_16.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_16.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))

        except Exception as e:
            pyautogui.alert(e)      
#-------------------------------CLIENTS---------------------------------#
    def client_page(self):
        try:
            self.stackedWidget_4.setCurrentIndex(2)
        except Exception as e:
            pyautogui.alert(e)           
    def clients_ajoute_page(self):
        try:
            self.dockWidget_2.show()
            self.stackedWidget_8.setCurrentIndex(2)  
        except Exception as e:
            pyautogui.alert(e)    
    def clients_insert_data(self):
        try:
            name=self.client_name_2.text()
            date=datetime.date.today()
            phone=self.client_phone_3.value()
            cridit=self.client_phone_4.value()
            codpar=self.client_name_3.text()
            penf=self.ext_user_name_3.currentText()
            idnumber=random.randrange(10000000)
            dis=0
            user="" 
            state="1"
            cur.execute(f"""insert into clients values("{name}","{date}","{phone}","{cridit}","{codpar}","{penf}","{dis}","{user}","{idnumber}","{state}") """)
            self.client_tamplate()
            con.commit()
            self.client_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def client_tamplate(self):
        try:
            cur.execute(""" select * from clients where clientstate="1" """)
            bring=cur.fetchall()
            self.tableWidget_14.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_14.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_14.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
                   
        except Exception as e:
            pyautogui.alert(e)   
    def client_buttons(self):
        try:
            row=self.tableWidget_14.rowCount()
            for row in range(int(row)):
                self.client_delete_button=QPushButton(self)
                self.client_update_button=QPushButton(self)
                icondel=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/icons8-remove-30.png")
                iconup=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/edit.png")
                self.client_delete_button.setIcon(QtGui.QIcon(icondel))
                self.client_update_button.setIcon(QtGui.QIcon(iconup))
                size= QSize(20, 20)
                self.client_delete_button.setIconSize(size)
                self.client_update_button.setIconSize(size)
                self.client_delete_button.setStyleSheet("""QPushButton{
                background-color: rgb(255, 255, 255)

                }
                QPushButton:pressed{
                    padding-top: 5px;
                    }""")
                self.client_update_button.setStyleSheet("""QPushButton{
                    background-color: rgb(0, 0, 0,0);
                    text-align:left;                          
                }
                QPushButton:pressed{
                padding-top: 5px;

                }
                                """)                
                self.tableWidget_14.setCellWidget(row,8,self.client_delete_button)
                self.tableWidget_14.setCellWidget(row,9,self.client_update_button)
                self.client_delete_button.clicked.connect(self.client_delete)
                self.client_update_button.clicked.connect(self.client_update)                     
        except Exception as e:
            pyautogui.alert(e)
    def client_delete(self):
        try:
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,8)
            idnumber=item.text()
            cur.execute(f"""update clients set clientstate='0' where clientid="{idnumber}"  """)   
            self.client_tamplate()
            con.commit() 
            self.client_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def client_update(self):
        try:
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,8)
            idnumber=item.text()
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,0)
            name=item.text()
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,2)
            phone=item.text()
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,3)
            cridit=item.text()
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,4)
            codepar=item.text()
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,5)
            penf=item.text()
            cur.execute(f"""update clients set clientname="{name}",clientphone="{phone}",clientcridit="{cridit}"
              ,clientcodepar="{codepar}",clientpenf="{penf}"  where clientid="{idnumber}"  """)
            self.client_tamplate()
            con.commit()
            self.client_buttons()

            
        except Exception as e:
            pyautogui.alert(e)
    def client_trash(self) :
        try:
            self.stackedWidget_2.setCurrentIndex(1)
            cur.execute(""" select * from clients where clientstate = '0' """)
            bring=cur.fetchall() 
            self.tableWidget_24.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_24.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_24.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alert(e)             
            #________________________________________________________________##
    def clients_payment_page(self):
        try:    
            self.dockWidget_2.show()
            self.stackedWidget_8.setCurrentIndex(3)
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,8)
            idnumber=item.text()
            self.lineEdit.setText(idnumber)
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,6)
            discount=item.text()
            self.lineEdit_3.setText(discount)


        except Exception as e:
            pyautogui.alert(e)              
    def client_payment(self):
        try:
            amount=self.payement_amount_2.value()
            date=datetime.date.today()
            pricebottles=self.payement_bottle_2.value()
            type=self.comboBox.currentText()
            extraitname=self.comboBox_2.currentText()
            namebottles=self.comboBox_3.currentText()
            clientid=self.lineEdit.text() 
            paymentid=random.randrange(100000000)
            state='active'
            user=""
            cur.execute(f"""insert into clientpay values("{amount}","{date}","{pricebottles}","{type}","{extraitname}","{namebottles}","{user}","{clientid}","{paymentid}","{state}")""")
            
            self.client_buttons()  


            discount=self.lineEdit_3.text()
            cur.execute(f"""select typediscount from extraittype where typename="{type}" """)
            bring=cur.fetchall()
            for t in bring:
                for u in t:
                    cur.execute(f"""select typequantity from extraittype where typename="{type}"  """)
                    row=cur.fetchall()
                    for y in row:
                        for a in y:
                            res=(float(u)*100)/(float(a))
                            resu=res/100
                            result=amount*resu       
                            re=float(discount)+result
                            self.lineEdit_3.setText(str(re))
                            cur.execute(f"""update clients set clientdiscount="{re}" """)
                            self.client_tamplate()
            con.commit()   
            self.reset()
            self.rest_tow()     
        except Exception as e:
            pyautogui.alert(e)
    def ayoub(self):
        try:
            type=self.comboBox.currentText()
            idnumber=self.lineEdit.text()
            totalpay=self.payement_amount_2.value()
            discount=self.lineEdit_3.text()
            cur.execute(f"""select typediscount from extraittype where typename="{type}" """)
            bring=cur.fetchall()
            for t in bring:
                for u in t:
                    cur.execute(f"""select typequantity from extraittype where typename="{type}"  """)
                    row=cur.fetchall()
                    for y in row:
                        for a in y:
                            res=(float(u)*100)/(float(a))
                            resu=res/100
                            result=totalpay*resu       
                            re=float(discount)+result
                            self.lineEdit_3.setText(str(re))
                            cur.execute(f"""update clients set clientdiscount="{re}" where clienti="{idnumber}" """)
                            self.client_tamplate()
        except Exception as e:
            pyautogui.alert(e)    
    def client_payment_table(self):
        try:
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,6)
            discount=item.text()
            self.lineEdit_4.setText(discount)
            self.dockWidget_2.show()
            self.dockWidget_2.resize(1000,700)
            self.stackedWidget_8.setCurrentIndex(6)     
            row=self.tableWidget_14.currentRow()
            item=self.tableWidget_14.item(row,8)
            idnumber=item.text()
            state="active"
            self.lineEdit_2.setText(idnumber)
            cur.execute(f"""select peymentpay,paymentdate,paymentbottles,typename,extraitname,bottlesname,clientid,paymentid from clientpay where clientid="{idnumber}"   """)
            bring=cur.fetchall()
            self.tableWidget_21.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_21.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_21.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))



            
        except Exception as e:
            pyautogui.alert(e)                                                       
#-------------------------------SETTINGS--------------------------------#
    def settings_page(self):
        self.stackedWidget_4.setCurrentIndex(1)
    #----------------USERS----------------------#
    def utilusateur_page(self):
        self.stackedWidget_5.setCurrentIndex(1)
    def users_ajoute_page(self):
        self.dockWidget_2.show()
        self.stackedWidget_8.setCurrentIndex(1) 
    def user_insert_data(self):
        try:
            name=self.user_fullname_2.text()
            phone=self.user_phone_2.value()
            password=self.user_password_2.text()
            date=datetime.date.today()
            user="user"
            idnumber=random.randrange(10000000)
            state="1"
            cur.execute(f"""insert into users values("{name}","{phone}","{password}","{user}","{date}","{idnumber}","{state}")""")
            self.user_tamplate()
            con.commit()
            self.user_buttons()

        except Exception as e:
            pyautogui.alert(e)
    def user_tamplate(self):
        try:
            cur.execute("""select * from users where userstate = '1' """)
            bring=cur.fetchall() 
            self.tableWidget_12.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_12.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_12.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
                    

        except Exception as e:
            pyautogui.alert(e)       
    def user_update(self):
        try:
            row=self.tableWidget_12.currentRow()
            item=self.tableWidget_12.item(row,5)
            idnumber=item.text()
            row=self.tableWidget_12.currentRow()
            item=self.tableWidget_12.item(row,0)
            name=item.text()
            row=self.tableWidget_12.currentRow()
            item=self.tableWidget_12.item(row,1)
            phone=item.text()
            row=self.tableWidget_12.currentRow()
            item=self.tableWidget_12.item(row,2)
            password=item.text()
            cur.execute(f"""update users set username="{name}" , userphone="{phone}" ,userpassword="{password}" where userid="{idnumber}"     """)
            self.user_tamplate()
            con.commit()
       
            self.user_buttons()

        except  Exception as e:
            pyautogui.alert(e) 
    def user_delete(self):
        try:
            row=self.tableWidget_12.currentRow()
            item=self.tableWidget_12.item(row,5)
            idnumber=item.text()
            cur.execute(f"""update users set userstate='0' where userid="{idnumber}" """)
            self.user_tamplate()
            con.commit()
      
            self.user_buttons()
            
        except Exception as e:
            pyautogui.alert(e)
    def user_buttons(self):
        row=self.tableWidget_12.rowCount()
        for row in range(int(row)):
            self.user_delete_button=QPushButton(self)
            self.user_update_button=QPushButton(self)
            icondel=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/icons8-remove-30.png")
            iconup=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/edit.png")
            self.user_delete_button.setIcon(QtGui.QIcon(icondel))
            self.user_update_button.setIcon(QtGui.QIcon(iconup))
            size= QSize(20, 20)
            self.user_delete_button.setIconSize(size)
            self.user_update_button.setIconSize(size)
            self.user_delete_button.setStyleSheet("""QPushButton{
                background-color: rgb(255, 255, 255)

                }
                QPushButton:pressed{
                    padding-top: 5px;
                    }""")
            self.user_update_button.setStyleSheet("""QPushButton{
                    background-color: rgb(0, 0, 0,0);
                    text-align:left;                          
                }
                QPushButton:pressed{
                padding-top: 5px;

                }
                                """)                 
            self.tableWidget_12.setCellWidget(row,5,self.user_delete_button)
            self.tableWidget_12.setCellWidget(row,6,self.user_update_button)
            self.user_delete_button.clicked.connect(self.user_delete)
            self.user_update_button.clicked.connect(self.user_update)   
    def user_trash(self) :
        try:
            self.stackedWidget_2.setCurrentIndex(0)
            cur.execute("""select * from users where userstate = '0' """)
            bring=cur.fetchall() 
            self.tableWidget_9.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_9.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_9.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alert(e)                                         
    def user_searsh(slef):
        try:
            searah=self.lineEdit_8.text()    
            cur.execute(f"""select * from users where userstate = '1' and username=%"{searsh}"%  """)
            bring=cur.fetchall() 
            self.tableWidget_12.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_12.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_12.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alert(e)             
    #----------------------TRASH-----------------#     
    def trash_page(self):
        self.stackedWidget_5.setCurrentIndex(0) 
#-------------------------------SPEND-----------------------------------#
    def dashboard_page(self):
        self.stackedWidget_4.setCurrentIndex(0)
    def spend_page(self):
        try:
            self.stackedWidget_4.setCurrentIndex(0)
        except Exception as e:
            pyautogui.alert(e)
    def spend_add_page(self):
        try:
            self.dockWidget_2.show()
            self.stackedWidget_8.setCurrentIndex(8)
        except Exception as e:
            pyautogui.alert(e)    
    def spend_insert_data(self):
        try:
            name=self.ext_type_name_4.text()
            price=self.ayoub.value()
            idnumber=random.randrange(1000000)
            state="1"
            cur.execute(f"""insert into spend values("{name}","{price}","{idnumber}","{state}")""")
            cur.execute("""select * from spend """)
            bring=cur.fetchall()
            self.tableWidget.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
            con.commit()
            self.spend_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def spend_tamplate(self):
        try:
            cur.execute("""select * from spend where spendstate="1" """)
            bring=cur.fetchall() 
            self.tableWidget.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alert(e) 
    def spend_delete(self):
        try:
            row=self.tableWidget.currentRow()
            item=self.tableWidget.item(row,2)
            idnumber=item.text()
            cur.execute(f"""update spend set spendstate="0" where spendid="{idnumber}" """)
            self.spend_tamplate()
            con.commit()
            self.spend_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def spend_update(self):
        try:
            row=self.tableWidget.currentRow()
            item=self.tableWidget.item(row,2)
            idnumber=item.text()
            row=self.tableWidget.currentRow()
            item=self.tableWidget.item(row,0)
            name=item.text()
            row=self.tableWidget.currentRow()
            item=self.tableWidget.item(row,1)
            price=item.text()
            cur.execute(f"""update spend set spendname="{name}",spendpeice="{price}" where spendid="{idnumber}" """)
            self.spend_tamplate()
            con.commit()
            self.spend_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def spend_buttons(self):
        try:
            row=self.tableWidget.rowCount()
            for row in range(int(row)):
                self.spend_delete_button=QPushButton(self)
                self.spend_update_button=QPushButton(self)
                icondel=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/icons8-remove-30.png")
                iconup=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/edit.png")
                self.spend_delete_button.setIcon(QtGui.QIcon(icondel))
                self.spend_update_button.setIcon(QtGui.QIcon(iconup))
                size= QSize(20, 20)
                self.spend_delete_button.setIconSize(size)
                self.spend_update_button.setIconSize(size)
                self.spend_delete_button.setStyleSheet("""QPushButton{
                background-color: rgb(255, 255, 255)

                }
                QPushButton:pressed{
                    padding-top: 5px;
                    }""")
                self.spend_update_button.setStyleSheet("""QPushButton{
                    background-color: rgb(0, 0, 0,0);
                    text-align:left;                          
                }
                QPushButton:pressed{
                padding-top: 5px;

                }
                                """)                
                self.tableWidget.setCellWidget(row,2,self.spend_delete_button)
                self.tableWidget.setCellWidget(row,3,self.spend_update_button)
                self.spend_delete_button.clicked.connect(self.spend_delete)
                self.spend_update_button.clicked.connect(self.spend_update)  
        except Exception as e:
            pyautogui.alert(e)            
    def spend_searash(self):
        try:
            searsh=self.lineEdit_11.text()    
            cur.execute(f"""select * from spend where spendstate="1" and spendname=%"{searsh}"% """)
            bring=cur.fetchall() 
            self.tableWidget.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alert(e)             
#-------------------------------39a9aer---------------------------------#
    def parex_page(self):
        try:
            self.stackedWidget_4.setCurrentIndex(5)
        
        except Exception as e:
            pyautogui.alert(e)
    def parex_add_page(self):
        try:
            self.dockWidget_2.show()
            self.stackedWidget_8.setCurrentIndex(10)
        except Exception as e:
            pyautogui.alert(e)
    def parex_insert_data(self):
        try:
            name=self.ext_name_4.text()
            price=self.spinBox_15.value()
            quantity=self.spinBox_14.value()
            idnumber=random.randrange(10000000)
            state="1"
            date=datetime.date.today()            
            cur.execute(f"""insert into parex values("{name}","{price}","{quantity}","{date}","{idnumber}","{state}")""")
            self.parex_tamplate()
            con.commit()
            self.parex_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def parex_tamplate(self):

        try:
            cur.execute("""select * from parex where parexstate="1" """)
            bring=cur.fetchall()
            self.tableWidget_3.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_3.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_3.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
                                
        except Exception as e :
            pyautogui.alert(e)            
    def parex_buttons(self):
        try:
            row=self.tableWidget_3.rowCount()
            for row in range(int(row)):
                self.parex_delete_button=QPushButton(self)
                self.parex_update_button=QPushButton(self)
                icondel=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/icons8-remove-30.png")
                iconup=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/edit.png")
                self.parex_delete_button.setIcon(QtGui.QIcon(icondel))
                self.parex_update_button.setIcon(QtGui.QIcon(iconup))
                size= QSize(20, 20)
                self.parex_delete_button.setIconSize(size)
                self.parex_update_button.setIconSize(size)
                self.parex_delete_button.setStyleSheet("""QPushButton{
                background-color: rgb(255, 255, 255)

                }
                QPushButton:pressed{
                    padding-top: 5px;
                    }""")
                self.parex_update_button.setStyleSheet("""QPushButton{
                    background-color: rgb(0, 0, 0,0);
                    text-align:left;                          
                }
                QPushButton:pressed{
                padding-top: 5px;

                }
                                """)                
                self.tableWidget_3.setCellWidget(row,4,self.parex_delete_button)
                self.tableWidget_3.setCellWidget(row,5,self.parex_update_button)
                self.parex_delete_button.clicked.connect(self.parex_delete)
                self.parex_update_button.clicked.connect(self.parex_update)  
        except Exception as e:
            pyautogui.alert(e) 
    def parex_delete(self):
        try:
            row=self.tableWidget_3.currentRow()
            item=self.tableWidget_3.item(row,4)
            idnumber=item.text()
            cur.execute(f"""update parex set parexstate="0" where parexid="{idnumber}"  """)
            self.parex_tamplate()
            con.commit()
            self.parex_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def parex_update(self):
        try:
            row=self.tableWidget_3.currentRow()
            item=self.tableWidget_3.item(row,4)
            idnumber=item.text()
            row=self.tableWidget_3.currentRow()
            item=self.tableWidget_3.item(row,0)
            name=item.text()
            row=self.tableWidget_3.currentRow()
            item=self.tableWidget_3.item(row,1)
            price=item.text()
            row=self.tableWidget_3.currentRow()
            item=self.tableWidget_3.item(row,2)
            quantity=item.text()
            cur.execute(f"""update parex set parexname="{name}",parexprice="{price}",parexquantity="{quantity}" where parexid="{idnumber}"   """)
            self.parex_tamplate()
            con.commit()
            self.parex_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def parex_searsh(self):
        try:
            searsh=self.lineEdit_16.text()    
            cur.execute(f"""select * from parex where parexstate="1" and parexname= %"{searsh}"% """)
            bring=cur.fetchall()
            self.tableWidget_3.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_3.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_3.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
                                
        except Exception as e :
            pyautogui.alert(e)         
#------------ ------------------parfume original------------------------#
    def parfume_page(self):
        try:
            self.stackedWidget_4.setCurrentIndex(6)
        
        except Exception as e:
            pyautogui.alert(e)
    def parfume_add_page(self):
        try:
            self.dockWidget_2.show()
            self.stackedWidget_8.setCurrentIndex(9)
        except Exception as e:
            pyautogui.alert(e)
    def parfume_insert_data(self):
        try:
            name=self.ext_name_3.text()
            price=self.spinBox_12.value()
            quantity=self.spinBox_13.value()
            idnumber=random.randrange(10000000)
            state="1"
            date=datetime.date.today() 
            cur.execute(f"""insert into parfume values("{name}","{price}","{quantity}","{date}","{idnumber}","{state}")""")
            self.parfume_tamplate()
            con.commit()
            self.parfume_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def parfume_tamplate(self):
        try:
            cur.execute("""select * from parfume where parfumestate='1' """)
            bring=cur.fetchall()
            self.tableWidget_4.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_4.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_4.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))

        except Exception as e:
            pyautogui.alert(e)
    def parfume_delete(self):
        try:
            row=self.tableWidget_4.currentRow()
            item=self.tableWidget_4.item(row,4)
            idnumber=item.text()
            cur.execute(f"""update parfume set parfumestate="0" where parfumeid="{idnumber}"  """)
            self.parfume_tamplate()
            con.commit()
            self.parfume_buttons()
        except Exception as e:
            pyautogui.alert(e)
    def parfume_update(self):
        try:
            row=self.tableWidget_4.currentRow()
            item=self.tableWidget_4.item(row,4)
            idnumber=item.text()
            row=self.tableWidget_4.currentRow()
            item=self.tableWidget_4.item(row,0)
            name=item.text()
            row=self.tableWidget_4.currentRow()
            item=self.tableWidget_4.item(row,1)
            price=item.text()
            row=self.tableWidget_4.currentRow()
            item=self.tableWidget_4.item(row,2)
            quantity=item.text()
            cur.execute(f"""update parfume set parfumename="{name}",parfumeprice="{price}",parfumequantity="{quantity}" where parfumeid="{idnumber}"   """)
            self.parfume_tamplate()
            con.commit()
            self.parfume_buttons()
        except Exception as e:
            pyautogui.alert(e)  
    def parfume_buttons(self):

        try:
            row=self.tableWidget_4.rowCount()
            for row in range(int(row)):
                self.parfume_delete_button=QPushButton(self)
                self.parfume_update_button=QPushButton(self)
                icondel=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/icons8-remove-30.png")
                iconup=QtGui.QPixmap("C:/Users/YouPal/OneDrive/Bureau/MY_JOB_ZARA/icons1/edit.png")
                self.parfume_delete_button.setIcon(QtGui.QIcon(icondel))
                self.parfume_update_button.setIcon(QtGui.QIcon(iconup))
                size= QSize(20, 20)
                self.parfume_delete_button.setIconSize(size)
                self.parfume_update_button.setIconSize(size)
                self.parfume_delete_button.setStyleSheet("""QPushButton{
                background-color: rgb(255, 255, 255)

                }
                QPushButton:pressed{
                    padding-top: 5px;
                    }""")
                self.parfume_update_button.setStyleSheet("""QPushButton{
                    background-color: rgb(0, 0, 0,0);
                    text-align:left;                          
                }
                QPushButton:pressed{
                padding-top: 5px;

                }
                                """)                
                self.tableWidget_4.setCellWidget(row,4,self.parfume_delete_button)
                self.tableWidget_4.setCellWidget(row,5,self.parfume_update_button)
                self.parfume_delete_button.clicked.connect(self.parfume_delete)
                self.parfume_update_button.clicked.connect(self.parfume_update)  
        except Exception as e:
            pyautogui.alert(e)           
    def parfume_searsh(self):
        try:
            searsh=self.lineEdit_17.text()    
            cur.execute(f"""select * from parfume where parfumestate='1' and parfumename= %"{searsh}"% """)
            bring=cur.fetchall()
            self.tableWidget_4.setRowCount(0)
            for index,value in enumerate(bring):
                self.tableWidget_4.insertRow(index)
                for indexs,values in enumerate(value):
                    self.tableWidget_4.setItem(index,indexs,QtWidgets.QTableWidgetItem(values))
        except Exception as e:
            pyautogui.alert(e)            
if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
   

        
        