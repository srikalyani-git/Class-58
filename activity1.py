num = input("Enter your number:")
state = ""
for i in range(len(num)):
    if num[i] == num[-(1+i)]:
        state = "True"
    else:
        state = "False"

if state == "True":
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")
