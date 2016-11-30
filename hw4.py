# Name: Mackenzie Francisco
# uniqname: mackfran
# Section Day/Time: Thursday/1-2PM
# References:
	## http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound
	## 

from pygame import *
from pygame.sprite import *
from random import *

DELAY = 1000;
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

# adds a title
pygame.display.set_caption("Gilmore Girls")

clock = pygame.time.Clock()

# sets image positions
background_position = [0,0]

# loads images
background_image = pygame.image.load("gilmore-girls.bmp").convert()

f = font.Font("RobotoSlab-Regular.ttf", 25)

coffee = Coffee()
mug = Mug()
sprites = RenderPlain(coffee, mug)

hits = 0
time.set_timer(USEREVENT + 1, DELAY)

pygame.mixer.music.load("gilmoresong.wav")
pygame.mixer.music.play(loops=-1)

gameExit = False
while not gameExit:
	screen.blit(background_image, background_position)

	for event in pygame.event.get():
		if event.type == QUIT:
			gameExit = True
		elif event.type == MOUSEBUTTONDOWN:
			if mug.hit(coffee):
				coffee.move()
				hits += 1
				time.set_timer(USEREVENT + 1, DELAY)
		elif event.type == USEREVENT + 1:
			coffee.move()

	# copy background image to screen
	screen.blit(background_image, background_position)
	text = f.render("Score = " + str(hits), False, (0,0,0))
	screen.blit(text, (5, 0))

	sprites.update()
	sprites.draw(screen)
	display.update()

#pygame.mixer.music.stop()
pygame.quit()
quit() # exits python
