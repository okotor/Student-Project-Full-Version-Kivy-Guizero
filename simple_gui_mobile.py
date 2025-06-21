from kivy.app import App
from kivy_config.simple_kivy_config import *
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from simple_main import *
import webbrowser

### Login Screen
class FirstScreen(Screen):
    def __init__(self, on_button_press, **kwargs):
        super().__init__(**kwargs)
        self.on_button_press = on_button_press
        self.widget_positions = {}
        # Calculate center of the screen
        self.widget_positions['central_x'] = Window.width / 2
        self.widget_positions['central_y'] = Window.height / 2


        ## Loading Main Layout
        main_layout = FloatLayout(
            size_hint=(1, 1)
        )

        self.create_image_box(main_layout)
        self.create_play_ad_box(main_layout)
        self.create_login_box(main_layout)
        self.create_register_box(main_layout)

        self.add_widget(main_layout)

        """Window.bind(on_resize=self.update_layout)"""

    ##  Functions to Generate Widgets
    def create_box(self, size_hint, pos_hint, children):
        box = FloatLayout(
            size_hint=size_hint,
            pos_hint=pos_hint
        )

        for child in children:
            box.add_widget(child)
        return box

    def create_image_box(self, layout):
        image1_path = "images/a_fat_burner_pic1.png"
        image_widget = Image(
            source=image1_path,
            size_hint=(None, None),
            size=(400, 400),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.5}
        )

        image_box = self.create_box(
            size_hint=(1, 0.1),
            pos_hint={'x': 0,
                      'y': 0.9},
            children=[image_widget]
        )
        layout.add_widget(image_box)

    def create_play_ad_box(self, layout):
        center_x = Window.width / 2
        center_y = Window.height / 2

        ad_label = Label(
            text="Advertisement & Instructions",
            font_size='20sp',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.83}
        )
        
        self.widget_positions['play_button'] = Button(
            text="Play Ad",
            size_hint=(None, None),
            size=(75, 40),
            pos_hint={'center_x': 0.198,
                'center_y': 0.43}
        )
        
        self.widget_positions['stop_button'] = Button(
            text="Stop Ad",
            size_hint=(None, None),
            size=(75, 40),
            pos_hint={'center_x': 0.353,
                      'center_y': 0.43}
        )
    
        self.widget_positions['youtube_button'] = Button(
            text='Watch Before You Start',
            size_hint=(None, None),
            size=(220, 40),
            pos_hint={'center_x': 0.65,
                      'center_y': 0.43}    
        )
        

        self.widget_positions['play_button'].bind(on_press=self.play_ad_kivy)
        self.widget_positions['stop_button'].bind(on_press=self.stop_ad_kivy)
        self.widget_positions['youtube_button'].bind(on_press=self.on_button_press)

        play_ad_box = self.create_box(
            size_hint=(1, 0.1),
            pos_hint={'x': 0,
                      'y': 0.8},
            children=[ad_label, self.widget_positions['play_button'], self.widget_positions['stop_button'], self.widget_positions['youtube_button']]
        )
        layout.add_widget(play_ad_box)

    def create_login_box(self, layout):
        login_label = Label(
            text="Login",
            font_size='20sp',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.8}
        )
        
        self.user_spinner = Spinner(
            text='Select user',
            values=[],
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.32}
        )
        self.user_spinner.bind(text=self.user_pick)

        self.users_load(self.user_spinner)

        login_box = self.create_box(
            size_hint=(1, 0.1),
            pos_hint={'x': 0,
                      'y': 0.7},
            children=[login_label,
                      self.user_spinner]
        )
        layout.add_widget(login_box)

    def create_register_box(self, layout):
        register_label = Label(
            text="Register a new user",
            font_size='20sp',
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.94}
        )

        username_label = Label(
            text="Please enter your username:",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.87}
        )

        self.username_input = TextInput(
            multiline=False,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.8}
        )

        sex_label = Label(
            text="Please choose your sex:",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.72}
        )

        self.sex_spinner = Spinner(
            text='Female',
            values=["Female", "Male"],
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.65}
        )

        height_label = Label(
            text="Please choose your height in cm:",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.55}
        )

        self.height_slider = Slider(
            min=90,
            max=250,
            value=165,
            size_hint=(None, 0.1),  # Fixed width, adjust height as a percentage of parent
            width=300,  # Fixed width
            pos_hint={'center_x': 0.5,
                      'center_y': 0.5}
        )
        self.height_slider.bind(value=self.update_height_label)

        self.height_label = Label(
            text="Height: 165 cm",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.45}
        )

        dob_label = Label(
            text="Select your date of birth:",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.385}
        )

        day_label = Label(
            text="Day:",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.3,
                      'center_y': 0.34}
        )

        self.day_spinner = Spinner(
            text='1',
            values=[str(i) for i in range(1, 32)],
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.3,
                      'center_y': 0.28}
        )

        month_label = Label(
            text="Month:",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.34}
        )

        self.month_spinner = Spinner(
            text='01',
            values=["01", "02", "03", "04",
                    "05", "06", "07", "08",
                    "09", "10", "11", "12"
                    ],
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.28}
        )

        year_label = Label(
            text="Year:",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.7,
                      'center_y': 0.34}
        )

        self.year_spinner = Spinner(
            text='2009',
            values=[str(i) for i in range(1907, 2024)],
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.7,
                      'center_y': 0.28}
        )

        self.register_button = Button(
            text="Register",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5,
                      'center_y': 0.19}
        )
        self.register_button.bind(on_press=self.user_register)

        self.username_taken_label = Label(
            text="",
            size_hint=(1, None),  # Stretch horizontally, fixed height
            height=100,  # Fixed height for demonstration
            text_size=(None, 100),  # Wrap text based on the height
            halign='center',
            valign='top',
            padding=(10)
        )
        self.username_taken_label.bind(size=self.update_text_size)

        register_box = self.create_box(
            size_hint=(1, 0.7),
            pos_hint={'x': 0, 
                      'y': 0},
            children=[
                register_label, username_label, self.username_input, sex_label, self.sex_spinner,
                height_label, self.height_slider, self.height_label, dob_label,
                day_label, self.day_spinner, month_label, self.month_spinner,
                year_label, self.year_spinner, self.register_button, self.username_taken_label
            ]
        )
        layout.add_widget(register_box)

    ## Widget Functions
    def update_text_size(self, instance, value):
        # Update the text size to wrap within the label width
        instance.text_size = (instance.width - 20, None)  # Add padding consideration

    def play_ad_kivy(self, instance):
        play_ad()

    def stop_ad_kivy(self, instance):
        stop_ad()

    def users_load(self, spinner):
        # Clear the current spinner values
        spinner.values = ()  
        usernames = users_load_google_sheet()
        # Add usernames to the spinner
        spinner.values = usernames[1:]  # Skip header row

    def user_pick(self, instance, picked_user_str):
        picked_user_str = self.user_spinner.text.strip()
        picked_user = user_pick_google_sheet(picked_user_str)
        create_and_or_load_google_sheet(sheet_name=picked_user.user_sheet_str)
        self.welcome_user(instance, picked_user.username)
        self.manager.current = 'second_screen'
    
    def welcome_user(self, instance, user):
        self.manager.get_screen('second_screen').update_welcome_label(f'Welcome, {user}!')

    def update_height_label(self, instance, value):
        self.height_label.text = f"Height: {int(value)} cm"

    # Function to be called when the "Register" button is pressed
    def user_register(self, instance):
        username = self.username_input.text.strip()
        # Check if the username contains only alphanumeric characters and no spaces
        if not username.isalnum() or ' ' in username:
            self.username_taken_label.text = (
                "Username contains symbols"
                " other than numbers or letters"
                " (including spaces). Please change it."
            )
            return
        # Open the Google Sheet and worksheet
        worksheet = access_usersdata_sheet()
        existing_usernames = username_check(worksheet, username, self.username_taken_label)
        if existing_usernames == False:
            return
        # Store user data
        day = self.day_spinner.text
        month = self.month_spinner.text
        year = self.year_spinner.text
        # Format the date column as date
        dob = datetime.strptime(f"{day}/{month}/{year}", "%d/%m/%Y")
        # Create an instance of the User class
        new_user = User(
            username,
            self.sex_spinner.text,
            int(self.height_slider.value),
            dob.strftime("%d/%m/%Y")
        )
        user_record_create(new_user, worksheet, existing_usernames)
        self.users_load(self.user_spinner)
        self.username_taken_label.text = "User successfully registered."

    def update_layout(self, *args):
        x = self.widget_positions['central_x']
        y = self.widget_positions['central_y']
        self.widget_positions['play_button'].pos = {x - 100, y + 100}
        self.widget_positions['stop_button'].pos = {x - 100, y + 100}
        self.widget_positions['youtube_button'].pos = {x - 100, y + 100}

### Main Screen
class SecondScreen(Screen):
    def __init__(self, on_button_press, **kwargs):
        super().__init__(**kwargs)
        self.on_button_press = on_button_press

        ## Functions Generating Widgets
        # Place an image
        image2_path = "images/schema_white.png"
        self.image_widget = Image(
            source=image2_path,
            size_hint=(1, None),
            height=510,
            pos_hint={'center_x': 0.5,
                      'center_y': 0.43}
        )

        self.welcome_label = Label(
            text=f"",
            bold=True,
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5,
                      'top': 1.035}
        )

        optimal_fat_header = Label(
            text="Please enter your weight in kilograms (kg):",
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5,
                      'top': 1.01}
        )

        self.optimal_fat_txtbox = TextInput(
            size_hint=(None, None),
            size=(50, 40),
            pos_hint={'center_x': 0.5,
                      'top': 0.94}
        )

        self.current_fat_header = Label(
            text="Please enter the sum of your three\nskinfold areas in millimeters (mm):",
            size_hint=(1, None),  # Stretch horizontally, fixed height
            height=100,  # Fixed height for demonstration
            text_size=(None, 100),  # Wrap text based on the height
            halign='center',
            valign='top',
            padding=(25,25),
            pos_hint={'center_x': 0.35,
                      'top': 0.922}
        )
        self.current_fat_header.bind(size=self.update_text_size)

        self.how_to_button = Button(
            text='How To Obtain It?',
            size_hint=(None, None),
            size=(155, 30),
            pos_hint={'center_x': 0.805,
                      'top': 0.881}    
        )
        self.how_to_button.bind(on_press=self.on_button_press)

        self.current_fat_txtbox = TextInput(
            size_hint=(None, None),
            size=(50, 40),
            pos_hint={'center_x': 0.5,
                      'top': 0.832}
        )

        calculate_button = Button(
            text="Calculate My Current & Optimal Fat Level",
            size_hint=(None, None),
            size=(350, 40),
            pos_hint={'center_x': 0.5, 'top': 0.775}
        )
        calculate_button.bind(on_press=self.calculate_basic_user_data)

        self.current_fat_text = Label(
            text="",
            size_hint=(1, None),  # Stretch horizontally, fixed height
            height=100,  # Fixed height for demonstration
            text_size=(None, 100),  # Wrap text based on the height
            halign='center',
            valign='top',
            padding=(40,40),
            pos_hint={'center_x': 0.5,
                      'top': 0.585}
        )
        self.current_fat_text.bind(size=self.update_text_size)

        self.optimal_fat_text = Label(
            text="", 
            size_hint=(1, None),  # Stretch horizontally, fixed height
            height=100,  # Fixed height for demonstration
            text_size=(None, 100),  # Wrap text based on the height
            halign='center',
            valign='top',
            padding=(30, 30),
            pos_hint={'center_x': 0.5,
                      'top': 0.485}
        )
        self.optimal_fat_text.bind(size=self.update_text_size)

        self.bmr_text = Label(
            text="", 
            size_hint=(1, None),  # Stretch horizontally, fixed height
            height=100,  # Fixed height for demonstration
            text_size=(None, 100),  # Wrap text based on the height
            halign='center',
            valign='top',
            padding=(20,20),
            pos_hint={'center_x': 0.5,
                      'top': 0.3655}
        )
        self.bmr_text.bind(size=self.update_text_size)

        self.back_button = Button(
            text="Store Today's User Data in a Google Sheet",
            size_hint=(None, None),
            size=(350, 40),
            pos_hint={'center_x': 0.5,
                      'top': 0.14},
            on_press=lambda instance: self.store_todays_data(instance, todays_date_str, todays_data_list)
        )

        self.todays_data_text = Label(
            text="",
            size_hint=(0.6, 0.05),
            pos_hint={'center_x': 0.5,
                      'top': 0.1}
        )

        self.change_user_button = Button(
            text="Change User",
            size_hint=(None, None),
            size=(170, 40),
            pos_hint={'center_x': 0.5, 'top': 0.055},
            on_press=self.user_logout
        )

        # List of widgets to add
        widgets = [
            self.image_widget,
            self.welcome_label,
            optimal_fat_header,
            self.optimal_fat_txtbox,
            self.current_fat_header,
            self.current_fat_txtbox,
            self.how_to_button,
            calculate_button,
            self.current_fat_text,
            self.optimal_fat_text,
            self.bmr_text,
            self.back_button,
            self.todays_data_text,
            self.change_user_button,
        ]

        # Add all widgets to the layout
        for widget in widgets:
            self.add_widget(widget)

    ## Widget Functions
    def update_text_size(self, instance, value):
        # Update the text size to wrap within the label width
        instance.text_size = (instance.width - 20, None)  # Add padding consideration

    def update_welcome_label(self, new_text):
        self.welcome_label.text = new_text

    def calculate_basic_user_data(self, instance):
        try:    
            fat_data['weight'] = round(float(self.optimal_fat_txtbox.text), 2)
            fat_data['skinfolds_sum'] = round(float(self.current_fat_txtbox.text), 2)
            picked_user = calculate_fat_data()
            self.current_fat_text.text = (
                "Your current fat balance"
                f" is:\n    {fat_data['cur_fat_lvl']}kg fat"
                f" ({fat_data['cur_fat_perc']}%)\n"
            )
            self.optimal_fat_text.text = (
                "Your recommended fat balance\nrange right now"
                f" is between\n{fat_data['min_opt_fat_lvl']}kg"
                f" ({picked_user.minimum_optimal_body_fat_perc}%) and {fat_data['max_opt_fat_lvl']}kg"
                f" ({picked_user.maximum_optimal_body_fat_perc}%)\n\n    Your"
                f" optimal weight range (BMI) is between\n{fat_data['min_opt_weight']} "
                f"and {fat_data['max_opt_weight']}kg."
            ) 
            self.bmr_text.text = (
                "Without any activity"
                ", you should be able to\nconsume up to"
                f": {fat_data['cal_main_lvl']}kcal to "
                "preserve\n" + "" * 15 + "your current weight."
            )
        except:
            self.current_fat_text.text = (
                "   You must type a "
                "whole\n       or decimal number in both fields."
            )
            self.optimal_fat_text.text = ""
            self.bmr_text.text = ""

    def store_todays_data(self, instance, todays_date_str, todays_data_list):
        have_some_data = basic_calc_made_or_not()
        if have_some_data:
            worksheet = access_picked_user_google_sheet()
            date_column = worksheet.col_values(1)  # Assuming date is in the first column
            if todays_date_str in date_column:
                self.show_info_popup()
            else:
                worksheet.append_row(todays_data_list)
                self.todays_data_text.text = "Today's data stored."
        else:
            self.todays_data_text.text = (
                "You must first calculate"
                " your current & optimal fat level."
            )

    def show_info_popup(self):
        popup_layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )
        info_label = Label(
            text="Do you want to update it?"
        )
        popup_layout.add_widget(info_label)

        button_layout = BoxLayout(
            orientation='horizontal',
            spacing=10
        )
        button1 = Button(
            text="Yes"
        )
        button1.bind(on_press=self.update_todays_data)
        button2 = Button(
            text="No"
        )
        button2.bind(on_press=self.update_not)
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        popup_layout.add_widget(button_layout)
        self.info_popup = Popup(
            title="Today's data has already been stored.",
            content=popup_layout,
            size_hint=(None, None),
            size=(400, 200)
        )
        self.info_popup.open()

    def update_todays_data(self, instance):
        self.info_popup.dismiss()
        update_todays_data_google_sheet()
        self.todays_data_text.text = "Today's data updated."

    def update_not(self, instance):
        self.info_popup.dismiss()

    def user_logout(self, instance):
        # Switch back to the first screen
        self.manager.current = 'first_screen'
        # Reset GUI elements
        self.current_fat_txtbox.text = ""
        self.optimal_fat_txtbox.text = ""
        self.current_fat_text.text = ""
        self.optimal_fat_text.text = ""
        self.bmr_text.text = ""
        self.todays_data_text.text = ""
        # Restart main program's variables
        user_restart()

### App
class FatBurnerApp(App):
    def build(self):
        sm = ScreenManager()

        self.screen1 = FirstScreen(
            on_button_press=self.on_button_press,
            name='first_screen'
        )
        sm.add_widget(self.screen1)
        
        self.screen2 = SecondScreen(
            on_button_press=self.on_button_press,
            name='second_screen'
        )
        sm.add_widget(self.screen2) 

        return sm
    
    def on_button_press(self, instance):
        # URL to open
        url = 'https://youtu.be/hvC2TDs95xY?si=eVcK6IbKbOleZs-M'
        webbrowser.open(url)
    
if __name__ == "__main__":
    FatBurnerApp().run()
