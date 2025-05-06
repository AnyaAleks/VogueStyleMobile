from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config
import os

# Настройка бэкенда
Config.set('graphics', 'backend', 'sdl2')
Config.set('graphics', 'multisamples', '0')  # Отключаем сглаживание для теста
Window.size = (360, 640)


class HomeScreen(Screen): pass


class ServicesScreen(Screen): pass


class MasterScreen(Screen): pass


class ErrorScreen(Screen): pass


class VogueStyleApp(App):
    def build(self):
        # Проверка существования файлов
        for f in ['home.kv', 'services.kv', 'master.kv', 'error.kv']:
            if not os.path.exists(f'screens/{f}'):
                print(f"Файл не найден: screens/{f}")
                return Label(text=f"Ошибка: файл {f} не найден")

        # Загрузка интерфейсов
        Builder.load_file('screens/home.kv')
        Builder.load_file('screens/services.kv')
        Builder.load_file('screens/master.kv')
        Builder.load_file('screens/error.kv')

        # Создаем экраны
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ServicesScreen(name='services'))
        sm.add_widget(MasterScreen(name='master'))
        sm.add_widget(ErrorScreen(name='error'))

        # Устанавливаем начальный экран
        sm.current = 'home'
        return sm


if __name__ == '__main__':
    try:
        VogueStyleApp().run()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        input("Нажмите Enter для выхода...")