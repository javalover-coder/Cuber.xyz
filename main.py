import sys, time, random
from functions import *
import pygame as pg
#initialization
pg.init()
win = pg.display.set_mode((500,500))
pg.display.set_caption("Cuber.xyz")
win_msg = 'You Win :)'
lose_msg = "You Lose :("
f = pg.font.SysFont(None,48)
win_rect = win.get_rect()

cubeSize = 20
#rgb colors
yellow = (255,255,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
randomColor = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
bigColor = (0,100,200)
food = [random.randrange(1,500),random.randrange(1,500),10,10]
Bfood = [random.randrange(1,500),random.randrange(1,500),10,10]
cube = {
	'X': 250,
	'Y': 250,
	'speed': 5,
	'size' : 20
}
cube_rect = pg.Rect(cube['X'],cube['Y'],cube['size'],cube['size'])
food_rect = pg.Rect(food[0],food[1],food[2],food[3])
Bfood_rect = pg.Rect(Bfood[0],Bfood[1],Bfood[2],Bfood[3])
run = True
while run:
	pg.time.delay(10)
	win.fill(white)
	pg.draw.rect(win,bigColor,cube_rect)
	pg.draw.rect(win,randomColor,food_rect)
	pg.draw.rect(win,yellow,Bfood_rect)
	food_status = True
	Bfood_statue = True
	cube,run = check_keypress(cube,run)
	collision_status = check_collisions(cube_rect,food_rect, Bfood_rect)
	cube_status = check_cube_size(cube)
	if cube_status == -1:
		msg_image = f.render(lose_msg, False,red)
		msg_rect = msg_image.get_rect()
		msg_rect.center = win_rect.center
		win.blit(msg_image, msg_rect)
		run = False
	if cube_status == 0:
		bigColor =(0,100,200) 
	if cube_status == 1:
		bigColor = (240,240,100)
	if cube_status == 2:
		msg_image = f.render(win_msg, False,green)
		msg_rect = msg_image.get_rect()
		msg_rect.center = win_rect.center
		win.blit(msg_image, msg_rect)
		run = False
	if collision_status != -1:
		if collision_status == 1:
			randomColor = (random.randrange(1,255),random.randrange(1,255),random.randrange(1,255))
			food = [random.randrange(1,500),random.randrange(1,500),10,10]
			cube['size'] += 10
		if collision_status == 0:
			Bfood = [random.randrange(1,500),random.randrange(1,500),10,10]
			cube['size'] -= 10


	cube_rect = pg.Rect(cube['X'],cube['Y'],cube['size'],cube['size'])
	food_rect = pg.Rect(food[0],food[1],food[2],food[3])
	Bfood_rect = pg.Rect(Bfood[0],Bfood[1],Bfood[2],Bfood[3])
	pg.display.flip()
	
