import sys, time, random
import pygame as pg

def check_keypress(cube,run):
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
	keys = pg.key.get_pressed()
	if keys[pg.K_RIGHT]:
		if cube['X'] >= 480:
			cube['X'] = 480
		else:
			cube['X'] += cube['speed']
	if keys[pg.K_LEFT]:
		if cube['X'] <= 0:
			cube['X'] = 0
		else:
			cube['X'] -= cube['speed']
	if keys[pg.K_UP]:
		if cube['Y'] <= 0:
			cube['Y'] = 0
		else:
			cube['Y'] -= cube['speed']
	if keys[pg.K_DOWN]:
		if cube['Y'] >= 480:
			cube['Y'] = 480
		else:
			cube['Y'] += cube['speed']
	if keys[pg.K_q]:
		run = False
	return cube, run
def check_collisions(collider,food, Bfood):
	if pg.Rect.colliderect(collider,food):
		return 1
	elif pg.Rect.colliderect(collider,Bfood):
		return 0
	else:
		return -1
def check_cube_size(cube):
	
	if cube['size'] <= 0:
		return -1
	elif cube['size'] >= 50 and cube['size'] <=100:
		return 1
	elif cube['size'] >=100:
		return 2
	else: 
		return 0
