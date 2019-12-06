def order(list):
    # Début de ton code
    
    # Initialise la liste à renvoyer
    result = []
    # Tant que la liste d'origine n'est pas vide
    for x in range(0, len(list)):
        # Détermine la valeur minimum dans la liste d'origine
        minimum = min(list)
        # Détermine la place de la valeur minimum dans la liste d'origine
        index = list.index(minimum)
        # Ajoute la valeur minimum de la liste d'origine dans la liste à renvoyer
        result.append(minimum)
        # Supprimer la valeur minimum de la liste d'origine
        del list[index]
    # Renvoie la liste
    return result
    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], [1, 2, 3]),
    ([3, 1, 2], [1, 2, 3]),
    ([50, 0, -12, 0], [-12, 0, 0, 50]),
    (["pomme", "banane", "orange"], ["banane", "orange", "pomme"]),
)

for test in tests:
    print(f"L'appel  order({test[0]})  renvoie: {order(test[0])} (résultat attendu: {test[1]})")
