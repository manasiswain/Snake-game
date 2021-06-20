import time
import random
import pygame
from pygame.locals import *
SIZE=38
class Apple:
    def __init__(self,screen):
        self.screen = screen
        self.apl=pygame.image.load("resources/apple.png").convert()
        self.x=SIZE*2
        self.y=SIZE*2
    def draw(self):
        self.screen.blit(self.apl,(self.x,self.y))
        pygame.display.flip()
    def move(self):
        self.screen.fill((0, 0, 0))
        self.x=random.randint(0,532)
        self.y=random.randint(0,532)
class Snake:
    def __init__(self,screen,length):
        self.screen=screen
        self.length=length
        self.block=pygame.image.load("resources/box.png").convert()
        self.x=[SIZE]*length
        self.y=[SIZE]*length
        self.direction="right"
    def increaselength(self):
        self.length+=1
        self.x.append(0)
        self.y.append(0)
    def draw(self):
        self.screen.fill((0,0,0))
        for i in range(self.length):
            self.screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
    def move_up(self):
        self.direction="up"
    def move_down(self):
        self.direction="down"
    def move_left(self):
        self.direction="left"
    def move_right(self):
        self.direction="right"
    def move(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i] = self.y[i - 1]
        if(self.direction=="up"):
            self.y[0]-= SIZE
        elif (self.direction == "down"):
            self.y[0]+= SIZE
        if (self.direction == "left"):
            self.x[0]-= SIZE
        if (self.direction == "right"):
            self.x[0]+=SIZE
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface=pygame.display.set_mode((570,570))
        self.snake=Snake(self.surface,1)
        self.apple=Apple(self.surface)
        self.snake.draw()
        self.apple.draw()
        self.s1 = pygame.mixer.Sound("resources/arcade-game-simple-background-music.mp3")
        pygame.mixer.Sound.play(self.s1)
    def collision(self,x1,y1,x2,y2):
        if(x1>=x2 and x1<=x2+SIZE):
            if (y1 >= y2 and y1 <= y2 + SIZE):
                return(True)
        return(False)
    def go(self):
        self.surface.fill((255,0,0))
        font = pygame.font.Font(None, 30)
        gover1 = font.render(f"GAME OVER!Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(gover1,(150, 285))
        gover2= font.render("To play again press Enter to Exit press Escape!",True,(255,255,255))
        self.surface.blit(gover2,(80,310))
        pygame.display.flip()
    def disp_score(self):
        font=pygame.font.Font(None,30)
        score=font.render(f"Score:{self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(480,550))
    def run(self):

        running = True
        pause=False
        while running:
            for event in pygame.event.get():
                if (event.type == KEYDOWN):
                    if(pause==False):
                        if (event.key == K_UP):
                            self.snake.move_up()
                        elif (event.key == K_DOWN):
                            self.snake.move_down()
                        elif (event.key == K_RIGHT):
                            self.snake.move_right()
                        elif (event.key == K_LEFT):
                            self.snake.move_left()
                        elif (event.key == K_ESCAPE):
                            self.s1.stop()
                            running = False
                    else:
                        if (event.key == K_ESCAPE):
                            self.s1.stop()
                            exit(0)
                        if(event.key==K_RETURN):
                            pause=False
                            self.s1 = pygame.mixer.Sound("resources/arcade-game-simple-background-music.mp3")
                            pygame.mixer.Sound.play(self.s1)
                            self.snake = Snake(self.surface, 1)
                            self.apple = Apple(self.surface)
                            self.snake.draw()
                            self.apple.draw()

                if (event.type == QUIT):
                    running = False
            try:
                if(pause==False):
                    self.snake.move()
                    self.apple.draw()
                    self.disp_score()
                    pygame.display.flip()
                    if (self.snake.x[0]==570):
                        self.s1.stop()
                        print("yo")
                        sound = pygame.mixer.Sound("resources/game-lose-sound.mp3")
                        pygame.mixer.Sound.play(sound)
                        raise ('game over')
                    if (self.snake.y[0]==570):
                        self.s1.stop()
                        sound = pygame.mixer.Sound("resources/game-lose-sound.mp3")
                        pygame.mixer.Sound.play(sound)
                        raise ('game over')
                    if (self.snake.x[0]==0):
                        self.s1.stop()
                        sound = pygame.mixer.Sound("resources/game-lose-sound.mp3")
                        pygame.mixer.Sound.play(sound)
                        raise ('game over')
                    if (self.snake.y[0] == 0):
                        self.s1.stop()
                        sound = pygame.mixer.Sound("resources/game-lose-sound.mp3")
                        pygame.mixer.Sound.play(sound)
                        raise ('game over')
                    if(self.collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y)):
                        sound=pygame.mixer.Sound("resources/Ding-sound-effect.mp3")
                        pygame.mixer.Sound.play(sound)
                        self.apple.move()
                        self.snake.increaselength()
                    for i in range(3,self.snake.length):
                        if (self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i])):
                            self.s1.stop()
                            sound = pygame.mixer.Sound("resources/game-lose-sound.mp3")
                            pygame.mixer.Sound.play(sound)
                            raise('game over')
            except Exception as e:
                self.go()
                pause=True

            time.sleep(0.2)


if __name__=="__main__":
    game=Game()
    game.run()



