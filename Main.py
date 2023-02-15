from MakeDict import list_elements, get_colors
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math


# Function for creating a text box with more information once a element has been clicked on
def create_fig(evt):
    if evt.inaxes:
        global elements
        num = fig.axes.index(evt.inaxes)
        if ((num+1) % 18) == 0:     # Figure out the group and period of the element
            group = 17
            period = math.floor((num+1)/18)-1
        else:
            group = ((num+1) % 18)-1
            period = math.floor((num+1)/18)

        # From here your period and group don't change, so it's clearest to create a
        # variable:
        element = elements[period, group]
        # That way you don't have a shitload of dictionary accesses, which is kinda
        # unclear and error-prone

        # This next if-check is weird. Adding it ensures that your code doesn't break if
        # element isn't a dict, but perhaps it should break in that case. The goal of this
        # part is to show information about an element in a window. If element isn't a
        # dict, you won't show anything, and this will be a 'silent' bug. This is more
        # difficult to debug than a crash, and since showing information about an element
        # is the core functionality of your program, I think that it's fine if it crashes
        # when it can't do this job.
        #
        # However that's an opinion, but if you don't want to do that I would add a log
        # (import logging;logging.warning(), or just print()) statement explaining that
        # something is going wrong and you don't know what. If you then find out that you
        # _can_ explain what's going wrong before running the code, you don't have to log
        # an error, and you can just fix the bug ;)
        if type(elements[period, group]) == dict:
            newfig, newax = plt.subplots(figsize=(5, 5))
            newax.set_axis_off()
            # Display the detailed information of the element
            newax.text(0.05, 0.95, f'{elements[period, group]["Element"]}', fontsize=20)

            # You have a lot of duplicate code below. This isn't bad per se, but there's
            # also a lot of manual number decreasing (0.04 per row), which is error-prone.
            # Since you're basically iterating over (text+elementvalue), you could create
            # a for-loop. Pseudocode:

            rows = [
                ("Symbol: ", element["Symbol"]),
                ("Atomic number: ", element["Atomic number"]),
                ("Atomic mass: ", f'{element["Atomic mass"]} u'),
                ("Phase at T=298K: ", f'{element["Phase"] or "Unknown"}'),
                # etc
            ]

            # and then something like

            first_row_y = 0.9
            size_per_row = 0.04
            for i, row in enumerate(rows):
                y = first_row_y - (i * size_per_row)
                newax.text(0.05, y, row[0], fontsize=10)
                newax.text(0.55, y, row[1], fontsize=10)

            # That's it!

            # enumerate is fancy but you can also do
            # i = 0
            # for row in rows:
            #     ...
            #     i += 1
            # which is exactly the same as enumerate
            # https://docs.python.org/3/library/functions.html#enumerate

            # The reason you would do this is because then, if you want to change
            # something, you only need to change it in 1 place. Imagine changing x=0.55 ->
            # x=0.70, you would need to
            # 1) replace every one
            # 2) don't forget one
            # 3) check that you haven't forgotten one
            # 4) check that you haven't mistyped one row
            # 5) if you're replacing _all_ 0.55 in the file, check that you aren't
            #    replacing a 0.55 that's not meant to be an x-value.
            #
            # Or, imagine that you don't want to include electronegativity, or want to
            # order the rows by alphabet! That means a lot of manual shuffling,
            # recalculating -0.04's, whatever, and a lot of (manual) testing to see that
            # you haven't screwed anything up.

            # Also, in your old code, there's a lot going on. Sometimes the left side is
            # only a string and the right side is whatever comes out of your elements
            # dict, but sometimes it's more complicated, and you have a unit on the right
            # side, or replace it with "Unknown". This is now happening inside
            # if-statements inside newax.text() function calls, which makes it difficult
            # to see what exactly you are doing where.

            # If you move the text generation to one part of the code, and then the
            # newax.text() function calls in another, you can see more clearly what the
            # logical part of your code is, which makes it easy to ever explain or change
            # it in the future.

            newax.text(0.05, 0.9,  'Symbol: ', fontsize=10)
            newax.text(0.55, 0.9,  f'{elements[period, group]["Symbol"]}', fontsize=10)

            newax.text(0.05, 0.86, 'Atomic number: ', fontsize=10)
            newax.text(0.55, 0.86, f'{elements[period, group]["Atomic number"]}', fontsize=10)

            newax.text(0.05, 0.82, 'Atomic mass: ', fontsize=10)
            newax.text(0.55, 0.82, f'{elements[period, group]["Atomic mass"]} u', fontsize=10)

            newax.text(0.05, 0.78, 'Phase at T=298K: ', fontsize=10)
            newax.text(0.55, 0.78, f'{elements[period, group]["Phase"]}', fontsize=10) \
                if elements[period, group]["Phase"] != "" else newax.text(0.55, 0.78, 'Unknown', fontsize=10)

            newax.text(0.05, 0.74, 'Type: ', fontsize=10)
            newax.text(0.55, 0.74, f'{elements[period, group]["Type"]}', fontsize=10) \
                if elements[period, group]["Type"] != "" else newax.text(0.55, 0.74, 'Unknown', fontsize=10)

            newax.text(0.05, 0.7,  'Electronegativity: ', fontsize=10)
            newax.text(0.55, 0.7,  f'{elements[period, group]["Electronegativity"]}', fontsize=10) \
                if elements[period, group]["Electronegativity"] != "" else newax.text(0.55, 0.7, 'Unknown', fontsize=10)

            newax.text(0.05, 0.66, 'Density: ', fontsize=10)
            newax.text(0.55, 0.66, f'{elements[period, group]["Density"]} g/cm^3', fontsize=10) \
                if elements[period, group]["Density"] != "" else newax.text(0.55, 0.66, 'Unknown', fontsize=10)

            newax.text(0.05, 0.62, 'Melting point: ', fontsize=10)
            newax.text(0.55, 0.62, f'{elements[period, group]["Melting point"]}K', fontsize=10) \
                if elements[period, group]["Melting point"] != "" else newax.text(0.55, 0.62, 'Unknown', fontsize=10)

            newax.text(0.05, 0.58, 'Boiling point: ', fontsize=10)
            newax.text(0.55, 0.58, f'{elements[period, group]["Boiling point"]}K', fontsize=10) \
                if elements[period, group]["Boiling point"] != "" else newax.text(0.55, 0.58, 'Unknown', fontsize=10)

            newax.text(0.05, 0.54, 'Discoverer: ', fontsize=10)
            newax.text(0.55, 0.54, f'{elements[period, group]["Discoverer"]}', fontsize=10) \
                if elements[period, group]["Discoverer"] != "" else newax.text(0.55, 0.54, 'Unknown', fontsize=10)

            newax.text(0.05, 0.5,  'Year: ', fontsize=10)
            newax.text(0.55, 0.5,  f'{elements[period, group]["Year"]}', fontsize=10) \
                if elements[period, group]["Year"] != "" else newax.text(0.55, 0.5, 'Unknown', fontsize=10)

            newfig.show()


# The list of elements
elements = list_elements()

# Keeping track of where an element needs to be print
subPlotRow = 0
subPlotCol = 0

# Parameters for the boxes around the elements
left, width = 0, 1
bottom, height = 0, 1
right = left + width
top = bottom + height

# Creating the plot
fig, ax = plt.subplots(10, 18, figsize=(18, 9))

# Iterating over every subplot and inserting the text of the element
for rowPlot in ax:
    for plot in rowPlot:
        if type(elements[subPlotRow, subPlotCol]) == dict:
            # Disable the axis, so text can be put in place
            plot.set_axis_off()

            # Build a rectangle in axes coords, principle comes from this website:
            # https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html
            p = plt.Rectangle((left, bottom), width, height, fill=True,
                              color=elements[subPlotRow, subPlotCol]["Color"], alpha=0.3)
            p.set_transform(plot.transAxes)
            p.set_clip_on(False)
            plot.add_patch(p)

            # Write the symbol in the middle of the box
            plot.text(0.5 * (left + right), 0.55 * (bottom + top),
                      elements[subPlotRow, subPlotCol]["Symbol"],
                      fontsize=15,
                      horizontalalignment='center',
                      verticalalignment='center', )
            # Write the atom number in the top left corner of the box
            plot.text(left + 0.05, top - 0.05,
                      elements[subPlotRow, subPlotCol]["Atomic number"],
                      fontsize=6,
                      horizontalalignment='left',
                      verticalalignment='top', )
            # Write the Name of the element under the symbol in the centre of the box
            plot.text(0.5 * (left + right), 0.27 * (bottom + top),
                      elements[subPlotRow, subPlotCol]["Element"],
                      fontsize=5,
                      horizontalalignment='center',
                      verticalalignment='center', )
            # Write the atomic weight in the bottom left corner of the box
            plot.text(left + 0.03, bottom + 0.01,
                      elements[subPlotRow, subPlotCol]["Atomic mass"],
                      fontsize=5,
                      horizontalalignment='left',
                      verticalalignment='bottom', )

        else:
            # If there is no element still disable the plot borders
            plot.set_axis_off()

        subPlotCol += 1     # Keep track of the column
    subPlotRow += 1         # Keep track of the row
    subPlotCol = 0          # Reset column count when a new row is indexed

# Inserting the numbers of actinides and lanthanides
for x in range(2):
    plot = ax[x+5][2]
    plot.set_axis_off()

    p = plt.Rectangle((left, bottom), width, height, fill=False)
    p.set_transform(plot.transAxes)
    p.set_clip_on(False)
    plot.add_patch(p)
    if x == 0:
        plot.text(0.5 * (left + right), 0.5 * (bottom + top), "57-71",
                  fontsize=12,
                  horizontalalignment='center',
                  verticalalignment='center', )
    else:
        plot.text(0.5 * (left + right), 0.5 * (bottom + top), "89-103",
                  fontsize=12,
                  horizontalalignment='center',
                  verticalalignment='center', )

# Making the legend
patches = [mpatches.Patch(color=get_colors()[key], alpha=0.3, label=key) for key in list(get_colors())[0:-1]]
plt.figlegend(handles=patches, loc="upper center", fontsize=12)

# Connect a button press event to show more info when an element has been pressed
fig.canvas.mpl_connect("button_press_event", create_fig)

# Create the periodic table
plt.show()
