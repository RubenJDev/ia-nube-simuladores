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

malas = sum(1 for t, m, c in GUARDADAS if dice(t, m) != c)
print(f"con las guardadas falla {malas} de {len(GUARDADAS)}")
for caja in ("mesa", "zumo"):
    dichas = [dice(t, m) for t, m, c in GUARDADAS if c == caja]
    print(f"de {caja}: a mesa {dichas.count('mesa')},"
          f" a zumo {dichas.count('zumo')}")
