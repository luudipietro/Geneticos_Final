import numpy as np
import matplotlib.pyplot as plt

def vapor_tacho(t, t0):
    """Calcula el vapor de un tacho individual en el tiempo t."""
    # La duración es siempre 1 unidad de tiempo
    if t0 <= t <= t0 + 1:
        return 1 - (2*t0 - 2*t + 1)**2
    return 0

def generar_curva_perfecta(n_tachos, delta_t=0.63):
    """
    Genera los tiempos de inicio y la curva de vapor total.
    delta_t = 0.5 es el punto de equilibrio matemático para estas parábolas.
    """
    # 1. Crear el cronograma (Schedule) equidistante
    t_inicios = [i * delta_t for i in range(n_tachos)]
    
    # 2. Definir el intervalo de tiempo para la simulación
    t_final = max(t_inicios) + 1.2 # Un margen después del último tacho
    t_espacio = np.linspace(0, t_final, 1000)
    
    # 3. Calcular el vapor total
    vapor_total = []
    for t in t_espacio:
        v_instante = sum(vapor_tacho(t, t0) for t0 in t_inicios)
        vapor_total.append(v_instante)
        
    return t_espacio, vapor_total, t_inicios

# --- EJECUCIÓN ---
N = 3  # Puedes cambiar este valor (5 a 20 según tu TP)
t, v_total, inicios = generar_curva_perfecta(N)

# Visualización
plt.figure(figsize=(12, 6))

# Dibujar tachos individuales en el fondo
for t0 in inicios:
    v_indiv = [vapor_tacho(ti, t0) for ti in t]
    plt.plot(t, v_indiv, color='gray', alpha=0.2, linestyle='--')

# Dibujar la curva maestra
plt.plot(t, v_total, label=f'Consumo Total (N={N})', color='#2ecc71', linewidth=3)

# Referencias visuales
plt.axhline(y=max(v_total), color='red', linestyle=':', label='Pico Máximo')
plt.title(f'Solución Ideal: Meseta de Vapor para {N} Tachos', fontsize=14)
plt.xlabel('Tiempo (t)', fontsize=12)
plt.ylabel('Vapor Total', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

print(f"--- Análisis de la Solución ---")
print(f"Tiempo total de ciclo (timespan): {max(inicios) + 1:.2f}")
print(f"Consumo máximo alcanzado: {max(v_total):.2f}")
print(f"Variabilidad (Desviación Estándar): {np.std(v_total):.4f}")