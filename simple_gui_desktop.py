from guizero import *
from simple_main import *

###GUI functions
# Prepopulates the users combo and repopulates it after a user registers
def users_load(combo):
    combo.clear()
    usernames = users_load_google_sheet()
    # Add usernames to the combo box
    for username in usernames[1:]:  # Skip header row
        combo.append(username)

def user_pick():
    picked_user_str = user_combo.value
    picked_user = user_pick_google_sheet(picked_user_str)
    welcome_text.value = f"Welcome, {picked_user.username}!"
    create_and_or_load_google_sheet(sheet_name=picked_user.user_sheet_str)
    window1.hide()
    window2.show()

# Function to be called when the "Register" button is pressed
def user_register():
    username = register_textbox.value
    # Check if the username contains only alphanumeric characters and no spaces
    if not username.isalnum() or ' ' in username:
        username_taken_text.value = (
            "Username contains symbols other"
            " than numbers or letters (including spaces)."
            " Please change it."
        )
        return
    # Open the Google Sheet and worksheet
    worksheet = access_usersdata_sheet()
    existing_usernames = username_check(worksheet, username, username_taken_text)
    if existing_usernames == False:
        return
    # Store user data
    day = day_combo.value
    month = month_combo.value
    year = year_combo.value
    # Format the date column as date
    dob = datetime.strptime(f"{day}/{month}/{year}", "%d/%m/%Y")
    # Create an instance of the User class
    new_user = User(
        username,
        str(combo7.value),
        slider10.value,
        dob.strftime("%d/%m/%Y")
    )
    user_record_create(new_user, worksheet, existing_usernames)
    users_load(user_combo)
    username_taken_text.value = "User successfully registered."

def calculate_basic_user_data():
    try:
        fat_data['weight'] = round(float(optimal_fat_txtbox.value), 2)
        fat_data['skinfolds_sum'] = round(float(current_fat_txtbox.value), 2)
        picked_user = calculate_fat_data()
        current_fat_text.value = (
            f"Your current fat balance is:"
            f"\n{fat_data['cur_fat_lvl']}kg fat ({fat_data['cur_fat_perc']}%)"
        )
        optimal_fat_text.value = (
            f"Your recommended fat balance range right now is "
            f"between\n{fat_data['min_opt_fat_lvl']}kg "
            f"({picked_user.minimum_optimal_body_fat_perc}%) "
            f"and\n{fat_data['max_opt_fat_lvl']}kg ({picked_user.maximum_optimal_body_fat_perc}%)"
            f"\n\n Your optimal weight range (BMI) is between {fat_data['min_opt_weight']} "
            f"and {fat_data['max_opt_weight']}kg."
        ) 
        bmr_text.value = (
            f"\n       Without any activity,"
            f"\nyou should be able to consume up to:"
            f"\n{fat_data['cal_main_lvl']}kcal\nto "
            "preserve your current weight.       "
        )
    except:
        current_fat_text.value = (
            "You must type a "
            "whole or decimal number\nin both fields."
        )
        optimal_fat_text.value = ""
        bmr_text.value = ""

def store_todays_data():
    have_some_data = basic_calc_made_or_not()
    if have_some_data:
        worksheet = access_picked_user_google_sheet()
        # Get all dates from the first column
        date_column = worksheet.col_values(1)  # Assuming the date is stored in the first column
        # Check if today's date is already in the date column
        if todays_date_str in date_column:
            info_window2.show(wait=True)
        else:  
            worksheet.append_row(todays_data_list)
            todays_data_text.value = "Today's data stored."
    else: 
        todays_data_text.value = (
            "You must first calculate "
            "your current & optimal fat level."
        )

def update_todays_data():
    info_window2.hide()
    update_todays_data_google_sheet()
    todays_data_text.value = "Today's data updated."

def update_not():
    info_window2.hide()

def user_logout():
    #Regenerate login window
    window2.hide()
    window1.show()
    #Restart GUI
    welcome_text.value = ""
    current_fat_txtbox.clear()
    optimal_fat_txtbox.clear()
    current_fat_text.value = ""
    optimal_fat_text.value = ""
    bmr_text.value = ""
    todays_data_text.value = ""
    #Restart main program's variables
    user_restart()

###GUI App
app = App(title="Fat Burner", width=775, height=775)

##LOGIN WINDOW
window1 = Box(app)

# Image box
image_box = Box(window1, height="fill", align="top")
image_widget = Picture(image_box,image="images/a_fat_burner_pic2.png", width=400, height=100)

# Ad box
# Create buttons to control music
ad_box = Box(window1, height="fill", align="left", border=True)
ad_text = Text(ad_box, "  Play Advertisement  ", size=15, font="Segoe UI bold")
play_button = PushButton(ad_box, text="Play", command=play_ad)
stop_button = PushButton(ad_box, text="Stop", command=stop_ad)

# Login box
login_box = Box(window1, height="fill", align="right", border=True)
login_text = Text(login_box, "Login", size=15, font="Segoe UI bold")
user_text = Text(login_box, "  Choose user:  ")
user_combo = Combo(login_box, options=[], command=user_pick)
users_load(user_combo)

# Register box
register_box = Box(window1, height="fill", align="top", border=True)            
register_text = Text(register_box, "Register a new user", size=15, font="Segoe UI bold")
username_text = Text(register_box, "Please enter your username:")
register_textbox = TextBox(register_box)
sex_text = Text(register_box, "Please choose your sex:")
sex_combo = Combo(register_box, options=["Female", "Male"])
height_text = Text(register_box, "  Please choose your height in cm:  ")
height_slider = Slider(register_box, start=0, end=250)
Text(register_box, text="Select your date of birth:")
Text(register_box, text="Day:")
day_combo = Combo(register_box, options=[str(i) for i in range(1, 32)])
Text(register_box, text="Month:")
month_combo = Combo(register_box,
    options=["01", "02", "03", "04",
             "05", "06", "07", "08",
             "09", "10", "11", "12"])
Text(register_box, text="Year:")
year_combo = Combo(register_box, options=[str(i) for i in range(1907, 2024)])
submit_button = PushButton(register_box, text="Register", command=user_register)
username_taken_text = Text(register_box, text="")


##MAIN WINDOW
window2 = Box(app, visible=False)

# Welcome text
welcome_text = Text(window2, text=(f""))

# Calculate basic data
current_fat_header = Text(
    window2,
    text=(
        "        Please enter the sum"
        " of your three skinfold areas in milimeters (mm):"
    )
)
current_fat_txtbox = TextBox(window2)
optimal_fat_header = Text(
    window2,
    text=(f"Please enter your weight in kilograms (kg):")
)
optimal_fat_txtbox = TextBox(window2)
button = PushButton(
    window2,
    command=calculate_basic_user_data,
    text="Calculate My Current & Optimal Fat Level"
)
current_fat_text = Text(window2, text ="")
optimal_fat_text = Text(window2, text ="")
bmr_text = Text(window2, text="")

# Store data and logout
store_button = PushButton(
    window2,
    command=store_todays_data,
    text="Store Today's Data"
)
info_window2 = Window(
    window2,
    title="Attenzione",
    width=300,
    height=200
)
info_window2.hide()
info_text = Text(
    info_window2,
    text=(
        "      Today's record has already been made."
        "\nDo you want to update today's data?"
    ),
    align="top"
)
yes_button = PushButton(
    info_window2,
    command=update_todays_data,
    text="      Yes      ",
    align="left"
)
no_button = PushButton(
    info_window2,
    command=update_not,
    text="      No      ",
    align="right"
)
todays_data_text = Text(
    window2,
    text =""
)
button = PushButton(
    window2,
    command=user_logout,
    text="      Change User      ",
    align="top"
)

# Display an image
image_widget = Picture(
    window2,
    image="images/schema_black.png",
    width=250,
    height=250,
    align="bottom"
)

app.display()

