def drawText(window, text, percentages=[.5, .5], startCoords=[1, 1]):
    """
    drawText - given a single or multiline string, draw it in the given window
    at percentage positions or coordinates provided. whatever method of
    positioning choosed, the other parameter must be set to None.  percentage
    positions = percentage distance from top and left. coordinates = coordinates
    distance from top and left.

    arguments:
         window -- stdscr object
         text -- single / multiline string to be drawn
         percentages -- list in form [yPercentage, xPercentage]
         startCoords -- list in form [startXcoord, startYcoord]
    """
    if percentages is not None:
        textLength = len(text.splitlines()[0])
        textHeight = len(text.splitlines())
        windowHeight, windowWidth = window.getmaxyx()

        startCoords = [int((windowWidth - textLength) * percentages[0]),
                       int((windowHeight - textHeight) * percentages[1])]

    for yIndex, s in enumerate(text.splitlines(), startCoords[1]):
        window.addstr(yIndex, startCoords[0], s)


def drawLevel(window, level):
    drawText(window, level.visibleLevelRaw, None, [1, 1])
