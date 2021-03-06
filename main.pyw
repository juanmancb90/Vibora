# -*- coding: utf-8 -*-
from controlador.controlador import *
import ctypes
"""
Autor: Carlos Andrés Moreno
Blog: http://www.carmoreno.github.io
Github: http://www.github.com/CarMoreno
Version de la app: 1.0

Vibora Calculator es una aplicación construida en Python 2.7 utilizando la librería gráfica PyQt versión 4,
la arquitectura siguiendo el patrón MVC, la parte visual de esta calculadora está basada en Nollr Calculator,
una calculadora hecha con HTML, CSS Y JS disponible en http://apps.nollr.com/calculator.
Espero que pueda ser útil para quien la pueda necesitar.

pull request son bien recibidos :)
"""
if __name__ == '__main__':
	myappid = u'CarMoreno.ViboraCalculator.1.0' # arbitrary string
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

	#Motor de funcionamiento
	app = QtGui.QApplication(sys.argv)
	app.setWindowIcon(QtGui.QIcon('images/icon.png'))
	# app.setFixedSize(300,200)
	myapp = ControladorCalculator()
	myapp.show()
	sys.exit(app.exec_())