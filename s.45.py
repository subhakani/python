print("Enter 'x' for exit.");
print("Enter any two numbers: ");
num1 = input();
if num1 == 'x':
    exit();
else:
    num2 = input();
    number1 = int(num1);
    number2 = int(num2);
    count = 0;
    if number1 > number2:
    	largest = number1;
    	count = 1;
    elif number1 < number2:
    	largest = number2;
    	count = 1;
    else:
        print("\nBoth the numbers are equal to each other.");
    if count == 1:
        print("\nLargest of the given two numbers is", largest);

