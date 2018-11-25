def addBorder(window, borders='╚╝╔╗═║'):
    """
    addBorder - adds a border around a given window

    arguments:
         window -- stdscr object
         borders -- string containing border values in the form:
            ''.join([
                bottomLeftCorner,
                bottomRightCorner,
                topLeftCorner,
                topRightCorner,
                leftRightSides,
                topBottomSides
            ])
    """
    height, width = window.getmaxyx()
    for y in range(height - 1):
        for x in range(width - 1):
            if y == height - 2 and x == 0:
                # bottom left corner
                window.addstr(y, x, borders[0])
            elif y == height - 2 and x == width - 2:
                # bottom right corner
                window.addstr(y, x, borders[1])
            elif y == 0 and x == 0:
                # top left corner
                window.addstr(y, x, borders[2])
            elif y == 0 and x == width - 2:
                # top right corner
                window.addstr(y, x, borders[3])
            elif y == 0 or y == height - 2:
                # left right sides
                window.addstr(y, x, borders[4])
            elif x == 0 or x == width - 2:
                # top bottom sides
                window.addstr(y, x, borders[5])
