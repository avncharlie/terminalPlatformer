import time

import terminalDraw
import terminalConstants


class level:
    """
    level - represents a level

    handles scrolling, visible parts of level and editing level
    """

    def __init__(self, rawLevel):
        self.raw = rawLevel
        self.level = self.raw.splitlines()
        self.index = [0, 77]
        self._setVisible()
        self.maxIndex = len(self.level[0])

    def _setVisible(self):
        """ setVisible - sets visible part of level """
        self.visibleLevel = [line[self.index[0]: self.index[1]]
                             for line in self.level]
        self.visibleLevelRaw = '\n'.join(self.visibleLevel)

    def scroll(self, scrollRight=True):
        """ scroll - scrolls one column to the left or right"""
        if scrollRight:
            if not self.index[1] == self.maxIndex:
                self.index = [self.index[0] + 1, self.index[1] + 1]
        else:
            if not self.index[0] == 0:
                self.index = [self.index[0] - 1, self.index[1] - 1]
        self._setVisible()


def gameLoop(gameWindow, level):
    """
    gameLoop - runs the main game loop. this works as a normal game loop. first
    user input is handled, then all the game objects are updated, then it is
    rendered. the game loop uses values from the terminalConstants library,
    namely the GAME_FPS value.

    arguments:
         gameWindow -- stdscr object
    """
    secondsPerFrame = 1/terminalConstants.GAME_FPS
    while True:
        # process input

        # if c == ord('w'):
        # if c == ord('s'):

        c = gameWindow.getch()
        if c == ord('a'):
            level.scroll(scrollRight=False)
        if c == ord('d'):
            level.scroll(scrollRight=True)
        elif c == ord('q'):
            break

        # update
        #   advance game simulation one step

        # render
        #   draw game
        terminalDraw.drawLevel(gameWindow, level)
        gameWindow.refresh()

        time.sleep(secondsPerFrame)
