from PyQt5 import QtCore, QtGui, Qt, QtWidgets
import MyModel
from MyDelegate import MyDelegate
from ioc_ui import Ui_MainWindow
import auth_ui
from psp.Pv import Pv
import pyca
import utils
import os
import sys
import pty
import time
import pwd
import socket

class authdialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
      QtWidgets.QDialog.__init__(self, parent)
      self.ui = auth_ui.Ui_Dialog()
      self.ui.setupUi(self)

def caput(pvname,value,timeout=1.0):
    try:
        pv = Pv(pvname)
        pv.connect(timeout)
        pv.get(ctrl=False, timeout=timeout)
        pv.put(value, timeout)
        pv.disconnect()
    except pyca.pyexc as e:
        print('pyca exception: %s' %(e))
    except pyca.caexc as e:
        print('channel access exception: %s' %(e))

######################################################################
 
class GraphicUserInterface(QtWidgets.QMainWindow):
    def __init__(self, app, hutch):
        QtWidgets.QMainWindow.__init__(self)
        self.__app = app
        self.myuid = pwd.getpwuid(os.getuid())[0]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Not sure how to do this in designer, so we put it randomly and move it now.
        self.ui.statusbar.addWidget(self.ui.userLabel)

        d = sys.path[0]
        while os.path.islink(d):
            l = os.readlink(d)
            if l[0] != '/':
                l = os.path.join(os.path.dirname(d), l)
            d = l
        version = os.path.basename(d)
        if len(version) > 1 and version[0] == 'R':
            version = " %s" % version
        else:
            version = ""
        self.setWindowTitle("%s IocManager%s" % (hutch.upper(), version))
        self.hutch = hutch
        self.authdialog = authdialog(self)
        self.model = MyModel.MyModel(hutch)
        self.utimer = QtCore.QTimer()
        self.delegate = MyDelegate(None, hutch)
        self.ui.actionApply.triggered.connect(self.doApply)
        self.ui.actionSave.triggered.connect(self.doSave)
        self.ui.actionRevert.triggered.connect(self.model.doRevert)
        self.ui.actionReboot.triggered.connect(self.doReboot)
        self.ui.actionHard_Reboot.triggered.connect(self.doHardReboot)
        self.ui.actionReboot_Server.triggered.connect(self.doServerReboot)
        self.ui.actionLog.triggered.connect(self.doLog)
        self.ui.actionConsole.triggered.connect(self.doConsole)
        self.ui.actionRemember.triggered.connect(self.model.doSaveVersions)
        self.ui.actionAuth.triggered.connect(self.doAuthenticate)
        self.ui.actionQuit.triggered.connect(self.doQuit)
        self.ui.actionHelp.triggered.connect(self.doHelp)
        self.ui.findpv.returnPressed.connect(self. doFindPV)
        self.utimer.timeout.connect(self.unauthenticate)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.setItemDelegate(self.delegate)
        self.ui.tableView.verticalHeader().setVisible(False)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.resizeRowsToContents()
        self.ui.tableView.setSortingEnabled(True)
        self.ui.tableView.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.ui.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tableView.selectionModel().selectionChanged.connect(self.getSelection)
        self.ui.tableView.customContextMenuRequested.connect(self.showContextMenu)
        self.currentIOC = None
        self.currentBase = None
        self.pvlist = []
        self.model.startPoll()
        self.unauthenticate()

    def closeEvent(self, event):
        self.disconnectPVs()
        self.model.cleanupChildren()
        QtWidgets.QMainWindow.closeEvent(self, event)

    def disconnectPVs(self):
        for pv in self.pvlist:
            try:
                pv.disconnect()
            except:
                pass
        self.pvlist = []

    def displayPV(self, pv, e=None):
        try:
            if e is None:
                pv.gui.setText(pv.format % pv.value)
        except:
            pass

    def doApply(self):
        if not self.authorize_action(True):
            return
        self.model.doApply()

    def doHelp(self):
        d = QtWidgets.QDialog();
        d.setWindowTitle("IocManager Help")
        d.layout = QtWidgets.QVBoxLayout(d)
        d.label1 = QtWidgets.QLabel(d)
        d.label1.setText("Documentation for the IocManager can be found on confluence:")
        d.layout.addWidget(d.label1)
        d.label2 = QtWidgets.QLabel(d)
        d.label2.setText("https://confluence.slac.stanford.edu/display/PCDS/IOC+Manager+User+Guide")
        d.layout.addWidget(d.label2)
        d.buttonBox = QtWidgets.QDialogButtonBox(d)
        d.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        d.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        d.layout.addWidget(d.buttonBox)
        d.buttonBox.accepted.connect(d.accept)
        d.exec_()

    def doFindPV(self):
        d = QtWidgets.QDialog();
        d.setWindowTitle("Find PV: %s" % self.ui.findpv.text())
        d.layout = QtWidgets.QVBoxLayout(d)
        te = QtWidgets.QPlainTextEdit(d)
        te.setMinimumSize(QtCore.QSize(600, 200))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        te.setFont(font)
        te.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        te.setMaximumBlockCount(500)
        te.setPlainText("")
        result = self.model.findPV(str(self.ui.findpv.text())) # Return list of (pv, ioc, alias)
        if type(result) == list:
            for l in result:
                if l[2] != "":
                    te.appendPlainText("%s --> %s (%s)" % l)
                else:
                    te.appendPlainText("%s --> %s%s" % l)     # Since l[2] is empty!
            if len(result) == 1:
                sm = self.ui.tableView.selectionModel()
                idx = self.model.createIndex(self.model.findid(l[1]), 0)
                sm.select(idx, Qt.QItemSelectionModel.SelectCurrent)
                self.ui.tableView.scrollTo(idx, Qt.QAbstractItemView.PositionAtCenter)
            elif len(result) == 0:
                te.appendPlainText("Searching for '%s' produced no matches!\n" % self.ui.findpv.text())
        else:
            te.appendPlainText(result)
        d.layout.addWidget(te)
        d.buttonBox = QtWidgets.QDialogButtonBox(d)
        d.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        d.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        d.layout.addWidget(d.buttonBox)
        d.buttonBox.accepted.connect(d.accept)
        d.exec_()
                             
    def doQuit(self):
        self.close()
        
    def doSave(self):
        if not self.authorize_action(True):
            return
        self.model.doSave()

    def doReboot(self):
        if self.currentBase:
            caput(self.currentBase + ":SYSRESET", 1)

    def doHardReboot(self):
        if self.currentIOC:
            self.model.rebootIOC(self.currentIOC)

    def doServerReboot(self):
        if self.currentIOC:
            if not self.authorize_action(False):
                return
            self.model.rebootServer(self.currentIOC)
    
    def doLog(self):
        if self.currentIOC:
            self.model.viewlogIOC(self.currentIOC)
    
    def doConsole(self):
        if self.currentIOC and (self.model.getVar('allow_console') or self.authorize_action(False)):
            self.model.connectIOC(self.currentIOC)
    
    def dopv(self, name, gui, format):
        pv = Pv(name, initialize=True)
        if pv != None:
            gui.setText("")
            pv.gui = gui
            pv.format = format
            self.pvlist.append(pv)
            pv.add_monitor_callback(lambda e: self.displayPV(pv, e))
            try:
                pv.wait_ready(0.5)
                pv.monitor()
            except:
                pass

    def getSelection(self, selected, deselected):
        try:
            row = selected.indexes()[0].row()
            ioc = self.model.data(self.model.index(row, MyModel.IOCNAME), QtCore.Qt.EditRole).value()
            host = self.model.data(self.model.index(row, MyModel.HOST), QtCore.Qt.EditRole).value()
            if ioc == self.currentIOC:
                return
            self.disconnectPVs()
            self.currentIOC = ioc
            self.ui.IOCname.setText(ioc)
            base = utils.getBaseName(ioc)
            self.currentBase = base
            if base != None:
                self.dopv(base + ":HEARTBEAT", self.ui.heartbeat, "%d")
                self.dopv(base + ":TOD",       self.ui.tod,       "%s")
                self.dopv(base + ":STARTTOD",  self.ui.boottime,  "%s")
                pyca.flush_io()
            d = utils.netconfig(host)
            try:
                self.ui.location.setText(d['location'])
            except:
                self.ui.location.setText("")
            try:
                self.ui.description.setText(d['description'])
            except:
                self.ui.description.setText("")
        except:
            pass
    
    def showContextMenu(self, pos):
        index = self.ui.tableView.indexAt(pos)
        menu = QtWidgets.QMenu()
        menu.addAction("Add New IOC")
        if index.row() != -1:
            menu.addAction("Delete IOC")
            if not self.model.isHard(index):
                if not self.model.inConfig(index):
                    menu.addAction("Add Running to Config")
                if self.model.notSynched(index):
                    menu.addAction("Set from Running")
                if self.model.needsApply(index):
                    menu.addAction("Apply Configuration")
                menu.addAction("Remember Version")
            if self.model.isChanged(index):
                menu.addAction("Revert IOC")
            menu.addAction("Edit Details")
        gpos = self.ui.tableView.viewport().mapToGlobal(pos)
        selectedItem = menu.exec_(gpos)
        if selectedItem != None:
            txt = selectedItem.text()
            if txt == "Revert IOC":
                self.model.revertIOC(index)
            elif txt == "Delete IOC":
                self.model.deleteIOC(index)
            elif txt == "Add New IOC":
                self.addIOC(index)
            elif txt == "Set from Running":
                self.model.setFromRunning(index)
            elif txt == "Add Running to Config":
                self.model.addExisting(index)
            elif txt == "Remember Version":
                self.model.saveVersion(index)
            elif txt == "Edit Details":
                self.model.editDetails(index)
            elif txt == "Apply Configuration":
                self.model.applyOne(index)

    def setParent(self, gui, iocfn, dir):
        if dir != "":
            gui.setText(utils.findParent(iocfn(), dir))

    def addIOC(self, index):
        d=QtWidgets.QFileDialog(self, "Add New IOC", utils.EPICS_SITE_TOP + "ioc/" + self.hutch)
        d.setFileMode(Qt.QFileDialog.Directory)
        d.setOptions(Qt.QFileDialog.ShowDirsOnly|Qt.QFileDialog.DontUseNativeDialog)
        d.setSidebarUrls([QtCore.QUrl("file://" + os.getenv("HOME")),
                          QtCore.QUrl("file://" + utils.EPICS_SITE_TOP + "ioc/" + self.hutch),
                          QtCore.QUrl("file://" + utils.EPICS_SITE_TOP + "ioc/common"),
                          QtCore.QUrl("file://" + utils.EPICS_DEV_TOP )])
        l=d.layout()

        tmp=QtWidgets.QLabel()
        tmp.setText("IOC Name *+")
        l.addWidget(tmp, 4, 0)
        namegui=QtWidgets.QLineEdit()
        l.addWidget(namegui, 4, 1)

        tmp=QtWidgets.QLabel()
        tmp.setText("Alias")
        l.addWidget(tmp, 5, 0)
        aliasgui=QtWidgets.QLineEdit()
        l.addWidget(aliasgui, 5, 1)

        tmp=QtWidgets.QLabel()
        tmp.setText("Host *")
        l.addWidget(tmp, 6, 0)
        hostgui=QtWidgets.QLineEdit()
        l.addWidget(hostgui, 6, 1)

        tmp=QtWidgets.QLabel()
        tmp.setText("Port (-1 = HARD IOC) *+")
        l.addWidget(tmp, 7, 0)
        portgui=QtWidgets.QLineEdit()
        l.addWidget(portgui, 7, 1)

        tmp=QtWidgets.QLabel()
        tmp.setText("Parent")
        l.addWidget(tmp, 8, 0)
        parentgui=QtWidgets.QLineEdit()
        parentgui.setReadOnly(True)
        l.addWidget(parentgui, 8, 1)

        tmp=QtWidgets.QLabel()
        tmp.setText("* = Required Fields for Soft IOCs.")
        l.addWidget(tmp, 9, 0)

        tmp=QtWidgets.QLabel()
        tmp.setText("+ = Required Fields for Hard IOCs.")
        l.addWidget(tmp, 10, 0)


        fn = lambda dir : self.setParent(parentgui, namegui.text, dir)
        d.directoryEntered.connect(fn)
        d.currentChanged.connect(fn)

        while True:
            if d.exec_() == Qt.QDialog.Rejected:
                return
            name  = str(namegui.text())
            alias = str(aliasgui.text())
            host  = str(hostgui.text())
            port  = str(portgui.text())
            try:
                dir = str(d.selectedFiles()[0])
            except:
                dir = ""
            try:
                n = int(port)
            except:
                QtWidgets.QMessageBox.critical(None,
                                           "Error",
                                           "Port is not an integer!",
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
                continue
            if name == "" or (n != -1 and (host == "" or port == "" or dir == "")):
                QtWidgets.QMessageBox.critical(None,
                                           "Error",
                                           "Failed to set required parameters for new IOC!",
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
                continue
            self.model.addIOC(name, alias, host, port, dir)
            return

    def authenticate_user(self, user, password):
        if user == "":
            user = self.myuid
        need_su = self.myuid != user
        if not utils.check_ssh(user, self.hutch):
            if self.model.userIO != None:
                try:
                    os.close(self.model.userIO)
                except:
                    pass
            self.model.userIO = None
            self.ui.userLabel.setText("User: " + self.myuid)
            self.model.user = self.myuid
            return self.myuid == user
        #
        # Try to use su to become the user.  If this fails, one of the
        # I/O operations below will raise an exception, because the su
        # will exit.
        #
        (pid, fd) = pty.fork()
        if pid == 0:
            try:
                if need_su:
                    if utils.COMMITHOST == socket.gethostname().split(".")[0]:
                        os.execv("/usr/bin/su", ["su", user, "-c", "/bin/tcsh -if"])
                    else:
                        os.execv("/usr/bin/ssh", ["ssh", user + "@" + utils.COMMITHOST, "/bin/tcsh", "-if"])
                else:
                    if utils.COMMITHOST == socket.gethostname().split(".")[0]:
                        print("C")
                        os.execv("/bin/tcsh", ["tcsh", "-if"])
                    else:
                        print("D")
                        os.execv("/usr/bin/ssh", ["ssh", utils.COMMITHOST, "/bin/tcsh", "-if"])
            except:
                pass
            print("Say what?  execv failed?")
            sys.exit(0)
        l = utils.read_until(fd, "(assword:|> )").group(1)
        if l != "> ":
            os.write(fd, password + "\n")
            l = utils.read_until(fd, "> ")
        if utils.KINIT != None and password != "":
            os.write(fd, utils.KINIT + "\n")
            l = utils.read_until(fd, ": ")
            os.write(fd, password + "\n")
            l = utils.read_until(fd, "> ")
        #
        # Sigh.  Someone once had a file named time.py in their home 
        # directory.  So let's go somewhere where we know the files.
        #
        os.write(fd, "cd %s\n" % utils.TMP_DIR)
        l = utils.read_until(fd, "> ")
        self.model.user = user
        if self.model.userIO != None:
            try:
                os.close(self.model.userIO)
            except:
                pass
        self.model.userIO = fd
        if need_su:
            self.utimer.start(10 * 60000)  # Let's go for 10 minutes.
        self.ui.userLabel.setText("User: " + user)

    def doAuthenticate(self):
        result = self.authdialog.exec_()
        user = self.authdialog.ui.nameEdit.text()
        password = str(self.authdialog.ui.passEdit.text())
        self.authdialog.ui.passEdit.setText("")
        if result == QtWidgets.QDialog.Accepted:
            try:
                self.authenticate_user(user, password)
            except:
                print("Authentication as %s failed!" % user)
                self.unauthenticate()

    def unauthenticate(self):
        self.utimer.stop()
        self.authenticate_user(self.myuid, "")

    def authorize_action(self, file_action):
        # The user might be OK.
        if (utils.check_auth(self.model.user, self.hutch) and
            (not file_action or utils.check_ssh(self.model.user, self.hutch) == file_action)):
            return True
        # If the user isn't OK, give him or her a chance to authenticate.
        if self.model.user == self.myuid:
            self.doAuthenticate()
        if (utils.check_auth(self.model.user, self.hutch) and
            (not file_action or utils.check_ssh(self.model.user, self.hutch) == file_action)):
            return True
        QtWidgets.QMessageBox.critical(None,
                                   "Error", "Action not authorized for user %s" % self.model.user,
                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        return False
