num = input("Enter a word or a number to test for palindrome or 'exit' ")

for i in num:
    if num == "exit":
        break
    elif num == "EXIT":
        break
    elif num.lower() == num[::-1].lower():
        print(num," is a palindrome!")
        break
    else:
        print(num, " is not a palindrome.")
        break

