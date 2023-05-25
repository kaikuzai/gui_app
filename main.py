from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
import wikipedia

Builder.load_file('frontend.kv')

class MainApp(App):
    
    def build(self):
        return RootWidget()


class FirstScreen(Screen):
    
    def get_image_link(self):
        query = self.manager.current_screen.ids.user_query.text
        wikipedia_page = wikipedia.page(query, auto_suggest=False)
        image_link = wikipedia_page.images[0]
        return image_link

    def download_image(self):
        image_path = 'files/image.jpeg'
        headers = {'User-Agent':'WikiImageSearch/1.0 (https://doesnotexist.com) generic-library/1.0'}
        req = requests.get(self.get_image_link, headers=headers)

        with open(image_path, 'wb') as f:
            f.write(req.content)
        return image_path

    def set_image(self):
            self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

MainApp().run()

