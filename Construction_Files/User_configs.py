'''Contains the user class
Represents a customer in the banking system.
'''
class User:
    def __init__(self, name: str, account_number:int , age:int , gender:str):
        self._name = name
        self._account_number = int(account_number)
        self._age = age
        self.gender = gender

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be string")

        if not isinstance(account_number, int) :
            raise ValueError("Account number must be a number value")

        if not isinstance(age, int):
            raise ValueError("Age must be in number value")

        if gender not in ["M", "F"]:
            raise ValueError("Gender must be M for Male and F for Female")

    def show_details(self):
        print("-------------------------------------")
        print("Name of the customer is:", self._name)
        print("Account number:", self._account_number)
        print("Age of the customer is:", self._age)
        gender_dict = {"M": "Male", "F": "Female"}
        print(f"Gender :{gender_dict.get(self.gender,"Invalid gender detail given")}")

mohiz = User("ab",12,23,"M")
mohiz.show_details()
