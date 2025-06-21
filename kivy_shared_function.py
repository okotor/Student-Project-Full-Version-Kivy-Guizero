from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class FirstScreen(Screen):
    def __init__(self, on_button_press, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.on_button_press = on_button_press
        
        layout = BoxLayout(orientation='vertical')
        
        # Button to navigate to the second screen
        button = Button(text='Go to Second Screen', on_press=self.go_to_second_screen)
        layout.add_widget(button)
        
        # Button using the shared function
        shared_button = Button(text='Shared Function', on_press=self.on_button_press)
        layout.add_widget(shared_button)
        
        self.add_widget(layout)

    def go_to_second_screen(self, instance):
        self.manager.current = 'second'

class SecondScreen(Screen):
    def __init__(self, on_button_press, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.on_button_press = on_button_press
        
        layout = BoxLayout(orientation='vertical')
        
        # Button to navigate to the first screen
        button = Button(text='Go to First Screen', on_press=self.go_to_first_screen)
        layout.add_widget(button)
        
        # Button using the shared function
        shared_button = Button(text='Shared Function', on_press=self.on_button_press)
        layout.add_widget(shared_button)
        
        self.add_widget(layout)

    def go_to_first_screen(self, instance):
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Create screens and pass the shared function to each screen
        self.first_screen = FirstScreen(on_button_press=self.on_button_press, name='first')
        self.second_screen = SecondScreen(on_button_press=self.on_button_press, name='second')

        # Add screens to the screen manager
        self.screen_manager.add_widget(self.first_screen)
        self.screen_manager.add_widget(self.second_screen)

        return self.screen_manager

    def on_button_press(self, instance):
        print("Shared button pressed!")

if __name__ == '__main__':
    MyApp().run()