from matplotlib import pyplot as plt
import numpy as np

lista_03 = [0.3 * x for x in range(20)]
lista_04 = [0.4 * x for x in range(20)]
lista_05 = [0.5 * x for x in range(20)]
lista_06 = [0.6 * x for x in range(20)]
lista_07 = [0.7 * x for x in range(20)]
lista_08 = [0.8 * x for x in range(20)]
lista_09 = [0.9 * x for x in range(20)]


intervalo = [x/10 for x in range(200)]

def VaporTacho_i(t, t0):
  return 1 - (2*t0-2*t + 1)**2 if t > t0 and t < t0+1 else 0

def VaporTotal(t_inicios, intervalo):
  return [sum([VaporTacho_i(t,t0) for t0 in t_inicios]) for t in intervalo]


def variacion_total(data):
    return np.sum(np.abs(np.diff(data)))
    # print(f'Media: {np.mean(data)}')
    # #print(f'Lista {data}')
    # print(f'Std: {np.std(data)}')
    # print(f'Coef Var {np.std(data)/np.mean(data)}')
    # return np.std(data) / np.mean(data)

vtotal_03 = VaporTotal(lista_03, intervalo)
vtotal_04 = VaporTotal(lista_04, intervalo)
vtotal_05 = VaporTotal(lista_05, intervalo)
vtotal_06 = VaporTotal(lista_06, intervalo)
vtotal_07 = VaporTotal(lista_07, intervalo)
vtotal_08 = VaporTotal(lista_08, intervalo)
vtotal_09 = VaporTotal(lista_09, intervalo)

variacion_03 = variacion_total(vtotal_03)
variacion_04 = variacion_total(vtotal_04)
variacion_05 = variacion_total(vtotal_05)
variacion_06 = variacion_total(vtotal_06)
variacion_07 = variacion_total(vtotal_07)
variacion_08 = variacion_total(vtotal_08)
variacion_09 = variacion_total(vtotal_09)

print(variacion_03)
print(variacion_04)
print(variacion_05)
print(variacion_06)
print(variacion_07)
print(variacion_08)
print(variacion_09)

plt.plot(intervalo, vtotal_03, label='total_03')
plt.plot(intervalo, vtotal_04, label='total_04')
plt.plot(intervalo, vtotal_05, label='total_05')
plt.plot(intervalo, vtotal_06, label='total_06')
plt.plot(intervalo, vtotal_07, label='total_07')
plt.plot(intervalo, vtotal_08, label='total_08')
plt.plot(intervalo, vtotal_09, label='total_09')


plt.show()