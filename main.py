import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d.axes3d import get_test_data

# Zad1
# Wygeneruj wykres liniowy dla z od 0 do 2pi, x = sin(z), y = 2cos(z).

fig = plt.figure()
ax = fig.gca(projection="3d")
z = np.linspace(0, 2 * np.pi, 100)
x = np.sin(z)
y = 2 * np.cos(z)
ax.plot(x, y, z, label="Zadanie1")
ax.legend()
plt.show()

# Zad2
# Wygeneruj wykres punktowy dla 5 różnych losowych serii
# z użyciem różnych znaczników i kolorów:
# https://matplotlib.org/api/markers_api.html


def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
n = 50
for c, m, zlow, zhigh in [("r", "o", -50, -30), ("b", "^", -40, -20),
                          ("g", "v", -30, -10), ("y", "s", -20, -5),
                          ("m", "*", -50, -5)]:
    xs = randrange(n, 0, 25)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_zlabel("z label")
plt.show()

# Zad3
# Wygeneruj wykres z przykładu 3 w 5 różnych kolorystkach:
# https://matplotlib.org/examples/color/colormaps_reference.html

fig = plt.figure()
ax = fig.gca(projection="3d")
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
lista = ["PuOr", "hot", "coolwarm", "spring", "cool"]
kolor = np.random.choice(lista)
surf = ax.plot_surface(X, Y, Z, cmap=kolor, linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

# Zad4
# Wygeneruj z pomocą dokumentacji wykres słupkowy z przykładu 4
# wykorzystując 5 różnych kombinacji wyglądu.

fig = plt.figure(figsize=(20, 5))
ax1 = fig.add_subplot(151, projection="3d")
ax2 = fig.add_subplot(152, projection="3d")
ax3 = fig.add_subplot(153, projection="3d")
ax4 = fig.add_subplot(154, projection="3d")
ax5 = fig.add_subplot(155, projection="3d")
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade=True, color="r")
ax1.set_title("wykres zacieniony czerwony")
ax2.bar3d(x, y, bottom, width, depth, top, shade=False, color="y")
ax2.set_title("wykres niezacieniony zolty")
ax3.bar3d(x, y, bottom, width, depth, top, shade=True, color="m")
ax3.set_title("wykres zacieniony magenta")
ax4.bar3d(x, y, bottom, width, depth, top, shade=False, color="b")
ax4.set_title("wykres niezacieniony niebieski")
ax5.bar3d(x, y, bottom, width, depth, top, shade=True, color="g")
ax5.set_title("wykres zacieniony zielony")
plt.show()

# Zad5
# W przykładzie 3 zmień gęstość próbek do wykresu na krok 0.1
# oraz włącz antyaliasing. Wyświetl pierwotny i nowy wykres obok siebie.

fig = plt.figure()
ax1 = fig.add_subplot(121, projection="3d")
ax2 = fig.add_subplot(122, projection="3d")
X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
lista = ["PuOr", "hot", "coolwarm", "spring", "cool"]
kolor = np.random.choice(lista)
surf1 = ax1.plot_surface(X, Y, Z, cmap=kolor, linewidth=0, antialiased=False)
ax1.set_zlim(-1.01, 1.01)
ax1.zaxis.set_major_locator(LinearLocator(10))
ax1.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
fig.colorbar(surf1, shrink=0.5, aspect=5)

surf2 = ax2.plot_surface(X, Y, Z, cmap=kolor, linewidth=0, antialiased=True)
ax2.set_zlim(-1.01, 1.01)
ax2.zaxis.set_major_locator(LinearLocator(10))
ax2.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
fig.colorbar(surf2, shrink=0.5, aspect=5)
plt.show()
