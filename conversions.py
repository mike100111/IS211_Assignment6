
# Converts Celcius to Kelvin
def convertCelsiusToKelvin(value):
    return round(value + 273.15,2)

#Converts Celcius to Fahrenheit
def convertCelsiusToFahrenheit(value):
    return round(value * 9.0/5.0 + 32.0,2)

# COnverts Fahrenheit to Celcius
def convertFahrenheitToCelcius(value):
    return round((value - 32) * 5.0/9.0,2)

# Convert Farenheit to Kelvin
def convertFarehnheitToKelvin(value):
    return round((value + 459.67) * 5.0/9.0,2)

# Convert Kelvin to Farenheit
def convertKelvinToFarhenheiht(value):
    return round(value * 9.0/5.0 - 459.67,2)

# Convert Kelvin to Celcius
def convertKelvinToCelcius(value):
    return round(value - 273.15,2)

    
