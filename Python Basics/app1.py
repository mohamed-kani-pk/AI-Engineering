#Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values.  
personDetails = {
  "first_name": "John", "last_name": "Doe",
  "age": 30, "city": "New York"}
print(personDetails)
print(personDetails["first_name"])
print(personDetails["last_name"])
print(personDetails.get("age"))
print(personDetails.get("city"))
print(personDetails.keys())
print(personDetails.values())
print(personDetails.items())
print(f"The full name is {personDetails['first_name']} {personDetails['last_name']}.")
print(personDetails.get("age1"))
print(personDetails.get("Age", "Age not found"))  #returns the value of the key if it exists, otherwise returns the default value.

personDetails["age"] = 31
print(personDetails)
personDetails["country"] = "USA"
print(personDetails)
personDetails["email"] = "johdoe@gmail.com"
print(personDetails)
personDetails.pop("city")
print(personDetails) 
personDetails.pop("country") 
print(personDetails) 
personDetails["country"] = "USA"
print(personDetails)
personDetails.popitem()  #removes the last inserted item
print(personDetails)
del personDetails["email"] #removes the specified item
print(personDetails)
# del personDetails  #removes the entire dictionary
# print(personDetails)  #this will raise an error because the dictionary no longer exists.
#personDetails.clear()  #removes all the items from the dictionary
#print(personDetails)  #this will print an empty dictionary.

for Key in personDetails:
    print(Key)  #prints the keys of the dictionary
    
for value in personDetails.values():
    print(value)  #prints the values of the dictionary
  
for key,value in personDetails.items():
    print(f"{key} -> {value}")  #prints the keys and values of the dictionary
    
family = {
  "mom" : {"name": "Tina", "age": 50},
  "dad" : {"name": "John", "age": 55},
  "son" : {"name": "Mike", "age": 20}
}

for member, details in family.items():
    print(f"{member} -> Name: {details['name']}, Age: {details['age']}")  #prints the keys and values of the dictionary
    
speakers = {
  "Alice" : {"topic": "Python Programming", "time": "10:00 AM"},
  "Bob" : {"topic": "Data Science", "time": "11:00 AM"},
  "Charlie" : {"topic": "Machine Learning", "time": "12:00 PM"} 
}
for speaker, details in speakers.items():
  print(f"{speaker} will be speaking on ")
  for detail in details:
    print(f"{detail}: {details[detail]}")  #prints the keys and values of the nested dictionary     
    
#User input
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!") 
age = int(input("Enter your age: "))
if age >= 18:
  print("You are an adult.")   
else:
  print("You are a minor.")
  
counter = 1;
while counter <= 5:
  print(f"Counter: {counter}")
  counter += 1

ingredients = ["flour", "sugar", "eggs", "milk","flour", "butter", "flour"]
counter = 0
while "flour" in ingredients:
  counter += 1
  ingredients.remove("flour")
  
print(f"Removed 'flour' {counter} times. Remaining ingredients: {ingredients}")

ingredients = ["flour", "sugar", "eggs", "milk", "flour", "butter", "flour"]

counter = 0

while "flour" in ingredients or "sugar" in ingredients:
    if "flour" in ingredients:
        ingredients.remove("flour")
    elif "sugar" in ingredients:
        ingredients.remove("sugar")
    counter += 1

print(counter)
print(ingredients)