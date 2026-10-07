# Aprender a separar naranjas mirando cajas que ya están hechas.
# Cada naranja: (tamaño en gramos, manchas de 0 a 10, caja).
NARANJAS = [
    (250, 2, "mesa"),
    (130, 3, "zumo"),
    (220, 6, "mesa"),
    (370, 2, "zumo"),
    (280, 4, "mesa"),
    (160, 7, "zumo"),
    (250, 8, "mesa"),
    (340, 6, "zumo"),
    (220, 1, "mesa"),
    (400, 8, "zumo"),
    (280, 7, "mesa"),
    (130, 2, "zumo"),
]
# Bajo el paño: naranjas que la regla no ve mientras aprende.
GUARDADAS = [
    (250, 5, "mesa"),
    (220, 3, "mesa"),
    (280, 2, "mesa"),
    (160, 4, "zumo"),
    (370, 5, "zumo"),
    (130, 6, "zumo"),
    (340, 3, "zumo"),
    (250, 9, "mesa"),
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
