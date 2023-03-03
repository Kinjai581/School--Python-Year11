def FizzBuzz(int): # Using a function so that the code is only run when it is called.
  if int%3 == 0 and int%5 == 0: # if the number is divisible by both 3 and 5, print 'FizzBuzz'
    print('Output: Fizzbuzz')
  elif int%3 == 0: # if the number is divisible by  only 3, print 'Fizz'
      print('Output: Fizz')
  elif int%5 == 0: # if the number is divisible by only 5, print 'Buzz'
      print('Output: Buzz')
  else: # Otherwise, if the number is divisible by neither 3 or 5, output the number
      print(f"Output: {int}")
      
# Input
FizzBuzz(int(input('Input: ')))
