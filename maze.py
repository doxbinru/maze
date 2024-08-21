from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0 :
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635 :
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435 :
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x < 470:
            self.direction = 'right'
        if self.rect.x > 620:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1,color_2,color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.image = Surface((wall_width, wall_height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        walls.add(self)
    def draw(self):
        window.blit(self.image, self.rect)

window = display.set_mode((700,500))
display.set_caption('Maze')
background = transform. scale(image. load('background.jpg'), (700,500))
clock = time.Clock()

mixer. init()
mixer. music.load('Sonic Mine - Drugs.mp3')
mixer. music.play()
mixer.music.set_volume(0.1)

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial', 70)
win = font.render('you win', True, (0,255,0))
lose = font.render('you lose', True, (0,255,0))

player = Player('hero.png',5,420, 4)
monster = Enemy('pngwing.com (1).png',620,280, 2)
final = GameSprite('treasure.png',580, 420, 0)
walls = sprite.Group()
w1 = Wall(150,200,100,100,20,450,10)





game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game =False
    if not finish:
        window.blit(background, (0,0))
        player.reset()
        player.update()
        monster.reset()
        monster.update()
        final.reset()
        walls.draw(window)
        if sprite.collide_rect(player,final):
            window.blit(win, (200,200))
            money.play()
            finish = True
        if sprite.spritecollide(player, walls, False) or sprite.collide_rect(player, monster):
            window.blit(lose, (200,200))
            kick.play()
            finish = True

    display.update()
    clock.tick(60)


