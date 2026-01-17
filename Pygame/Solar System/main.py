import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

sun_angle = 0
earth_angle = 0
mars_angle = 0


def load_texture(filename):
    textureSurface = pygame.image.load(filename)
    textureData = pygame.image.tostring(textureSurface, "RGB", 1)

    width = textureSurface.get_width()
    height = textureSurface.get_height()

    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glTexImage2D(
        GL_TEXTURE_2D, 0, GL_RGB,
        width, height, 0,
        GL_RGB, GL_UNSIGNED_BYTE, textureData
    )

    return texID


def draw_textured_planet(radius, texID):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texID)

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    glRotatef(-90, 1, 0, 0)
    gluSphere(quadric, radius, 40, 40)

    glDisable(GL_TEXTURE_2D)


def SolarSystem():
    global earth_angle, mars_angle, sun_angle

    # SUN
    glPushMatrix()
    glRotatef(sun_angle, 0, 1, 0)
    draw_textured_planet(1, sun_tex)
    glPopMatrix()

    # EARTH
    glPushMatrix()
    glRotatef(earth_angle, 0, 1, 0)
    glTranslatef(3, 0, 0)
    draw_textured_planet(0.5, earth_tex)
    glPopMatrix()

    # MARS
    glPushMatrix()
    glRotatef(mars_angle, 0, 1, 0)
    glTranslatef(5, 0, 0)
    draw_textured_planet(0.4, mars_tex)
    glPopMatrix()

    earth_angle += 1
    mars_angle += 0.5
    sun_angle += 0.3


def main():
    global sun_tex, earth_tex, mars_tex

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Textured Solar System")

    gluPerspective(45, display[0] / display[1], 0.1, 50)
    glTranslatef(0, 0, -12)
    glEnable(GL_DEPTH_TEST)

    sun_tex = load_texture("sun.jpg")
    earth_tex = load_texture("earth.jpg")
    mars_tex = load_texture("mars.jpg")

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        SolarSystem()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
