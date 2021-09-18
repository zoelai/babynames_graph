
import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['magenta', 'red', 'purple', 'green', 'blue', 'orange']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = ((width - GRAPH_MARGIN_SIZE*2)/len(YEARS) * year_index) + 20
    return int(x_coordinate)



def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #######################
    count = 0
    for year in YEARS:
        if count <= len(YEARS):
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, count), 0, get_x_coordinate(CANVAS_WIDTH, count), CANVAS_HEIGHT)
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, count) + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[count], anchor=tkinter.NW)
            count += 1

    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color_index = 0
    for name in lookup_names:
        for i in range(len(YEARS)-1):
            x_1 = get_x_coordinate(CANVAS_WIDTH, i)
            x_2 = get_x_coordinate(CANVAS_WIDTH, i + 1)

            # point 1
            if str(YEARS[i]) in name_data[name]:
                y_1 = int(name_data[name][str(YEARS[i])]) * (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)/1000 + GRAPH_MARGIN_SIZE
                y_1_text = int(name_data[name][str(YEARS[i])])
            else:
                y_1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                y_1_text = '*'

            # point 2
            if str(YEARS[i+1]) in name_data[name]:
                y_2 = int(name_data[name][str(YEARS[i + 1])]) * (CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE)/1000 + GRAPH_MARGIN_SIZE
                y_2_text = int(name_data[name][str(YEARS[i + 1])])
            else:
                y_2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                y_2_text = '*'

            # draw line for each name
            canvas.create_line(x_1, y_1, x_2, y_2, width=LINE_WIDTH, fill=COLORS[color_index])
            canvas.create_text(x_1 + TEXT_DX, y_1, text=f'{name} {y_1_text}', anchor=tkinter.SW, fill=COLORS[color_index])
            canvas.create_text(x_2 + TEXT_DX, y_2, text=f'{name} {y_2_text}', anchor=tkinter.SW,
                               fill=COLORS[color_index])

        if color_index < len(COLORS) - 1:
            color_index += 1
        else:
            color_index = 0




# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
