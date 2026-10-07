# Aprender a separar naranjas mirando cajas que ya están hechas.
# Cada naranja: (tamaño, manchas, caja), las dos notas de 0 a 10.
NARANJAS = [
    (5, 2, "mesa"),
    (1, 3, "zumo"),
    (4, 6, "mesa"),
    (9, 2, "zumo"),
    (6, 4, "mesa"),
    (2, 7, "zumo"),
    (5, 8, "mesa"),
    (8, 6, "zumo"),
    (4, 1, "mesa"),
    (10, 8, "zumo"),
    (6, 7, "mesa"),
    (1, 2, "zumo"),
]
# Bajo el paño: naranjas que la regla no ve mientras aprende.
GUARDADAS = [
    (5, 5, "mesa"),
    (4, 3, "mesa"),
    (6, 2, "mesa"),
    (2, 4, "zumo"),
    (9, 5, "zumo"),
    (1, 6, "zumo"),
    (8, 3, "zumo"),
    (5, 9, "mesa"),
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
