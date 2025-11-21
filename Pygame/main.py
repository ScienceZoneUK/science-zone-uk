import random
import pygame
import math

import background

colours = {
    "cave": (0, 0, 0),
    "walls": (30, 30, 30),
    "player": (255, 255, 255),
}

tail_colours = [(200, 200, 0), (255, 0, 0), (255, 165, 0)]

DISPLAY_SIZE = [1000, 700]
PLAYER_SIZE = [50, 50]
PLAYER_RECT = [
    round(DISPLAY_SIZE[0]/2 - PLAYER_SIZE[0]/2),
    round(DISPLAY_SIZE[1]/2 - PLAYER_SIZE[1]/2),
    PLAYER_SIZE[0], PLAYER_SIZE[1]]
PLATFORM_HEIGHT = 20
GRAVITY = -0.01


class Player:
    def __init__(self, rect, colour):
        self.rect = pygame.Rect(rect)
        self.vector = [0, 0]
        self.angle = .5  # in pi radians. ie: 2 = 2pi radians. 0 radians is down, increasing anticlockwise.
        self.speed = 10  # hypo of triangle, where x and y for movement are found via trig with self.angle
        self.colour = colour
        self.tail = []
        self.tail_decay = 1

    def update(self, objects):
        delta_x = self.speed*math.sin(self.angle * math.pi)
        delta_y = self.speed*math.cos(self.angle * math.pi)

        self.move(0, 0, [])
        self.update_tail(-delta_x, -delta_y)
        return [delta_x, delta_y]
    
    def move(self, dx, dy, objects):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0, objects)
        if dy != 0:
            self.move_single_axis(0, dy, objects)

        self.apply_gravity()

    def apply_gravity(self):
        self.move_clockwise()

    def move_clockwise(self, amount=-0.01):
        self.move_angle(amount)
        self.rollover_angle()

    def move_anticlockwise(self,  amount=0.02):
        self.move_angle(amount)
        self.rollover_angle()

    def move_angle(self, amount):
        self.angle += amount

    def rollover_angle(self):
        # This ensures the angle stays between 0 and 2pi. Rollover should be un-noticeable if changes are kept small.
        if self.angle <= 0:
            self.angle = 2
        elif self.angle >= 2:
            self.angle = 0

    def move_single_axis(self, dx, dy, objects):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in objects:
            if self.rect.colliderect(wall.rect):
                if dx > 0:  # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0:  # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0:  # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0:  # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

    def update_tail(self, dx, dy):
        for rect in self.tail:

            rect.move_ip(dx, dy)
            rect.inflate_ip(-self.tail_decay, -self.tail_decay)
            if rect.width <= self.tail_decay or rect.height <= self.tail_decay:
                self.tail.remove(rect)

        self.tail.append(self.rect.copy())

    def draw(self, display):
        pygame.draw.ellipse(display, self.colour, self.rect)

        for rect in self.tail:
            tailcolour = random.choice(tail_colours)
            pygame.draw.ellipse(display, tailcolour, rect)


class Coin:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.colour = (200, 200, 0)

    def move(self, movement):
        self.rect = self.rect.move(movement)

    def check_collide(self, player):
        if self.rect.colliderect(player.rect):
            return True
        return False

    def draw(self, display):
        pygame.draw.circle(display, self.colour, self.rect.center, round(self.rect.width/2))

class evil:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.colour = (255, 0, 0)

    def move(self, movement):
        self.rect = self.rect.move(movement)

    def check_collide(self, player):
        if self.rect.colliderect(player.rect):
            return True
        return False

    def draw(self, display):
        pygame.draw.circle(display, self.colour, self.rect.center, round(self.rect.width/2))

class CoinManager:
    def __init__(self, boundary):
        self.boundary = pygame.Rect(boundary)
        self.coins = []
        self.spawn_chance = 0.02

        self.evilCoins = []

    def spawn(self, cave):
        current_piece = cave.pieces[len(cave.pieces) - 1]
        x = current_piece.rect.x
        y = random.randint(current_piece.rect.y, current_piece.rect.bottom)

        coin = Coin([x, y, cave.size, cave.size])
        self.coins.append(coin)

    def evilSpawn(self, cave):
        current_piece = cave.pieces[len(cave.pieces) - 1]
        x = current_piece.rect.x
        y = random.randint(current_piece.rect.y, current_piece.rect.bottom)

        evilCoin = evil([x, y, cave.size, cave.size])
        self.evilCoins.append(evilCoin)


    def update(self, movement, player, cave):
        score = 0

        for coin in self.coins:
            coin.move(movement)

            if coin.check_collide(player):
                score += 1
                self.delete(coin)

            elif self.check_delete(coin):
                self.delete(coin)

        for evilCoin in self.evilCoins:
            evilCoin.move(movement)

            if evilCoin.check_collide(player):
                score -= 1
                self.evilCoins.remove(evilCoin)

            elif self.check_delete(evilCoin):
                self.evilCoins.remove(evilCoin)

        if self.check_spawn():
            self.spawn(cave)
            self.evilSpawn(cave)

        return score

    def check_spawn(self):
        if random.random() <= self.spawn_chance:
            return True
        return False

    def check_delete(self, coin):
        if not self.boundary.colliderect(coin.rect):
            return True

    def delete(self, coin):
        self.coins.remove(coin)

    def draw(self, display):
        for coin in self.coins:
            coin.draw(display)

        for evilCoin in self.evilCoins:
            evilCoin.draw(display)


def main():
    pygame.init()
    display = pygame.display.set_mode(DISPLAY_SIZE)
    pygame.display.set_caption("Project Hermes")
    clock = pygame.time.Clock()
    FPS = 30

    cave = background.Cave(display.get_rect(), 20, colours["cave"])
    
    coin_manager = CoinManager(display.get_rect())

    player = Player(PLAYER_RECT, colours["player"])
    distance = 0
    score = 0

    end = False
    while not end:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.move_anticlockwise()
        if keys[pygame.K_s]:
            print("%s - %s" % (distance, score))
        if keys[pygame.K_p]:
            pygame.image.save(display, "soar.png")	

        # Logic
        movement = player.update([])
        distance += round(movement[0] / 10)

        # Covert to move landscape
        movement[0] = -movement[0]
        movement[1] = -movement[1]

        score += coin_manager.update(movement, player, cave)
        
        hit = cave.update(movement, player)
        if hit:
            end = True

        # Drawing
        display.fill(colours["walls"])

        cave.draw(display)
        coin_manager.draw(display)
        player.draw(display)

        font = pygame.font.SysFont("Arial", 36)
        txtsurf = font.render("Score: " + str(score), True, (255, 0 ,0))
        display.blit(txtsurf,(100 - txtsurf.get_width() // 2, 50 - txtsurf.get_height() // 2))

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
