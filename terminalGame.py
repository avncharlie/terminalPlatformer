import time

import terminalDraw
import terminalConstants


class level:
    """
    level - represents a level

    handles scrolling, visible parts of level and editing level
    """

    def __init__(self, rawLevel):
        # all level processing is through self.level
        self.level = rawLevel.splitlines()

        # holds index bounds of visible part of level
        self.visibleIndexes = {
            'leftRightIndex': [0, 77],
            'topBottomIndex': [len(self.level) - 21, len(self.level)]
        }

        # using self.visibleIndexes, calculate visible parts of level
        # and store in self.visibleLevel and self.visibleLevelRaw
        self._setVisible()

        # maximum bounds whole level
        self.maxRightIndex = len(self.level[0])
        self.maxBottomIndex = len(self.level)

    def _setVisible(self):
        """ _setVisible - sets visible part of level """
        # list comprehension to quickly grap visible level using indexes
        self.visibleLevel = [
            line[
                self.visibleIndexes['leftRightIndex'][0]:
                self.visibleIndexes['leftRightIndex'][1]
            ]
            for line in
            self.level[
                    self.visibleIndexes['topBottomIndex'][0]:
                    self.visibleIndexes['topBottomIndex'][1]
                ]
        ]
        # used for displaying level
        self.visibleLevelRaw = '\n'.join(self.visibleLevel)

    def scroll(self, scrollRight=True, scrollTop=None):
        """
        scroll - scrolls the visible area of the level, either left, right, up
        or down.

        arguments:
            scrollRight -- a boolean value indicating whether to scroll right.
            If set to false will scroll left. if scrolling top and bottom is
            required, set to None.
            scrollTop -- a boolean value indicating whether to scroll top.
            If set to false will scroll bottom. if scrolling left and right is
            required, set to None.
        """
        if scrollRight is not None:
            if scrollRight:
                # if level not scrolled to rightmost index already, scroll to
                # right
                if not self.visibleIndexes['leftRightIndex'][1] == \
                        self.maxRightIndex:
                    self.visibleIndexes['leftRightIndex'] = [
                        self.visibleIndexes['leftRightIndex'][0] + 1,
                        self.visibleIndexes['leftRightIndex'][1] + 1
                    ]
            else:
                # if level not scrolled to leftmost index already, scroll to
                # left
                if not self.visibleIndexes['leftRightIndex'][0] == 0:
                    self.visibleIndexes['leftRightIndex'] = [
                        self.visibleIndexes['leftRightIndex'][0] - 1,
                        self.visibleIndexes['leftRightIndex'][1] - 1
                    ]
        else:
            if scrollTop:
                # if level not scrolled to topmost index already, scroll to top
                if not self.visibleIndexes['topBottomIndex'][0] == 0:
                    self.visibleIndexes['topBottomIndex'] = [
                        self.visibleIndexes['topBottomIndex'][0] - 1,
                        self.visibleIndexes['topBottomIndex'][1] - 1
                    ]
            else:
                # if level not scrolled to topmost index already, scroll to
                # bottom
                if not self.visibleIndexes['topBottomIndex'][1] == \
                        self.maxBottomIndex:
                    self.visibleIndexes['topBottomIndex'] = [
                        self.visibleIndexes['topBottomIndex'][0] + 1,
                        self.visibleIndexes['topBottomIndex'][1] + 1
                    ]

        # set visible part of level using new indexes
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
    startTiming = secondsPerFrame
    frameCount = 0
    while True:
        # process input
        c = gameWindow.getch()
        if c == ord('w'):
            level.scroll(scrollRight=None, scrollTop=True)
        if c == ord('s'):
            level.scroll(scrollRight=None, scrollTop=False)
        if c == ord('a'):
            level.scroll(scrollRight=False)
        if c == ord('d'):
            level.scroll(scrollRight=True)
        if c == ord('p'):
            terminalConstants.GAME_SHOW_FPS = not terminalConstants.GAME_SHOW_FPS
        elif c == ord('q'):
            break
        # update
        #   advance game simulation one step
        # render
        #   draw game

        terminalDraw.drawLevel(gameWindow, level)

        # calculate and show FPS
        if terminalConstants.GAME_SHOW_FPS:
            if frameCount % terminalConstants.GAME_UPDATE_FPS_CHECK == 0:
                FPS = int(1 / (time.time() - startTiming))
            startTiming = time.time()

            terminalDraw.drawText(
                    gameWindow,
                    'fps: ' + str(FPS),
                    percentages=None,
                    startCoords=[
                        70,
                        1])

        gameWindow.refresh()

        frameCount = frameCount + 1

        time.sleep(secondsPerFrame)
