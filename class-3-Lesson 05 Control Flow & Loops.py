# Lesson 05: Control Flow & Loops

#!} Comparison Operators

# == Equal
# != Not Equal
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to


# Taking user input for two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Performing comparisons
print(f"{x} == {y} ->", x == y)   # Equality check
print(f"{x} != {y} ->", x != y)   # Not equal check
print(f"{x} > {y}  ->", x > y)    # Greater than check
print(f"{x} < {y}  ->", x < y)    # Less than check
print(f"{x} >= {y} ->", x >= y)   # Greater than or equal check
print(f"{x} <= {y} ->", x <= y)   # Less than or equal check


# Step 1: User Se Input Lena
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
#1) input() function user se value lene ke liye use hota hai.
#2) int() function is input ko integer (number) me convert karta hai.

#Example:
# Enter first number: 10
# Enter second number: 20
#Ab x = 10 aur y = 20 ho gaya.

#Step 2: Comparison Operators Ka Use
#Ab hum dono numbers ko compare karenge.

# 1️⃣ Equality Check gye (==)
print(f"{x} == {y} ->", x == y)

#Yeh check karega ki x aur y barabar hain ya nahi.
#Agar dono same hain toh True, warna False.
#Example:
#10 == 20 -> False

#2️⃣ Not Equal (!=)
print(f"{x} != {y} ->", x != y)

#Yeh check karega ki x aur y alag hain ya nahi.
#Agar alag hain toh True, warna False.
#Example:
#10 != 20 -> True

#3️⃣ Greater Than (>)
print(f"{x} > {y}  ->", x > y)

#Yeh check karega ki x greater than y hain ya nahi.
#Agar x greater than y hain toh True, warna False.
#Example:
#10 > 20 -> False

#4️⃣ Less Than (<)
print(f"{x} < {y}  ->", x < y)

#Yeh check karega ki x, y se chhota hai ya nahi.
#Example:
#   10 < 20 -> True

#5️⃣ Greater Than or Equal to (>=)
print(f"{x} >= {y} ->", x >= y)

#Yeh check karega ki x, y ke barabar ya bada hai.

#Example:
#10 >= 20 -> False

#6️⃣ Less Than or Equal to (<=)
print(f"{x} <= {y} ->", x <= y)

#Yeh check karega ki x, y ke barabar ya chhota hai. 

#Example:
#10 <= 20 -> True

#Final Output Example
#Agar user input kare:

#Enter first number: 10  
#Enter second number: 20

# 10 == 20 -> False
# 10 != 20 -> True
# 10 > 20  -> False
# 10 < 20  -> True
# 10 >= 20 -> False
# 10 <= 20 -> True


# Agar user input kare:
#Enter first number: 50  
#Enter second number: 50

# 50 == 50 -> True
# 50 != 50 -> False
# 50 > 50  -> False
# 50 < 50  -> False
# 50 >= 50 -> True
# 50 <= 50 -> True


##2} (Logical Operators)

# and
# or
# not

age: int = 25
is_student: bool = True

# Check if age is greater than 18 AND is_student is True
if age > 18 and is_student:
    print("You are eligible for a student discount.")

    #Step 1: User Se Input Lena
    age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"

# 🔹 input() → User se age aur student status lene ke liye hai.
# 🔹 int(input("Enter your age: ")) → Yeh user ka age input integer me convert karega.
# 🔹 input("Are you a student? (yes/no): ") → Yeh user se poochta hai ki woh student hai ya nahi.
# 🔹 .strip().lower() → Yeh input ko clean karta hai (taake " Yes " ya "YES" bhi "yes" ban jaye).
# 🔹 == "yes" → Agar user "yes" likhe, to is_student = True, warna False.

# ✅ Example:
# Enter your age: 25
# Are you a student? (yes/no): Yes

# 💡 age = 25, is_student = True


#Step 2: (❁´◡`❁)📚Student Discount Check
discount_message = "You are eligible for a student discount." if age > 18 and is_student else "No student discount available."
print(discount_message)
# 🔹 if age > 18 and is_student → Check karta hai ki:

# age 18 se zyada ho AND
# is_student True ho.
# 🔹 Ternary Operator (if-else short form) → Yeh ek hi line me condition check karne ka tareeka hai.
# ✅ Example Output:

# You are eligible for a student discount.
#(Agar age = 25 aur is_student = True ho)


#Step 3: (❁´◡`❁)🎁Special Discount Check
if age in range(0, 12) or age > 60:
    print("You qualify for a special discount.")

#🔹 range(0, 12) → Yeh check karta hai ki age 0 se 11 ke beech hai ya nahi.
#🔹 or age > 60 → Agar age 60 se zyada hai to bhi discount milega.

#✅ Example:
#Agar age = 5 ho to output hoga:

#You qualify for a special discount.


#Step 4: (❁´◡`❁)🎁Student 📙Na Hone Ka Check
if not is_student:
    print("You are not a student.")
#🔹 not is_student → Yeh check karega agar is_student = False ho.
#🔹 Agar user student nahi hai, tabhi yeh print hoga.

#✅ Example Output:
#You are not a student.

#Full Example Run🎲
#Enter your age: 25
#Are you a student? (yes/no): Yes

#You are eligible for a student discount.

#(●'◡'●)
#Enter your age: 10
#Are you a student? (yes/no): no

#You qualify for a special discount.
#You are not a student.

#😊🚀Summary (Jo Important Hai)
#✔️ User se age aur student status le raha hai
#✔️ Agar age > 18 aur student ho, to student discount de raha hai
#✔️ Agar age < 12 ya > 60 ho, to special discount de raha hai
#✔️ Agar student nahi ho, to message print ho raha hai

# User input for age and student status
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"

# Check if eligible for a student discount
discount_message = "You are eligible for a student discount." if age > 18 and is_student else "No student discount available."
print(discount_message)

# Check for special discount eligibility
if age in range(0, 12) or age > 60:
    print("You qualify for a special discount.")

# Check if the person is NOT a student
if not is_student:
    print("You are not a student.")


##3} The if Statement📜

num: int = 10

if num > 0:
    print("The number is positive.")

# num = 10 → Yeh variable num ko 10 set kar raha hai.
# if num > 0: → Yeh check kar raha hai ke num zero se bada hai ya nahi.
# Agar True ho, to print karega: "The number is positive."
# Agar False hota (jaise num = -5 hota), to kuch print nahi hota.

#Alternative 1: User Se Input Lena🧸
num = int(input("Enter a number: "))  # User se number input le raha hai

if num > 0:
    print(f"{num} is a positive number.")  # Output me number dikhayega
# 🔹 Yeh fixed value (10) ki jagah user se number maang raha hai.
# 🔹 f"{num}" ka matlab hai ke output me actual number bhi dikhega.

# ✅ Example Run:
# Enter a number: 5
# 5 is a positive number.

##4} The else Statement🚫

num: int = 10

if num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# num = 10 → Yeh variable num ko 10 set kar raha hai.
# if num > 0: → Yeh check kar raha hai ke num zero se bada hai ya nahi.
# Agar True ho, to print karega: "The number is positive."
# Agar False ho, to print karega: "The number is negative."


##5} The elif Statement🚫

num: int = 10

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# num = 10 → Yeh variable num ko 10 set kar raha hai.
# if num > 0: → Yeh check kar raha hai ke num zero se bada hai ya nahi.
# Agar True ho, to print karega: "The number is positive."
# elif num < 0: → Yeh check kar raha hai ke num zero se chhota hai ya nahi.
# Agar True ho, to print karega: "The number is negative."
# else: → Agar dono conditions false ho, to print karega: "The number is zero."


##6} Nested if Statements🚫

num: int = 10

if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is negative.")

# num = 10 → Yeh variable num ko 10 set kar raha hai.
# if num > 0: → Yeh check kar raha hai ke num zero se bada hai ya nahi. 
# Agar True ho, to print karega: "The number is positive."
# Agar False ho, to kuch print nahi hota.   



##7} Practical Examples
#Example 1: Simple Calculator📱

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Performing calculation based on user input
if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:  # Checking for division by zero
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operation! Please enter +, -, *, or /📱")


#Example 2: Age Verification🚗 for Driving License

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for a driving license. 🚗")
elif age > 0:
    print("You are too young to get a driving license. ❌")
else:
    print("Invalid age entered. Please enter a valid number.")




#Example 3: 🚦Traffic Light System
light = input("Enter traffic light color (red/yellow/green): ").strip().lower()

if light == "red":
    print("Stop! 🚦")
elif light == "yellow":
    print("Slow down! ⚠️")
elif light == "green":
    print("Go! ✅")
else:
    print("Invalid input. ❌")


##8} For Loop

#For loop is used to iterate over a sequence (like a list, tuple, string, etc.)

#Syntax:
#for variable in sequence:
#    body of the loop


# 🔹 Alternative 1: Using While Loop
fruits = ["apple", "banana", "cherry"]
index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1


# 🔹 Alternative 2: Using List Comprehension
fruits = ["apple", "banana", "cherry"]
[print(fruit) for fruit in fruits]
#Loop ek hi line me likha hai (List comprehension).

# 🔹 Alternative 3: Checking Membership (in / not in)
fruits = ["apple", "banana", "cherry"]

# Checking if 'banana' is in the list
if "banana" in fruits:
    print("Banana is in the list. ✅")

# Checking if 'grape' is NOT in the list
if "grape" not in fruits:
    print("Grape is NOT in the list. ❌")


# 🔹 Alternative 4: Using enumerate() (Index + Value Together)
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Index ke sath fruit name bhi print hoga.


# 🔹 Alternative 5: Using map() Function
fruits = ["apple", "banana", "cherry"]
list(map(print, fruits))
# Loop ek hi line me likha hai (map function).
# map() function se print kiya, explicit loop likhne ki zaroorat  .


# ⏳ Final Thoughts: 
# ✔️ Agar simple loop chahiye → Alternative 1 & 2 (While loop, List comprehension)
# ✔️ Agar membership check karna hai → Alternative 3 (in & not in)
# ✔️ Agar index ke sath print karna hai → Alternative 4 (enumerate())
# ✔️ Agar functional programming chahiye → Alternative 5 (map())


##Range Function

# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


# 🔹 Example 2: Step Size (range(start, end, step))
# Print even numbers from 0 to 10
for i in range(0, 11, 2):
    print(i)
# Output: 0 2 4 6 8 10
# 📌 Yahan step=2 use kiya gaya hai, jo har baar 2 number jump karega.


# 🔹 Example 3: Reverse Order (range(start, end, -step))
for i in range(10, 0, -1):
    print(i)
# Output: 10 9 8 7 6 5 4 3 2 1
# 📌 Yahan step=-1 use kiya gaya hai, jo har baar 1 number kam karega.




# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)
# Output: 2 4 6 8 10

##Controlling Loops

# 🔹 break: Break the loop when condition is met.
# Stop loop when number is 5
for i in range(1, 11):
    if i == 5:
        break  # Loop will stop when i is 5
    print(i)
# Output: 1 2 3 4
# 📌 Yahan loop 5 par break ho gaya, isliye 5 ke baad ke numbers nahi print hue.


























#Membership Operators

# in
# not in

#Identity Operators

# is
# is not

#Bitwise Operators

# &
# |
# ^
# ~
# <<
# >>



#Arithmetic Operators

# +
# -
# *
# /
# %
# **
# //

#Assignment Operators

# =
# +=
# -=
# *=
# /=
# %=
# **=
# //=







