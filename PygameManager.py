
class PygameManager:
    def __init__(self, pygame):
        self.clock = pygame.time.Clock()
        self.pygame = pygame

    def setup(self):
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((640, 480))

    def clockTick(self):
        self.clock.tick(60)

    def teardown(self):
        self.pygame.quit()