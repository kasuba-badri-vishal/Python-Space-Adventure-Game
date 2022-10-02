
class Enemy3:
    def __init__(self, xpos, ypos, imagepath1, imagepath2, imagepath3, imagepath4):

        self.xpos = xpos
        self.ypos = ypos
        self.isalive = True
        self.life = 100

        self.surface1 = pygame.image.load(imagepath1).convert_alpha()
        self.surface2 = pygame.image.load(imagepath2).convert_alpha()
        self.surface3 = pygame.image.load(imagepath3).convert_alpha()
        self.surface4 = pygame.image.load(imagepath4).convert_alpha()
        self.presentsurface = self.surface1

        self.font = pygame.font.Font('fonts/alba/ALBAS___.TTF', 50)
        print(self.surface1.get_width())
        print(self.surface1.get_height())

        self.centerx = self.xpos + self.presentsurface.get_width()/2
        self.centery = self.ypos - self.presentsurface.get_height()/2



    def move(self, direction):

        if direction =='d':
            if self.ypos < 950:
                self.ypos += .1
                self.centery = self.ypos - self.presentsurface.get_height()/2
            else:
                self.isalive = False
        elif direction == 'u':

            if self.ypos > 0:
                self.ypos -= .1
                self.centery = self.ypos - self.presentsurface.get_height()/2

        elif direction =='r':
            if self.xpos + self.presentsurface.get_width() < 1080:
                self.xpos += .1
                self.centerx = self.xpos + self.presentsurface.get_width()/2

        elif direction == 'l':
            if self.xpos > 0:
                self.xpos -= .1
                self.centerx = self.xpos + self.presentsurface.get_width()/2


    def display(self, screen):

        life_val = str(self.life)
        lineinfo = self.font.render(life_val, False, (255, 255, 255))

        if self.life >= 75:
            self.presentsurface = self.surface1
        elif self.life >= 50:
            self.presentsurface = self.surface1
        elif self.life >= 25:
            self.presentsurface = self.surface1
        else:
            self.presentsurface = self.surface1

        screen.blit(self.presentsurface, (self.xpos, self.ypos))
        CANVAS.blit(lineinfo, (self.xpos, self.ypos))

