import conversions_refactored
import unittest

# class to store data for the conversion test items
class testUnit:

    def __init__(self, fromUnit, toUnit, value, convertedValue):
        self.fromUnit = fromUnit
        self.toUnit = toUnit
        self.value = value
        self.convertedValue = convertedValue


class testConversions(unittest.TestCase):

    # Known calculations to run test 
    knownCalculations = (testUnit('celcius', 'farenheit',500.00,932.00),
                         testUnit('celcius', 'farenheit',490.00,914.00),
                         testUnit('celcius', 'farenheit',480.00,896.00),
                         testUnit('celcius', 'farenheit',470.00,878.00),
                         testUnit('celcius', 'farenheit',460.00,860.00),
                         testUnit('farenheit', 'kelvin',932.00,773.15),
                         testUnit('farenheit', 'kelvin',914.00,763.15),
                         testUnit('farenheit', 'kelvin',896.00,753.15),
                         testUnit('farenheit', 'kelvin',878.00,743.15),
                         testUnit('farenheit', 'kelvin',860.00,733.15),
                         testUnit('celcius', 'kelvin',500.00,773.15),
                         testUnit('celcius', 'kelvin',490.00,763.15),
                         testUnit('celcius', 'kelvin',480.00,753.15),
                         testUnit('celcius', 'kelvin',470.00,743.15),
                         testUnit('celcius', 'kelvin',460.00,733.15),
                         testUnit('mile', 'yard',1.00,1760.00),
                         testUnit('mile', 'yard',2.00,3520.00),
                         testUnit('mile', 'yard',3.00,5280.00),
                         testUnit('mile', 'yard',4.00,7040.00),
                         testUnit('mile', 'yard',27.00,47520.00),
                         testUnit('mile', 'meter',1.00,1609.35),
                         testUnit('mile', 'meter',2.00,3218.69),
                         testUnit('mile', 'meter',3.00,4828.04),
                         testUnit('mile', 'meter',4.00,6437.39),
                         testUnit('mile', 'meter',27.00,43452.37),
                         testUnit('meter', 'yard',1.00,1.09),
                         testUnit('meter', 'yard',2.00,2.19),
                         testUnit('meter', 'yard',3.00,3.28),
                         testUnit('meter', 'yard',4.00,4.37),
                         testUnit('meter', 'yard',27.00,29.53)
                         )
        

    def test_conversions(self):
        # Convert 1 direction
        for x in self.knownCalculations:
            # run convertsion passing correct values to fuction
            result = conversions_refactored.convert(x.fromUnit, x.toUnit, x.value)
            # check result
            self.assertEqual(result, x.convertedValue)
            # print what was tested
            print 'Testing '  + str(x.value) + ' ' + x.fromUnit + ' converts to ' + str(x.convertedValue) + ' ' + x.toUnit +'.'
        #Convert Opposite Direction        
        for x in self.knownCalculations:
            # run convertsion passing correct values to fuction
            result = conversions_refactored.convert(x.toUnit, x.fromUnit, x.convertedValue)
            # check result
            self.assertEqual(result, x.value)
            # print what was tested
            print 'Testing '  + str(x.convertedValue) + ' ' + x.toUnit + ' converts to ' + str(x.value) + ' ' + x.fromUnit +'.'
           
        
if __name__ == '__main__':
    unittest.main()
    

