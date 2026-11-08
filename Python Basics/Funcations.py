#function
def greet(name):
    return f"Hello, {name}!"
  
greetings = greet("Mohamed")
print(greetings)

#Passing information to a function
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    
greet("Mohamed", 22)

#positional and named arguments
greet(name="Mohamed", age=22)
greet(age=22, name="Mohamed")

#Default arguments
def car_detail(carname="BMW", caryear=2020):
    print(f"Car Name: {carname}, Car Year: {caryear}")
    
car_detail("Toyota", 2022)
car_detail("Honda")
car_detail(caryear=2021)
car_detail(carname="Ford", caryear=2023)
car_detail(carname="Chevrolet")
car_detail()

#Retrun values
def add_numbers(a, b):
    return a + b    
  
result = add_numbers(5, 10)
print(f"The sum is: {result}")

first_name = "Mohamed"
last_name = "Kani"
print(first_name,"-",last_name)  # This will print the values of the defined variables
print(first_name+"-"+last_name)  # This will concatenate the two strings and print the result
print(first_name,last_name,sep="*")  # This will print the values with a '*' separator

#Return and Doc string

def multiple(a, b):
    """This function takes two numbers and returns their product.
     Args:
         a (int or float): The first number.
         b (int or float): The second number.    
    Returns:
          int or float: The product of the two numbers.
    """
    return a * b
  
result = multiple(5, 2.6)
print(result)

#Passing a list as an argument to a Funcation

def print_list_elements(my_list):
    for element in my_list:
        print(element)
        
print_list_elements([1, 2, 3, 4, 5])

#Passing an Arbitary number of arguments to a function
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
  
result = sum_numbers(1, 2, 3, 4, 5)
print(f"The sum of the numbers is: {result}")
result = sum_numbers(10, 20, 30)
print(f"The sum of the numbers is: {result}")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
  
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics',worked_for='princeton university')
print(user_profile)