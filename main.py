import sys
import pyautogui
import logging
import time
from os import listdir
from os.path import isfile, join
import os
import glob

log_dir = 'logs/'
num_files = sum(1 for entry in listdir(log_dir) if isfile(join(log_dir,entry)))

# remove logs after 10 logs
if num_files > 10:
    files = glob.glob(log_dir)
    for f in files:
        os.remove(f)

day = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday) + '-' + str(time.localtime().tm_hour) + '-' + str(time.localtime().tm_min) + '-' + str(time.localtime().tm_sec)

logging.basicConfig(filename="logs/%s.log"%day, format='%(asctime)s %(message)s', filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

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
            world_map = win.connect_window.lobby_window.game_map
            client = win.connect_window.client
        elif win.map_generator_window:
            world_map = win.map_generator_window.lobby_window.game_map
            client = win.map_generator_window.lobby_window.client
            server_thread = win.map_generator_window.server_thread
    except AttributeError as e:
        print(e)
        exit(1)

    if client and client.started:
        window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, world_map, client, '--debug' in sys.argv, server_thread)
        window.run()
