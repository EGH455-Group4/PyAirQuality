'''Will hold information belonging to the enviro LCD screen.'''
import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont

from screen.screen import Screen

class EnvScreen(Screen):
    '''Implements the Screen class, and connects to the actual hardware.'''
    def __init__(self):
        self.disp = ST7735.ST7735(
            port=0,
            cs=1,
            dc=9,
            backlight=12,
            rotation=270,
            spi_speed_hz=10000000
        )
        self.disp.begin()

        self.font_size = 20
        self.font = ImageFont.truetype(UserFont, self.font_size)

    def set_lcd_screen(self, message: str) -> bool:
        '''Will log out the set option.'''
        print("set lcd screen to " + message)

        img = Image.new('RGB', (self.disp.width, self.disp.height), color=(0, 0, 0))

        draw = ImageDraw.Draw(img)

        draw.rectangle((0, 0, self.disp.width, self.disp.height), (255, 255, 255))

        draw.text((0, 0), message, font=self.font, fill=(0, 0, 0))

        self.disp.display(img)
        return True
