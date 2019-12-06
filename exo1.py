def isInside(list, element):
    # Début de ton code
    for item in list:
        if item == element:
            return True
    # Je dois attendre la fin de la boucle pour avoir testé tous les éléments de la liste
    # et donc pouvoir affirmer que l'élément que je cherchais ne s'y trouve pas
    # Je dois donc retirer l'indentation pour signifier au Python qu'il faut attendre
    # la fin de la boucle pour renvoyer False
    return False
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], 2, True),
    ([1, 2, 3], -1, False),
    (["pomme", "banane", "orange"], "pomme", True),
    (["pomme", "banane", "orange"], "cerise", False),
)

for test in tests:
    print(f"L'appel  isInside({test[0]}, {test[1]})  renvoie: {isInside(test[0], test[1])} (résultat attendu: {test[2]})")
