from collections import deque

def voisinsCase(plateau, case):
    i, j = case
    voisins = {(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)}
    return {(x, y) for x, y in voisins if 0 <= x < len(plateau) and 0 <= y < len(plateau[0]) and not plateau[x][y]}

def voisinsCases(plateau, cases):
    return {voisin for case in cases for voisin in voisinsCase(plateau, case)}

def accessible(plateau, case):
    cases_accessibles = set()
    cases_a_verifier = deque([case])

    while cases_a_verifier:
        current_case = cases_a_verifier.popleft()
        cases_accessibles.add(current_case)
        cases_a_verifier.extend(voisinsCase(plateau, current_case) - cases_accessibles)

    return cases_accessibles

def chemin(plateau, deb, fin):
    return fin in accessible(plateau, deb)


plateau = [
    [True, False, False, False],
    [False, True, True, False]
]

print(chemin(plateau, (1, 3), (1, 0)))  
print(chemin(plateau, (1, 3), (0, 1))) 
