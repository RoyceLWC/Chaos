import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

# Resizing graph
# plt.figure(figsize=(4, 3), dpi=300) # have dpi > 300 to not have it look pixelated.

# 1st line
plt.plot(x, y, label='line', color='r', linewidth=3, linestyle='--', marker='x', markersize=10, markeredgecolor='blue')
# Shorthand notation after x,y possible, see documentation

# 2nd line
x2 = np.arange(0, 4.5, 0.5)
plt.plot(x2, x2**2, label='x^2')

# Axis and titles
plt.xlabel('x')
plt.ylabel('y')
plt.title('First Graph', fontdict={
    'fontname': 'Calibri',
    'fontsize': 20
})

# Tick increments
plt.xticks([0, 1, 2, 3, 4])
plt.yticks([n for n in range(0, 17, 2)])

plt.legend()  # Displays the labels

# Saving graph
# plt.savefig('firstgraph.png', dpi=300)  # Saves graph in the same directory

plt.show()
