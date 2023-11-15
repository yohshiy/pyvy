# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bin\window_text.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_textDialog(object):
    def setupUi(self, textDialog):
        textDialog.setObjectName("textDialog")
        textDialog.resize(800, 600)
        self.gridLayout = QtWidgets.QGridLayout(textDialog)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.text = QtWidgets.QPlainTextEdit(textDialog)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 1, 0, 1, 20)
        self.preview = QTextOverlayPreview(textDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setScaledContents(True)
        self.preview.setObjectName("preview")
        self.gridLayout.addWidget(self.preview, 0, 0, 1, 20)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonAlignLeft = QtWidgets.QPushButton(textDialog)
        self.buttonAlignLeft.setMaximumSize(QtCore.QSize(24, 16777215))
        self.buttonAlignLeft.setCheckable(True)
        self.buttonAlignLeft.setObjectName("buttonAlignLeft")
        self.buttonGroup = QtWidgets.QButtonGroup(textDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.buttonAlignLeft)
        self.horizontalLayout.addWidget(self.buttonAlignLeft)
        self.buttonAlignCenter = QtWidgets.QPushButton(textDialog)
        self.buttonAlignCenter.setMaximumSize(QtCore.QSize(24, 16777215))
        self.buttonAlignCenter.setCheckable(True)
        self.buttonAlignCenter.setChecked(True)
        self.buttonAlignCenter.setObjectName("buttonAlignCenter")
        self.buttonGroup.addButton(self.buttonAlignCenter)
        self.horizontalLayout.addWidget(self.buttonAlignCenter)
        self.buttonAlignRight = QtWidgets.QPushButton(textDialog)
        self.buttonAlignRight.setMaximumSize(QtCore.QSize(24, 16777215))
        self.buttonAlignRight.setCheckable(True)
        self.buttonAlignRight.setObjectName("buttonAlignRight")
        self.buttonGroup.addButton(self.buttonAlignRight)
        self.horizontalLayout.addWidget(self.buttonAlignRight)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(textDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 19, 3, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(textDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 4, 1, 1)
        self.spinFontSize = QtWidgets.QSpinBox(textDialog)
        self.spinFontSize.setMinimumSize(QtCore.QSize(47, 0))
        self.spinFontSize.setMinimum(1)
        self.spinFontSize.setMaximum(9999)
        self.spinFontSize.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spinFontSize.setProperty("value", 64)
        self.spinFontSize.setObjectName("spinFontSize")
        self.gridLayout.addWidget(self.spinFontSize, 5, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(textDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 6, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonColorFont = QtWidgets.QPushButton(textDialog)
        self.buttonColorFont.setMinimumSize(QtCore.QSize(22, 22))
        self.buttonColorFont.setMaximumSize(QtCore.QSize(22, 22))
        self.buttonColorFont.setObjectName("buttonColorFont")
        self.horizontalLayout_3.addWidget(self.buttonColorFont)
        self.buttonColorShadow = QtWidgets.QPushButton(textDialog)
        self.buttonColorShadow.setMinimumSize(QtCore.QSize(22, 22))
        self.buttonColorShadow.setMaximumSize(QtCore.QSize(22, 22))
        self.buttonColorShadow.setObjectName("buttonColorShadow")
        self.horizontalLayout_3.addWidget(self.buttonColorShadow)
        self.buttonColorBox = QtWidgets.QPushButton(textDialog)
        self.buttonColorBox.setMinimumSize(QtCore.QSize(22, 22))
        self.buttonColorBox.setMaximumSize(QtCore.QSize(22, 22))
        self.buttonColorBox.setObjectName("buttonColorBox")
        self.horizontalLayout_3.addWidget(self.buttonColorBox)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 10, 1, 8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonMarkerIgnore = QtWidgets.QPushButton(textDialog)
        self.buttonMarkerIgnore.setEnabled(False)
        self.buttonMarkerIgnore.setCheckable(True)
        self.buttonMarkerIgnore.setObjectName("buttonMarkerIgnore")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(textDialog)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.buttonMarkerIgnore)
        self.horizontalLayout_2.addWidget(self.buttonMarkerIgnore)
        self.buttonMarkerStart = QtWidgets.QPushButton(textDialog)
        self.buttonMarkerStart.setEnabled(False)
        self.buttonMarkerStart.setCheckable(True)
        self.buttonMarkerStart.setObjectName("buttonMarkerStart")
        self.buttonGroup_2.addButton(self.buttonMarkerStart)
        self.horizontalLayout_2.addWidget(self.buttonMarkerStart)
        self.buttonMarkerBoth = QtWidgets.QPushButton(textDialog)
        self.buttonMarkerBoth.setEnabled(False)
        self.buttonMarkerBoth.setCheckable(True)
        self.buttonMarkerBoth.setChecked(True)
        self.buttonMarkerBoth.setObjectName("buttonMarkerBoth")
        self.buttonGroup_2.addButton(self.buttonMarkerBoth)
        self.horizontalLayout_2.addWidget(self.buttonMarkerBoth)
        self.buttonMarkerEnd = QtWidgets.QPushButton(textDialog)
        self.buttonMarkerEnd.setEnabled(False)
        self.buttonMarkerEnd.setCheckable(True)
        self.buttonMarkerEnd.setObjectName("buttonMarkerEnd")
        self.buttonGroup_2.addButton(self.buttonMarkerEnd)
        self.horizontalLayout_2.addWidget(self.buttonMarkerEnd)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 18)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.spinShadowX = QtWidgets.QSpinBox(textDialog)
        self.spinShadowX.setMinimumSize(QtCore.QSize(70, 0))
        self.spinShadowX.setMinimum(-9999)
        self.spinShadowX.setMaximum(9999)
        self.spinShadowX.setProperty("value", 0)
        self.spinShadowX.setObjectName("spinShadowX")
        self.horizontalLayout_4.addWidget(self.spinShadowX)
        self.spinShadowY = QtWidgets.QSpinBox(textDialog)
        self.spinShadowY.setMinimumSize(QtCore.QSize(70, 0))
        self.spinShadowY.setMinimum(-9999)
        self.spinShadowY.setMaximum(9999)
        self.spinShadowY.setProperty("value", 0)
        self.spinShadowY.setObjectName("spinShadowY")
        self.horizontalLayout_4.addWidget(self.spinShadowY)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 7, 1, 3)
        self.spinBoxWidth = QtWidgets.QSpinBox(textDialog)
        self.spinBoxWidth.setMinimumSize(QtCore.QSize(47, 0))
        self.spinBoxWidth.setMinimum(0)
        self.spinBoxWidth.setMaximum(9999)
        self.spinBoxWidth.setProperty("value", 5)
        self.spinBoxWidth.setObjectName("spinBoxWidth")
        self.gridLayout.addWidget(self.spinBoxWidth, 5, 5, 1, 1)
        self.line = QtWidgets.QFrame(textDialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 18, 3, 1)
        self.comboFont = QtWidgets.QFontComboBox(textDialog)
        self.comboFont.setObjectName("comboFont")
        self.gridLayout.addWidget(self.comboFont, 5, 0, 1, 2)

        self.retranslateUi(textDialog)
        self.buttonBox.accepted.connect(textDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(textDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(textDialog)

    def retranslateUi(self, textDialog):
        _translate = QtCore.QCoreApplication.translate
        textDialog.setWindowTitle(_translate("textDialog", "Add text (unfinished & unstable!!!)"))
        self.preview.setText(_translate("textDialog", "PREVIEW HERE"))
        self.buttonAlignLeft.setText(_translate("textDialog", "L"))
        self.buttonAlignCenter.setText(_translate("textDialog", "C"))
        self.buttonAlignRight.setText(_translate("textDialog", "R"))
        self.label_6.setText(_translate("textDialog", "Box padding"))
        self.spinFontSize.setSuffix(_translate("textDialog", "px"))
        self.label_7.setText(_translate("textDialog", "Shadow offset"))
        self.buttonColorFont.setToolTip(_translate("textDialog", "Text color"))
        self.buttonColorFont.setText(_translate("textDialog", "T"))
        self.buttonColorShadow.setToolTip(_translate("textDialog", "Drop-shadow color"))
        self.buttonColorShadow.setText(_translate("textDialog", "S"))
        self.buttonColorBox.setToolTip(_translate("textDialog", "Background box color"))
        self.buttonColorBox.setText(_translate("textDialog", "BG"))
        self.buttonMarkerIgnore.setText(_translate("textDialog", "Ignore trim markers"))
        self.buttonMarkerStart.setText(_translate("textDialog", "Until start marker"))
        self.buttonMarkerBoth.setText(_translate("textDialog", "Between start and end markers"))
        self.buttonMarkerEnd.setText(_translate("textDialog", "After end marker"))
        self.spinShadowX.setSuffix(_translate("textDialog", "px"))
        self.spinShadowX.setPrefix(_translate("textDialog", "X: "))
        self.spinShadowY.setSuffix(_translate("textDialog", "px"))
        self.spinShadowY.setPrefix(_translate("textDialog", "Y: "))
        self.spinBoxWidth.setSuffix(_translate("textDialog", "px"))
from widgets import QTextOverlayPreview


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    textDialog = QtWidgets.QDialog()
    ui = Ui_textDialog()
    ui.setupUi(textDialog)
    textDialog.show()
    sys.exit(app.exec_())
