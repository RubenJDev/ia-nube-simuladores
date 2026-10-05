# Un lote de naranjas sin separar. Cada una: (tamaño, manchas), las
# dos notas de 0 a 10. Nadie dice qué tipos hay: se hacen K montones.
NARANJAS = [
    (8, 5), (1, 2), (2, 8), (9, 4), (2, 1), (1, 7),
    (7, 6), (2, 3), (3, 7), (8, 3), (3, 2), (2, 6),
    (9, 6), (1, 1), (1, 8), (7, 4), (8, 7),
]
K = 2
# Los K centros de partida: K naranjas del lote, sorteadas con la
# semilla 1. Con otra semilla se parte de otras.
centros = [(7, 4), (2, 3)]


def mas_cercano(tamano, manchas):
    mejor, mejor_d = 0, None
    for i, (x, y) in enumerate(centros):
        dx, dy = tamano - x, manchas - y
        d = dx * dx + dy * dy
        if mejor_d is None or d < mejor_d:
            mejor, mejor_d = i, d
    return mejor


def inercia(montones):
    total = 0.0
    for (tamano, manchas), i in zip(NARANJAS, montones):
        x, y = centros[i]
        dx, dy = tamano - x, manchas - y
        total += dx * dx + dy * dy
    return total


montones = None
for vuelta in range(1, 21):
    # 1. cada naranja, al montón del centro que tiene más cerca
    nuevos = [mas_cercano(t, m) for t, m in NARANJAS]
    if nuevos == montones:
        break  # nadie cambia de montón: ya no se va a mover
    montones = nuevos
    # 2. cada centro, a la media de las naranjas de su montón
    for i in range(K):
        suyas = [n for n, j in zip(NARANJAS, montones) if j == i]
        if suyas:  # un montón vacío deja su centro donde estaba
            centros[i] = (
                sum(t for t, _ in suyas) / len(suyas),
                sum(m for _, m in suyas) / len(suyas),
            )
    print(f"vuelta {vuelta}: inercia {inercia(montones):.2f}")

for i, (x, y) in enumerate(centros):
    print(f"montón {i + 1}: centro ({x:.2f}, {y:.2f}),"
          f" {montones.count(i)} naranjas")
