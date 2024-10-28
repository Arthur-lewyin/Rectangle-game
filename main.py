import pygame
pygame.init()

screen=pygame.display.set_mode((800,800))

black = (0,0,0)
white = (255,255,255)
red= (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen.fill("pink")

class Rectangle():
    def __init__(self,color,dimensions):
        self.rect_surface = screen
        self.rect_color = color
        self.rect_dimensions = dimensions
    
    def draw_rect(self):
        self.rect_draw = pygame.draw.rect(self.rect_surface,self.rect_color,self.rect_dimensions)

#create object
#x-position, y-pos, width, height
greenRect= Rectangle(green,(50,20,100,120))
greenRect.draw_rect()

purpleRect = Rectangle("purple", (700,20,200,30))
purpleRect.draw_rect()

blueRect = Rectangle(blue, (50,700,130,220))
blueRect.draw_rect()

orangeRect = Rectangle("orange",(700,700,10,10))
orangeRect.draw_rect()

redRect = Rectangle(red, (200,200,400,400))
redRect.draw_rect()

yellowRect = Rectangle("yellow",(200,400,600,12))
yellowRect.draw_rect()


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()