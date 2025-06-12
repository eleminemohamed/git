def charger_taches():
    try:
        with open("taches.txt", "r") as file:
            return [line.strip().split(",") for line in file.readlines()]
    except FileNotFoundError:
        return []

def sauvegarder_taches(taches):
    with open("taches.txt", "w") as file:
        for tache in taches:
            file.write(",".join(tache) + "\n")

def ajouter_tache(taches):
    description = input("Entrez la nouvelle tâche : ")
    priorite = input("Entrez la priorité (basse/moyenne/haute) : ")
    taches.append([description, priorite])
    print("Tâche ajoutée avec succès.")

def supprimer_tache(taches):
    afficher_taches(taches)
    try:
        index = int(input("Entrez l'index de la tâche à supprimer : ")) - 1
        if 0 <= index < len(taches):
            taches.pop(index)
            print("Tâche supprimée avec succès.")
        else:
            print("Index invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")

def afficher_taches(taches):
    if not taches:
        print("\nAucune tâche.")
    else:
        print("\nListe des tâches :")
        for i, tache in enumerate(taches, start=1):
            print(f"{i}. {tache[0]} - Priorité: {tache[1]}")