from PyQt5 import QtCore, QtGui, QtWidgets
from Models.DbHandlerSections import DbHandler

class Ui_MainWindow(object):

    def __init__(self):
       """
       Initializes the object

       """
       self.db_obj = DbHandler()
       self.all_rcrds = {}
       self.angles_def = ["Mass", "Area", "AXB", "t", "R1",	"R2", "Cz",
                         "Cy",	"Tan?",	"Iz", "Iy",	"Iu(max)", "Iv(min)", 
                         "rz",	"ry", "ru(max)", "rv(min)", "Zz", "Zy",
                         "Zpz", "Zpy", "Source"]
       self.beams_def = ["Mass", "Area", "DB", "tw", "T", "FlangeSlope",
                          "R1",	"R2", "Iz", "Iy", "rz",	"ry", "Zz", 
                          "Zy",	"Zpz", "Zpy", "Source"]
       self.channels_def = ["Mass", "Area", "D", "B", "tw",	"T",
           	                "FlangeSlope", "R1", "R2", "Cy", "Iz",
                            "Iy", "rz", "ry", "Zz", "Zy", "Zpz", "Zpy", "Source"]

    def setupUi(self, MainWindow):
        """
        This function will set up the UI elements.
        
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 50, 581, 361))
        self.widget.setObjectName("widget")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 321, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Select designation")
        self.comboBox.activated.connect(self.showdetails)
        self.listView = QtWidgets.QListView(self.widget)
        self.listView.setGeometry(QtCore.QRect(120, 90, 256, 192))
        self.listView.setObjectName("listView")
        self.model = QtGui.QStandardItemModel()
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 300, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuOsdag_Application = QtWidgets.QMenu(self.menubar)
        self.menuOsdag_Application.setObjectName("menuOsdag_Application")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOsdag_Application.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.set_up_cmbbx()

    def set_up_cmbbx(self):
        """
        This function will set up the combobox's
        items for Angles, Beams and Channels
        designation.

        :returns: None
        :rtype: None
        :author: Mushir

        """
        angles_recrd = self.db_obj.get_angles_record()
        beams_recrd = self.db_obj.get_beams_record()
        chnnels_recrd = self.db_obj.get_channels_record()
        all_rcrds = angles_recrd + beams_recrd + chnnels_recrd
        for each_rcrd in all_rcrds:
            designtn_val = each_rcrd[1]
            self.all_rcrds[designtn_val] = list(each_rcrd[2:])
            self.comboBox.addItem(designtn_val)

    def showdetails(self, selected_index):
        """
        This function will get the all details
        for selected item of combobox and
        show the details for designations.

        :param selected_index: contains selected item's index
        :type selected_index: integer
        :returns: None
        :rtype: None
        :author: Mushir

        """
        headers = []
        selected_value = self.comboBox.itemText(selected_index).strip()
        recrd_details = self.all_rcrds.get(selected_value, [])
        if "x" or "X" in selected_value:
            headers = self.angles_def
        elif selected_value.startswith(("JB", "LB", "MB", "NPB")):
            headers = self.beams_def
        elif selected_value.starswith(("MC")):
            headers = self.channels_def
        self.model.clear()
        for index, each_val in enumerate(recrd_details):
            label = headers[index]
            self.model.appendRow(QtGui.QStandardItem("%s --> %s " % \
                                    (label, str(each_val))))
        self.listView.setModel(self.model)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Osdag"))
        self.centralwidget.setToolTip(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "Add Section"))
        self.menuOsdag_Application.setTitle(_translate("MainWindow", "Osdag Application"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

