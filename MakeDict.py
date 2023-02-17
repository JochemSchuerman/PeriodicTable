import csv
import numpy as np


def list_elements():
    # Create 10x18 matrix for all elements to go into
    elements = np.empty((10, 18), dtype=dict)
    # Make a cvs reader
    with open('Periodic Table of Elements.csv') as csv_elements:
        csv_reader = csv.reader(csv_elements, delimiter=',')
        next(csv_reader)

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

            # Setting the element to the correct place
            if dict_element["Type"] == "Lanthanide":
                x = 8
                y = int(dict_element["Atomic number"]) - 54
            elif dict_element["Type"] == "Actinide":
                x = 9
                y = int(dict_element["Atomic number"]) - 86
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
