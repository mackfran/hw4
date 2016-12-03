# Name: Mackenzie Francisco
# uniqname: mackfran
# Section Day/Time: Thursday/1-2PM
# References: GSIs, Colleen Feola, Angel Tsai
	## http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound
	## http://programarcadegames.com/python_examples/f.php?file=timer.py
	## http://stackoverflow.com/questions/23982907/python-library-pygame-centering-text
	## http://programarcadegames.com/python_examples/show_file.php?file=moving_sprites.py
	## http://thepythongamebook.com/en:pygame:step014

# imports necessary modules
from pygame import *
from pygame.sprite import *
from random import *

# seeds a timer to move sprites
DELAY = 1000;

class Coffee(Sprite):
	def __init__(self):
		# calls the Sprite constructor
		Sprite.__init__(self)
		# loads an image to represent the object
		self.image = image.load("coffee.bmp").convert_alpha()
		# updates the position of the object
		self.rect = self.image.get_rect()

	# moves coffee beans to a random location
	def move(self):
		randX = randint(0, 750)
		randY = randint(0, 550)
		self.rect.center = (randX,randY)

class Kitten(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("kitten.bmp").convert_alpha()
		self.rect = self.image.get_rect()

	# moves kitten to a random location
	def move(self):
		randX = randint(0, 750)
		randY = randint(0, 550)
		self.rect.center = (randX, randY)

class Mug(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = image.load("mug.bmp").convert_alpha()
		self.rect = self.image.get_rect()

	# checks if mug collided with coffee or kitten
	def hit(self, target):
		return self.rect.colliderect(target)

	# makes the mug sprite move with the cursor
	def update(self):
		self.rect.center = mouse.get_pos()

# main
init()

# creates a surface
screen = pygame.display.set_mode((800,600)) # initializes with a tuple
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# adds a title
pygame.display.set_caption("Gilmore Girls")

# sets background image position
background_position = [0,0]

# loads background image
background_image = pygame.image.load("gilmore-girls.bmp").convert()

# hides the cursor so we only see the mug
mouse.set_visible(False)

# creates two fonts of different sizes
f1 = font.Font("RobotoSlab-Regular.ttf", 25)
f2 = font.Font("RobotoSlab-Regular.ttf", 120)

# creates coffees, kittens, and a mug using the constructors
coffee1 = Coffee()
coffee2 = Coffee()
kitten1 = Kitten()
kitten2 = Kitten()
kitten3 = Kitten()
kitten4 = Kitten()
kitten5 = Kitten()
mug = Mug()

# creates sprite groups so similar objects can be updated at once
coffee_list = pygame.sprite.Group()
kitten_list = pygame.sprite.Group()
coffee_sprites = RenderPlain(coffee1, coffee2)
kitten_sprites = RenderPlain(kitten1, kitten2, kitten3, kitten4, kitten5)
mug_sprite = RenderPlain(mug)
hits = 3

# initializes timer
time.set_timer(USEREVENT + 1, DELAY)

# creates a Clock object and initializes a countdown
clock = pygame.time.Clock()
frame_count = 0
frame_rate = 25
start_time = 30

# loads music and plays it on repeat
pygame.mixer.music.load("gilmoresong.wav")
pygame.mixer.music.play(loops=-1)
# loads sound effects
clink = pygame.mixer.Sound("clink.wav")
meow = pygame.mixer.Sound("meow.wav")

gameExit = False
# loops until user quits
while not gameExit:
	# draws background to the screen
	screen.blit(background_image, background_position)

	# checks if the player is doing something
	for event in pygame.event.get():
		# if the player clicks close, exits the game loop
		if event.type == QUIT:
			gameExit = True
		# if the player moves the mouse, starts detecting collisions and moving objects
		elif event.type == MOUSEMOTION:
			# if mug collides with the coffee1 object, the following happens:
			if mug.hit(coffee1):
				# plays corresponding sound effect
				clink.play(loops=0, maxtime=0)
				# moves the coffee to a random location
				coffee1.move()
				# adds one to the player's score
				hits += 1
				# resets the timer
				time.set_timer(USEREVENT + 0, DELAY)
			if mug.hit(coffee2):
				clink.play(loops=0, maxtime=0)
				coffee2.move()
				hits += 1
				time.set_timer(USEREVENT + 0, DELAY)
			# if mug collides with the kitten1 object, the following happens:
			if mug.hit(kitten1):
				# plays corresponding sound effect
				meow.play(loops=0, maxtime=0)
				# moves the kitten to a random location
				kitten1.move()
				# subtracts one from the player's score
				hits -= 1
				# resets the timer
				time.set_timer(USEREVENT + 0, DELAY)				
			if mug.hit(kitten2):
				meow.play(loops=0, maxtime=0)
				kitten2.move()
				hits -= 1
				time.set_timer(USEREVENT + 0, DELAY)				
			if mug.hit(kitten3):
				meow.play(loops=0, maxtime=0)
				kitten3.move()
				hits -= 1
				time.set_timer(USEREVENT + 0, DELAY)				
			if mug.hit(kitten4):
				meow.play(loops=0, maxtime=0)
				kitten4.move()
				hits -= 1
				time.set_timer(USEREVENT + 0, DELAY)			
			if mug.hit(kitten5):
				meow.play(loops=0, maxtime=0)
				kitten5.move()
				hits -= 1
				time.set_timer(USEREVENT + 0, DELAY)
		# moves the objects when time has passed
		elif event.type == USEREVENT + 1:
			coffee1.move()
			coffee2.move()
			kitten1.move()
			kitten2.move()
			kitten3.move()
			kitten4.move()
			kitten5.move()

	# copy background image to screen
	screen.blit(background_image, background_position)
	score_text = f1.render("Score = " + str(hits), False, (0,0,0))
	screen.blit(score_text, (5, 0))

	# calculates total seconds
	total_sec = start_time - (frame_count // frame_rate)
	
	# when time runs out, the following happens:
	if total_sec < 0:
		# prevents time from going into the negatives
		total_sec = 0
		# draws "GAME OVER" text to the middle of the screen
		game_over_text = f2.render("GAME OVER", False, (255,0,0))
		text_rect = game_over_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
		screen.blit(game_over_text, text_rect)
		# makes objects disappear
		coffee1.kill()
		coffee2.kill()
		kitten1.kill()
		kitten2.kill()
		kitten3.kill()
		kitten4.kill()
		kitten5.kill()
		# movement of the cursor stops making collisions/updating the score
		pygame.event.set_blocked(pygame.MOUSEMOTION)

	# calculates total minutes and seconds
	minutes = total_sec // 60
	seconds = total_sec % 60
	# formats countdown
	countdown = "Time remaining: {0:02}:{1:02}".format(minutes, seconds)
	# draws countdown text to the screen
	countdown_text = f1.render(countdown, True, (0,0,0))
	screen.blit(countdown_text, (300,0))
	# increments and limits frames per second
	frame_count += 1
	clock.tick(frame_rate)

	# updates and redraws sprites
	coffee_sprites.update()
	coffee_sprites.draw(screen)
	kitten_sprites.update()
	kitten_sprites.draw(screen)
	mug_sprite.update()
	mug_sprite.draw(screen)
	display.update()

pygame.mixer.music.stop() # stops the music
pygame.quit() # exits pygame
quit() # exits python
