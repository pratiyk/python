choice = int(input('please enter a number: '))
def function(choice):
     for num in range (1, choice):
          if num % 3 == 0 and num % 5 == 0:
               print("fizzbuzz")
          elif num % 3 == 0:
               print("fizz")
          elif num % 5 == 0:
               print("buzz")

function(choice)