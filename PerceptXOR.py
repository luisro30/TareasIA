import numpy as np

def funcionEscalon(v):
    if v >= 0:
        return 1
    else:
        return 0

# Diseñando el Modelo de Perceptrón
def modeloPerceptron(x, w, b):
    v = np.dot(w, x) + b
    y = funcionEscalon(v)
    return y

def funcionNOT(x):
    wNOT = -1
    bNOT = 0.5
    return modeloPerceptron(x, wNOT, bNOT)

def funcionAND(x):
    w = np.array([1, 1])
    bAND = -1.5
    return modeloPerceptron(x, w, bAND)

def funcionOR(x):
    w = np.array([1, 1])
    bOR = -0.5
    return modeloPerceptron(x, w, bOR)

# Función Lógica XOR
# con llamadas a las funciones AND, OR y NOT
# en secuencia
def funcionXOR(x):
    y1 = funcionAND(x)
    y2 = funcionOR(x)
    y3 = funcionNOT(y1)
    x_final = np.array([y2, y3])
    salidaFinal = funcionAND(x_final)
    return salidaFinal

# Probando el Modelo de Perceptrón
prueba1 = np.array([0, 1])
prueba2 = np.array([1, 1])
prueba3 = np.array([0, 0])
prueba4 = np.array([1, 0])

print("XOR({}, {}) = {}".format(0, 1, funcionXOR(prueba1)))
print("XOR({}, {}) = {}".format(1, 1, funcionXOR(prueba2)))
print("XOR({}, {}) = {}".format(0, 0, funcionXOR(prueba3)))
print("XOR({}, {}) = {}".format(1, 0, funcionXOR(prueba4)))