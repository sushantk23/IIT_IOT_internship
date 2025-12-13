
num = input("Enter a 4-digit number: ")
if len(num) == 4 and num.isdigit():
    reversed_num = num[::-1]
    if num == reversed_num:
        print(num, "is a palindrome.")
    else:
        print(num, "is not a palindrome.")
else:
    print("Error: Please enter a valid 5-digit number.")