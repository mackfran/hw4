# Name: Mackenzie Francisco
# uniqname: mackfran
# Section Day/Time: Thursday/1-2PM
# References:
	## http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound
	## http://programarcadegames.com/python_examples/f.php?file=timer.py
	## http://stackoverflow.com/questions/23982907/python-library-pygame-centering-text

from pygame import *
from pygame.sprite import *
from random import *

DELAY = 800;
bgcolor = (0,42,196)

class Coffee(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("coffee.bmp").convert_alpha()
		self.rect = self.image.get_rect()

	def move(self):
		randX = randint(0, 750)
		randY = randint(0, 550)
		self.rect.center = (randX,randY)

class Kitten(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("kitten.bmp").convert_alpha()
		self.rect = self.image.get_rect()

	def move(self):
		randX = randint(0, 750)
		randY = randint(0, 550)
		self.rect.center = (randX, randY)

class Mug(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("mug.bmp").convert_alpha()
		self.rect = self.image.get_rect()

	def hit(self, target):
		return self.rect.colliderect(target)

	def update(self):
		self.rect.center = mouse.get_pos()

init()

# creates a surface
screen = pygame.display.set_mode((800,600)) # initializes with a tuple
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# adds a title
pygame.display.set_caption("Gilmore Girls")

# sets image positions
background_position = [0,0]

# loads images
background_image = pygame.image.load("gilmore-girls.bmp").convert()

f1 = font.Font("RobotoSlab-Regular.ttf", 25)
f2 = font.Font("RobotoSlab-Regular.ttf", 120)

coffee1 = Coffee()
coffee2 = Coffee()
coffee3 = Coffee()
coffee4 = Coffee()
coffee5 = Coffee()
kitten = Kitten()
mug = Mug()

coffee_list = pygame.sprite.Group()
# for i in range(5):
# 	cof = Coffee(coffee_list)
# 	cof.add(coffee_list)

sprites = RenderPlain(kitten, mug)
coffee_sprites = RenderPlain(coffee1, coffee2, coffee3, coffee4, coffee5)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

clock = pygame.time.Clock()
frame_count = 0
frame_rate = 25
start_time = 30

pygame.mixer.music.load("gilmoresong.wav")
pygame.mixer.music.play(loops=-1)

gameExit = False
while not gameExit:
	screen.blit(background_image, background_position)

	for event in pygame.event.get():
		if event.type == QUIT:
			gameExit = True
		elif event.type == MOUSEMOTION:
			if mug.hit(coffee1):
				coffee1.move()
				hits += 1
				time.set_timer(USEREVENT + 1, DELAY)
			if mug.hit(coffee2):
				coffee2.move()
				hits += 1
				time.set_timer(USEREVENT + 1, DELAY)
			if mug.hit(coffee3):
				coffee3.move()
				hits += 1
				time.set_timer(USEREVENT + 1, DELAY)
			if mug.hit(coffee4):
				coffee4.move()
				hits += 1
				time.set_timer(USEREVENT + 1, DELAY)
			if mug.hit(coffee5):
				coffee5.move()
				hits += 1
				time.set_timer(USEREVENT + 1, DELAY)
			if mug.hit(kitten):
				kitten.move()
				hits -= 1
				time.set_timer(USEREVENT + 1, DELAY)
		elif event.type == USEREVENT + 1:
			coffee1.move()
			coffee2.move()
			coffee3.move()
			coffee4.move()
			coffee5.move()
			kitten.move()

	# copy background image to screen
	screen.blit(background_image, background_position)
	score_text = f1.render("Score = " + str(hits), False, (0,0,0))
	screen.blit(score_text, (5, 0))

	total_sec = start_time - (frame_count // frame_rate)
	if total_sec < 0:
		total_sec = 0
		game_over_text = f2.render("GAME OVER", False, (255,0,0))
		text_rect = game_over_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
		screen.blit(game_over_text, text_rect)

	minutes = total_sec // 60
	seconds = total_sec % 60
	countdown = "Time remaining: {0:02}:{1:02}".format(minutes, seconds)
	countdown_text = f1.render(countdown, True, (0,0,0))
	screen.blit(countdown_text, (300,0))
	frame_count += 1
	clock.tick(frame_rate)
	
	coffee_sprites.update()
	coffee_sprites.draw(screen)
	sprites.update()
	sprites.draw(screen)
	display.update()

pygame.mixer.music.stop()
pygame.quit()
quit() # exits python
