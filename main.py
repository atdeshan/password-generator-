import random
numbers = int(input("numbers : "))
letters = int(input('number of characters : '))
symbol = int(input ('number of symbols : '))
print(numbers,letters,symbol)
list_of_symbol = ['!','@','#']
list_of_numbers = ['1','2','3','4','5','6','7','8','9']
list_of_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
passwordList = []
for i in range (numbers):
    passwordList.append(random.choice(list_of_numbers))

for i in range (symbol):
    passwordList.append(random.choice(list_of_symbol))

for i in range (letters):
    passwordList.append(random.choice(list_of_letters))

random.shuffle(passwordList)
print(passwordList)
password = ''
for i in passwordList:
    password += i
print(password)