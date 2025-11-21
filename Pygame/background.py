# Ben-Ryder 2019

import pygame
import random


class Star:
    def __init__(self, rect, colour):
        self.rect = rect
        self.colour = colour

    def draw(self, display):
        pygame.draw.rect(display, self.colour, self.rect)


class Starscape:
    def __init__(self, boundary):
        self.amount = 350
        self.boundary = pygame.Rect(boundary)
        self._generate()

    def _generate(self):
        self.stars = []
        for s in range(self.amount):
            x = random.randint(0, self.boundary.width)
            y = random.randint(0, self.boundary.height)
            size = random.choice([2, 2, 2, 2, 3, 4])
            rect = [x, y, size, size]
            colour = (255, 255, 255)

            self.stars.append(
                Star(rect, colour)
            )

    def draw(self, display):
        for star in self.stars:
            pygame.draw.rect(display, star.colour, star.rect)


class CavePiece:
    def __init__(self, rect, colour):
        self.rect = pygame.Rect(rect)
        self.colour = colour

    def move(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def draw(self, display):
        pygame.draw.rect(display, self.colour, self.rect)


class Cave:
    def __init__(self, boundary, size, colour):
        self.boundary = pygame.Rect(boundary)

        self.size = size
        self.scale = [round(self.boundary.width / self.size), round(self.boundary.height / self.size)]
        self.colour = colour
        self.pieces = []

        # Values are in number of squares.
        self.gap_minimum = 10
        self.gap_maximum = self.scale[1] - 2
        self.piece_difference = 1  # maximum scale amounts the next piece can be different by

        # Initially making cave fill screen to edge
        length = round(self.boundary.width/self.size)
        for square in range(length):
            self.spawn_cave()
            self.move([-self.size, 0])

    def update(self, movement, player):
        self.move(movement)
        self.check_delete()
        self.check_spawn()

        return self.check_wall_hit(player)

    def move(self, movement):
        for wall in self.pieces:
            wall.move(movement[0], movement[1])

    def check_delete(self):
        if not self.boundary.colliderect(self.pieces[0]):
            self.pieces.pop(0)

    def check_spawn(self):
        if self.boundary.colliderect(self.pieces[len(self.pieces)-1]):
            self.spawn_cave()

    def spawn_cave(self):
        if len(self.pieces) == 0:
            x = self.boundary.right
            gap_size = random.randint(self.gap_minimum, self.gap_maximum)
            leftover = self.scale[1] - gap_size
            top = round(leftover) / 2

        else:
            previous_piece = self.pieces[len(self.pieces) - 1]
            x = previous_piece.rect.right

            previous_y = int(previous_piece.rect.y / self.size)
            difference = random.randint(0, self.piece_difference)
            difference = random.choice([difference, -difference])
            top = previous_y + difference

            previous_size = int(previous_piece.rect.height / self.size)
            gap_size = random.randint(previous_size - abs(difference), previous_size + abs(difference))

            if gap_size < self.gap_minimum:
                gap_size = self.gap_minimum
            elif gap_size > self.gap_maximum:
                gap_size = self.gap_maximum
            if top == previous_y:
                pass

        rect = [x, top * self.size, self.size, self.size*gap_size]
        self.pieces.append(CavePiece(rect, self.colour))

    def check_wall_hit(self, player):
        corners = [False, False,
                   False, False]
        for cave_piece in self.pieces[int(self.scale[0]*0.3):int(self.scale[0]*0.6)]:
            if cave_piece.rect.collidepoint(player.rect.topleft):
                corners[0] = True
            if cave_piece.rect.collidepoint(player.rect.topright):
                corners[1] = True
            if cave_piece.rect.collidepoint(player.rect.bottomleft):
                corners[2] = True
            if cave_piece.rect.collidepoint(player.rect.bottomright):
                corners[3] = True
        if False in corners:  # no cave piece registered a players corner, must have collided with wall.
            return True
        return False

    def draw(self, display):
        for wall in self.pieces:
            wall.draw(display)
