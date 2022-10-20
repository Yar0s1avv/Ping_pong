from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updater(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.x < 630:
            self.rect.y += self.speed
    def updatel(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_W] and self.rect.x > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_S} and self.rect.x < 630:
            self.rect.y += self.speed


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PING PONG")

background = transform.scale(image.load("images.jfif"), (win_width, win_height))

clock = pygame.time.Clock()

FPS = 30
game = True
while game:
    for event in event.get():
        if event.type == QUIT:
            game = False
    window.blit()

    clock.tick(40)
    display.update()