def rankInsideStr(string, character):
    # Début de ton code
    rank = 0
    for currentCharacter in string:
        if currentCharacter == character:
            return rank
        rank += 1
    return None
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
