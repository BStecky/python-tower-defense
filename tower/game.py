import pygame

from tower.constants import (
        DESIRED_FPS,
        IMAGE_SPRITES,
        PATH_COLORS,
        INTENSITY_FREQUENCY,
        KEY_BACKGROUND,
        KEY_SHRUB,
        KEY_ENEMY,
        KEY_TURRET,
        MAX_ESCAPED,
        MOUSE_LEFT,
        MOUSE_RIGHT,
        SCREENRECT,
        SOUNDS,
        SPRITES,
        TILES_X,
        TILES_Y,
    )

@dataclass
class TowerGame:

    screen: pygame.Surface
    screen_rect: pygame.Rect
    fullscreen: bool

    @classmethod
    def create(cls, fullscreen=False):
        game = cls(
            screen=None,
            screen_rect=SCREENRECT,
            fullscreen=fullscreen,
        )
        game.init()
        return game

    def loop(self):
        pass

    def quit(self):
        pygame.quit()
    
    def start_game(self):
        self.loop()

    def init(self):
        pygame.init()
        window_style = pygame.FULLSCREEN if self.fullscreen else 0
        # This is for 32 bits of color depth, 32 bits allows for semi-transclucent pixels
        bit_depth = pygame.display.mode_ok(self.screen_rect.size, window_style, 32)
        screen = pygame.display.set_mode(self.screen_rect.size, window_style, bit_depth)
        # Sound mixer, with reasonable default settings
        pygame.mixer.pre_init(
            frequency=44100,
            size=32,
            # 2 = stereo, not the number of channels
            channels=2,
            buffer=512,
        )
        pygame.font.init()
        return screen


    clock = pygame.time.Clock()
    while True:
        # game loop yeaaaa
        pygame.display.set_caption(f"FPS {round(clock.get_fps())}")
        clock.tick(DESIRED_FPS)