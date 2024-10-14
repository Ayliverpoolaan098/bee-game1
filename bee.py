import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 500

score = 0 
game_over = False

bee = Actor("bee")
bee.pos = 100, 100

flower = Actor("flower")
flower.pos = 200,200

def draw():
    screen.blit("backround",(0,0))
    flower.draw()
    bee.draw()
pgzrun.go()