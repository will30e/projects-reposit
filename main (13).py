# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE

print ("Select an operation")
print ("1. ADD")
print ("2. SUBTRACT")
print ("3. MULTIPLY")
print ("4. DIVIDE")

operation = input()

if operation == "1":
  numb1 = input ("Enter the first number: ")
  numb2 = input ("Enter the second number: ")
  print ("The sum is " + str(int(numb1) + int(numb2)))
elif operation == "2":
  numb1 = input ("Enter the first number: ")
  numb2 = input ("Enter the second number: ")
  print ("The difference is " + str(int(numb1) - int(numb2)))

elif operation == "3":
  numb1 = input ("Enter the first number: ")
  numb2 = input ("Enter the second number: ")
  print ("The product is " + str(int(numb1) * int(numb2)))

elif operation == "4":
  numb1 = input ("Enter the first number: ")
  numb2 = input ("Enter the second number: ")
  print ("The result is " + str(int(numb1) / int(numb2)))

else:
  print ("Invalid Entry")