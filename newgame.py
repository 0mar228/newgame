from pygame import*
from random import randint

class Game_sprite():
    def __init__(self, img, w, h, x, y):
        self.image = transform.scale(img, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        screen.blit(self.image, self.rect)

class Dino(Game_sprite):
    def __init__(self):
        super().__init__(image.load('dino.png'),145 , 110, 100, 345)
        self.costumes =[image.load('dino.png'), image.load('dino 2.png'), image.load('dino 3.png'), image.load('dino 4.png'), image.load('dino 5.png'), image.load('dino 6.png')]
        for i in range(len(self.costumes)):
            self.costumes[i] = transform.scale(self.costumes[i], (145, 110))
        self.costume = 0
        self.isJump = False
        self.jumpCount = -21

    def update(self):
        self.costume += 1
        if self.costume > 29:
            self.costume = 0
        self.image = self.costumes[self.costume//5]
        if self.isJump:
            self.rect.y += self.jumpCount
            self.jumpCount += 1
            if self.jumpCount > 21:
                self.jumpCount = -21
                self.isJump = False

        super().update()

class Cactus(Game_sprite):
    def __init__(self): 
        super().__init__(image.load('cactus.png'),60 , 115, 900, 340)
    
    def update(self):
        global score, scoretext
        if self.rect.x <= -60:
            self.rect.x = 960
            score += 10
            scoretext = f.render(str(score), 1, (0, 0, 0))
        self.rect.x -= 10
        super().update()

screen = display.set_mode((900, 600))
display.set_caption('DINOSAWR')
background = transform.scale(image.load('fonk.jpg'), (900,600))
dino = Dino()
cactus = Cactus()

button_play = transform.scale(image.load('play.png'), (250, 250))
button_quit = transform.scale(image.load('exit.png'), (250, 250))

clock = time.Clock()
game = True
menu = True
finish = True


score = 0
font.init()
f = font.Font(None, 36)
scoretext = f.render(str(score), 1, (0, 0, 0))

highscore = 0
with open('highscore.txt', 'r') as file:
    highscore = int(file.read())

hightext = f.render('Points: ' + str(highscore), 1, (0, 0, 0))



while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                dino.isJump = True
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                x, y = mouse.get_pos()
                if menu:
                    if x > 350 and x < 600 and y > 100 and y < 350:
                        menu = False
                        finish = False
                        if menu == True:
                            highscore = 0
                    if x > 350 and x < 600 and y > 300 and y < 550:
                        game = False

    screen.blit(background, (0,0))
    if menu:
        screen.blit(button_play, (350, 100))    
        screen.blit(button_quit, (350, 300))
    elif not (finish):
        if dino.rect.colliderect(cactus.rect):
            finish = True
            menu = True
            dino = Dino()
            cactus = Cactus()

        dino.update()
        cactus.update()
        screen.blit(scoretext, (10, 10))
    display.update()


with open('highscore.txt', 'w') as file:
    file.write(str(highscore))  