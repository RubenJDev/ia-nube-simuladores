# Aprender a separar naranjas mirando cajas que ya están hechas.
# Cada naranja: (tamaño, manchas, caja), las dos notas de 0 a 10.
NARANJAS = [
    (8, 1, "mesa"),
    (2, 2, "zumo"),
    (3, 6, "zumo"),
    (4, 8, "zumo"),
    (5, 7, "zumo"),
    (3, 4, "zumo"),
    (6, 9, "zumo"),
    (1, 3, "zumo"),
    (2, 7, "zumo"),
    (4, 5, "zumo"),
    (5, 9, "zumo"),
    (1, 1, "zumo"),
    (3, 2, "zumo"),
    (2, 9, "zumo"),
    (6, 8, "zumo"),
    (4, 4, "zumo"),
]

# La regla memoriza: cada naranja va a la caja de la más parecida
# de las cajas, la que está más cerca en tamaño y manchas.


def dice(tamano, manchas):
    cerca = min(NARANJAS, key=lambda o: (o[0] - tamano) ** 2
                + (o[1] - manchas) ** 2)
    return cerca[2]


fallos = sum(1 for t, m, c in NARANJAS if dice(t, m) != c)
print(f"la regla memoriza las {len(NARANJAS)} naranjas de las cajas")
print(f"en las cajas falla {fallos} de {len(NARANJAS)}")
