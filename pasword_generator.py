import random
print("welcome to your password generator")
chars="qwertyuiopasdfghjklzxcvbnm,./!@#$%^&*()_+}[|?><1234567890"
numbers=input("Amount of pasword to genetate ")
numbers=int(numbers)
lenght=input("Enter your pasword lenght please:")
lenght=int(lenght)
print("\nhere are your password:")
for pwd in range(numbers):
    password=''
    for c in range(lenght):
        password+=random.choice(chars)

    print(password)

