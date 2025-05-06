from kivy.utils import get_color_from_hex


class AppStyles:
    # Цвета
    PRIMARY = get_color_from_hex('#6a0dad')  # Фиолетовый
    WHITE = get_color_from_hex('#ffffff')
    LIGHT_PURPLE = get_color_from_hex('#f3e5ff')
    DARK_TEXT = get_color_from_hex('#333333')

    # Размеры
    TITLE_SIZE = '32sp'
    SUBTITLE_SIZE = '18sp'
    BUTTON_HEIGHT = 50

    @staticmethod
    def colored_button():
        return {
            'background_normal': '',
            'background_color': AppStyles.PRIMARY,
            'color': AppStyles.WHITE,
            'font_size': '16sp',
            'size_hint_y': None,
            'height': AppStyles.BUTTON_HEIGHT

        }