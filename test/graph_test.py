import sys
import pyqtgraph as pg

def graph_1(data):
    # create plot
    plt = pg.plot()
    plt.showGrid(x=True, y=True)
    plt.addLegend()

    # set properties
    plt.setLabel('left', 'Taux d utilisage', units='%')
    plt.setLabel('bottom', 'Temps', units='s')
    plt.setXRange(0, 10)
    plt.setYRange(0, 100)
    plt.setWindowTitle('pyqtgraph plot')

    # plot
    plt.plot(range(0, 10), data, pen='b', symbol='x', symbolPen='b', symbolBrush=0.2, name='red')

    return plt


def main():
    app = pg.QtWidgets.QApplication(sys.argv)

    # Get data from another program
    data = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

    # Call the graph function
    graph = graph_1(data)

    # Display the graph
    graph.show()

    # Terminate the application
    sys.exit(app.exec())


if __name__ == "__main__":
  main()