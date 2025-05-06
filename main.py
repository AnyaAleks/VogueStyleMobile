from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from styles import AppStyles


# Объявляем классы экранов
class HomeScreen(Screen):
    pass


class ServicesScreen(Screen):
    pass


class MasterScreen(Screen):
    pass


class ErrorScreen(Screen):
    pass


class VogueStyleApp(App):
    def build(self):
        self.styles = AppStyles()  # Инициализация стилей

        # Загрузка kv-файлов
        Builder.load_file('styles.kv')
        Builder.load_file('screens/home.kv')
        Builder.load_file('screens/services.kv')
        Builder.load_file('screens/master.kv')
        Builder.load_file('screens/error.kv')

        # Создаем ScreenManager
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ServicesScreen(name='services'))
        sm.add_widget(MasterScreen(name='master'))
        sm.add_widget(ErrorScreen(name='error'))

        return sm


if __name__ == '__main__':
    VogueStyleApp().run()