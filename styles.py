from kivy.utils import get_color_from_hex
from kivy.properties import ListProperty

class AppStyles:
    # Цветовая палитра
    PRIMARY = get_color_from_hex('#6a0dad')  # Основной фиолетовый
    PRIMARY_DARK = get_color_from_hex('#4b077d')  # Тёмный фиолетовый
    SECONDARY = get_color_from_hex('#9c27b0')  # Акцентный цвет
    WHITE = get_color_from_hex('#ffffff')
    LIGHT_PURPLE = get_color_from_hex('#f3e5ff')
    DARK_TEXT = get_color_from_hex('#333333')
    CARD_BACKGROUND = get_color_from_hex('#f9f3ff')
    ACCENT_COLOR = get_color_from_hex('#ff6b6b')  # Для спецпредложений

    # Размеры
    TITLE_SIZE = '28sp'
    SUBTITLE_SIZE = '18sp'
    BUTTON_HEIGHT = 50
    CARD_RADIUS = 15