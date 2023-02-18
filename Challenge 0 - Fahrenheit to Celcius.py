# You need to define your functions first using the formula in order for them to work.

def convertToFahrenheit(degreesCelsius):
    celsiusConvert = degreesCelsius * (9/5) + 32
    return celsiusConvert

def convertToCelsuis(degreesFahrenheit):
    fahrenheitConvert = (degreesFahrenheit - 32) * 5/9
    return fahrenheitConvert
 
# Note: This code was copied from the exercise section of the document. The assert keyword allows you to test if a condition in your code returns True. 
# If it isn't, the program will raise an assertion error.
assert convertToCelsuis(0) == -17.77777777777778
assert convertToCelsuis(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsuis(convertToFahrenheit(15)) == 15
    
degreesCelsius = int(input("Input degrees Celsius: "))
print(f"Fahrenheit output: {convertToFahrenheit(degreesCelsius)}") # Prints the inputed amount of celsius in fahrenheit.
degreesFahrenheit = int(input("Input degrees Fahrenheit: "))
print(f"Celsius output: {convertToCelsius(degreesFahrenheit)}") # Prints the inputed amount of celsius in fahrenheit. 
