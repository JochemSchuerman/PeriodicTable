from MakeDict import list_elements
import matplotlib.pyplot as plt
import math

elements = list_elements()

subPlotRow = 0
subPlotCol = 0

fig, ax = plt.subplots(10, 18, figsize=(18, 9))

for rowPlot in ax:
    for plot in rowPlot:
        if type(elements[subPlotRow, subPlotCol]) == dict:
            # Disable the axis, so text can be put in place
            plot.set_axis_off()

            # Build a rectangle in axes coords, code from:
            # https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_alignment.html
            left, width = 0, 1
            bottom, height = 0, 1
            right = left + width
            top = bottom + height
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
                      fontsize=4,
                      horizontalalignment='center',
                      verticalalignment='center', )
            # Write the atomic weight in the bottom left corner of the box
            plot.text(left + 0.03, bottom + 0.01,
                      elements[subPlotRow, subPlotCol]["Atomic mass"],
                      fontsize=5,
                      horizontalalignment='left',
                      verticalalignment='bottom', )

        else:
            plot.set_axis_off()

        subPlotCol += 1     # Keep track of the column
    subPlotRow += 1         # Keep track of the row
    subPlotCol = 0          # Reset column count when a new row is indexed


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

        if type(elements[period, group]) == dict:
            newfig, newax = plt.subplots(figsize=(5, 5))
            newax.set_axis_off()
            # Display the detailed information of the element
            newax.text(0.05, 0.95, f'{elements[period, group]["Element"]}', fontsize=20)

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


fig.canvas.mpl_connect("button_press_event", create_fig)

plt.show()      # Create the periodic table
