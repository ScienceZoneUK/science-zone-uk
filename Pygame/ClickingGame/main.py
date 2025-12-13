import gui, time, random, pygame

class RunningButton(gui.Button):

	size = (50, 50)

	def __init__(self, window_size):
		gui.Button.__init__(self, self.random_pos(window_size), self.size, "", (255, 0, 0))
		
		self.pressed_color = (252, 3, 73)
		self.hover_color = (252, 3, 165)
		self.window_size = window_size
		
	def random_pos(self, window_size=None):
		if window_size == None: window_size = self.window_size
		size_x = window_size[0]
		size_y = window_size[1]
		pos_x = random.randint(self.size[0], size_x - self.size[0])
		pos_y = random.randint(self.size[1], size_y - self.size[1])
		return (pos_x, pos_y)
		
class CGUI(gui.GUI):

	size = (500, 650)
	
	def __init__(self):
		gui.GUI.__init__(self, self.size)
		pygame.display.set_caption("clicking game")
		pygame.mouse.set_visible(True)
		
		self.background_image = pygame.image.load("bg2.png")
		self.game_is_over = False
		self.time_limit = 10. # in seconds
		self.reset_game()
		
		
	def update_time_limit(self):
		self.time_limit = 10.
		for i in range(1, self.level):
			self.time_limit *= 5./10.
			
	def update_level(self):
		self.level = 1 + self.score // 20000
		
	
	def reset_game(self):
		self.rb = RunningButton((500, 400))
		self.rb.onclick = self.rb_clicked
		self.buttons = []
		self.buttons.append(self.rb)
		
		self.time_left = 0
		self.time_left_caption = gui.Caption((10, 500), 50, (self.size[0], 50), str(self.time_left), 0, (255,255,255), (30,10,10))
		self.captions.append(self.time_left_caption)
		
		self.level = 1
		self.level_caption = gui.Caption((10, 550), 50, (self.size[0], 50), str(self.level), 0, (255,255,255), (10,30,10))
		self.captions.append(self.level_caption)
		
		self.score = 0
		self.score_caption = gui.Caption((10, 600), 50, (self.size[0], 50), str(self.score), 0, (255,255,255), (10,10,30))
		self.captions.append(self.score_caption)
		
		
		
		self.last_clicktime = time.time()
		self.update_time_limit()
		
	
	def rb_clicked(self):
		if not self.game_is_over:
			self.rb.pos = self.rb.random_pos()
			self.last_clicktime = time.time()
			self.score += int(self.time_left * 100) * self.level
		else:
			pass
			#self.game_is_over = False
			#self.reset_game()
		
	def game_over(self):
		self.time_left_caption.text = "GAME OVER"
		self.game_is_over = True
		self.rb.pressed_color = (255, 0, 0)
		self.rb.hover_color = (255, 0, 0)
		
	def inloop(self):
		if self.game_is_over: return
		now = time.time()
		diff = now - self.last_clicktime
		self.time_left = self.time_limit - diff
		if self.time_left <= 0:
			self.game_over()
		else:
			self.time_left_caption.text = "TIME LEFT: " + str(int(self.time_left*10)/10.) + " seconds"
			self.score_caption.text = "SCORE : " + str(self.score) + " points"
			self.level_caption.text = "LEVEL: " + str(self.level)
			blue = int(255 * self.time_left / self.time_limit)
			red = 255 - blue
			green = int(0.8 * red)
			self.rb.color = (red, green, blue)
		self.update_level()
		self.update_time_limit()
		
		
		
if __name__ == "__main__":
	cg = CGUI()
	cg.start()