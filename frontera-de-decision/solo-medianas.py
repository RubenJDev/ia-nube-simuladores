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
VUELTAS = 20

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
