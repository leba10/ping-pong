from pygame import*



class Gamesprite(sprite.sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, weight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (weight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Gamesprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed



back = (photo)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)



game = True
finish = False
clock = time.clock()
FPS = 60



racket1 = Player('raket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 50)


font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 180))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 180))


speed_x = 3
speed_y = 3


while game:
    for e in event.get():
        if e.type == QUIT:
            