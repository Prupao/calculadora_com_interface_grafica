from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
interface = uic.loadUi("interface_da_calculadora.ui")


def soma() -> float:
    n1 = float(interface.le_numero1.text())
    n2 = float(interface.le_numero2.text())
    return interface.lcd_DisplayResult.display(n1 + n2)


def subtrair() -> float:
    n1 = float(interface.le_numero1.text())
    n2 = float(interface.le_numero2.text())
    return interface.lcd_DisplayResult.display(n1 - n2)


def multiplicar() -> float:
    n1 = float(interface.le_numero1.text())
    n2 = float(interface.le_numero2.text())
    return interface.lcd_DisplayResult.display(n1 * n2)


def dividir() -> float:
    n1 = float(interface.le_numero1.text())
    n2 = float(interface.le_numero2.text())
    return interface.lcd_DisplayResult.display(n1 / n2)


def limpa() -> None:
    interface.le_numero1.setText("")
    interface.le_numero2.setText("")
    interface.lcd_DisplayResult.display(0)
