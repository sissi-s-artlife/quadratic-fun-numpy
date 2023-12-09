import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()
x = np.linspace(-10, 10, 100)
y = x ** 2
sc = ax.scatter(x, y, c=x, cmap='viridis')  # Use x for colors

def update(frame):
    # Change the color mapping smoothly using the frame index
    sc.set_array(x[:frame])
    sc.set_offsets(np.column_stack((x[:frame], y[:frame])))
    return sc,

ani = FuncAnimation(fig, update, frames=len(x), interval=50, repeat=False)
plt.colorbar(sc, ax=ax, label='X-axis')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Animating Color Change with f(x) = x^2')
plt.grid(True)
plt.show()
