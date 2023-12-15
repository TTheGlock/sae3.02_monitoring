import matplotlib.pyplot as plt

def graph(data):
    # Créer le graphique
    plt.plot(data, color='blue', linestyle='solid')

    # Configurer le graphique
    plt.xlabel("Temps (s)")
    plt.ylabel("Charge CPU (%)")
    plt.ylim([0, 100])
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Ajouter un titre
    plt.title("Charge CPU")

    # Ajouter une légende
    plt.legend(["Charge CPU"], loc="upper left")

    # Ajouter des bordures
    plt.grid(axis='both', linestyle='--')

    # Aligner les données
    plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Afficher le graphique
    plt.show()


if __name__ == "__main__":
    # Définir les données
    data = [35, 36, 37, 38, 39, 38, 37, 53, 53, 54]

    # Afficher le graphique
    graph(data)

