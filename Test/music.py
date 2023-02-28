# Imports required modules
import pygame
from pygame import mixer
from time import sleep

# Initialise mixer
pygame.init()
mixer.init()

# Placeholders
muteButton = "placeholder, make one please"

# Defines checkifmuteOn, which constantly checks if mute is ON. Activates when mute is OFF.
def checkifmuteOn():
    while mixer.music.get_busy() is True:
        sleep(0.1)
        if muteButton == "pressed":
            mixer.music.stop()
            checkifmuteOff()

# Defines playmusic, which plays the music.
def playmusic():
    mixer.music.load("test/Xtrullor_and_Zoftle - Gold.mp3")
    mixer.music.play(loops = -1)
    mixer.music.set_volume(0.15)
    checkifmuteOn()

# Defines checkifmuteOff, which constantly checks if mute is OFF. Activates when mute is ON.
def checkifmuteOff():
    while mixer.music.get_busy() is False:
        sleep(0.1)
        if muteButton == "not active/off":
            playmusic()

# Starts playing the music
playmusic()