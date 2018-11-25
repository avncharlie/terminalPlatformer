def drawText(window, text, percentages):
    """
    drawText - given a single or multiline string, draw it in the given window
    at percentage positions provided. percentage positions = percentage distance
    from top and left.

    arguments:
         window -- stdscr object
         text -- single / multiline string to be drawn
         percentages -- list in form [yPercentage, xPercentage]
    """
    textLength = len(text.splitlines()[0])
    textHeight = len(text.splitlines())
    windowHeight, windowWidth = window.getmaxyx()

    startCoords = [int((windowWidth - textLength) * percentages[0]),
                   int((windowHeight - textHeight) * percentages[1])]

    for yIndex, s in enumerate(text.splitlines(), startCoords[1]):
        window.addstr(yIndex, startCoords[0], s)
