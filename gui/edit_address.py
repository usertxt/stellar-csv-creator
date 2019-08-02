from PyQt5 import QtWidgets

class EditDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.nickname = QtWidgets.QLineEdit(self)
        self.address = QtWidgets.QLineEdit(self)
        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, self)

        layout = QtWidgets.QFormLayout(self)
        layout.addRow("Nickname", self.nickname)
        layout.addRow("Address", self.address)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        return self.nickname.text(), self.address.text()
