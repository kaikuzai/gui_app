from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class MainApp(App):
    
    def build(self):
        return RootWidget()


class FirstScreen(Screen):
    
    def search_image(self):
        pass 

class RootWidget(ScreenManager):
    pass

MainApp().run()

