"""
36 - Encapsulation
"""

# -----------------------------
# Example 1 - Public Member
# -----------------------------
class Student :
    def __init__(self,name):
        self.name = name

student =Student("ali")
print(student.name)

# -----------------------------
# Example 2 - Protected Member
# -----------------------------

class Student:
    def __init__(self,age):
        self._age = age
student = Student()
print(student._age)

# -----------------------------
# Example 3 - Private Member
# -----------------------------

class User:
    def __init__(self,password):
        self.__password = "1234"
user = User()
# print(user.__password)  # AttributeError
print(user._User__password)


# -----------------------------
# Example 4 - Private + Property
# -----------------------------

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance


account = BankAccount(10000)

print(account.balance)

# -----------------------------
# Example 5 - Name Mangling
# -----------------------------

class Demo:

    def __init__(self):
        self.__secret = "Python"


demo = Demo()

print(dir(demo))