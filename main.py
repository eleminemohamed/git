from fonctionnalite import *

def afficher_menu():
    print("\nMenu:")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Afficher les tâches")
    print("4. Quitter")

if __name__ == "__main__":
    taches = charger_taches()

    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")

        if choix == "1":
            ajouter_tache(taches)
        elif choix == "2":
            supprimer_tache(taches)
        elif choix == "3":
            afficher_taches(taches)
        elif choix == "4":
            sauvegarder_taches(taches)
            print("Sortie du gestionnaire de tâches.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")