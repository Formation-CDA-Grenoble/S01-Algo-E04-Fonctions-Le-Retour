def rankInside(list, element):
    # Début de ton code
    
    # Initiliase le rang de l'objet à rechercher
    rank = 0
    # Pour chaque élément dans la liste
    for item in list:
        # Si l'élément est égal à l'élément recherché
        if item == element:
            # Renvoie le rang de l'objet à rechercher
            return rank
        # Incrémente le rang de l'object à rechercher
        rank += 1
    # Si l'objet demandé n'a pas été trouvé, renvoie None
    return None

    # Fin de ton code



# Pas touche!
tests = (
    ([1, 2, 3], 2, 1),
    ([1, 2, 3], -1, None),
    (["pomme", "banane", "orange"], "pomme", 0),
    (["pomme", "banane", "orange"], "cerise", None),
)

for test in tests:
    print(f"L'appel  rankInside({test[0]}, {test[1]})  renvoie: {rankInside(test[0], test[1])} (résultat attendu: {test[2]})")
