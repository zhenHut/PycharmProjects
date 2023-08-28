import pygame


class Items(pygame.sprite.Sprite):
    def destroy(self, spieler1_item, spieler2_item, item_rect, ball):
        # kollision mit ball
        if item_rect.colliderect(ball):
            if ball.ball_markierung == 1:
                spieler1_item += 1
                self.kill()
                print(spieler1_item)
            if ball.ball_markierung == 2:
                spieler2_item += 1
                self.kill()


class Shrimp(Items):
    def __init__(self):
        super().__init__()
        self.item_x = 500
        self.item_y = 300
        self.item_image = pygame.image.load('Shrimp.png').convert_alpha()

        # größe skalieren
        self.item_image = pygame.transform.scale(self.item_image, (50, 20))
        self.item_rect = self.item_image.get_rect(center=[self.item_x, self.item_y])

    def item_draw(self, screen, x, y):
        item_image = pygame.transform.scale(self.item_image, (50, 20))
        item_rect = item_image.get_rect(center=[x, y])
        screen.blit(item_image, item_rect)

    def get_item_x(self):
        return self.item_x

    def set_item_x(self, item_x):
        self.item_x = item_x

    def get_item_y(self):
        return self.item_y

    def set_item_y(self, item_y):
        self.item_y = item_y

    def get_item_rect(self):
        return self.item_rect

    def set_item_rect(self, item_rect):
        self.item_rect = item_rect

# (center=[self.item_x, self.item_y])


# Item anzeige
def item_display(x, y, screen, farbe):
    item_display ="Items"
    font = pygame.font.SysFont(None, 70)
    text = font.render(item_display, True, farbe.rot)
    screeni = screen.blit(text, [x, y])
