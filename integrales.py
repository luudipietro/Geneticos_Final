from math import sqrt

import numpy as np

intervalo = [x/10 for x in range(200)]

def VaporTacho_i(t, t0):
  return 1 - (2*t0-2*t + 1)**2 if t > t0 and t < t0+1 else 0

def VaporTotal(t_inicios, intervalo):
  return [sum([VaporTacho_i(t,t0) for t0 in t_inicios]) for t in intervalo]


def longitud_arco(vapor_total):
    suma_distancias = 0
    for i in range(len(vapor_total)-1):
        suma_distancias += sqrt((i+1 - i) ** 2 + (vapor_total[i+1] - vapor_total[i]) ** 2)
    distancia_recta = sqrt((len(vapor_total) -1) ** 2 + (vapor_total[-1] - vapor_total[0]) ** 2)

    return suma_distancias / distancia_recta


def primera_derivada(y_anterior, y_posterior, delta_x):
   return (y_posterior-y_anterior) / (2 * delta_x)

def curvatura(vapor_total):
   suma_curvatura = 0
   for i in range(1, len(vapor_total)-1):
      derivada = primera_derivada(vapor_total[i+1], vapor_total[i-1], 0.1)
      k_i = abs(derivada) / (1 + derivada **2)
      suma_curvatura += (k_i * 0.1)
   return suma_curvatura


sol = [0.0, 0.291, 0.582, 0.873, 1.164, 1.4549999999999998, 1.746, 2.037, 2.328, 2.6189999999999998, 2.9099999999999997, 3.2009999999999996, 3.492, 3.783, 4.074, 4.364999999999999, 4.656, 4.947, 5.2379999999999995, 5.529]
sol2 = [0.0, 0.291, 0.582, 0.873, 1.164, 1.4549999999999998, 1.746, 2.037, 2.328, 2.6189999999999998, 2.9099999999999997, 3.2009999999999996, 3.492, 3.783, 4.074, 4.364999999999999, 8, 7, 9, 11]
print(longitud_arco(VaporTotal(sol, intervalo)))
print(longitud_arco(VaporTotal(sol2, intervalo)))
print(curvatura(VaporTotal(sol, intervalo)))
print(curvatura(VaporTotal(sol2, intervalo)))