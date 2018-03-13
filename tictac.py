''' Tic Tac Toe
Jan 15, 2015
'''
import pygame, sys
from pygame.locals import *
import draw

HEIGHT,WIDTH = 480,640
RED = pygame.Color(255,0,0)
GREEN = pygame.Color(0,255,0)
BLUE = pygame.Color(0,0,255)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
YELLOW = pygame.Color(255,255,0)
ORANGE = pygame.Color(255,100,0)

pygame.init()
fpsClock = pygame.time.Clock()

unit_h = int(HEIGHT/3)
unit_w = int(WIDTH/3)

windowSurfaceObj = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("content//a2d.jpg")	
pygame.display.set_icon(icon)

play = 0
menu_screen = True
select  = False
idle = True
idle2 = True
mute = False
p1_wins, p2_wins, ties =0,0,0


grid_array, val, winner, turns = draw.clear(HEIGHT,WIDTH,windowSurfaceObj)

while True:
	
	if menu_screen and idle:
		volume = draw.menu(WIDTH,HEIGHT,windowSurfaceObj)
		idle = False
	elif menu_screen == False and select == False and idle2:
		pygame.mixer.music.load('content//Smoothie_Samba.mp3')
		pygame.mixer.music.play(-1, 0.0)
		idle2 = False
		
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit() 
		elif event.type == MOUSEBUTTONDOWN:
			
			mouse_pos = pygame.mouse.get_pos() #gets mouse position
			if menu_screen ==False and play == 2:#2 player

				print(mouse_pos)
				grid_array, val, turns = draw.update_grid(unit_h, unit_w, mouse_pos, grid_array,windowSurfaceObj, val, turns) #draws the shape according to the turn
				print(grid_array)
				winner=draw.check(grid_array,val, turns)		#checks the weiner
				if winner!=0: 					
					if winner == 1:
						p1_wins+=1
					elif winner == 2:
						p2_wins+=1
					elif winner == 3:
						ties += 1
					
					p1_wins, p2_wins, ties = draw.win_msg(winner, windowSurfaceObj, WIDTH,HEIGHT, p1_wins, p2_wins, ties, play)
					play = 0
			elif menu_screen ==False and play == 1:#for Ez mode against computer
				grid_array, val, turns = draw.update_grid(unit_h,unit_w,mouse_pos,grid_array,windowSurfaceObj,val,turns)
				
				winner = draw.check(grid_array, val, turns)
				if winner!=0: 					
					if winner == 1:
						p1_wins+=1
					elif winner == 2:
						p2_wins+=1
					elif winner == 3:
						ties += 1
					p1_wins, p2_wins, ties = draw.win_msg(winner, windowSurfaceObj, WIDTH,HEIGHT, p1_wins, p2_wins, ties, play)
					play = 3
				
				if val == 2 and play == 1:
					grid_array, val, turns = draw.ai(ai, grid_array, unit_h, unit_w, mouse_pos, windowSurfaceObj, val, turns)
					winner = draw.check(grid_array, val, turns)
					if winner!=0: 					
						if winner == 1:
							p1_wins+=1
						elif winner == 2:
							p2_wins+=1
						elif winner == 3:
							ties += 1
						p1_wins, p2_wins, ties = draw.win_msg(winner, windowSurfaceObj, WIDTH,HEIGHT, p1_wins, p2_wins, ties, play)
						play = 3

					
			elif menu_screen:#if you are the menu screen
				if int(WIDTH/4) <= mouse_pos[0] <=(int(WIDTH/4)+int(WIDTH/2)) and int(HEIGHT/3) <= mouse_pos[1] <= (int(HEIGHT/3) + int(HEIGHT/5)): #if u wanna play 2 player
					grid_array, val, winner, turns = draw.clear(HEIGHT,WIDTH,windowSurfaceObj)
					menu_screen = False
					play = 2
				elif int(WIDTH/4) <= mouse_pos[0] <= (int(WIDTH/4) + int(WIDTH/2)) and int((2*HEIGHT)/3) <= mouse_pos[1] <= (int((2*HEIGHT)/3) + int(HEIGHT/5)) and select == False:#if u wanna play one player it brings up another window for u to select ur difficulty
					select = True
					pygame.draw.rect(windowSurfaceObj,YELLOW,(int(WIDTH/8),int(HEIGHT/8),(WIDTH - (2*int(WIDTH/8))),(HEIGHT - (2*int(HEIGHT/8)))),0)#(x,y,width,height) of rectangle
					pygame.draw.rect(windowSurfaceObj,GREEN,(int(WIDTH/4),int(HEIGHT/4),(int(WIDTH/2)),(int(HEIGHT/8))),0)#(x,y,width,height) of rectangle
					pygame.draw.rect(windowSurfaceObj,ORANGE,(int(WIDTH/4),2*int(HEIGHT/4)-12,(int(WIDTH/2)),(int(HEIGHT/8))),0)#(x,y,width,height) of rectangle
					pygame.draw.rect(windowSurfaceObj,RED,(int(WIDTH/4),3*int(HEIGHT/4)-25,(int(WIDTH/2)),(int(HEIGHT/8))),0)#(x,y,width,height) of rectangle
					
					menu_screen = False
					msg = 'Select a difficulty'
					msg2 = 'EZ MODE'
					msg3 = 'Meh'
					msg4 = 'INSANE'
					
					draw.message(msg,(WIDTH/2),((3*HEIGHT)/16),windowSurfaceObj, 32,BLACK)
					draw.message(msg2,(WIDTH/2),int(HEIGHT/3),windowSurfaceObj, 64,BLACK)
					draw.message(msg3,(WIDTH/2),2*int(HEIGHT/4)+25,windowSurfaceObj, 64, BLACK)
					draw.message(msg4,(WIDTH/2),3*int(HEIGHT/4),windowSurfaceObj, 64, BLACK)
				# elif 8*int(WIDTH)/9 <= mouse_pos[0] <= (8*int(WIDTH)/9+int(WIDTH)/16) and 5*int(HEIGHT)/8 <= mouse_pos[1] <= (5*int(HEIGHT)/8 + int(HEIGHT)/8):
					# volume = volume + 0.1
					# pygame.mixer.set_volume(volume)
					# print(pygame.mixer.music.get_volume())
				# elif 8*int(WIDTH)/9 <= mouse_pos[0] <= (8*int(WIDTH)/9+int(WIDTH)/16) and (5*int(HEIGHT)/8+int(HEIGHT)/16) <= mouse_pos[1] <= (5*int(HEIGHT)/8 + int(HEIGHT)/8):
					# if volume != 0:
						# volume = volume - 0.1
						# pygame.mixer.set_volume(volume)
					# print(pygame.mixer.music.get_volume())
			elif select and int(WIDTH/4) <= mouse_pos[0] <= (int(WIDTH/4) + int(WIDTH/2)) and int(HEIGHT/4) <= mouse_pos[1] <= (int(HEIGHT/4) + (int(HEIGHT/8))): #if u click ez mode

				grid_array, val, winner, turns = draw.clear(HEIGHT,WIDTH,windowSurfaceObj)
				select = False
				menu_screen = False
				play = 1
				ai=1

			elif select and int(WIDTH/4) <= mouse_pos[0] <= (int(WIDTH/4) + int(WIDTH/2)) and 2*int(HEIGHT/4)-12 <= mouse_pos[1] <= (2*int(HEIGHT/4)-12 + (int(HEIGHT/8))): #if u click ez mode

				grid_array, val, winner, turns = draw.clear(HEIGHT,WIDTH,windowSurfaceObj)
				select = False
				menu_screen = False
				play = 1
				ai=2
				
			elif select and int(WIDTH/4) <= mouse_pos[0] <= (int(WIDTH/4) + int(WIDTH/2)) and 3*int(HEIGHT/4)-25 <= mouse_pos[1] <= (3*int(HEIGHT/4)-25 + (int(HEIGHT/8))): #if u click ez mode

				grid_array, val, winner, turns = draw.clear(HEIGHT,WIDTH,windowSurfaceObj)
				select = False
				menu_screen = False
				play = 1
				ai= 3	
					
		elif event.type == KEYDOWN:
			if event.key == K_SPACE and menu_screen == False and select == False: #if u press space it resets the grid
				grid_array, val, winner, turns = draw.clear(HEIGHT,WIDTH,windowSurfaceObj)
				if play == 0:
					play = 2
				elif play == 3:
					play = 1
			elif event.key == K_ESCAPE:
				if menu_screen:#quits if u press escape when ur at the menu
					pygame.quit()
					sys.exit() 
				else: #brings u back to the menu if u press escape
					play = 0
					p1_wins, p2_wins, ties =0,0,0
					menu_screen = True
					idle = True
					idle2 = True
					select = False
			elif event.key == K_m:
				if mute:
					pygame.mixer.music.unpause()
					mute = False
				else:
					pygame.mixer.music.pause()
					mute = True
		
	pygame.display.update()
	fpsClock.tick(30)
