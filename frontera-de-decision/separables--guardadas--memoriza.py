# Aprender a separar naranjas mirando cajas que ya están hechas.
# Cada naranja: (tamaño, manchas, caja), las dos notas de 0 a 10.
NARANJAS = [
    (8, 2, "mesa"),
    (3, 6, "zumo"),
    (9, 4, "mesa"),
    (2, 2, "zumo"),
    (7, 1, "mesa"),
    (4, 8, "zumo"),
    (6, 3, "mesa"),
    (5, 7, "zumo"),
    (9, 1, "mesa"),
    (3, 4, "zumo"),
    (7, 4, "mesa"),
    (6, 9, "zumo"),
]
# Bajo el paño: naranjas que la regla no ve mientras aprende.
GUARDADAS = [
    (5, 3, "mesa"),
    (4, 2, "mesa"),
    (6, 5, "zumo"),
    (8, 0, "mesa"),
    (2, 5, "zumo"),
    (9, 6, "mesa"),
    (4, 6, "zumo"),
    (7, 3, "mesa"),
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

malas = sum(1 for t, m, c in GUARDADAS if dice(t, m) != c)
print(f"con las guardadas falla {malas} de {len(GUARDADAS)}")
for caja in ("mesa", "zumo"):
    dichas = [dice(t, m) for t, m, c in GUARDADAS if c == caja]
    print(f"de {caja}: a mesa {dichas.count('mesa')},"
          f" a zumo {dichas.count('zumo')}")
