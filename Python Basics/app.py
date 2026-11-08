first_program = "hello world"
first_program = first_program.title()
print(first_program)
message = "This is Mohamed kani"
message = message.upper()
print(message)
name = " Mohamed        "
name = name.strip()
name_message = f"My name is {name}"
print(name_message)

#Numbers
age = 25
print(age)
total = age + 5
print(total)
total = age - 5
print(total)
total = age * 5
print(total)
total = age / 5
print(total)

#Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange")
print(fruits) 
fruits.remove("banana")
print(fruits) 
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(len(fruits))
print("banana" in fruits)
fruits.append("banana")
print(fruits.sort())  #sort the list in alphabetical order and returns none.
print(fruits)
fruits.reverse()
print(fruits) 
removedfruit = fruits.pop()
print(f"Removed fruit: {removedfruit}")
print(fruits)
fruits.clear()
print(fruits)

fruits = ["apple", "banana", "cherry"]
print(f"The fruits list has {len(fruits)} items.")
print(f"The first fruit is {fruits[0]} and the last fruit is {fruits[-1]}.")  
print(f"the first fruit is {fruits[0].title()} and the last fruit is {fruits[-1].title()}.")

#sort the list in alphabetical order
ages=[25, 30, 20, 35, 28]
print(f"Original ages: {ages}")
ages.sort()
print(f"Sorted ages: {ages}")

#reverse the list
print(f"Original ages: {ages}")
ages.reverse()
print(f"Reversed ages: {ages}")

#sort the list in descending order
ages.sort(reverse=True)
print(f"Sorted ages in descending order: {ages}")

Items = ["apple", "banana", "cherry", 2 , "date", 4, "elderberry"]
# Items.sort() throws an error because the list contains both strings and integers, which cannot be compared directly. To sort the list, we can convert all items to strings first.
print(f"Before sorting: {Items}")
Items.sort(key=str)
print(f"Sorted Items: {Items}")

#for loop
for fruit in fruits:
    print(fruit.title()) 
    
#Range function
list_of_numbers = list(range(1, 11))
print(list_of_numbers)
list_of_even_numbers = list(range(2, 21, 2))
print(list_of_even_numbers)
list_of_odd_numbers = list(range(1, 21, 2))
print(list_of_odd_numbers)
list_Nums = []
for num in range(1, 11):
    list_Nums.append(num)
print(list_Nums)

#statistic funcations
print(f"Sum of numbers: {sum(list_Nums)}")
print(f"Minimum number: {min(list_Nums)}")
print(f"Maximum number: {max(list_Nums)}")

list_squares = []
for num in range(1,11):
  list_squares.append(num**2)
print(list_squares)
#List comprehension
list_squares.clear()
print(list_squares)
list_squares = [num**2 for num in range(0,10)]
print(list_squares)

#Tuples - Immutable lists
names = ("Alice", "Bob", "Charlie")
try:
    names.pop()  # This will raise an AttributeError because tuples do not have a pop method.
except AttributeError as e:
    print(f"Error: {e}")
    
try:
  names[0] = "David"  # This will raise a TypeError because tuples do not support item assignment.
except TypeError as e:
  print(f"Error: {e}")  
print(names)

for name in names:
    print(name)

#if-else statements
age = 20 
if age >= 18:
  print("You are an adult.")  
else:
  print("You are a minor.")
    
#elif keyword
temperature = 15
if temperature < 0:
  print("It's freezing!")
elif temperature < 10:
  print("It's quite cold.")
elif temperature < 20:
  print("It's mild.")
else:
  print("It's warm.") 

participants = ["Alice", "Bob", "Charlie"]
if "Alice" in participants: 
  print("Alice is participating.")
else:
  print("Alice is not participating.")
  
#AND Logical Operators
age = 25
income = 50000
if age >= 18 and income >= 40000:
  print("You are eligible for the loan.")
else:
  print("You are not eligible for the loan.")
  
#OR Logical Operators
age = 16
if age < 18 or age > 65:
  print("You are not eligible for the program.")  
else:
  print("You are eligible for the program.")
  
activities = ["cycling", "swimming", "museum","picnic"]
group_interest = ["art", "history", "cycling"]

if "museum" in activities and ("art" in group_interest or "history" in group_interest):
  print("The group is interested in visiting the museum.")
elif "cycling" in activities and "cycling" in group_interest:
  print("The group is interested in cycling.")
else:
  print("The group has no specific interests.")
  
# In Python, values can be treated as either truthy or falsy.
# - Falsy values: False, 0, "" (empty string), None, [] (empty list).
# - Truthy values: True, non-zero numbers, non-empty strings, non-empty lists.

print(any(group_interest))  # Returns True if any element in the list is truthy
print(all(group_interest))  # Returns True if all elements in the list are truthy

#check for Inequality
age = 20 
if age != 18:
  print("You are not 18 years old.")
  
#inner-if statements
day="Saturday"
fridge_items = ["milk", "eggs", "bread"]
if day == "Saturday":
    if "milk" in fridge_items and "eggs" in fridge_items:
        print("You can make pancakes.")
    else:
        print("You need to buy milk  for pancakes.")
elif day == "Sunday":
    if "bread" in fridge_items:
        print("You can make French toast.")
    else:
        print("You need to buy bread for French toast.")
else:
    print("It's a weekday. No special breakfast plans.")