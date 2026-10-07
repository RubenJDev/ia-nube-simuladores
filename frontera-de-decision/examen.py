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
VUELTAS = 3

# La regla es una recta: si la suma sale positiva, va a la mesa.
peso_tamano = 0
peso_manchas = 0
sesgo = 0


def dice(tamano, manchas):
    suma = peso_tamano * tamano + peso_manchas * manchas + sesgo
    return "mesa" if suma > 0 else "zumo"


for vuelta in range(1, VUELTAS + 1):
    errores = 0
    for tamano, manchas, caja in NARANJAS:
        if dice(tamano, manchas) != caja:
            # se ha equivocado: mueve la recta hacia esta naranja
            signo = 1 if caja == "mesa" else -1
            peso_tamano += signo * tamano
            peso_manchas += signo * manchas
            sesgo += signo
            errores += 1
    print(f"vuelta {vuelta}, errores: {errores}")

fallos = sum(1 for t, m, c in NARANJAS if dice(t, m) != c)
print(f"regla: a la mesa si {peso_tamano}*tamaño"
      f" {peso_manchas:+}*manchas {sesgo:+} > 0")
print(f"con esa regla falla {fallos} de {len(NARANJAS)}")

malas = sum(1 for t, m, c in GUARDADAS if dice(t, m) != c)
print(f"con las guardadas falla {malas} de {len(GUARDADAS)}")
for caja in ("mesa", "zumo"):
    dichas = [dice(t, m) for t, m, c in GUARDADAS if c == caja]
    print(f"de {caja}: a mesa {dichas.count('mesa')},"
          f" a zumo {dichas.count('zumo')}")
