'''Contains the user class
Represents a customer in the banking system.
'''
class User:
    def __init__(self, name, account_number, age, gender):
        self.name = name
        self.account_number = int(account_number)
        self.age = age
        self.gender = gender

    def show_details(self):
        print("-------------------------------------")
        print("Name of the customer is:", self.name)
        print("Account number:", self.account_number)
        print("Age of the customer is:", self.age)
        if self.gender == "M":
            print("Gender: Male")
        elif self.gender == "F":
            print("Gender: Female")
        else:
            print("Invalid gender detail given")

mohiz = User("ab",12,23,"M")
mohiz.show_details()