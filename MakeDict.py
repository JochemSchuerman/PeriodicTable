import csv
import numpy as np


def list_elements():
    # Create 10x18 matrix for all elements to go into
    elements = np.empty((10, 18), dtype=dict)
    # Make a cvs reader
    with open('Periodic Table of Elements.csv') as csv_elements:
        csv_reader = csv.reader(csv_elements, delimiter=',')
        next(csv_reader)
        # A counter for the lathanides and actinides
        lath_counter = 3
        act_counter = 3
        # For every row (element) in the csv file create an element instance, to be added to the array 'elements' later
        for row in csv_reader:
            dict_element = {
                "Atomic number": row[0],
                "Element": row[1],
                "Symbol": row[2],
                "Atomic mass": row[3],
                "Period": row[7],
                "Group": row[8],
                "Phase": row[9],
                "Type": row[15],
                "Electronegativity": row[17],
                "Density": row[19],
                "Melting point": row[20],
                "Boiling point": row[21],
                "Discoverer": row[23],
                "Year": row[24],
                "Color": get_colors()[row[15]]
            }

            # This part (for iteration), starting here, is all doing 1 thing: determine
            # the x and y coordinate of the element based on its period, group, and type
            # (lath or act). You can create a function get_x_y_element and pass element.
            #
            # This will not work as is, since your current code uses lath_counter and
            # act_counter, which depend on the order of the csv file. However, the
            # periodic table isn't about correctly-ordered csv files, but about elements.
            # I think it's clearer if you let y be calculated by the properties explicitly
            # present in the csv-file.

            # If the type of the element is not Lanthanide or Actinide, the element should be
            # placed at index [period, group]
            if (dict_element["Type"] != "Lanthanide") and (dict_element["Type"] != "Actinide"):
                elements[int(dict_element["Period"])-1, int(dict_element["Group"])-1] = dict_element
            # If the element is type Lanthanide place it in the Lanthanide group.
            elif dict_element["Type"] == "Lanthanide":
                elements[8, lath_counter] = dict_element
                lath_counter += 1
            # If the element is type Actinide place it in the Actinide group.
            elif dict_element["Type"] == "Actinide":
                elements[9, act_counter] = dict_element
                act_counter += 1

            # OK that might involve some thinking, if you'd like to keep that to a minimum
            # you can also rewrite it to something like this, which does exactly the same
            # but slightly clearer:
            if dict_element["Type"] == "Lanthanide":
                x = 8
                y = lath_counter
                lath_counter += 1
            elif dict_element["Type"] == "Actinide":
                x = 9
                y = act_counter
                act_counter += 1
            else:
                x = int(dict_element["Period"]) - 1
                y = int(dict_element["Group"]) - 1

            elements[x, y] = dict_element
    return elements


def get_colors():
    return {
        "Nonmetal": 'green',
        "Noble Gas": 'purple',
        "Alkali Metal": 'orange',
        "Alkaline Earth Metal": 'yellow',
        "Metalloid": 'cyan',
        "Halogen": 'magenta',
        "Metal": 'blue',
        "Transition Metal": 'red',
        "Lanthanide": 'brown',
        "Actinide": 'pink',
        "Transactinide": 'grey',
        "": 'grey'
    }
