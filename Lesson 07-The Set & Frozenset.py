##1}. The Set Data Type

# 1️⃣ Creating a Set
# A set {} curly brackets ya set() function se banaya jata hai:
# Creating a set
numbers = {1, 2, 3, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set (Important!)
empty_set = set()  # ✅ Correct
empty_dict = {}  # ❌ This is a dictionary, NOT a set!


# 2️⃣ Duplicate Values Not Allowed
# Sets automatically remove duplicate values:
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}


# 3️⃣ Adding & Removing Elements
# Adding elements
numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}

# 🧼remove() → Element ko delete karta hai, error deta hai agar element na ho
numbers.remove(3)
print(numbers)  # Output: {1, 2, 4, 5, 6}

# discard() → Element ko delete karta hai, error nahi deta hai agar element na ho
numbers.discard(3)
print(numbers)  # Output: {1, 2, 4, 5, 6}


# pop() → Random element remove karta hai
numbers.pop()
print(numbers)  # Output: {2, 4, 5, 6}


# clear() → Set ko empty karta hai
numbers.clear()


# 4️⃣ Set Operations
# union() → Dono sets ko combine karta hai (Duplicates remove hote hain)
set1 = {1, 2, 3,4}
set2 = {4, 5, 6,2}
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5, 6}


# intersection() → Common elements return karta hai
#jo duplicates ho gai woh aagi value
result = set1.intersection(set2)
print(result)  # Output: {2,4}

# difference() → Jo sirf pehle set me hain, wo return karta hai
result = set1.difference(set2)
print(result)  # Output: {1, 3}


# symmetric_difference() → Jo elements unique hain dono sets me, wo return karta hai
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 3, 5,6}


# 5️⃣ Checking Membership
# in → Check karta hai ke koi element set me mojood hai ya nahi
print(3 in set1)  # Output: True
print(10 in set1)  # Output: False


# The set is unordered
my_set = {10, 20, 30, 40, 50}
print(my_set)


set2: set = {'Java', 'Python', 'JavaScript', 'java'}
print(set2)


# The set is Unchangeable
# The set is unchangeable, means we can't change the items after the set is created.
# But we can add new items.
# 🔥 Example: Set Elements are Immutable
# my_set = {1, 2, 3, 4, 5}
# my_set[0] = 10  # This will raise an error


# ✅ But You Can Add or Remove Elements
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}


# Try to change an item (this will raise an error)
try:
    my_set[0] = 10  # Sets are unordered, so indexing doesn't work
except TypeError as e:
    print("*TypeError*  ABC : ", e)  # Output: 'set' object does not support item assignment

print("Program execution continues as normal because we handle the error condition in try except block")


# 2️⃣ remove() → Element hata sakte ho

my_set.remove(2)
print(my_set)  
# Output: {1, 3, 4}
# 3️⃣ discard() → Remove karta hai, lekin error nahi deta

my_set.discard(10)  # 10 set me nahi hai, but koi error nahi aayega
print(my_set)
# 4️⃣ pop() → Random element remove karta hai


my_set.pop()
print(my_set)
# 5️⃣ clear() → Poora set empty kar deta hai

my_set.clear()
print(my_set)  # Output: set()


# Use difference_update() method to remove multiple element at once.

# 🔹 Example: Using difference_update()
# Original set
set1 = {1, 2, 3, 4, 5, 6}

# Removing multiple elements (2, 4, 6) at once
set1.difference_update({2, 4, 6})

print(set1)  
# Output: {1, 3, 5}


# 🔥 Example: If Some Elements Are Not in the Set
set1 = {10, 20, 30, 40}
set1.difference_update({20, 50, 60})  # 50 & 60 are not in set1

print(set1)  
# Output: {10, 30, 40}  (No error, just removes 20)


# Define the set
my_set = {4, 5, 6,'a'}

print("Before:", my_set)

# Add multiple items
my_set.update([7, 8, 9, "Hello"])
print("After:", my_set)  


# Using the union() method or | operator:

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

# Using union() method
result = set1.union(set2)
print(result)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


# ✅ Example: Using | (Union Operator)
my_set: set   = {1, 2, 3, 5}
my_set_2: set = {1, 5, 6, 7}

my_set3: set  = my_set | my_set_2 # | operator
print(my_set3)
#output: {1, 2, 3, 5, 6, 7}

# 1️⃣ Union of Multiple Sets
# Using the union() method:
set1 = {1, 2}
set2 = {3, 4}
set3 = {5, 6}

# Using union()
result = set1.union(set2, set3)
print(result)  # Output: {1, 2, 3, 4, 5, 6}

# Using | operator
result = set1 | set2 | set3
print(result)  # Output: {1, 2, 3, 4, 5, 6}


# 2️⃣ Union with a List or Tuple
set1 = {1, 2, 3}
list1 = [3, 4, 5]

result = set1.union(list1)
print(result)  # Output: {1, 2, 3, 4, 5}


# 3️⃣ Union with an Empty Set
set1 = {1, 2, 3}
empty_set = set()

print(set1 | empty_set)  # Output: {1, 2, 3}


# 4️⃣ Union with a Dictionary
# Using the union() method:
set1 = {1, 2, 3}
my_dict = {'a': 1, 'b': 2}

result = set1.union(my_dict)
print(result)  # Output: {1, 2, 3, 'a', 'b'}



## The Frozenset

# 1️⃣ Creating a Frozenset
# Using the frozenset() constructor:
# Creating a normal set
normal_set = {1, 2, 3}

# Creating a frozenset
frozen = frozenset({1, 2, 3, 4, 5})

print(frozen)  
# Output: frozenset({1, 2, 3, 4, 5})

my_frozenset: frozenset = frozenset([1,2,3, "Hello! World🌏"])
print("my_frozenset  = ", my_frozenset)
#output: my_frozenset  =  frozenset({1, 2, 3, 'Hello! World'})

# Yeh ek immutable set (frozenset) banata hai.
# Matlab: Iske elements badal nahi sakte, naya element add nahi ho sakta, aur koi element remove bhi nahi ho sakta.


my_set: set = {1,2,3, "Hello! World"}
my_frozenset2: frozenset = frozenset(my_set)
print("my_frozenset2 = ",my_frozenset2)
#output: my_frozenset2 =  frozenset({1, 2, 3, 'Hello! World'})

##Set Methods
my_set: set  = {1, 2, 3, "Hello! World", 4, 5, 6}
my_set2: set = {1, 2, 3, "Hello! World", 8, 9}

# 1. (●'◡'●)difference()
print("difference()           = ", my_set.difference(my_set2))
#output: difference()           =  {4, 5, 6}

# Yeh method my_set ke woh elements return karega jo my_set2 me nahi hain.
# Matlab: my_set me se my_set2 ke elements hata do.


# 2. (●'◡'●)intersection()
print("intersection()         = ", my_set.intersection(my_set2))
#output: intersection()         =  {1, 2, 3, 'Hello! World'}

# Yeh method my_set aur my_set2 ke common elements return karega.
# Matlab: Dono sets me jo same elements hain, wahi milenge.


# 3. union()
print("union()                = ", my_set.union(my_set2))
#output: union()                =  {1, 2, 3, 4, 5, 6, 8, 9, 'Hello! World'}

# Yeh method my_set aur my_set2 ke saare unique elements ko ek naya set me daal kar return karega.
# Matlab: Dono sets ko mila do, aur duplicate elements hata do.


# 4. (●'◡'●)isdisjoint()
print("isdisjoint()           = ", my_set.isdisjoint(my_set2))

#output: isdisjoint()           =  False
# Yeh method check karega ki dono sets me koi bhi common element hai ya nahi.
# Agar koi bhi common element nahi hai toh True, warna False return karega.

# 5. (●'◡'●)symmetric_difference()
print("symmetric_difference() = ", my_set.symmetric_difference(my_set2))
#output: symmetric_difference() =  {4, 5, 6, 8, 9}

# Yeh method my_set aur my_set2 ke sirf unique elements return karega.
# Matlab: Jo elements dono sets me nahi milte, wahi rahenge.


# 6. issuperset()
my_set2 = {1, 2, 3, "Hello! World"}
print("issuperset()           = ", my_set.issuperset(my_set2))

# Yeh method check karega ki my_set ke saare elements my_set2 ke andar hain ya nahi.
# Agar my_set2 ke saare elements my_set me milte hain, toh True, warna False.


# 7. issubset()
print("issubset()             = ", my_set2.issubset(my_set))

#output: issubset()             =  False
# Yeh method check karega ki my_set2 ka har element my_set ke andar hai ya nahi.
# Agar my_set2 ke saare elements my_set me hain, toh True, warna False.


# prompt: generate examples of all the method of set
set1: set = {1, 2, 3, 4, 5}
set2: set = {4, 5, 6, 7, 8}


# 🔹1. add(element) (❁´◡`❁)
set1.add(6)
print(f"add(6): {set1}")
#output: add(6): {1, 2, 3, 4, 5, 6}

# Set me naya element add karta hai.


# 🔹2. clear() (❁´◡`❁)
set1.clear()
print(f"clear(): {set1}")
#output: clear(): set()

# Set ko empty karta hai.

# 🔹3. copy() (❁´◡`❁)
set_copy: set = set1.copy()
print(f"copy(): {set_copy}")
#output: copy(): {1, 2, 3, 4, 5, 6}

# Set ka duplicate (copy) return karta hai.


# 🔹4. difference() (❁´◡`❁)
difference_set: set = set1.difference(set2)
print(f"difference(): {difference_set}")

#output: difference(): Output: {1, 2, 3, 6}

# Set ke elements jo set2 me nahi hain, woh return karega.


# 🔹5. difference_update() (❁´◡`❁)
set1.difference_update(set2)
print(f"difference_update(): {set1}")
#output: difference_update(): {1, 2, 3, 6}

# Set ke elements jo set2 me nahi hain, woh update/hata dena karega.


# 🔹6. discard() (❁´◡`❁)
set1.discard(6)
print(f"discard(): {set1}")
#output: discard(): {1, 2, 3,4,5}

# Agar element set me ho, toh remove kar deta hai.
# Agar element na ho, error nahi aata!


# 🔹7. intersection() (❁´◡`❁)
intersection_set: set = set1.intersection(set2)
print(f"intersection(): {intersection_set}")

# Dono sets ke common elements return karta hai.

# 🔹8. intersection_update() (❁´◡`❁)
set1.intersection_update(set2)
print(f"intersection_update(): {set1}")

# set1 ko update karke sirf common elements rakh deta hai.


# 🔹9. isdisjoint() (❁´◡`❁)
print(f"isdisjoint(): {set1.isdisjoint(set2)}")
print(f"isdisjoint(): {set1.isdisjoint({9,10})}")
# Check karta hai ki koi common element hai ya nahi.
# Agar common element nahi hai, toh True.
# Agar common element hai, toh False.


# 🔹10. issubset() (❁´◡`❁)
print(f"issubset(): {set1.issubset(set2)}")
print(f"issubset(): { {1,2}.issubset(set1) }")
# Check karta hai ki set1, set2 ka subset hai ya nahi.
# Agar set1 ke sare elements set2 me hain, toh True.


# 🔹11. issuperset() (❁´◡`❁)
print(f"issuperset(): {set1.issuperset(set2)}")
print(f"issuperset(): { {1,2,3,4,5}.issuperset(set1) }")
# Check karta hai ki set1, set2 ko contain karta hai ya nahi.
# Agar karta hai, toh True.


# 🔹12. pop() (❁´◡`❁)
# removed_element: int = set1.pop()
# print(f"pop(): {removed_element}")
# print(f"set after pop(): {set1}")
# Set me se ek random element hata deta hai.


# 🔹13. remove() (❁´◡`❁)
# set1.remove(6)
# print(f"remove(): {set1}")
# Set me se ek specific element hata deta hai.


# 🔹14. symmetric_difference() (❁´◡`❁)
symmetric_difference_set: set = set1.symmetric_difference(set2)
print(f"symmetric_difference(): {symmetric_difference_set}")
# Dono sets ke unique elements return karta hai.


# 🔹15. symmetric_difference_update() (❁´◡`❁)
set1.symmetric_difference_update(set2)
print(f"symmetric_difference_update(): {set1}")
# Set1 ko update karke dono sets ke unique elements rakh deta hai.


# 🔹16. union() (❁´◡`❁)
union_set: set = set1.union(set2)
print(f"union(): {union_set}")
# Dono sets ke saare unique elements return karta hai.


# 🔹17. update() (❁´◡`❁)
set1.update(set2)
print(f"update(): {set1}")
# Set1 ko update karke set2 ke elements rakh deta hai.



# Create some example frozensets🌼
frozen_set1: frozenset = frozenset([1, 2, 3, 4])
frozen_set2: frozenset = frozenset([3, 4, 5, 6])
frozen_set3: frozenset = frozenset([1, 2])

print(f"frozen_set1: {frozen_set1}")
print(f"frozen_set2: {frozen_set2}")
print(f"frozen_set3: {frozen_set3}")
print("\n----------\n")
# Methods that work with frozensets (since they are immutable)
# These methods return a new frozenset or a boolean value

# 1. difference(): Returns a new frozenset with elements present in the first frozenset but not in the second.
difference_set: frozenset = frozen_set1.difference(frozen_set2)
print(f"difference(): {difference_set}")  # Output: frozenset({1, 2})

# 2. intersection(): Returns a new frozenset containing only elements common to both frozensets.
intersection_set: frozenset = frozen_set1.intersection(frozen_set2)
print(f"intersection(): {intersection_set}")  # Output: frozenset({3, 4})

# 3. union(): Returns a new frozenset containing all unique elements from both frozensets.
union_set: frozenset = frozen_set1.union(frozen_set2)
print(f"union(): {union_set}")  # Output: frozenset({1, 2, 3, 4, 5, 6})

# 4. symmetric_difference(): Returns a new frozenset with elements that are in either of the sets but not in both.
symmetric_difference_set: frozenset = frozen_set1.symmetric_difference(frozen_set2)
print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: frozenset({1, 2, 5, 6})

# 5. isdisjoint(): Returns True if the two frozensets have no elements in common; otherwise, False.
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozen_set2)}")  # Output: False
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozenset([7, 8]))}")  # Output: True

# 6. issubset(): Returns True if all elements of the first frozenset are present in the second frozenset.
print(f"issubset(): {frozen_set3.issubset(frozen_set1)}")  # Output: True
print(f"issubset(): {frozen_set1.issubset(frozen_set3)}")  # Output: False

# 7. issuperset(): Returns True if all elements of the second frozenset are present in the first frozenset.
print(f"issuperset(): {frozen_set1.issuperset(frozen_set3)}")  # Output: True
print(f"issuperset(): {frozen_set3.issuperset(frozen_set1)}")  # Output: False

# 8. copy(): Returns a new frozenset that is a shallow copy of the original.
copy_set: frozenset = frozen_set1.copy()
print(f"copy(): {copy_set}")  # Output: frozenset({1, 2, 3, 4})
print(f"copy() is same object?: {copy_set is frozen_set1}") # Output: True because frozensets are immutable
