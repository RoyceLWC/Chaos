# Logistic map | x[n+1] = rx[n](1-x[n])
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns  # Improving visualisations

# r-value
r = 2  # Starting point

# Constant
limit = 100
refining_value = 1  # Making the peaks more pronounced (combat aliasing)

# Initialising a figure (where the graph will be plotted)
fig = plt.figure()

# Styling the graph
sns.set_style('darkgrid')

# Marking the x-axis and y-axis
axis = plt.axes(
    xlim=(0, limit*refining_value),
    ylim=(0, 1),
    xlabel='n',
    ylabel='$x_n$'
)

# Initialising a line variable (refers to an explicit/user-created plotting space with .axes)
line, = axis.plot([], [], label=f'r={r}', color=sns.color_palette('deep')[0], lw=2)  # Unpacking
legend = plt.legend()


# Initialising the animation
def init_func():
    line.set_data([], [])
    if r >= 3.95:
        anim.pause()
    return line,  # Makes note of the previous references for the 'blitting' algorithm


xdata, ydata = [0], [0.5]


# Where the animation takes place; called repeatedly by FuncAnimation object to generate the next frame.
def update_plot(i):
    global xdata, ydata, r  # Reinitialising each list on repeat (to avoid line joining back to start)
    if i == 0:
        xdata, ydata = [0], [0.5]
        r += 0.05  # Increment

    x = i*refining_value

    prev_y = ydata[i-1]
    y = r*prev_y*(1-prev_y)

    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    legend.get_texts()[0].set_text(f'r={round(r, 2)}')  # Update indicated r-value in the legend

    return line, legend  # Maintain both the line and legend for reference in the next frame


anim = FuncAnimation(
    fig,
    update_plot,
    frames=limit,
    init_func=init_func,
    interval=1,  # Minimum time that passes between frames
    blit=True,  # Optimises repetitive drawing by rendering non-changing graphic elements into a background image.
    repeat=True
)

# fig.show()
plt.title(
    'r-dependent behaviour',
    c=sns.color_palette('deep')[0],
    fontdict={
        'fontname': 'monospace',
        'fontsize': 16,
        'fontweight': 'roman'
    }
)
plt.show()
