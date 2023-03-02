# Imports required modules
import pygame
from pygame import mixer
from time import sleep

# Initialise mixer
pygame.init()
mixer.init()

mute = "off"

# Defines changevar, which changes the value of mute.
def changeVar():
    if mute == "off":
        mute = "on" and 1
    if mute == "on" and not 1:
        mute = "off"
    if mute == "on" and 1:
        mute = "on"

# Defines checkifmuteOn, which constantly checks if mute is ON. Activates when mute is OFF.
def checkifmuteOn():
    while mixer.music.get_busy() is True:
        sleep(0.1)
        if mute == "on":
            mixer.music.stop()
            checkifmuteOff()

# Defines playmusic, which plays the music and activates checkifmuteOn.
def playmusic():
    mixer.music.load("test/Xtrullor_and_Zoftle - Gold.mp3")
    mixer.music.play(loops = -1)
    mixer.music.set_volume(0.15)
    checkifmuteOn()

# Defines checkifmuteOff, which constantly checks if mute is OFF. Activates when mute is ON.
def checkifmuteOff():
    while mixer.music.get_busy() is False:
        sleep(0.1)
        if mute == "off":
            playmusic()

# Starts playing the music
playmusic()