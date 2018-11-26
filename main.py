#!/usr/bin/env python3


import curses

import terminalWindowUtils
import terminalDraw
import terminalGame
import terminalConstants


RESOURCE_PATHS = {
    'txt_terminal': 'gameResources/txt_terminal',
    'level_1': 'gameResources/levels/lvl_1'
}


RESOURCES = {key: open(RESOURCE_PATHS[key]).read() for key in RESOURCE_PATHS}


def main(screen):
    # clear screen
    screen.clear()

    # set up game window
    gameWindow = curses.newwin(
        terminalConstants.GAME_WINDOW_HEIGHT,
        terminalConstants.GAME_WINDOW_WIDTH,
        int(curses.LINES / 2 - terminalConstants.GAME_WINDOW_HEIGHT / 2),
        int(curses.COLS / 2 - terminalConstants.GAME_WINDOW_WIDTH / 2)
    )

    # make getch non blocking
    gameWindow.nodelay(True)

    # add border
    terminalWindowUtils.addBorder(gameWindow)

    level_1 = terminalGame.level(RESOURCES['level_1'])
    terminalDraw.drawLevel(gameWindow, level_1)

    # game loop
    terminalGame.gameLoop(gameWindow, level_1)


curses.wrapper(main)
