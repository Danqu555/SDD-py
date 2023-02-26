import pygame
from pygame import mixer
from time import sleep

# Initialise mixer
pygame.init()
mixer.init()

################# TODO #####################################################################
muteButton = "placeholder, make one please"
battleship = "placeholder, also make one please"

def checkmuteOff():
    while mixer.music.get_busy() is True:
        sleep(0.1)
        if battleship == "hit":
            mixer.Sound.play("explosion.mp3")
            sleep(2)
        if battleship == "miss":
            mixer.Sound.play("splash.wav")
            sleep(2)
            
        #################################################### TODO BELOW #####################
        if muteButton == "pressed":
            mixer.music.stop()
            checkmuteOn()

def playmusic():
    mixer.music.load("Xtrullor_and_Zoftle - Gold.mp3")
    mixer.music.play(loops = -1)
    mixer.music.set_volume(0.15)
    checkmuteOff()

def checkmuteOn():
    while mixer.music.get_busy() is False:
        sleep(0.1)
        ### TODO ###
        if muteButton == "not active/off":
            playmusic()

playmusic()

#### TODO For KEVIN ####
# ADD SOUND EFFECT LIKE SPLASH AND EXPLOSIOn
