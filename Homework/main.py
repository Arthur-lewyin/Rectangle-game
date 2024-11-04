import pygame

screen=pygame.display.set_mode((800,800))

black = (0,0,0)
white = (255,255,255)
red= (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen.fill("pink")

class Ball():
    def __init__(self,color,center,radius):
        self.s= screen
        self.color = color
        self.center = center
        self.radius = radius

    def drawCircle(self):
        pygame.draw.circle(self.s,self.color,self.center,self.radius)

c1= Ball(black,(400,400),100)
c2= Ball(white,(200,200),50)
c3= Ball(green,(600,600),25)

c1.drawCircle()
c2.drawCircle()
c3.drawCircle()
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()