import sys  # Importation du module sys pour les opérations système.
import pyqtgraph as pg  # Importation de la bibliothèque pyqtgraph sous l'alias pg.

def graph_1(data, nom_charge):
    # Création d'un objet de type plot pour afficher le graphique.
    plt = pg.plot()
    plt.showGrid(x=True, y=True)  # Affichage des grilles pour les axes x et y.
    plt.addLegend()  # Ajout d'une légende au graphique.

    # Configuration des propriétés du graphique.
    plt.setLabel('left', 'Taux d utilisage', units='%')  # Label de l'axe des ordonnées.
    plt.setLabel('bottom', 'Temps', units='s')  # Label de l'axe des abscisses.
    plt.setXRange(0, 10)  # Définition de la plage des valeurs de l'axe des abscisses.
    plt.setYRange(0, 100)  # Définition de la plage des valeurs de l'axe des ordonnées.
    plt.setWindowTitle(nom_charge)  # Attribution du titre de la fenêtre du graphique.

    # Traçage du graphique.
    plt.plot(range(0, 10), data, pen='b', symbol='x', symbolPen='b', symbolBrush=0.2, name='red')
    # Traçage des données avec des points reliés par des lignes bleues et des croix en tant que symboles.

    return plt  # Renvoi de l'objet graphique créé.


def main():
    app = pg.QtWidgets.QApplication(sys.argv)  # Création d'une instance de l'application PyQtGraph.

    # Obtention des données à partir d'un autre programme (données factices).
    data = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50]

    nom = 'bonsoir'  # Attribution d'un nom (factice) à utiliser comme titre pour le graphique.

    # Appel de la fonction graph_1 avec les données et le nom en paramètres.
    graph = graph_1(data, nom)

    # Affichage du graphique.
    graph.show()

    # Exécution de l'application et gestion de l'événement d'arrêt.
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  # Appel de la fonction main lorsque le fichier est exécuté en tant que script.
