print("Enter 'y' for exit.");
string = input("Enter any string to count character: ");
if string == 'y':
    exit();
else:
    char = input("Enter a character to count to count from above string: ");
    val = string.count(char);
    print("Total = ",val);
