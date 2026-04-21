import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parametri della molla
k = 10 # Costante elastica (N/m)
m = 5 # Massa (kg)
b = 0.5 # Costante di smorzamento (kg/s), determina la velocità della molla nell'arrivare al centro
A = 1.0  # Ampiezza ridotta per stare nei limiti degli assi
omega_0 = np.sqrt(k / m) # Pulsazione non smorzata
gamma = b / (2 * m) # Coefficiente di smorzamento
omega_d = np.sqrt(omega_0**2 - gamma**2) # Pulsazione smorzata

# Tempo
t_max = 20 # Tempo massimo di simulazione (s)
dt = 0.05 # Intervallo di tempo (s)
t = np.arange(0, t_max, dt) # Tempo

# Funzione per calcolare la posizione smorzata nel tempo
def posizione_molla_smorzata(t, A, omega_d, gamma):
    # Formula per la posizione in un sistema smorzato (senza forza esterna)
    return A * np.exp(-gamma * t) * np.cos(omega_d * t)

# Impostazione della grafica figura
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 0.5)
ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)  # Linea di equilibrio
line, = ax.plot([], [], lw=2, color='blue')
dot, = ax.plot([], [], 'ro', markersize=10)  # Pallino rosso

def init():
    line.set_data([], [])
    dot.set_data([], [])
    return line, dot

def update(frame):
    x = posizione_molla_smorzata(t[frame], A, omega_d, gamma)

    # Molla come onda seno che va da 0 a x (si comprime/allunga)
    n_spire = 10
    x_wave = np.linspace(0, x, 300)
    y_wave = 0.1 * np.sin(np.linspace(0, n_spire * 2 * np.pi, 300))

    line.set_data(x_wave, y_wave)
    dot.set_data([x], [0])  # Lista con un elemento, centrato su y=0
    return line, dot

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt * 1000)

plt.title("Molla Smorzata")
plt.xlabel("Posizione (m)")
plt.ylabel("Deformazione")
plt.show()