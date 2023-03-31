userName = input("Please enter your name: ")
userAge = input("Please enter your age: ")
userGender = input("Please enter your gender: ")

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = int(age)
        self.gender = gender
    def fly(self):
        print(f'{self.name} is flyings')

user1 = User(userName, userAge, userGender)
print(user1.age)
user1.fly()