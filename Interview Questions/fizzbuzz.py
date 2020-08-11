##Given an input, print all numbers up to and including that input, 
# unless they are divisible by 3, then print "fizz" instead, or if they are divisible by 5, print "buzz". If the number is divisible by both, print "fizzbuzz".


def fizzbuzz(n):
    

# Please do not modify the code below this line.
# When you run your code, you will need to enter 
# an input in the terminal below, where the prompt appears


  for i in range(1,n+1):
    if i % 5 != 0 and i%3 != 0:
      print(i)
    if i % 5 == 0 and i % 3 != 0:
      print("buzz")
    if i % 5 != 0 and i % 3 == 0:
      print("fizz")
    if i % 5 == 0 and i%3 == 0:
      print("fizzbuzz")


test_case = int(input("Please enter an input number:"+"\n"))
fizzbuzz(test_case)


