import sys
import pyautogui
import logging
import time
from os import listdir
from os.path import isfile, join
import os
import glob

log_dir = 'logs/'

day = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday) + '-' + str(time.localtime().tm_hour) + '-' + str(time.localtime().tm_min) + '-' + str(time.localtime().tm_sec)

logging.basicConfig(filename="logs/%s.log"%day, format='%(asctime)s %(levelname)s %(message)s', filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
for logger_name in logging.root.manager.loggerDict:
    print(logger_name)

from PyQt5.QtWidgets import QApplication

from game_screens import Game
from start_screens.welcome_window import WelcomeWindow

SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
SCREEN_WIDTH, SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.9), int(SCREEN_HEIGHT * 0.9)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WelcomeWindow()
    win.show()
    app.exec_()
    client = None
    world_map = None
    server_thread = None
    try:
        if win.connect_window:
            #TODO: limit looping and display what is going on to user
            while world_map is None:
                try:
                    world_map = win.connect_window.lobby_window.game_map
                except AttributeError as e:
                    logger.error(e)
                    time.sleep(1)
            client = win.connect_window.client
        elif win.map_generator_window:
            world_map = win.map_generator_window.lobby_window.game_map
            client = win.map_generator_window.lobby_window.client
            server_thread = win.map_generator_window.server_thread
    except AttributeError as e:
        logger.error(e)
        exit(1)

    if client and client.started:
        window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, world_map, client, '--debug' in sys.argv, server_thread)
        window.run()
