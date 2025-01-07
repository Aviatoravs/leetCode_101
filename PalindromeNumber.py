x = int(input("Enter a Number to check if it is palindrome or not : "))
temp = abs(x)
rev = 0
while(temp > 0):
    temp0 = temp%10
    rev = rev*10 + temp0
    temp = temp//10
if(rev == abs(x)):
    print("This Number is palindrome")
