import matplotlib.pyplot as plt
import math

# Parameters for the boxes around the elements
LEFT, WIDTH = 0, 1
BOTTOM, HEIGHT = 0, 1
RIGHT = LEFT + WIDTH
TOP = BOTTOM + HEIGHT

# Plotting extra information
STARTING_Y = 0.9
SPACING = 0.04
FONT = 10


# Function for creating a text box with more information once an element has been clicked on
def create_fig(num, elements):
    if ((num+1) % 18) == 0:     # Figure out the group and period of the element
        group = 17
        period = math.floor((num+1)/18)-1
    else:
        group = ((num+1) % 18)-1
        period = math.floor((num+1)/18)

    element = elements[period, group]

    # Check if the click happened on an element (type dict), otherwise do nothing
    if type(element) == dict:
        newfig, newax = plt.subplots(figsize=(5, 5))
        newax.set_axis_off()

        # Display the name of the element
        newax.text(0.05, 0.95, f'{element["Element"]}', fontsize=FONT*2)

        # Define extra information of the element
        rows = [
            ("Symbol: ", get_attribute(element, "Symbol")),
            ("Atomic number: ", get_attribute(element, "Atomic number")),
            ("Atomic mass: ", get_attribute(element, "Atomic mass", "u")),
            ("Phase at T=298K: ", get_attribute(element, "Phase")),
            ("Type: ", get_attribute(element, "Type")),
            ("Electronegativity: ", get_attribute(element, "Electronegativity")),
            ("Density: ", get_attribute(element, "Density", " g/cm^3")),
            ("Melting point", get_attribute(element, "Melting point", "K")),
            ("Boiling point", get_attribute(element, "Boiling point", "K")),
            ("Discoverer", get_attribute(element, "Discoverer")),
            ("Year", get_attribute(element, "Year"))
        ]

        # PLot the extra information
        for i, row in enumerate(rows):
            y = STARTING_Y - (i * SPACING)
            newax.text(0.05, y, row[0], fontsize=FONT)
            newax.text(0.55, y, row[1], fontsize=FONT)

        newfig.show()


# Function to return the value
def get_attribute(element, key, unit=""):
    if element[key]:
        return f'{element[key] + unit}'
    return "Unknown"


# Function for plotting the element with a given layout
def plot_element(element, plot):
    # Build a rectangle in axes coords, principle comes from this website:
    # https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html
    p = plt.Rectangle((LEFT, BOTTOM), WIDTH, HEIGHT, fill=True,
                      color=element["Color"], alpha=0.3)
    p.set_transform(plot.transAxes)
    p.set_clip_on(False)
    plot.add_patch(p)
    # Write the symbol in the middle of the box
    plot.text(0.5 * (LEFT + RIGHT), 0.55 * (BOTTOM + TOP),
              element["Symbol"],
              fontsize=15,
              horizontalalignment='center',
              verticalalignment='center', )
    # Write the atom number in the top left corner of the box
    plot.text(LEFT + 0.05, TOP - 0.05,
              element["Atomic number"],
              fontsize=6,
              horizontalalignment='left',
              verticalalignment='top', )
    # Write the Name of the element under the symbol in the centre of the box
    plot.text(0.5 * (LEFT + RIGHT), 0.27 * (BOTTOM + TOP),
              element["Element"],
              fontsize=5,
              horizontalalignment='center',
              verticalalignment='center', )
    # Write the atomic weight in the bottom left corner of the box
    plot.text(LEFT + 0.03, BOTTOM + 0.01,
              element["Atomic mass"],
              fontsize=5,
              horizontalalignment='left',
              verticalalignment='bottom', )


# Function for inserting a text box with the range of atomic numbers of the lathanides and actinides
def lath_act(ax):
    # Inserting the numbers of actinides and lanthanides
    for x in range(2):
        plot = ax[x + 5][2]
        plot.set_axis_off()

        p = plt.Rectangle((LEFT, BOTTOM), WIDTH, HEIGHT, fill=False)
        p.set_transform(plot.transAxes)
        p.set_clip_on(False)
        plot.add_patch(p)
        if x == 0:
            plot.text(0.5 * (LEFT + RIGHT), 0.5 * (BOTTOM + TOP), "57-71",
                      fontsize=12,
                      horizontalalignment='center',
                      verticalalignment='center', )
        else:
            plot.text(0.5 * (LEFT + RIGHT), 0.5 * (BOTTOM + TOP), "89-103",
                      fontsize=12,
                      horizontalalignment='center',
                      verticalalignment='center', )
