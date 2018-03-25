# custom error class
class ConversionNotPossible(Exception):
    pass

formulas = {('celcius', 'kelvin'): ('value + 273.15'),
            ('celcius', 'farenheit'): ('value * 9.0/5.0 + 32.0'),
            ('farenheit', 'celcius'): ('(value - 32) * 5.0/9.0'),
            ('farenheit','kelvin'):('(value + 459.67) * 5.0/9.0'),
            ('kelvin','farenheit'):('value * 9.0/5.0 - 459.67'),
            ('kelvin','celcius'):('value - 273.15'),
            ('mile','yard'):('value * 1760.00'),
            ('mile','meter'):('value / 0.00062137'),
            ('yard','mile'):('value / 1760.00'),
            ('yard','meter'):('value / 1.0936'),
            ('meter','mile'):('value * 0.00062137'),
            ('meter','yard'):('value * 1.0936')}

def convert(fromUnit, toUnit, value):
    # Check if units are in dictionary to see if the types are a valid converstion
    if (fromUnit, toUnit) in formulas:
        # Convert and return
        return round(eval(formulas[(fromUnit, toUnit)]), 2)
    else:
        # Raise exception
        raise ConversionNotPossible
