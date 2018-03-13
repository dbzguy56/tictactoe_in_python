'''
draw.py
for drawing teh shapes for tic tac toe
'''
import pygame, sys
from pygame.locals import *
import random

RED = pygame.Color(255,0,0)
BLUE = pygame.Color(0,0,255)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
GREEN = pygame.Color(0,255,0)
YELLOW = pygame.Color(255,255,0)

def menu(WIDTH, HEIGHT, windowSurfaceObj):
	'''
	displays the menu options
	'''
	bgSurfaceObj = pygame.image.load("content//bg.jpg")	
	bgSurfaceObj = pygame.transform.scale(bgSurfaceObj,(WIDTH,HEIGHT))
	
	windowSurfaceObj.blit(bgSurfaceObj,(0,0))
	
	pygame.draw.rect(windowSurfaceObj,RED,(int(WIDTH/4),int(HEIGHT/3),int(WIDTH/2),int(HEIGHT/5)),0) #(x,y,width,height) of rectangle
	pygame.draw.rect(windowSurfaceObj,RED,(int(WIDTH/4),int((2*HEIGHT)/3),int(WIDTH/2),int(HEIGHT/5)),0) #(x,y,width,height) of rectangle
	# pygame.draw.rect(windowSurfaceObj,GREEN,(8*int(WIDTH)/9,5*int(HEIGHT)/8,int(WIDTH)/16, int(HEIGHT)/4),0)
	
	msg = 'Play 2P'
	msg2 = 'Play vs CPU'
	msg3 = 'UP'
	msg4 = 'DOWN'
	message(msg,(WIDTH/2),(HEIGHT/2)-25, windowSurfaceObj, 64,BLACK)
	message(msg2,(WIDTH/2),((3*HEIGHT)/4), windowSurfaceObj, 64,BLACK)
	# message(msg3,8*int(WIDTH)/9,5*int(HEIGHT)/8, windowSurfaceObj, 32,WHITE)
	# message(msg4,8*int(WIDTH)/9,6*int(HEIGHT)/8+25, windowSurfaceObj, 16,WHITE)
	
	pygame.mixer.music.load('content//Rainy_Nights,Rainy_Days.mp3')
	pygame.mixer.music.play(-1, 0.0)
	volume = pygame.mixer.music.set_volume(1)
	print(pygame.mixer.music.get_volume())
	
	return volume

def clear(h,w,windowSurfaceObj):
	'''
	clears the board and makes a new grid with a new pic
	'''
	num = random.randint(1,9)
	# if num == 1:
		# image = 'a1d.jpg'
	# elif num == 2:
		# image = 'a2d.jpg'
	# elif num == 3:
		# image = 'a3d.jpg'
	# elif num == 4:
		# image = 'a4d.jpg'
	# elif num == 5:
		# image = 'a5d.jpg'
	# elif num == 6:
		# image = 'a6d.jpg'
	# elif num == 7:
		# image = 'a7d.jpg'
	# elif num == 8:
		# image = 'a8d.jpg'
	# elif num == 9:
	
	image = "content//a9d.jpg"
		
	bgSurfaceObj = pygame.image.load(image)
	bgSurfaceObj = pygame.transform.scale(bgSurfaceObj,(w,h))
	windowSurfaceObj.blit(bgSurfaceObj,(0,0))
	grid(h, w,windowSurfaceObj)
	grid_array = [['' for x in range(3)] for x in range(3)]
	val = 1
	winner = 0
	turns = 0
	
	return grid_array, val, winner, turns

def grid(h, w, windowSurfaceObj):
	'''
	draws the grid of tic tac toe
	h,w - height and width of the window
	'''	
	unit_h = int(h/3)  #for each square its corresponding height and width
	unit_w = int(w/3)
	pygame.draw.line(windowSurfaceObj, BLACK, (unit_w,0) ,(unit_w,h), 5)
	pygame.draw.line(windowSurfaceObj, BLACK, (2*unit_w,0) ,(2*unit_w,h), 5)
	pygame.draw.line(windowSurfaceObj, BLACK, (0, unit_h) ,(w, unit_h), 5)
	pygame.draw.line(windowSurfaceObj, BLACK, (0, 2*unit_h) ,(w,2*unit_h), 5)

	return
	
def update_grid(unit_h, unit_w, mouse_pos, grid_array, windowSurfaceObj, val, turns):
	'''
	updates the grid array by using the mouse position or if it is grid_array[row][col]==3 then that is where the ai has placed its shape
	'''
	draw_shape = False
	if (grid_array[0][0]=='' and mouse_pos[0]  <= unit_w and mouse_pos[1] <= unit_h) or grid_array[0][0]== 3 : #row 1 col 1
		grid_array[0][0] = val
		coord = (10,10)
		draw_shape = True
	elif (grid_array[0][1]=='' and unit_w <= mouse_pos[0] < (2*unit_w) and mouse_pos[1] <= unit_h) or grid_array[0][1]== 3:#row 1 col 2
		grid_array[0][1] = val
		coord = (unit_w + 10,10)
		draw_shape = True
	elif (grid_array[0][2]=='' and (2*unit_w) < mouse_pos[0] and mouse_pos[1] <= unit_h) or grid_array[0][2]== 3 : #row 1 col 3
		grid_array[0][2] = val
		coord = ((2*unit_w) + 10,10)
		draw_shape = True
	elif (grid_array[1][0]=='' and mouse_pos[0] <= (unit_w) and unit_h < mouse_pos[1] <= (2*unit_h)) or grid_array[1][0]== 3: #row 2 col 1
		grid_array[1][0] = val
		coord = (10, unit_h + 10)
		draw_shape = True
	elif (grid_array[1][1]=='' and unit_w <= mouse_pos[0] < (2*unit_w) and unit_h < mouse_pos[1] <= (2*unit_h)) or grid_array[1][1]== 3: #row 2 col 2
		grid_array[1][1] = val
		coord = (unit_w + 10, unit_h + 10)
		draw_shape = True
	elif (grid_array[1][2]=='' and mouse_pos[0] >= (2*unit_w) and unit_h < mouse_pos[1] < (2*unit_h)) or grid_array[1][2]== 3: #row 2 col 3
		grid_array[1][2] = val
		coord = ((2*unit_w) + 10, unit_h + 10)
		draw_shape = True
	elif (grid_array[2][0]=='' and mouse_pos[0] < (unit_w) and mouse_pos[1] >= (2*unit_h)) or grid_array[2][0]== 3: #row 3 col 1
		grid_array[2][0] = val
		coord = (10, (2*unit_h) + 10)
		draw_shape = True
	elif (grid_array[2][1]=='' and unit_w < mouse_pos[0] < (2*unit_w) and mouse_pos[1] >= (2*unit_h)) or grid_array[2][1]== 3: #row 3 col 2
		grid_array[2][1] = val
		coord = (unit_w + 10, (2*unit_h) + 10)
		draw_shape = True
	elif (grid_array[2][2]=='' and mouse_pos[0] > (2*unit_w) and mouse_pos[1] >= (2*unit_h)) or grid_array[2][2]== 3: #row 3 col 3
		grid_array[2][2] = val
		coord = ((2 * unit_w)+ 10, (2*unit_h) + 10)
		draw_shape = True
	if draw_shape:
		shape(coord, unit_h, unit_w, windowSurfaceObj, val)
		if val == 1:
			val = 2
		else:
			val = 1
		turns+=1
	
	return grid_array, val, turns
	
def  shape(coord, unit_h, unit_w, windowSurfaceObj, val):
	'''
	draws teh shape
	val - is either 1 or 2 representing cross or circle
	coord is the top left coordinates of the shape
	'''
	if val == 1:
		p2 = ((coord[0] + unit_w)-20, (coord[1] + unit_h)-20 )
		p3 = ( coord[0] , (coord[1] + unit_h)-20 )
		p4 = ((coord[0] + unit_w)-20 , coord[1])
		pygame.draw.line(windowSurfaceObj, BLUE, (coord[0],coord[1]) , p2, 10)
		pygame.draw.line(windowSurfaceObj, BLUE, p3, p4, 10)
	elif val == 2:
		p1 = (coord[0] + int(unit_w/2))  - 20
		p2 = (coord[1] + int(unit_h/2)) - 10
		pygame.draw.circle(windowSurfaceObj, RED, (p1,p2), int(unit_h/2)-20, 10)
				
	return
	
	
def check(grid_array,val, turns):
	'''
	checks for a winner
	'''
	winner = 0
	
	if val == 1:
		val = 2
	elif val ==2:
		val = 1
	if grid_array[0][0]	 == val:
		if grid_array[0][1]==val and grid_array[0][2]==val: #1st row
			winner = val
		elif grid_array[1][0]==val and grid_array[2][0]==val: # 1st col
			winner=val
		elif grid_array[1][1]==val and grid_array[2][2]==val: #top left to bot right
			winner=val
	if grid_array[0][1] == val and grid_array[1][1]==val and grid_array[2][1]==val:#2nd row
		winner=val
	if grid_array[0][2] == val:
		if grid_array[1][1] ==val and grid_array[2][0]==val: #bot left to top right
			winner=val
		elif grid_array[1][2]==val and grid_array[2][2]==val: #3rd row
			winner=val
	if grid_array[1][0]==val and grid_array[1][1]==val and grid_array[1][2]==val:# col 2
		winner=val
	if grid_array[2][0]==val and grid_array[2][1]==val and grid_array[2][2]==val: # col 3
		winner=val
	print(turns)
	if turns == 9 and winner == 0:
		winner = 3
	return winner

def message(msg,w, h, windowSurfaceObj, font_size, color):
	'''
	prints the message onto the surface
	'''
	fontObj = pygame.font.SysFont('content//PressStart2P.ttf',font_size,True)
	msgSurfaceObj = fontObj.render(msg, False, color)
	msgRectObj = msgSurfaceObj.get_rect()
	if msg == 'UP' or msg == 'DOWN':
		msgRectObj.topleft = (w,h)
	else:
		msgRectObj.center = (w,h)
	windowSurfaceObj.blit(msgSurfaceObj,msgRectObj)
	
	return

def win_msg(winner, windowSurfaceObj, WIDTH,HEIGHT, p1_wins, p2_wins, ties, play):
	if winner == 3:
		msg = "Players Tied!"
	else:
		if play == 2:
			msg = "Player {} wins!".format(winner)
		if play ==1:
			if winner ==2:
				msg = "CPU wins!"
			elif winner ==1:
				msg = "Player 1 wins!"

	pygame.draw.rect(windowSurfaceObj,YELLOW,(int(WIDTH/8),int(HEIGHT/8),(WIDTH - (2*int(WIDTH/8))),(HEIGHT - (2*int(HEIGHT/8)))),0)#(x,y,width,height) of rectangle
	
	if play == 2:
		msg2 = "P1 wins: {}  P2 wins: {} Ties: {}".format(p1_wins,p2_wins, ties)
	elif play == 1:
		msg2 = "P1 wins: {}  CPU wins: {} Ties: {}".format(p1_wins,p2_wins, ties)
	msg3 = "Press Space to play again! :D"
	msg4 = "Press Escape to go back to the Menu"
	
	message(msg,(WIDTH/2),((HEIGHT/2)-50),windowSurfaceObj,64, BLACK)
	message(msg2,(WIDTH/2),(HEIGHT/2),windowSurfaceObj,32,BLACK)
	message(msg3,(WIDTH/2),(HEIGHT/2)+50,windowSurfaceObj,32,BLACK)
	message(msg4,(WIDTH/2), (HEIGHT/2)+100 ,windowSurfaceObj,  32, BLACK)
	
	
	return p1_wins, p2_wins, ties

def ai(ai, grid_array, unit_h, unit_w, mouse_pos, windowSurfaceObj, val, turns):
	'''
	is the artificial intelligence where:
	ai = 1 is where it randomly places its shape
	'''
	if (ai == 1 and turns!=9) or turns == 2:
		loop = True
		while loop : #keeps looping until it finds an empty space
			row_rnd = random.randint(0,2)
			col_rnd  = random.randint(0,2)
			if grid_array[col_rnd][row_rnd] == '':
				loop = False
				grid_array[col_rnd][row_rnd] = 3
				
		grid_array, val, turns = update_grid(unit_h,unit_w,mouse_pos,grid_array,windowSurfaceObj,val,turns)
		grid_array[col_rnd][row_rnd] = 2
		
	elif ai == 2 and turns!=9:
		col, row = line_check(grid_array, val)
		grid_array[col][row] = 3			
		grid_array, val, turns = update_grid(unit_h,unit_w,mouse_pos,grid_array,windowSurfaceObj,val,turns)
		grid_array[col][row] = 2
		print("ai: {} turns {}".format(ai, turns))
	elif ai == 3 and turns !=9:
		col, row = line_check(grid_array, 1)
		if col is None and row is None:
			loop = True
			while loop : #keeps looping until it finds an empty space
				row = random.randint(0,2)
				col  = random.randint(0,2)
				if grid_array[col][row] == '':
					loop = False	

		grid_array[col][row] = 3
		grid_array, val, turns = update_grid(unit_h,unit_w,mouse_pos,grid_array,windowSurfaceObj,val,turns)
		grid_array[col][row] = 2
		
	return grid_array, val, turns

def line_check(grid_array,val):
	'''
	looks for values to in a row then returns the row and col for the third place to make a line
	'''
	not_found = True
	col = None
	row = None
	
	# for col in range(3): i thought i could do it a different way but it was a bit too diffucult for me at the time
		# for row in range(3):
			
			# if grid_array[col][row] == val:
				# if row == 0 or row == 2:
					# row_check = 1#check below or above
				# elif row == 1:
					# row_check = 3 #check both above and below
				
				# if col == 0 or col == 2: 
					# col_check = 1#check to the right or left
				# elif col == 1:
					# col_check =3 #check both left and right
				
				# if grid_array[col_check][row_check] == val:
	
	if grid_array[0][0]	 == val:
		if grid_array[0][1]==val and grid_array[0][2]== '': #1st col
			col = 0
			row = 2
			not_found = False
		elif grid_array[1][0]==val and grid_array[2][0]== '': # 1st row
			col = 2
			row = 0
			not_found = False
		elif grid_array[1][1]==val and grid_array[2][2]== '': #top left to bot right
			col = 2
			row = 2
			not_found = False
	elif grid_array[0][1] == val and grid_array[1][1]==val and grid_array[2][1]== '':#2nd row
		col = 2
		row = 1 
		not_found = False
	elif grid_array[0][2] == val:
		if grid_array[1][1] ==val and grid_array[2][0]== '': #bot left to top right
			col = 2 
			row = 0
			not_found = False
		elif grid_array[1][2]==val and grid_array[2][2]== '': #3rd row
			col = 2 
			row = 2 
			not_found = False
	elif grid_array[1][0]==val and grid_array[1][1]==val and grid_array[1][2]== '':# col 2
		col = 1 
		row = 2 
		not_found = False
	elif grid_array[2][0]==val and grid_array[2][1]==val and grid_array[2][2]== '': # col 3
		col = 2 
		row = 2 
		not_found = False
	elif grid_array[1][2]==val and grid_array[1][1]==val and grid_array[1][2]== '': 
		col = 1 
		row = 2 
		not_found = False
	elif grid_array[0][2]==val and grid_array[0][1]==val and grid_array[0][0]== '': 
		col = 0 
		row = 0 
		not_found = False
	elif grid_array[2][2]==val and grid_array[2][1]==val and grid_array[2][0]== '': 
		col = 2
		row = 0 
		not_found = False
	elif grid_array[2][2]==val and grid_array[1][1]==val and grid_array[0][0]== '': 
		col = 0
		row = 0 
		not_found = False
	elif grid_array[2][2]==val and grid_array[2][1]==val and grid_array[2][0]== '': 
		col = 2
		row = 0 
		not_found = False
	elif grid_array[2][0]==val and grid_array[1][1]==val and grid_array[0][2]== '': 
		col = 0
		row = 2 
		not_found = False
	elif grid_array[2][0]==val and grid_array[1][0]==val and grid_array[0][0]== '': 
		col = 0
		row = 0 
		not_found = False
	elif grid_array[2][1]==val and grid_array[1][1]==val and grid_array[0][1]== '': 
		col = 0
		row = 1
		not_found = False
	elif grid_array[2][2]==val and grid_array[1][2]==val and grid_array[0][2]== '': 
		col = 0
		row = 2 
		not_found = False

	
	if not_found and val == 2:
		col, row = _place_turn(grid_array,val)
				
	return col, row
	
def _place_turn(grid_array,val):
	'''
	if there is a circle on the grid then tries to place another a circle adjacent to it if there is a spot available otherwise a random spot
	'''
	not_found = True
	if grid_array[0][0] == val:
		if grid_array[1][1] == '':
			col = 1
			row = 1
			not_found = False
		elif grid_array[1][0]=='':
			col = 1 
			row = 0
			not_found = False
		elif grid_array[0][1] =='':
			col = 0 
			row = 1
			not_found = False
	elif grid_array[1][0] == val:
		if grid_array[0][0] == '':
			col = 0
			row = 0
			not_found = False
		elif grid_array[1][1] == '':
			col = 1
			row = 1
			not_found = False
		elif grid_array[2][0] == '':
			col = 2
			row = 0			
			not_found = False
	elif grid_array[2][0] == val:
		if grid_array[1][1] == '':
			col = 1
			row = 1			
			not_found = False
		elif grid_array[1][0] == '':
			col = 1
			row = 0			
			not_found = False
		elif grid_array[2][1] == '':
			col = 2
			row = 1
			not_found = False
	elif grid_array[0][1] == val:
		if grid_array[1][1] == '':
			col = 1
			row = 1			
			not_found = False
		elif grid_array[0][0] == '':
			col = 0
			row = 0			
			not_found = False
		elif grid_array[0][2] == '':
			col = 0
			row = 2
			not_found = False
	elif grid_array[1][1] == val: #middle box
		if grid_array[2][0] == '':
			col = 2
			row = 0			
			not_found = False
		elif grid_array[1][0] == '':
			col = 1
			row = 0			
			not_found = False
		elif grid_array[0][0] == '':
			col = 0
			row = 0			
			not_found = False
		elif grid_array[0][1] == '':
			col = 0
			row = 1			
			not_found = False
		elif grid_array[2][1] == '':
			col = 2
			row = 1
			not_found = False
		elif grid_array[0][2] == '':
			col = 0
			row = 2			
			not_found = False
		elif grid_array[1][2] == '':
			col = 1
			row = 2			
			not_found = False
		elif grid_array[2][2] == '':
			col = 2
			row = 2
			not_found = False
	elif grid_array[2][1] == val:
		if grid_array[2][0] == '':
			col = 2
			row = 0			
			not_found = False
		elif grid_array[1][1] == '':
			col = 1
			row = 1
			not_found = False
		elif grid_array[2][2] == '':
			col = 2
			row = 2
			not_found = False
	elif grid_array[0][2] == val:
		if grid_array[1][1] == '':
			col = 1
			row = 1
			not_found = False
		elif grid_array[0][1] == '':
			col = 0
			row = 1			
			not_found = False
		elif grid_array[1][2] == '':
			col = 1
			row = 2			
			not_found = False
	elif grid_array[1][2] == val:
		if grid_array[1][1] == '':
			col = 1
			row = 1			
			not_found = False
		elif grid_array[0][2] == '':
			col = 0
			row = 2			
			not_found = False
		elif grid_array[2][2] == '':
			col = 2
			row = 2
			not_found = False
	elif grid_array[2][2] == val:
		if grid_array[1][1] == '':
			col = 1
			row = 1
			not_found = False
		elif grid_array[1][2] == '':
			col = 1
			row = 2			
			not_found = False
		elif grid_array[2][1] == '':
			col = 2
			row = 1			
			not_found = False
	
	if not_found:
		loop = True
		while loop : #keeps looping until it finds an empty space
			row = random.randint(0,2)
			col  = random.randint(0,2)
			if grid_array[col][row] == '':
				loop = False

	return col, row