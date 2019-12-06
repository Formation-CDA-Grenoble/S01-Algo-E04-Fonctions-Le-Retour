def rankInsideStr(string, character):
    # Début de ton code
    index = string.find(str(character))
    return index if index != -1 else None
    # Fin de ton code



# Pas touche!
tests = (
    ("pomme", "o", 1),
    ("pomme", "m", 2),
    ("pomme", "y", None),
    ("pomme", 3, None),
)

for test in tests:
    print(f"L'appel  rankInsideStr({test[0]}, {test[1]})  renvoie: {rankInsideStr(test[0], test[1])} (résultat attendu: {test[2]})")
