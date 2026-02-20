from matplotlib import pyplot as plt
import numpy as np


intervalo = [x/10 for x in range(200)]

def VaporTacho_i(t, t0):
  return 1 - (2*t0-2*t + 1)**2 if t > t0 and t < t0+1 else 0

def VaporTotal(t_inicios, intervalo):
  return [sum([VaporTacho_i(t,t0) for t0 in t_inicios]) for t in intervalo]



def variacion_total(data):
     return np.sum(np.abs(np.diff(data)))
#     #return np.std(data) / np.mean(data)

def primera_derivada(y_anterior, y_posterior, delta_x):
   return (y_posterior-y_anterior) / (2 * delta_x)

def curvatura(vapor_total):
   suma_curvatura = 0
   for i in range(1, len(vapor_total)-1):
      derivada = primera_derivada(vapor_total[i+1], vapor_total[i-1], 0.1)
      k_i = abs(derivada) / (1 + derivada **2)
      suma_curvatura += (k_i * 0.1)
   return suma_curvatura


decimal_list = [i/1000 for i in range(1000)]
min_variacion = float('inf')
mejor_resultado = {
    'tiempos':None,
    'consumo': None,
    'valor_variacion': None
}

for i in decimal_list:
    tiempos_inicio = [i * x for x in range(20)]
    #print(lista)
    vapor_total = VaporTotal(tiempos_inicio, intervalo)
    variacion_actual = curvatura(vapor_total)
    if variacion_actual < min_variacion:
        min_variacion = variacion_actual
        mejor_resultado.update({
            'tiempos':tiempos_inicio,
            'consumo': vapor_total,
            'valor_variacion': variacion_actual
        })
        
    
print(f'Menor valor de variacion: {mejor_resultado['valor_variacion']}')
print(f'Consumo: {mejor_resultado['consumo']}')    
print(f'Tiempos inicio {mejor_resultado["tiempos"]}')
for tacho in mejor_resultado['tiempos']:
    vt = [VaporTacho_i(t, tacho) for t in intervalo]
    plt.plot(intervalo, vt)
plt.plot(intervalo, mejor_resultado['consumo'])
plt.show()

