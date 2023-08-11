'''Will hold information belonging to the Enviro LCD screen.'''
import logging
# pylint: disable=E0611
from fonts.ttf import RobotoMedium as UserFont

from screen.screen import Screen
from models.constants import SHOW_IMAGE_PROCESSING

class EnvScreen(Screen):
    '''Implements the Screen class, and connects to the actual hardware.'''
    def __init__(self):
        import ST7735
        from PIL import ImageFont

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

    def set_lcd_screen(self, message: str):
        '''Will alter the LCD screen on the hardware.'''
        from PIL import Image, ImageDraw

        logging.info("setting lcd screen to %s", message)

        if message == SHOW_IMAGE_PROCESSING:
            image = Image.open("./lcd_picture.jpg")
            image = image.resize((self.disp.width, self.disp.height))
            self.disp.display(image)
        else:
            img = Image.new('RGB', (self.disp.width, self.disp.height), color=(0, 0, 0))

            draw = ImageDraw.Draw(img)

            draw.rectangle((0, 0, self.disp.width, self.disp.height), (255, 255, 255))

            draw.text((0, 0), message, font=self.font, fill=(0, 0, 0))

            self.disp.display(img)

        return True
