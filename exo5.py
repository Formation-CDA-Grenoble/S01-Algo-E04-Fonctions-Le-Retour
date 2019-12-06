import random

def mix(list):
    # Début de ton code

    # Initialise la liste à renvoyer
    result = []
    # Tant que la liste d'origine n'est pas vide
    while len(list) > 0:
        # Prend un élément au hasard de la liste d'origine
        index = random.randint(0, len(list) - 1)
        # Met l'élément dans la liste à renvoyer
        result.append(list[index])
        # Supprimer l'élément de la liste d'origine
        del list[index]
    # Renvoie la liste
    return result
    # Fin de ton code



# Pas touche!
tests = (
    (["a", "b", "c"]),
    (["pomme", "banane", "orange"]),
    ([1, 2, 3]),
    (["a", "b", "c", 1, 2, 3]),
)

for test in tests:
    print(f"L'appel  mix({test})  renvoie: {mix(test)}")
