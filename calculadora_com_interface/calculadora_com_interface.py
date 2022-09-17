from interface import *

interface.show()

try:
    soma()
    subtrair()
    multiplicar()
    dividir()
    limpa()
except ValueError:
    print('')


interface.pb_somar.clicked.connect(soma)
interface.pb_subtrair.clicked.connect(subtrair)
interface.pb_multiplicar.clicked.connect(multiplicar)
interface.pb_dividir.clicked.connect(dividir)
interface.pb_limpar.clicked.connect(limpa)
app.exec()
