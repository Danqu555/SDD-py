import pygame
from pygame import mixer
from time import sleep

# Initialise mixer
pygame.init()
mixer.init()

################# TODO #####################################################################
muteButton = "make one please"

def playmusic():
    mixer.music.load("Xtrullor_and_Zoftle - Gold.mp3")
    mixer.music.play(loops = -1)

playmusic()

while mixer.music.get_busy() is True:
    sleep(0.1)
    #################################################### TODO #####################
    if muteButton == "pressed":
        mute = True
        mixer.music.stop()
        
#### TODO For KEVIN ####
# ADD SOUND EFFECT LIKE SPLASH AND EXPLOSIOn



