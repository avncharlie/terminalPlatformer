#!/usr/bin/env python3


import curses
import terminalWindowUtils
import terminalDraw

GAME_WINDOW_HEIGHT = 24
GAME_WINDOW_WIDTH = 80

RESOURCE_PATHS = {
    'txt_terminal': 'gameResources/txt_terminal'
}


RESOURCES = {key: open(RESOURCE_PATHS[key]).read() for key in RESOURCE_PATHS}


def main(screen):
    screen.clear()

    gameWindow = curses.newwin(
        GAME_WINDOW_HEIGHT,
        GAME_WINDOW_WIDTH,
        int(curses.LINES / 2 - GAME_WINDOW_HEIGHT / 2),
        int(curses.COLS / 2 - GAME_WINDOW_WIDTH / 2)
    )

    terminalWindowUtils.addBorder(gameWindow)
    terminalDraw.drawText(gameWindow, RESOURCES['txt_terminal'], [0.50, 0.20])

    gameWindow.refresh()
    gameWindow.getkey()


curses.wrapper(main)
