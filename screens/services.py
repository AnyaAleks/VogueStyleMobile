from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, ObjectProperty
from kivy.clock import Clock
import json
import os


class ServicesScreen(Screen):
    services = ListProperty([])
    app = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.load_services)

    def load_services(self, dt):
        try:
            # Путь к файлу относительно расположения main.py
            json_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'services.json')

            with open(json_path, 'r', encoding='utf-8') as f:
                self.services = json.load(f)
        except Exception as e:
            print(f"Ошибка загрузки услуг: {e}")
            # Резервные тестовые данные
            self.services = [
                {"id": 1, "name": "Классический маникюр", "price": 1500},
                {"id": 2, "name": "Мужская стрижка", "price": 1200},
                {"id": 3, "name": "Окрашивание волос", "price": 3500}
            ]

    def on_services(self, instance, value):
        """Обновление списка при изменении данных"""
        if hasattr(self, 'rv'):
            self.rv.data = [{'service': service} for service in value]