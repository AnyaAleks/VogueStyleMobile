from kivy.app import App
from kivy.core.text import Label
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from styles import AppStyles
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty, StringProperty, Clock

from kivy.core.window import Window
Window.size = (360, 640)


class SplashScreen(Screen):
    def on_enter(self):
        # Запуск таймера на 5 секунд при входе на экран
        Clock.schedule_once(self.go_to_home, 5)  # Изменено на go_to_home

    def go_to_home(self, dt):
        self.manager.current = 'home'  # Измените 'main' на 'home'

# Объявляем классы экранов
class HomeScreen(Screen):
    salon_data = ListProperty([])
    selected_salon = StringProperty("")  # Для хранения выбранного салона

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_salon_data()

    def load_salon_data(self):
        # Готовая модель данных
        self.salon_data = [
            {"name": "VOGUESTYLE Центр", "address": "ул. Центральная, 1"},
            {"name": "VOGUESTYLE Север", "address": "ул. Северная, 5"},
            {"name": "VOGUESTYLE Юг", "address": "ул. Южная, 10"}
        ]
        # Установим первый салон по умолчанию
        if self.salon_data:
            self.selected_salon = self.salon_data[0]['name']

    def on_salon_select(self, selected_text):
        self.selected_salon = selected_text  # Обновите выбранный салон
        # Здесь вы можете добавить дополнительную логику, если это необходимо

    def show_salon_details(self, salon_name):
        details = next((s for s in self.salon_data if s['name'] == salon_name), None)
        if details:
            self.ids.details_container.clear_widgets()
            card = Factory.SalonCard()
            card.salon_name = details['name']
            card.salon_address = details['address']
            self.ids.details_container.add_widget(card)


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
        Builder.load_file('screens/splashScreen.kv')
        Builder.load_file('screens/home.kv')
        Builder.load_file('screens/services.kv')
        Builder.load_file('screens/master.kv')
        Builder.load_file('screens/error.kv')

        # Создаем ScreenManager
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(ServicesScreen(name='services'))
        sm.add_widget(MasterScreen(name='master'))
        sm.add_widget(ErrorScreen(name='error'))

        return sm


if __name__ == '__main__':
    VogueStyleApp().run()