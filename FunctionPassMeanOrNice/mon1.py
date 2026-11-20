
# Python 3.15.2

# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function_name(variable) means that we pass in the variable.
#           return variable means that we are returning the variable to
#           back to the calling function.



def start():
    # print(f"Hello, {get_name()}")
    f_name = "Sarah"
    l_name = "Connor"
    age = get_number()
    gender = "Female"
    get_info(f_name, l_name, age, gender)





def get_number():
    number = 28
    return number


def get_info(f_name, l_name, age, gender):
    print(f"My name is {f_name} {l_name}, my age is {age}, gender {gender}")
    
    
    
    
    # name = input("Enter your name: ")
    # return name 





if __name__ == "__main__":
    start()