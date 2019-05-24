# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_user_manage.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_adminUserManageWidget(object):
    def setupUi(self, adminUserManageWidget):
        adminUserManageWidget.setObjectName("adminUserManageWidget")
        adminUserManageWidget.resize(487, 469)
        adminUserManageWidget.setStyleSheet("/*\n"
"* The MIT License (MIT)\n"
"*\n"
"* Copyright : http://blog.csdn.net/liang19890820\n"
"*\n"
"* Author : 一去丶二三里\n"
"*\n"
"* Date : 2016/07/22\n"
"*\n"
"* Description : 白色靓丽\n"
"*\n"
"*/\n"
"\n"
"/**********子界面背景**********/\n"
"QWidget#customWidget {\n"
"        background: rgb(173, 202, 232);\n"
"}\n"
"\n"
"/**********子界面中央背景**********/\n"
"QWidget#centerWidget {\n"
"        background: rgb(232, 241, 252);\n"
"}\n"
"\n"
"/**********主界面样式**********/\n"
"QWidget#mainWindow {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(232, 241, 252);\n"
"}\n"
"\n"
"QWidget#messageWidget {\n"
"        background: rgba(173, 202, 232, 50%);\n"
"}\n"
"\n"
"QWidget#loadingWidget {\n"
"        border: none;\n"
"        border-radius: 5px;\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"QWidget#remoteWidget {\n"
"        border-top-right-radius: 10px;\n"
"        border-bottom-right-radius: 10px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-left: none;\n"
"        background: transparent;\n"
"}\n"
"\n"
"StyledWidget {\n"
"        qproperty-normalColor: rgb(65, 65, 65);\n"
"        qproperty-disableColor: rgb(180, 180, 180);\n"
"        qproperty-highlightColor: rgb(0, 160, 230);\n"
"        qproperty-errorColor: red;\n"
"}\n"
"\n"
"QProgressIndicator {\n"
"        qproperty-color: rgb(2, 65, 132);\n"
"}\n"
"\n"
"/**********提示**********/\n"
"QToolTip{\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"/**********菜单栏**********/\n"
"QMenuBar {\n"
"        background: rgb(187, 212, 238);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-left: none;\n"
"        border-right: none;\n"
"}\n"
"QMenuBar::item {\n"
"        border: 1px solid transparent;\n"
"        padding: 5px 10px 5px 10px;\n"
"        background: transparent;\n"
"}\n"
"QMenuBar::item:enabled {\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"QMenuBar::item:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QMenuBar::item:enabled:selected {\n"
"        border-top-color: rgb(111, 156, 207);\n"
"        border-bottom-color: rgb(111, 156, 207);\n"
"        background: rgb(198, 224, 252);\n"
"}\n"
"\n"
"/**********菜单**********/\n"
"QMenu {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(232, 241, 250);\n"
"}\n"
"QMenu::item {\n"
"        height: 22px;\n"
"        padding: 0px 25px 0px 20px;\n"
"}\n"
"QMenu::item:enabled {\n"
"        color: rgb(84, 84, 84);\n"
"}\n"
"QMenu::item:!enabled {\n"
"        color: rgb(155, 155, 155);\n"
"}\n"
"QMenu::item:enabled:selected {\n"
"        color: rgb(2, 65, 132);\n"
"        background: rgba(255, 255, 255, 200);\n"
"}\n"
"QMenu::separator {\n"
"        height: 1px;\n"
"        background: rgb(111, 156, 207);\n"
"}\n"
"QMenu::indicator {\n"
"        width: 13px;\n"
"        height: 13px;\n"
"}\n"
"QMenu::icon {\n"
"        padding-left: 2px;\n"
"        padding-right: 2px;\n"
"}\n"
"\n"
"/**********状态栏**********/\n"
"QStatusBar {\n"
"        background: rgb(187, 212, 238);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-left: none;\n"
"        border-right: none;\n"
"        border-bottom: none;\n"
"}\n"
"QStatusBar::item {\n"
"    border: none;\n"
"    border-right: 1px solid rgb(111, 156, 207);\n"
"}\n"
"\n"
"/**********分组框**********/\n"
"QGroupBox {\n"
"        font-size: 15px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-radius: 4px;\n"
"        margin-top: 10px;\n"
"}\n"
"QGroupBox::title {\n"
"        color: rgb(56, 99, 154);\n"
"        top: -12px;\n"
"        left: 10px;\n"
"}\n"
"\n"
"/**********页签项**********/\n"
"QTabWidget::pane {\n"
"        border: none;\n"
"        border-top: 3px solid rgb(0, 78, 161);\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"QTabWidget::tab-bar {\n"
"        border: none;\n"
"}\n"
"QTabBar::tab {\n"
"        border: none;\n"
"        border-top-left-radius: 4px;\n"
"        border-top-right-radius: 4px;\n"
"        color: white;\n"
"        background: rgb(120, 170, 220);\n"
"        height: 28px;\n"
"        min-width: 85px;\n"
"        margin-right: 5px;\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"QTabBar::tab:selected {\n"
"        color: white;\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"\n"
"QTabWidget#tabWidget::pane {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(232, 241, 252);\n"
"        margin-top: -1px;\n"
"}\n"
"\n"
"QTabBar#tabBar::tab {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        border-bottom: none;\n"
"        color: rgb(70, 71, 73);\n"
"        background: transparent;\n"
"}\n"
"QTabBar#tabBar::tab:hover {\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"QTabBar#tabBar::tab:selected {\n"
"        color: rgb(2, 65, 132);\n"
"        background: rgb(232, 241, 252);\n"
"}\n"
"\n"
"/**********表头**********/\n"
"QHeaderView{\n"
"        border: none;\n"
"        border-bottom: 3px solid rgb(0, 78, 161);\n"
"        background: transparent;\n"
"        min-height: 30px;\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"        border: none;\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding-left: 5px;\n"
"}\n"
"QHeaderView::section:horizontal:hover {\n"
"        color: white;\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"QHeaderView::section:horizontal:pressed {\n"
"        color: white;\n"
"        background: rgb(6, 94, 187);\n"
"}\n"
"QHeaderView::up-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"        image: url(:/White/topArrow);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
"        image: url(:/White/topArrowHover);\n"
"}\n"
"QHeaderView::down-arrow {\n"
"        width: 13px;\n"
"        height: 11px;\n"
"        padding-right: 5px;\n"
"        image: url(:/White/bottomArrow);\n"
"        subcontrol-position: center right;\n"
"}\n"
"QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
"        image: url(:/White/bottomArrowHover);\n"
"}\n"
"\n"
"/**********表格**********/\n"
"QTableView {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(224, 238, 255);\n"
"        gridline-color: rgb(111, 156, 207);\n"
"}\n"
"QTableView::item {\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        border: none;\n"
"        background: white;\n"
"        border-right: 1px solid rgb(111, 156, 207);\n"
"        border-bottom: 1px solid rgb(111, 156, 207);\n"
"}\n"
"QTableView::item:selected {\n"
"        background: rgba(255, 255, 255, 100);\n"
"}\n"
"QTableView::item:selected:!active {\n"
"        color: rgb(65, 65, 65);\n"
"}\n"
"QTableView::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"}\n"
"QTableView::indicator:enabled:unchecked {\n"
"        image: url(:/White/checkBox);\n"
"}\n"
"QTableView::indicator:enabled:unchecked:hover {\n"
"        image: url(:/White/checkBoxHover);\n"
"}\n"
"QTableView::indicator:enabled:unchecked:pressed {\n"
"        image: url(:/White/checkBoxPressed);\n"
"}\n"
"QTableView::indicator:enabled:checked {\n"
"        image: url(:/White/checkBoxChecked);\n"
"}\n"
"QTableView::indicator:enabled:checked:hover {\n"
"        image: url(:/White/checkBoxCheckedHover);\n"
"}\n"
"QTableView::indicator:enabled:checked:pressed {\n"
"        image: url(:/White/checkBoxCheckedPressed);\n"
"}\n"
"QTableView::indicator:enabled:indeterminate {\n"
"        image: url(:/White/checkBoxIndeterminate);\n"
"}\n"
"QTableView::indicator:enabled:indeterminate:hover {\n"
"        image: url(:/White/checkBoxIndeterminateHover);\n"
"}\n"
"QTableView::indicator:enabled:indeterminate:pressed {\n"
"        image: url(:/White/checkBoxIndeterminatePressed);\n"
"}\n"
"\n"
"/**********滚动条-水平**********/\n"
"QScrollBar:horizontal {\n"
"        height: 20px;\n"
"        background: transparent;\n"
"        margin-top: 3px;\n"
"        margin-bottom: 3px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"        height: 20px;\n"
"        min-width: 30px;\n"
"        background: rgb(170, 200, 230);\n"
"        margin-left: 15px;\n"
"        margin-right: 15px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"        background: rgb(165, 195, 225);\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"        width: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/arrowLeft);\n"
"        subcontrol-position: left;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"        width: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/arrowRight);\n"
"        subcontrol-position: right;\n"
"}\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-line:horizontal:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {\n"
"        background: transparent;\n"
"}\n"
"\n"
"/**********滚动条-垂直**********/\n"
"QScrollBar:vertical {\n"
"        width: 20px;\n"
"        background: transparent;\n"
"        margin-left: 3px;\n"
"        margin-right: 3px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"        width: 20px;\n"
"        min-height: 30px;\n"
"        background: rgb(170, 200, 230);\n"
"        margin-top: 15px;\n"
"        margin-bottom: 15px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"        background: rgb(165, 195, 225);\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"        height: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/topArrow);\n"
"        subcontrol-position: top;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"        height: 15px;\n"
"        background: transparent;\n"
"        image: url(:/White/bottomArrow);\n"
"        subcontrol-position: bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"        background: rgb(170, 200, 230);\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"        background: transparent;\n"
"}\n"
"\n"
"QScrollBar#verticalScrollBar:vertical {\n"
"        margin-top: 30px;\n"
"}\n"
"\n"
"/**********下拉列表**********/\n"
"QComboBox {\n"
"        height: 25px;\n"
"        border-radius: 4px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"}\n"
"QComboBox:enabled {\n"
"        color: rgb(84, 84, 84);\n"
"}\n"
"QComboBox:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"QComboBox:enabled:hover, QComboBox:enabled:focus {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QComboBox::drop-down {\n"
"        width: 20px;\n"
"        border: none;\n"
"        background: transparent;\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"        background: rgba(255, 255, 255, 30);\n"
"}\n"
"QComboBox::down-arrow {\n"
"        image: url(:/White/arrowBottom);\n"
"}\n"
"QComboBox::down-arrow:on {\n"
"        /**top: 1px;**/\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"        outline: none;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"        height: 25px;\n"
"        color: rgb(73, 73, 73);\n"
"}\n"
"QComboBox QAbstractItemView::item:selected {\n"
"        background: rgb(232, 241, 250);\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"\n"
"/**********进度条**********/\n"
"QProgressBar{\n"
"        border: none;\n"
"        text-align: center;\n"
"        color: white;\n"
"        background: rgb(173, 202, 232);\n"
"}\n"
"QProgressBar::chunk {\n"
"        background: rgb(16, 135, 209);\n"
"}\n"
"\n"
"QProgressBar#progressBar {\n"
"        border: none;\n"
"        text-align: center;\n"
"        color: white;\n"
"        background-color: transparent;\n"
"        background-image: url(\":/White/progressBar\");\n"
"        background-repeat: repeat-x;\n"
"}\n"
"QProgressBar#progressBar::chunk {\n"
"        border: none;\n"
"        background-color: transparent;\n"
"        background-image: url(\":/White/progressBarChunk\");\n"
"        background-repeat: repeat-x;\n"
"}\n"
"\n"
"/**********复选框**********/\n"
"QCheckBox{\n"
"        spacing: 5px;\n"
"}\n"
"QCheckBox:enabled:checked{\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"QCheckBox:enabled:!checked{\n"
"        color: rgb(70, 71, 73);\n"
"}\n"
"QCheckBox:enabled:hover{\n"
"        color: rgb(0, 78, 161);\n"
"}\n"
"QCheckBox:!enabled{\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"QCheckBox::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"        image: url(:/White/checkBox);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"        image: url(:/White/checkBoxHover);\n"
"}\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"        image: url(:/White/checkBoxPressed);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"        image: url(:/White/checkBoxChecked);\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"        image: url(:/White/checkBoxCheckedHover);\n"
"}\n"
"QCheckBox::indicator:checked:pressed {\n"
"        image: url(:/White/checkBoxCheckedPressed);\n"
"}\n"
"QCheckBox::indicator:indeterminate {\n"
"        image: url(:/White/checkBoxIndeterminate);\n"
"}\n"
"QCheckBox::indicator:indeterminate:hover {\n"
"        image: url(:/White/checkBoxIndeterminateHover);\n"
"}\n"
"QCheckBox::indicator:indeterminate:pressed {\n"
"        image: url(:/White/checkBoxIndeterminatePressed);\n"
"}\n"
"\n"
"/**********单选框**********/\n"
"QRadioButton{\n"
"        spacing: 5px;\n"
"}\n"
"QRadioButton:enabled:checked{\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"QRadioButton:enabled:!checked{\n"
"        color: rgb(70, 71, 73);\n"
"}\n"
"QRadioButton:enabled:hover{\n"
"        color: rgb(0, 78, 161);\n"
"}\n"
"QRadioButton:!enabled{\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"QRadioButton::indicator {\n"
"        width: 20px;\n"
"        height: 20px;\n"
"}\n"
"QRadioButton::indicator:unchecked {\n"
"        image: url(:/White/radioButton);\n"
"}\n"
"QRadioButton::indicator:unchecked:hover {\n"
"        image: url(:/White/radioButtonHover);\n"
"}\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"        image: url(:/White/radioButtonPressed);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"        image: url(:/White/radioButtonChecked);\n"
"}\n"
"QRadioButton::indicator:checked:hover {\n"
"        image: url(:/White/radioButtonCheckedHover);\n"
"}\n"
"QRadioButton::indicator:checked:pressed {\n"
"        image: url(:/White/radioButtonCheckedPressed);\n"
"}\n"
"\n"
"/**********输入框**********/\n"
"QLineEdit {\n"
"        border-radius: 4px;\n"
"        height: 25px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"}\n"
"QLineEdit:enabled {\n"
"        color: rgb(84, 84, 84);\n"
"}\n"
"QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QLineEdit:!enabled {\n"
"        color: rgb(80, 80, 80);\n"
"}\n"
"\n"
"/**********文本编辑框**********/\n"
"QTextEdit {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        color: rgb(70, 71, 73);\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"/**********滚动区域**********/\n"
"QScrollArea {\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"/**********滚动区域**********/\n"
"QWidget#transparentWidget {\n"
"        background: transparent;\n"
"}\n"
"\n"
"/**********微调器**********/\n"
"QSpinBox {\n"
"        border-radius: 4px;\n"
"        height: 24px;\n"
"        min-width: 40px;\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"}\n"
"QSpinBox:enabled {\n"
"        color: rgb(60, 60, 60);\n"
"}\n"
"QSpinBox:enabled:hover, QSpinBox:enabled:focus {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QSpinBox:!enabled {\n"
"        color: rgb(210, 210, 210);\n"
"        background: transparent;\n"
"}\n"
"QSpinBox::up-button {\n"
"        border-left: 1px solid rgb(111, 156, 207);\n"
"        width: 18px;\n"
"        height: 12px;\n"
"        border-top-right-radius: 4px;\n"
"        image: url(:/White/upButton);\n"
"}\n"
"QSpinBox::up-button:!enabled {\n"
"        background: transparent;\n"
"}\n"
"QSpinBox::up-button:enabled:hover {\n"
"        background: rgb(255, 255, 255, 30);\n"
"}\n"
"QSpinBox::down-button {\n"
"        border-left: 1px solid rgb(111, 156, 207);\n"
"        width: 18px;\n"
"        height: 12px;\n"
"        border-bottom-right-radius: 4px;\n"
"        image: url(:/White/downButton);\n"
"}\n"
"QSpinBox::down-button:!enabled {\n"
"        background: transparent;\n"
"}\n"
"QSpinBox::down-button:hover {\n"
"        background: rgb(255, 255, 255, 30);\n"
"}\n"
"\n"
"/**********标签**********/\n"
"QLabel#grayLabel {\n"
"        color: rgb(70, 71, 73);\n"
"}\n"
"\n"
"QLabel#highlightLabel {\n"
"        color: rgb(2, 65, 132);\n"
"}\n"
"\n"
"QLabel#redLabel {\n"
"        color: red;\n"
"}\n"
"\n"
"QLabel#grayYaHeiLabel {\n"
"        color: rgb(175, 175, 175);\n"
"        font-size: 16px;\n"
"}\n"
"\n"
"QLabel#blueLabel {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QLabel#listLabel {\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"QLabel#lineBlueLabel {\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"\n"
"QLabel#graySeperateLabel {\n"
"        background: rgb(200, 220, 230);\n"
"}\n"
"\n"
"QLabel#seperateLabel {\n"
"        background: rgb(112, 153, 194);\n"
"}\n"
"\n"
"QLabel#radiusBlueLabel {\n"
"        border-radius: 15px;\n"
"        color: white;\n"
"        font-size: 16px;\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"\n"
"QLabel#skinLabel[colorProperty=\"normal\"] {\n"
"        color: rgb(56, 99, 154);\n"
"}\n"
"QLabel#skinLabel[colorProperty=\"highlight\"] {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QLabel#informationLabel {\n"
"        qproperty-pixmap: url(:/White/information);\n"
"}\n"
"\n"
"QLabel#errorLabel {\n"
"        qproperty-pixmap: url(:/White/error);\n"
"}\n"
"\n"
"QLabel#successLabel {\n"
"        qproperty-pixmap: url(:/White/success);\n"
"}\n"
"\n"
"QLabel#questionLabel {\n"
"        qproperty-pixmap: url(:/White/question);\n"
"}\n"
"\n"
"QLabel#warningLabel {\n"
"        qproperty-pixmap: url(:/White/warning);\n"
"}\n"
"\n"
"QLabel#groupLabel {\n"
"        color: rgb(56, 99, 154);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        font-size: 15px;\n"
"        border-top-color: transparent;\n"
"        border-right-color: transparent;\n"
"        border-left-color: transparent;\n"
"}\n"
"\n"
"/**********按钮**********/\n"
"QToolButton#nsccButton {\n"
"        border: none;\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding: 10px;\n"
"        qproperty-icon: url(:/White/nscc);\n"
"        qproperty-iconSize: 32px 32px;\n"
"        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
"}\n"
"QToolButton#nsccButton:hover {\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"QToolButton#transferButton {\n"
"        border: none;\n"
"        color: rgb(2, 65, 132);\n"
"        background: transparent;\n"
"        padding: 10px;\n"
"        qproperty-icon: url(:/White/transfer);\n"
"        qproperty-iconSize: 32px 32px;\n"
"        qproperty-toolButtonStyle: ToolButtonTextUnderIcon;\n"
"}\n"
"QToolButton#transferButton:hover {\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"\n"
"/**********按钮**********/\n"
"QPushButton{\n"
"        border-radius: 4px;\n"
"        border: none;\n"
"        width: 75px;\n"
"        height: 25px;\n"
"}\n"
"QPushButton:enabled {\n"
"        background: rgb(120, 170, 220);\n"
"        color: white;\n"
"}\n"
"QPushButton:!enabled {\n"
"        background: rgb(180, 180, 180);\n"
"        color: white;\n"
"}\n"
"QPushButton:enabled:hover{\n"
"        background: rgb(100, 160, 220);\n"
"}\n"
"QPushButton:enabled:pressed{\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"\n"
"QPushButton#blueButton {\n"
"        color: white;\n"
"}\n"
"QPushButton#blueButton:enabled {\n"
"        background: rgb(0, 78, 161);\n"
"        color: white;\n"
"}\n"
"QPushButton:!enabled {\n"
"        background: rgb(180, 180, 180);\n"
"        color: white;\n"
"}\n"
"QPushButton#blueButton:enabled:hover {\n"
"        background: rgb(2, 65, 132);\n"
"}\n"
"QPushButton#blueButton:enabled:pressed {\n"
"        background: rgb(6, 94, 187);\n"
"}\n"
"\n"
"QPushButton#selectButton {\n"
"        border: none;\n"
"        border-radius: none;\n"
"        border-left: 1px solid rgb(111, 156, 207);\n"
"        background: transparent;\n"
"        image: url(:/White/scan);\n"
"        color: rgb(51, 51, 51);\n"
"}\n"
"QPushButton#selectButton:enabled:hover{\n"
"        background: rgb(187, 212, 238);\n"
"}\n"
"QPushButton#selectButton:enabled:pressed{\n"
"        background: rgb(120, 170, 220);\n"
"}\n"
"\n"
"QPushButton#linkButton {\n"
"        background: transparent;\n"
"        color: rgb(0, 160, 230);\n"
"        text-align:left;\n"
"}\n"
"QPushButton#linkButton:hover {\n"
"        color: rgb(20, 185, 255);\n"
"        text-decoration: underline;\n"
"}\n"
"QPushButton#linkButton:pressed {\n"
"        color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QPushButton#transparentButton {\n"
"        background: transparent;\n"
"}\n"
"\n"
"/*****************标题栏按钮*******************/\n"
"QPushButton#minimizeButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/minimizeHover);\n"
"}\n"
"QPushButton#minimizeButton:hover {\n"
"        image: url(:/White/minimize);\n"
"}\n"
"QPushButton#minimizeButton:pressed {\n"
"        image: url(:/White/minimizePressed);\n"
"}\n"
"\n"
"QPushButton#maximizeButton[maximizeProperty=\"maximize\"] {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/maximizeHover);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"maximize\"]:hover {\n"
"        image: url(:/White/maximize);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"maximize\"]:pressed {\n"
"        image: url(:/White/maximizePressed);\n"
"}\n"
"\n"
"QPushButton#maximizeButton[maximizeProperty=\"restore\"] {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/restoreHover);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"restore\"]:hover {\n"
"        image: url(:/White/restore);\n"
"}\n"
"QPushButton#maximizeButton[maximizeProperty=\"restore\"]:pressed {\n"
"        image: url(:/White/restorePressed);\n"
"}\n"
"\n"
"QPushButton#closeButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/closeHover);\n"
"}\n"
"QPushButton#closeButton:hover {\n"
"        image: url(:/White/close);\n"
"}\n"
"QPushButton#closeButton:pressed {\n"
"        image: url(:/White/closePressed);\n"
"}\n"
"\n"
"QPushButton#skinButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/skinHover);\n"
"}\n"
"QPushButton#skinButton:hover {\n"
"        image: url(:/White/skin);\n"
"}\n"
"QPushButton#skinButton:pressed {\n"
"        image: url(:/White/skinPressed);\n"
"}\n"
"\n"
"QPushButton#feedbackButton {\n"
"        border-radius: none;\n"
"        border-bottom-left-radius: 4px;\n"
"        border-bottom-right-radius: 4px;\n"
"        background: rgb(120, 170, 220);\n"
"        image: url(:/White/feedbackHover);\n"
"}\n"
"QPushButton#feedbackButton:hover {\n"
"        image: url(:/White/feedback);\n"
"}\n"
"QPushButton#feedbackButton:pressed {\n"
"        image: url(:/White/feedbackPressed);\n"
"}\n"
"\n"
"QPushButton#closeTipButton {\n"
"        border-radius: none;\n"
"        border-image: url(:/White/close);\n"
"        background: transparent;\n"
"}\n"
"QPushButton#closeTipButton:hover {\n"
"        border-image: url(:/White/closeHover);\n"
"}\n"
"QPushButton#closeTipButton:pressed {\n"
"        border-image: url(:/White/closePressed);\n"
"}\n"
"\n"
"QPushButton#changeSkinButton{\n"
"        border-radius: 4px;\n"
"        border: 2px solid rgb(111, 156, 207);\n"
"        background: rgb(204, 227, 252);\n"
"}\n"
"QPushButton#changeSkinButton:hover{\n"
"        border-color: rgb(60, 150, 200);\n"
"}\n"
"QPushButton#changeSkinButton:pressed, QPushButton#changeSkinButton:checked{\n"
"        border-color: rgb(0, 160, 230);\n"
"}\n"
"\n"
"QPushButton#transferButton {\n"
"        padding-left: 5px;\n"
"        padding-right: 5px;\n"
"        color: white;\n"
"        background: rgb(0, 78, 161);\n"
"}\n"
"QPushButton#transferButton:hover {\n"
"        background: rgb(2, 65, 132);\n"
"}\n"
"QPushButton#transferButton:pressed {\n"
"        background: rgb(6, 94, 187);\n"
"}\n"
"QPushButton#transferButton[iconProperty=\"left\"] {\n"
"        qproperty-icon: url(:/White/left);\n"
"}\n"
"QPushButton#transferButton[iconProperty=\"right\"] {\n"
"        qproperty-icon: url(:/White/right);\n"
"}\n"
"\n"
"QPushButton#openButton {\n"
"        border-radius: none;\n"
"        image: url(:/White/open);\n"
"        background: transparent;\n"
"}\n"
"QPushButton#openButton:hover {\n"
"        image: url(:/White/openHover);\n"
"}\n"
"QPushButton#openButton:pressed {\n"
"        image: url(:/White/openPressed);\n"
"}\n"
"\n"
"QPushButton#deleteButton {\n"
"        border-radius: none;\n"
"        image: url(:/White/delete);\n"
"        background: transparent;\n"
"}\n"
"QPushButton#deleteButton:hover {\n"
"        image: url(:/White/deleteHover);\n"
"}\n"
"QPushButton#deleteButton:pressed {\n"
"        image: url(:/White/deletePressed);\n"
"}\n"
"\n"
"QPushButton#menuButton {\n"
"        text-align: left center;\n"
"        padding-left: 3px;\n"
"        color: rgb(84, 84, 84);\n"
"        border: 1px solid rgb(111, 156, 207);\n"
"        background: white;\n"
"}\n"
"QPushButton#menuButton::menu-indicator{\n"
"        subcontrol-position: right center;\n"
"        subcontrol-origin: padding;\n"
"        image: url(:/White/arrowBottom);\n"
"        padding-right: 3px;\n"
"}\n"
"")
        self.adminUserBackBtn = QtWidgets.QPushButton(adminUserManageWidget)
        self.adminUserBackBtn.setGeometry(QtCore.QRect(410, 400, 51, 41))
        self.adminUserBackBtn.setObjectName("adminUserBackBtn")
        self.adminUserTable2 = QtWidgets.QTableWidget(adminUserManageWidget)
        self.adminUserTable2.setGeometry(QtCore.QRect(50, 140, 341, 301))
        self.adminUserTable2.setObjectName("adminUserTable2")
        self.adminUserTable2.setColumnCount(3)
        self.adminUserTable2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.adminUserTable2.setHorizontalHeaderItem(2, item)
        self.adminUserLineEdit2 = QtWidgets.QLineEdit(adminUserManageWidget)
        self.adminUserLineEdit2.setGeometry(QtCore.QRect(40, 50, 351, 41))
        self.adminUserLineEdit2.setText("")
        self.adminUserLineEdit2.setObjectName("adminUserLineEdit2")
        self.adminUserFindBtn = QtWidgets.QPushButton(adminUserManageWidget)
        self.adminUserFindBtn.setGeometry(QtCore.QRect(345, 52, 41, 36))
        self.adminUserFindBtn.setText("")
        self.adminUserFindBtn.setObjectName("adminUserFindBtn")
        self.adminUserLab = QtWidgets.QLabel(adminUserManageWidget)
        self.adminUserLab.setGeometry(QtCore.QRect(150, 100, 171, 41))
        self.adminUserLab.setObjectName("adminUserLab")

        self.retranslateUi(adminUserManageWidget)
        self.adminUserBackBtn.clicked.connect(adminUserManageWidget.adminUserBack)
        self.adminUserFindBtn.clicked.connect(adminUserManageWidget.adminUserFind)
        QtCore.QMetaObject.connectSlotsByName(adminUserManageWidget)

    def retranslateUi(self, adminUserManageWidget):
        _translate = QtCore.QCoreApplication.translate
        adminUserManageWidget.setWindowTitle(_translate("adminUserManageWidget", "Form"))
        self.adminUserBackBtn.setText(_translate("adminUserManageWidget", "返回"))
        item = self.adminUserTable2.horizontalHeaderItem(0)
        item.setText(_translate("adminUserManageWidget", "书籍"))
        item = self.adminUserTable2.horizontalHeaderItem(1)
        item.setText(_translate("adminUserManageWidget", "借出日期"))
        item = self.adminUserTable2.horizontalHeaderItem(2)
        item.setText(_translate("adminUserManageWidget", "归还日期"))
        self.adminUserLab.setText(_translate("adminUserManageWidget", "<html><head/><body><p><span style=\" font-size:14pt;\">用户名</span></p></body></html>"))


