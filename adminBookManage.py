# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminbookmanage.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminBookManage(object):
    def setupUi(self, adminBookManage):
        adminBookManage.setObjectName("adminBookManage")
        adminBookManage.resize(686, 344)
        self.adminBookSoldBtn = QtWidgets.QPushButton(adminBookManage)
        self.adminBookSoldBtn.setGeometry(QtCore.QRect(10, 270, 75, 51))
        self.adminBookSoldBtn.setObjectName("adminBookSoldBtn")
        self.adminBookFindBtn = QtWidgets.QPushButton(adminBookManage)
        self.adminBookFindBtn.setGeometry(QtCore.QRect(450, 10, 75, 23))
        self.adminBookFindBtn.setObjectName("adminBookFindBtn")
        self.adminBookFindEdit = QtWidgets.QLineEdit(adminBookManage)
        self.adminBookFindEdit.setGeometry(QtCore.QRect(10, 10, 291, 31))
        self.adminBookFindEdit.setObjectName("adminBookFindEdit")
        self.adminBookBackBtn = QtWidgets.QPushButton(adminBookManage)
        self.adminBookBackBtn.setGeometry(QtCore.QRect(580, 270, 75, 51))
        self.adminBookBackBtn.setObjectName("adminBookBackBtn")
        self.adminBookTableWidget = QtWidgets.QTableWidget(adminBookManage)
        self.adminBookTableWidget.setGeometry(QtCore.QRect(10, 70, 651, 181))
        self.adminBookTableWidget.setObjectName("adminBookTableWidget")
        self.adminBookTableWidget.setColumnCount(6)
        self.adminBookTableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminBookTableWidget.setHorizontalHeaderItem(5, item)
        self.comboBox = QtWidgets.QComboBox(adminBookManage)
        self.comboBox.setGeometry(QtCore.QRect(310, 10, 91, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(adminBookManage)
        self.adminBookFindBtn.clicked.connect(adminBookManage.adminBookFind)
        self.adminBookSoldBtn.clicked.connect(adminBookManage.adminBookSold)
        self.adminBookBackBtn.clicked.connect(adminBookManage.adminBookManageBack)
        QtCore.QMetaObject.connectSlotsByName(adminBookManage)

    def retranslateUi(self, adminBookManage):
        _translate = QtCore.QCoreApplication.translate
        adminBookManage.setWindowTitle(_translate("adminBookManage", "Form"))
        self.adminBookSoldBtn.setText(_translate("adminBookManage", "下架"))
        self.adminBookFindBtn.setText(_translate("adminBookManage", "查询"))
        self.adminBookBackBtn.setText(_translate("adminBookManage", "返回"))
        item = self.adminBookTableWidget.verticalHeaderItem(0)
        item.setText(_translate("adminBookManage", "新建行"))
        item = self.adminBookTableWidget.verticalHeaderItem(1)
        item.setText(_translate("adminBookManage", "2"))
        item = self.adminBookTableWidget.verticalHeaderItem(2)
        item.setText(_translate("adminBookManage", "3"))
        item = self.adminBookTableWidget.verticalHeaderItem(3)
        item.setText(_translate("adminBookManage", "4"))
        item = self.adminBookTableWidget.verticalHeaderItem(4)
        item.setText(_translate("adminBookManage", "5"))
        item = self.adminBookTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("adminBookManage", "书名"))
        item = self.adminBookTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("adminBookManage", "种类"))
        item = self.adminBookTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("adminBookManage", "作者"))
        item = self.adminBookTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("adminBookManage", "序列号"))
        item = self.adminBookTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("adminBookManage", "剩余"))
        item = self.adminBookTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("adminBookManage", "已借"))
        self.comboBox.setItemText(0, _translate("adminBookManage", "全部"))
        self.comboBox.setItemText(1, _translate("adminBookManage", "自传"))
        self.comboBox.setItemText(2, _translate("adminBookManage", "医学"))
        self.comboBox.setItemText(3, _translate("adminBookManage", "计算机"))

