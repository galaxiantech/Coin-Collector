import pygame, sys, math, random


pygame.init()

#vars
FPS = 30 #refresh rate
fps_clock = pygame.time.Clock()
x = 250
y = 100
a = False
s = False
w = False
d = False
x2 = 60
y2 = 60
dist = math.sqrt((x-x2)**2 + (y-y2)**2)

#set up window
screen = pygame.display.set_mode((1000, 700))#Width 1000px #Height 700px
pygame.display.set_caption('Distance Game')

#add colors here
BLACK = (0, 0, 0)
SKY = (0, 204, 255)
GREEN = (11, 102, 35)
WHITE = (255, 255, 255)
LIGHTGRAY = (211,211,211)

#game defs
def buddy():
	character = pygame.image.load('buddy.png')
	screen.blit(character, (x, y))
def coins(tup):
	coin = pygame.image.load('coin.png')
	screen.blit(coin, tup)
def randomnumber():
	x = random.randint(60, 940)
	y = random.randint(60, 640)
	return (x, y)
def distance(point1, point2):
    # Your code here...
    x = pow(point2[0] - point1[0], 2)
    y = pow(point2[1] - point1[1], 2)
    number = x + y
    result = math.sqrt(number)
    return result
	





#Modify number of coins (max is 899)
points = []
for i in range(25):
	randomlocation = randomnumber()
	points.append(randomlocation)
	

#game loop
while True:
	keystate = pygame.key.get_pressed()
	if keystate[pygame.K_d]:
		x = x+3
	if keystate[pygame.K_a]:
		x = x-3
	if keystate[pygame.K_w]:
		y = y-3
	if keystate[pygame.K_s]:
		y = y+3
	#sets the background color to black
	screen.fill(LIGHTGRAY)
	#pygame.draw.rect(screen, BLACK, (200, 0, 5, 700))
	#pygame.draw.rect(screen, BLACK, (400, 0, 5, 700))
	#pygame.draw.rect(screen, BLACK, (600, 0, 6, 700))
	#pygame.draw.rect(screen, BLACK, (800, 0, 5, 700))  
	
	#draw stuff here
	buddy()
	stufftodelete = []
	
	for i in range(len(points)):
		d = distance((x, y), points[i])
		if d > 60:
			coins(points[i])
		else:
			stufftodelete.append(i)
	for i in range(len(stufftodelete)):
		points.pop(stufftodelete[i])
	print(distance((x, y), (x2, y2)))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	
	
	pygame.display.update()
	fps_clock.tick(FPS)
