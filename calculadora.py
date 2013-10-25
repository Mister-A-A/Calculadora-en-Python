# -*- coding: utf-8 -*- 
from PyQt4 import QtCore, QtGui 
import sys 

class Mi_Programa(QtGui.QWidget): 
  
  def __init__(self, parent=None): 
    
    QtGui.QWidget.__init__(self, parent)
    self.setWindowTitle('Calculadora')
    self.resize(310,280) # Tamaño

    self.label = QtGui.QLabel("Primer Numero: ", self)
    self.label.setGeometry(QtCore.QRect(20, 80, 101, 16))
  
    self.label_2 = QtGui.QLabel("Segundo Numero: ", self)
    self.label_2.setGeometry(QtCore.QRect(20, 140, 91, 16))

    self.label_3 = QtGui.QLabel("CALCULADORA DE DOS NUMEROS: ",self)
    self.label_3.setGeometry(QtCore.QRect(90, 20, 131, 16))

    
    
    #Creamos el botón de suma
    self.sumar = QtGui.QPushButton("+",self)
    self.sumar.setGeometry(QtCore.QRect(60, 180, 20, 23))

    #Creamos el botón de resta
    self.restar = QtGui.QPushButton("-",self)
    self.restar.setGeometry(QtCore.QRect(90, 180, 20, 23))

    #Creamos el botón de multiplicar
    self.multiplicar = QtGui.QPushButton("*",self)
    self.multiplicar.setGeometry(QtCore.QRect(120, 180, 20, 23))

    #Creamos el botón de dividir
    self.dividir = QtGui.QPushButton("/",self)
    self.dividir.setGeometry(QtCore.QRect(150, 180, 20, 23))

    #Creamos el botón para limpiar
    self.limpiar = QtGui.QPushButton("Limpiar",self)
    self.limpiar.setGeometry(QtCore.QRect(180, 180, 70, 23))

    #Creamos la caja de texto para el primer numero
    self.primernumero = QtGui.QLineEdit("", self)
    self.primernumero.setGeometry(QtCore.QRect(130, 70, 161, 31))

    #Creamos la caja de texto para el segundo numero
    self.segundonumero = QtGui.QLineEdit("", self)
    self.segundonumero.setGeometry(QtCore.QRect(130, 130, 161, 31))

    #Creamos la caja de texto para mostrar el resultado de la suma
    self.sumita = QtGui.QLineEdit("", self)
    self.sumita.setGeometry(QtCore.QRect(75, 220, 161, 31))
        

    #Le damos la funcionalidad a los botones y llamamos a los def sumando, limpiando 
    self.connect(self.sumar, QtCore.SIGNAL('clicked()'), self.sumando)
    self.connect(self.restar, QtCore.SIGNAL('clicked()'), self.restando)
    self.connect(self.multiplicar, QtCore.SIGNAL('clicked()'), self.multiplicando)
    self.connect(self.dividir, QtCore.SIGNAL('clicked()'), self.dividiendo)
    self.connect(self.limpiar, QtCore.SIGNAL('clicked()'), self.limpiando) 

  def sumando(self): 
    primer_numero = int(self.primernumero.text())
    segundo_numero = int(self.segundonumero.text())
    lasuma=primer_numero+segundo_numero

    self.sumita.setText(str(lasuma))
    print "El resultado es totalmente correcto...!!!"

  def restando(self):
    primer_numero = int(self.primernumero.text())
    segundo_numero = int(self.segundonumero.text())
    laresta=primer_numero-segundo_numero
    self.sumita.setText(str(laresta))
    print "El resultado es totalmente correcto...!!!"

  def multiplicando(self): 
    primer_numero = int(self.primernumero.text())
    segundo_numero = int(self.segundonumero.text())
    lamultiplicacion=primer_numero*segundo_numero

    self.sumita.setText(str(lamultiplicacion))
    print "El resultado es totalmente correcto...!!!"

  def dividiendo(self): 
    primer_numero = int(self.primernumero.text())
    segundo_numero = int(self.segundonumero.text())
    ladivision=primer_numero/segundo_numero

    self.sumita.setText(str(ladivision))
    print "El resultado es totalmente correcto...!!!"

  def limpiando(self):
    self.sumita.setText("")
    self.primernumero.setText("")
    self.segundonumero.setText("")
    print "se limpio correctamente...!!!"
    
aplicacion = QtGui.QApplication(sys.argv) 
formulario = Mi_Programa() 
formulario.show() 
aplicacion.exec_() 
