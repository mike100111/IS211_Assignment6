import conversions
import unittest

class testConversions(unittest.TestCase):
    
    celToFaKnown = ((500.00,932.00),(490.00,914.00),(480.00,896.00),(470.00,878.00),(460.00,860.00))
    celToKelKnown = ((500.00,773.15), (490.00,763.15),(480.00,753.15),(470.00,743.15), (460.00,733.15))
    farToKelvin= ((932.00,773.15), (914.00,763.15),(896.00,753.15),(878.00,743.15),(860.00,733.15))

    def test_convertCelsiusToFahrenheit(self):    
        for x in self.celToFaKnown:
            result = conversions.convertCelsiusToFahrenheit(x[0])
            self.assertEqual(result, x[1])
            print 'Testing Celcius ' + str(x[0]) + ' converts to ' + str(x[1]) + ' Farenheiht.'

    def test_convertCelsiusToKelvin(self):    
        for x in self.celToKelKnown:
            result = conversions.convertCelsiusToKelvin(x[0])
            self.assertEqual(result, x[1])
            print 'Testing Celcius ' + str(x[0]) + ' converts to ' + str(x[1]) + ' Kelvin.'

    def test_convertFahrenheitToCelcius(self):    
        for x in self.celToFaKnown:
            result = conversions.convertFahrenheitToCelcius(x[1])
            self.assertEqual(result, x[0])
            print 'Testing Farenheiht ' + str(x[1]) + ' converts to ' + str(x[0]) + ' Celcius.'

    def test_convertFarehnheitToKelvin(self):    
        for x in self.farToKelvin:
            result = conversions.convertFarehnheitToKelvin(x[0])
            self.assertEqual(result, x[1])
            print 'Testing Farenheiht ' + str(x[0]) + ' converts to ' + str(x[1]) + ' Kelvin.'

    def test_convertKelvinToFarhenheiht(self):    
        for x in self.farToKelvin:
            result = conversions.convertKelvinToFarhenheiht(x[1])
            self.assertEqual(result, x[0])
            print 'Testing Kelvin ' + str(x[1]) + ' converts to ' + str(x[0]) + ' Farenheiht.'            

    def test_convertKelvinToCelcius(self):    
        for x in self.celToKelKnown:
            result = conversions.convertKelvinToCelcius(x[1])
            self.assertEqual(result, x[0])
            print 'Testing Kelvin ' + str(x[1]) + ' converts to ' + str(x[0]) + ' Celcius.'

            
        
if __name__ == '__main__':
    unittest.main()
    

