import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QMessageBox)
from PyQt5.QtGui import QIcon   # Para usar íconos


class ConsumoGasolina(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Consumo de Gasolina")
        self.setGeometry(200, 200, 350, 200)

        # 🚗 Establecer icono de la ventana
        self.setWindowIcon(QIcon("descarga.png"))  # Usa .png o .ico

        # Widgets básicos
        self.lblKm = QLabel("Kilómetros recorridos:")
        self.txtKm = QLineEdit()

        self.lblLitros = QLabel("Litros consumidos:")
        self.txtLitros = QLineEdit()

        self.lblPrecio = QLabel("Precio por litro ($):")
        self.txtPrecio = QLineEdit()

        self.botonCalcular = QPushButton("Calcular Consumo")
        self.botonCalcular.clicked.connect(self.calcularConsumo)

        # Layout (diseño vertical)
        layout = QVBoxLayout()
        layout.addWidget(self.lblKm)
        layout.addWidget(self.txtKm)
        layout.addWidget(self.lblLitros)
        layout.addWidget(self.txtLitros)
        layout.addWidget(self.lblPrecio)
        layout.addWidget(self.txtPrecio)
        layout.addWidget(self.botonCalcular)

        self.setLayout(layout)

    def calcularConsumo(self):
        try:
            # Tomar valores ingresados
            km = float(self.txtKm.text())
            litros = float(self.txtLitros.text())
            precio = float(self.txtPrecio.text())

            # Cálculos
            rendimiento = km / litros   # km por litro
            costo = litros * precio     # costo total

            # Mostrar resultados
            QMessageBox.information(
                self,
                "Resultado",
                f"Rendimiento: {rendimiento:.2f} km/L\n"
                f"Costo total: ${costo:.2f}"
            )

        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingresa solo números.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ConsumoGasolina()
    ventana.show()
    sys.exit(app.exec_())
