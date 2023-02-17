from MakeDict import list_elements, get_colors
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from CreateFig import create_fig, plot_element, lath_act

# The list of elements
elements = list_elements()

# Keeping track of where an element needs to be print
subPlotRow = 0
subPlotCol = 0


def create_fig_with_elements(evt):
    global elements
    global fig
    if evt.inaxes:
        num = fig.axes.index(evt.inaxes)
        create_fig(num, elements)


# Creating the plot
fig, ax = plt.subplots(10, 18, figsize=(18, 9))

# Iterating over every subplot and inserting the text of the element
for rowPlot in ax:
    for plot in rowPlot:
        # Disable the axis, so text can be put in place
        plot.set_axis_off()

        # Store the element in a variable, empty if there is no element in that spot
        element = elements[subPlotRow, subPlotCol]

        # Check if there is an element (type dict) that needs to be in that position
        # If there is an element plot the element, else do nothing
        if type(element) == dict:
            plot_element(element, plot)
        subPlotCol += 1     # Keep track of the column
    subPlotRow += 1         # Keep track of the row
    subPlotCol = 0          # Reset column count when a new row is indexed

# Insert the range of atomic numbers for the empty spots of the lathanides and actinides
lath_act(ax)

# Making the legend
patches = [mpatches.Patch(color=get_colors()[key], alpha=0.3, label=key) for key in list(get_colors())[0:-1]]
plt.figlegend(handles=patches, loc="upper center", fontsize=12)

# Connect a button press event to show more info when an element has been pressed
fig.canvas.mpl_connect("button_press_event", create_fig_with_elements)

# Create the periodic table
plt.show()
