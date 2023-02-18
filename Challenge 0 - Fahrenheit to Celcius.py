# You need to define your functions first using the formula in order for them to work.

def convertToFahrenheit(degreesCelcius):
    celciusConvert = degreesCelcius * (9/5) + 32
    return celciusConvert


def convertToCelcuis(degreesFahrenheit):
    fahrenheitConvert = (degreesFahrenheit - 32) * 5/9
    return fahrenheitConvert
 
# Note: This code was copied from the exercise section of the document. The assert keyword allows you to test if a condition in your code returns True. 
# If it isn't, the program will raise an assertion error.
assert convertToCelcuis(0) == -17.77777777777778
assert convertToCelcuis(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelcuis(convertToFahrenheit(15)) == 15
    
degreesCelcius = int(input("Celcuis: "))
print(f"Fahrenheit output: {convertToFahrenheit(degreesCelcius)}") # Prints the inputed amount of celcius in fahrenheit.
degreesFahrenheit = int(input("Fahrenheit: "))
print(f"Celcuis output: {convertToCelcuis(degreesFahrenheit)}") # Prints the inputed amount of celcius in fahrenheit. 
