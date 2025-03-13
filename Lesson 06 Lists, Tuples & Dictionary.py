
##1}. Lists in Python
fruits: list[str] = ["apple", "banana", "cherry"]
numbers: list[int] = [10, 20, 30, 40]
mixed: list[object] = ["hello", 42, 3.14, True]

# Accessing elements
print(fruits[0])  # Output: apple
print(numbers[2])  # Output: 30
print(mixed[1])   # Output: 42

##2}. Accessing List Elements
fruits: list = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: apple
print(fruits[-3])  # Output: apple, accessing element in reverse order
# Yahan fruits[0] ka matlab hai list ka pehla element, jo "apple" hai.
# fruits[-3] ka matlab hai list ka pehla element, jo "apple" hai.
# Python mein negative indexing ka matlab hota hai list ko right se access karna.

##3}. Adding Elements to a List
fruits: list = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
# .append() ek method hai jo kisi list ke end mein naya element add karta hai.

##4}. Removing Elements from a List
fruits: list = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']
# .remove() ek method hai jo kisi list se specific element ko remove karta hai.

##5}. Removing Elements from a List by Index
fruits: list = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry']
# .pop() ek method hai jo kisi list se specific index par element ko remove karta hai.

##6}. Modifying Lists
fruits: list = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']
# Yahan fruits[1] ka matlab hai list ka 2nd element, jo "banana" hai.
# 2nd element ko "orange" se replace kardiya hai.

##7}. List Slicing
fruits: list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])  # Output: ['cherry', 'orange', 'kiwi']
# Yahan fruits[2:5] ka matlab hai list ka 3rd element se 5th element tak.
# 3rd element include hota hai aur 5th element exclude hota hai.

# Start index: 2 → "cherry" se slicing start hogi ✅
# End index: 5 → "melon" exclude ho jayega ❌
# (Matlab sirf index 2, 3, aur 4 tak milega)
# Final output: ['cherry', 'orange', 'kiwi']

# Diagram Understanding:
# 📌 fruits[2:5] ka matlab:
# 🔢 "cherry" (Index 2) → ✅ Include
# 🔢 "orange" (Index 3) → ✅ Include
# 🔢 "kiwi" (Index 4) → ✅ Include
# 🚫 "melon" (Index 5) → ❌ Exclude


##8}. Common List Methods
fruits: list = ["apple", "banana", "cherry"]
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']
# .sort() ek method hai jo kisi list ko sort karta hai.

# Sorting a List
# 1. Default Sorting (Ascending Order)
numbers: list[int] = [3, 1, 4, 1, 5, 9] # unsorted list
numbers.sort()
print(numbers)  # Output: [1, 1, 3, 4, 5, 9]

# 2. Sorting in Descending Order (reverse=True)
numbers: list[int] = [3, 1, 4, 1, 5, 9] # unsorted list
numbers.sort(reverse=True)
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]

# 3. Sorting Strings
fruits: list[str] = ["apple", "banana", "cherry"]

# 3. Sorting by String Length (key=len)
words = ["cat", "elephant", "dog", "tiger", "lion"]  
sorted_words = sorted(words, key=len)  
print(sorted_words)  # Output: ['cat', 'dog', 'lion', 'tiger', 'elephant']
# sorted() function words ko chhoti length se badi length tak arrange kar raha hai.
# cat (3 letters) sabse chhota hai, isliye pehle aayega.
# dog (3 letters) bhi same hai toh alphabetical order me aayega.
# lion (4 letters) uske baad.
# elephant (sabse lamba word) last me chala gaya.

# 4. Sorting by Last Character (key=lambda word: word[-1])
# Agar bari se chhoti length ke mutabiq sort karna ho toh reverse=True ka use karte hain:
sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)  # Output: ['elephant', 'tiger', 'lion', 'dog', 'cat']
# Ab sabse lamba word pehle aayega aur chhota word last me.✨       


##9. Reverse Sorting
numbers: list[int] = [3, 1, 4, 1, 5, 9]
numbers.reverse()
print(numbers)  # Output: [9, 5, 4, 3, 1, 1]
# reverse() method numbers list ko reverse karta hai.
# 9 se start hua hai aur 1 se end ho jayega.


##10. Iterating Over Lists
# 1. Using for loop
colors: list[str] = ["pink", "red", "green"]
for color in colors:
    print(color)
# Output: pink
# red
# green

##11. Tuples in Python
tuple1: tuple = tuple(["apple", "banana", "cherry"]) # cast a list into tuple
tuple2: tuple = (10, 20, 30) # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True) # tuple

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)

# tuple1      = ('apple', 'banana', 'cherry')
# tuple2      = (10, 20, 30)
# mixed_tuple = ('hello', 42, 3.14, True)


##12. Creating Tuples
tuple1: tuple = tuple(["apple", "banana", "cherry"]) # cast a list into tuple
tuple2: tuple = (10, 20, 30) # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True) # tuple


##13. Accessing Elements
tuple1: tuple = ("apple", "banana", "cherry")
print(tuple1[0])  # Output: apple
print(tuple1[-1])  # Output: cherry


##14. Creating a Dictionary
# 1. Using curly braces {}
person: dict[str, str] = {"name": "John", "age": "25", "city": "New York"}

# 2. Using dict() constructor
person: dict[str, str] = dict({"name": "John", "age": "25", "city": "New York"})

##15. Accessing Dictionary Elements
person: dict[str, str] = {"name": "John", "age": "25", "city": "New York"}
print(person["name"])  # Output: John
print(person["age"])   # Output: 25
print(person["city"])  # Output: New York


# Syntax: {key: value, key: value, ...}
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Dictionary:", my_dict)
# Output: Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}

##16. Accessing Values
print("Name:", my_dict["name"])  # Access value using key
print("Age:", my_dict.get("age"))  # Using .get() method
# Name: Alice # Age: 25


##17. Adding and Updating Dictionary Elements
my_dict["email"] = "nanum@example.com"  # Adding new key-value pair
my_dict["age"] = 26  # Updating existing value
print("Updated Dictionary:", my_dict)

# Output: Updated Dictionary: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
# 🔹 "email" key add ho gayi.
# 🔹 "age" ka value update ho gaya (25 → 26).


##18. Removing Elements
my_dict.pop("age")  # Removing key-value pair using key
print("Updated Dictionary:", my_dict)

# Output: Updated Dictionary: {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}


##19. Iterating Over Dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Output: name: Alice
# city: New York
# email: nanum@example.com


##20. Deleting Items
# my_dict.pop("age")  # Removing key-value pair using key
# print("Updated Dictionary:", my_dict)

# Output: Updated Dictionary: {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}


##21. Dictionary Methods
# Python mein dictionary ek aisi data structure hoti hai jo key-value pairs store karti hai. 
# Matlab har key ka ek value hota hai.

# 1. .keys()
# 2. .values()
# 3. .items()
# 4. .get()
# 🔥 Example Dictionary
student = {
    "name": "Ali😎",
    "age": 20,
    "city": "Karachi🌇"
}
# Yahan "name", "age", aur "city" keys hain, aur inki values hain "Ali", 20, aur "Karachi".
# 1️⃣ Data Ko Access Karna
print(student.get("name"))  # Output: Ali
print(student.get("gender", "Not Found"))  # Output: Not Found
# keys()
print(student.keys())  
# values()
print(student.values())  
# Output: dict_values(['Ali', 20, 'Karachi'])
# items()
print(student.items())  
# Output: dict_items([('name', 'Ali'), ('age', 20), ('city', 'Karachi')])


# 2️⃣ Data Add Ya Update    
student.update({"age": 21, "gender": "female"})
print(student)  
# Output: {'name': 'Ali', 'age': 21, 'city': 'Karachi', 'gender': 'female'}

# setdefault()
student.setdefault("country", "Pakistan🤍💚")
print(student)
# Output: {'name': 'Ali', 'age': 21, 'city': 'Karachi', 'gender': 'Male', 'country': 'Pakistan'}

# 3️⃣ Data Remove
student.pop("age")
print(student)
# Output: {'name': 'Ali', 'city': 'Karachi', 'gender': 'Male', 'country': 'Pakistan'}

# popitem()
# Aakhri key-value pair delete karta hai
last_item = student.popitem()
print(last_item)  # Output: ('country', 'Pakistan')
print(student)


# clear()
# Puri Dictionary ko clear karta hai
student.clear()
print(student)
# Output: {}

# copy()
# Dictionary ko copy karta hai
student_copy = student.copy()
print(student_copy)
# Output: {'name': 'Ali', 'city': 'Karachi', 'gender': 'Male', 'country': 'Pakistan'}

# fromkeys()
# Dictionary ko create karta hai
# Ek naya dictionary banata hai jo sab keys ko ek same value assign kar deta hai:

keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "Unknown")
print(default_dict)  
# Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}


##22. Duplicate Key Not Allowed
# Dictionary mein duplicate keys nahi allowed hain.
# Agar same key ko do baar use karte hain toh pehle wala value replace ho jata hai.

# 🛑Example:
student = {
    "name": "Ali",
    "age": 20,
    "city": "Karachi",
    "age": 25  # Duplicate key
}

print(student)
# Output: {'name': 'Ali', 'age': 25, 'city': 'Karachi'}

##23. Multiple Values Store Karni Hon
# Dictionary mein multiple values store karne ke liye list, tuple, ya set ka use karte hain.

# 🛑Example:
student = {
    "name": "Ali",
    "age": [20, 25],  # Multiple values stored as list
    "city": "Karachi"
}

print(student)
# Output: {'name': 'Ali', 'age': [20, 25], 'city': 'Karachi'}

