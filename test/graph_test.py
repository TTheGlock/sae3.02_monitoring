# Importez la bibliothèque graphique Qt
import sys
from PySide6.QtCharts import QChart, QBarSeries, QBarSet, QChartView, QLineSeries
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QTableWidget

# Créez une application Qt
app = QApplication(sys.argv)

# Créez une fonction pour créer un graphique
def graph(data):
    # Créez un graphique
    chart = QChart()

    # Ajoutez les données au graphique
    for i in range(len(data)):
        chart.addSeries(QLineSeries([(i, data[i])]).setName(f"Point {i}"))

    # Configurez le graphique
    chart.setTitle("Charge CPU")
    chart.setYRange(0, 100)
    chart.setXRange(0, 9)

    # Créez un widget QChartView
    chartView = QChartView(chart)

    # Afficher le graphique
    chartView.show()

    # Afficher un message
    print("Le graphique a été créé avec succès.")

# Définir les données
data = [35, 36, 37, 38, 39, 38, 37, 53, 53, 54]

# Afficher le graphique
if __name__ == "__main__":
    graph(data)

# Exécutez l'application
app.exec_()
