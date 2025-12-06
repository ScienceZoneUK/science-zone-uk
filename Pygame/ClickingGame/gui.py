import pygame, sys, time
from pygame.locals import *


class TextInput(pygame.Surface):
	def __init__(self, pos, font_size, size, text="", margin=0, text_color=(200,200,200), background_color=(10,10,10)):
		pygame.Surface.__init__(self, size)
		
		self.speed = 2
		self.text = text
		self.active = False
		self.pos = pos
		self.size = size
		self.font_size = font_size
		self.text_color = text_color
		self.background_color = background_color
		self.margin = margin
		self.active_bg_color = (min(self.background_color[0]+20,255), min(self.background_color[1]+20,255), min(self.background_color[2]+20,255))
		
	def onclick(self):
		self.active = True
	
	def contains(self, pos):
		return (pos[0] >= self.pos[0] and\
		 pos[1] >= self.pos[1] and\
		 pos[0] <= self.pos[0]+self.size[0] and\
		 pos[1] <= self.pos[1]+self.size[1])
	
	def blit_on(self, surface):
		if self.active:
			self.fill(self.active_bg_color)
		else:
			self.fill(self.background_color)
		font = pygame.font.Font(None, self.font_size)
		text = font.render(self.text, 1, self.text_color)
		self.blit(text, (self.margin,self.margin))
		surface.blit(self, self.pos)
	
	def key_pressed(self, key):
		self.text += chr(key)


class AnimatedSprite(pygame.Surface):
	def __init__(self, pos, size):
		pygame.Surface.__init__(self, size)
		self.frames = []
		self.speed = 6
		self.frame_counter = 0
		self.background_color = (0,0,0)
		self.pos = pos
		
	def blit_on(self, surface):
		self.fill(self.background_color)
		self.blit(self.frames[self.frame_counter], (0,0))
		surface.blit(self, self.pos)
		
	def run(self):
		while not self.stopped():
			time.sleep(1. / self.speed)
			self.frame_counter += 1
			if self.frame_counter >= len(self.frames): self.frame_counter = 0


class Caption(pygame.Surface):
	def __init__(self, pos, font_size, size, text, margin=0, text_color=(100,100,100), background_color=(0,0,0)):
		pygame.Surface.__init__(self, size)
		self.text = text
		self.pos = pos
		self.size = size
		self.font_size = font_size
		self.text_color = text_color
		self.background_color = background_color
		self.margin = margin
	
	def blit_on(self, surface):
		self.fill(self.background_color)
		font = pygame.font.Font(None, self.font_size)
		text = font.render(self.text, 1, self.text_color)
		self.blit(text, (self.margin,self.margin))
		surface.blit(self, self.pos)


class Button(pygame.Surface):
	def __init__(self, pos, size, caption="", color=(100,100,100), text_color=(0,0,0)):
		pygame.Surface.__init__(self, size)
		self.onclick = None
		self.pressed = False
		self.hover = False
		self.caption = caption
		self.pos = pos
		self.size = size
		self.color = color
		self.text_color = text_color
		self.margin = 10
		self.pressed_color = (min(self.color[0]+100,255),min(self.color[1]+100,255),min(self.color[2]+100,255))
		self.hover_color = (min(self.color[0]+50,255),min(self.color[1]+50,255),min(self.color[2]+50,255))
	
	def blit_on(self, surface):
		self.fill(self.color)
		if self.hover: 
			self.fill(self.hover_color)
		if self.pressed:
			self.fill(self.pressed_color)

		font = pygame.font.Font(None, 16)
		text = font.render(self.caption, 1, self.text_color)
		self.blit(text, (self.margin,self.margin))
		surface.blit(self, self.pos)
	
	def contains(self, pos):
		return (pos[0] >= self.pos[0] and\
		 pos[1] >= self.pos[1] and\
		 pos[0] <= self.pos[0]+self.size[0] and\
		 pos[1] <= self.pos[1]+self.size[1])


class GUI:
	def __init__(self, size):
		pygame.init()
		self.screen = pygame.display.set_mode(size)
		self.buttons = []
		self.captions = []
		self.sprites = []
		self.text_inputs = []
		self.background_image = None
		self.running = True

	def start(self):
		self.preloop()
		clock = pygame.time.Clock()
		while self.running:
			for event in pygame.event.get():
				if event.type == QUIT:
					self.exit()
				elif event.type == MOUSEMOTION:
					for button in self.buttons:
						if button.contains(event.pos): 
							button.hover = True
						else: 
							button.hover = False
							button.pressed = False
				elif event.type == MOUSEBUTTONDOWN and event.button == 1:
					for button in self.buttons:
						if button.contains(event.pos): 
							button.pressed = True
					for text_input in self.text_inputs:
						if text_input.contains(event.pos):
							text_input.onclick()
						else:
							text_input.active = False
				elif event.type == MOUSEBUTTONUP and event.button == 1:
					for button in self.buttons:
						if button.pressed and button.onclick != None: 
							button.onclick()
						button.pressed = False
				elif event.type == KEYDOWN:
					for text_input in self.text_inputs:
						if text_input.active:
							text_input.key_pressed(event.key)
				self.react(event)
			self.inloop()
			self.screen.fill((0,0,0))
			if not self.background_image == None:
				self.screen.blit(self.background_image, (0,0))
			for button in self.buttons:
				button.blit_on(self.screen)
			for caption in self.captions:
				caption.blit_on(self.screen)
			for sprite in self.sprites:
				sprite.blit_on(self.screen)
			for text_input in self.text_inputs:
				text_input.blit_on(self.screen)
			pygame.display.flip()
			clock.tick(60)

	def exit(self):
		self.preexit()
		self.running = False
		sys.exit()

	def preloop(self):
		pass

	def inloop(self):
		pass

	def preexit(self):
		pass

	def react(self, event):
		pass

if __name__ == "__main__":

	testgui = GUI()
	testgui.start()
