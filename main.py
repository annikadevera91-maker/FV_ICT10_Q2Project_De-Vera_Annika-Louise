from pyscript import document

# SEATWORK 1


# Python list containing g10 ict club members
club_members = [
"Francis Fernandez", "Gavin Ruiz", "Edrian Correa", "Philip Ponce", "Julian Anaque", "Andrik David", "Annika De Vera", "Eliana Daet"]

def check_membership(event):
    # First and last name entered by the user and combine them into one full name
    fname = document.querySelector("#first-name").value.strip()
    lname = document.querySelector("#last-name").value.strip()
    full_name = f"{fname} {lname}"

    # Check whether the full name is in the club members list. 
    is_member = full_name in club_members

    # boolean indexing (True -> 1, False -> 0)
    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Welcome {full_name}, you are a member of the G10 ICT Club!"]
    
    bg_colors = ["#f8d7da", "#d1e7dd"]
    text_colors = ["#842029", "#0f5132"]

    index = int(is_member)
    message = messages[index]

    # Update result area UI
    result_div = document.querySelector("#result")
    result_div.innerText = message
    result_div.style.backgroundColor = bg_colors[index]
    result_div.style.color = text_colors[index]


#DRILL 2

# Python list containing g10 ict club members
club_members = [
"Gavin Ruiz", "Edrian Correa", "Philip Ponce", "Julian Anaque", "Andrik David", "Annika De Vera", "Eliana Daet", "Zecca Zeppola", "Tic Toc Tortora", "Ratio Randall", "Coccinella Cotoletta", "Farfallina Farfallona", "Grissino Gabbiano", "Biscotto Brontolone", "Falena Fettuccina", "Brum Brum Bradipo", "Maestro Mortadella", "Sedia Seppia"
]
club_members.sort()

def check_membership(event):
    # First and last name entered by the user and combine them into one full name
    fname = document.querySelector("#first-name").value.strip()
    lname = document.querySelector("#last-name").value.strip()
    full_name = f"{fname} {lname}"

    # Check whether the full name is in the club members list. 
    is_member = full_name in club_members

    # boolean indexing (True -> 1, False -> 0)
    messages = (f"Please Check if your name is in the list of G10 ICT Club Members:{club_members}. {full_name} is a member.",
                f"Please Check if your name is in the list of G10 ICT Club Members:{club_members}. {full_name} is not a member.")

    print.txt(f"Please Check if your name is in the list of G10 ICT Club Members:{club_members}. {full_name} is a member.")
    
    
    bg_colors = ["#f8d7da", "#d1e7dd"]
    text_colors = ["#721c24", "#155724"]

    index = int(is_member)
    message = messages[index]

    # Update result area UI
    result_div = document.querySelector("#result")
    result_div.innerText = message
    result_div.style.backgroundColor = bg_colors[index]
    result_div.style.color = text_colors[index]


#SKILLSTEST

# Dictionary of weather instruments and their corresponding information
weather_instruments = {
    "Thermometer": ("Air Temperature", "Degrees Celsius (°C)", "Measures how hot or cold the air is."),
    "Barometer": ("Atmospheric Pressure", "Hectopascals (hPa)", "Measures air pressure to help monitor weather changes."),
    "Anemometer": ("Wind Speed", "Kilometers per hour (km/h)", "Measures how fast the wind is blowing."),
    "Hygrometer": ("Relative Humidity", "Percent (%)", "Measures the amount of moisture in the air."),
    "Rain Gauge": ("Rainfall", "Millimeters (mm)", "Measures the amount of rainfall in an area."),
    "Wind Vane": ("Wind Direction", "Cardinal Directions", "Identifies the direction from which the wind is blowing."),
    "Weather Balloon": ("Atmospheric Conditions", "Varies", "Collects atmospheric data at different altitudes."),
    "Pyranometer": ("Solar Radiation", "Watts per square meter (W/m²)", "Measures incoming solar radiation.")
}
# Get the Input from HTML
def Search_Element(e):
    raw_input = document.getElementById("weather_instruments").value
    instrument_name = raw_input.strip().title()

    if not instrument_name:
        document.getElementById("instruments").innerText = "-"
        document.getElementById("measures").innerText = "Please enter an instrument name"
        document.getElementById("unit-of-measurement").innerText = "-"
        document.getElementById("purpose").innerText = "-"
        return
# Retrieve info from the dictionary
    result = weather_instruments.get(instrument_name, ("Weather Instrument not found", "-", "-"))
# Display the result in HTML
    document.getElementById("instruments").innerText = instrument_name
    document.getElementById("measures").innerText = result[0]
    document.getElementById("unit-of-measurement").innerText = result[1]
    document.getElementById("purpose").innerText = result[2]