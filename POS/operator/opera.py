from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class OperaWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        pass
    def quitt(self):
        return exit()

class OperaApp(App):
    def build(self):
        return OperaWindow()

if __name__ == "__main__":
    sa = OperaApp()
    sa.run()