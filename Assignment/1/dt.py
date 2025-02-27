#  Data Type 1 : String (str)
my_Name : str = "Kashan Malik"
my_Email : str = "kailord.business@gmail.com"

#  Data Type 2 : Integer (int)
my_Age : int = 15
my_RollNumber : int = 450613

#  Data Type 3 : Float (float)
Pi_value : float = 3.14159

#  Data Type 4 : Boolean (bool)
my_Age_is_greater_than_ten : bool = True
my_Age_is_less_than_eighteen : bool = False

#  Data Type 5 : List (list)
my_Hobbies : list = ["Coding", "Reading", "Exercising", "Cooking", "Learning"]

#  Data Type 6 : Tuple (tuple)
my_Address : tuple = ("Karachi", "Sindh")


#  Data Type 7 : Dictionary (dict)
my_Info : dict = {
    "Name": my_Name ,
    "Age": my_Age ,
    "Roll Number": my_RollNumber,
    "Email": my_Email ,
    "Address": my_Address ,
    "Hobbies": my_Hobbies ,
    "Is Age Greater than 10": my_Age_is_greater_than_ten ,
    "Is Age Less than 18": my_Age_is_less_than_eighteen ,
    }

# Accessing and printing the value of a specific keys
print(my_Info["Name"])
print(my_Info["Age"])
print(my_Info["Roll Number"])
print(my_Info["Email"])
print(my_Info["Address"])

# Data Type 8 : Set (set) 
my_set : set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# Data Type 9 : Custom Class (class)
class Person:
    
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def salam(self):
        return f"Assalm-u-Alaikum, my name is {self.name} and my age is {self.age} years old."
    
myself = Person("Kashan", 15)
print(myself.salam())
