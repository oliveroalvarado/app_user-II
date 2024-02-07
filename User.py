# '''
# create an app that will add a user
# ask for name, last name, age, location, dob
# give the user the ability to create a post
# '''
class Info:
    user_input = ""

    def __init__(self, name=None, last_name=None, age=None, location=None):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.location = location

# create and application interface for user to input
    def user_interface(self):
        print("Welcome to MyStory")
        print("NEW USER")
        print("RETURNING USER")

        choice = (self.get_user_input()).upper()
        self.user_choice(choice)
# receive user input
    def get_user_input(self):
        return input("Please choose one: ")

    def user_choice(self, choice):
        if choice == "NEW USER":
            self.name = input("First Name: ")
            self.last_name = input("Last Name: ")
            self.age = input("Age: ")
            self.location = input("Location: ")
            print("Welcome to MyStory")
            Info.user_input = input("Tell my Story: ")
            self.what_you_wrote()

        elif choice == "RETURNING USER":
            input("Welcome Back: ")
            print("Sorry we don't want you here")
            print("GOODBYE")
        
        else:
            print("Invalid")
        
    def what_you_wrote(self):
        print(f"You are {self.name} {self.last_name}, {self.age} years old, from {self.location}, and")
        print("Your story is: ", Info.user_input)

Info().user_interface()
# Info().what_you_wrote()

