# Aprender a separar naranjas mirando cajas que ya están hechas.
# Cada naranja: (tamaño en gramos, manchas de 0 a 10, caja).
NARANJAS = [
    (340, 1, "mesa"),
    (160, 2, "zumo"),
    (190, 6, "zumo"),
    (220, 8, "zumo"),
    (250, 7, "zumo"),
    (190, 4, "zumo"),
    (280, 9, "zumo"),
    (130, 3, "zumo"),
    (160, 7, "zumo"),
    (220, 5, "zumo"),
    (250, 9, "zumo"),
    (130, 1, "zumo"),
    (190, 2, "zumo"),
    (160, 9, "zumo"),
    (280, 8, "zumo"),
    (220, 4, "zumo"),
]
# Bajo el paño: naranjas que la regla no ve mientras aprende.
GUARDADAS = [
    (370, 2, "mesa"),
    (160, 4, "zumo"),
    (190, 8, "zumo"),
    (250, 6, "zumo"),
    (130, 5, "zumo"),
    (220, 7, "zumo"),
    (160, 1, "zumo"),
    (280, 7, "zumo"),
    (190, 3, "zumo"),
    (250, 8, "zumo"),
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
