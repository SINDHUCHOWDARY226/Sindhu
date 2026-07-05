#create a Tuple
person  = ("Sindhu", 20,"pink")
print(person)
#Acess Tuple elements
days = ("Monday", "Tuesday", "Wednesday","Thursday","Firday","Saturday","Sunday")
print(days[2])
#Tuple Concatenation
odd = (1, 3, 5)
even = (2, 4, 6)
result = odd + even
print(result)
#Tuple Unpacking
rectangle = (10 , 5)
length, width = rectangle
area = length + width
print("Area =", area)
#Checks if an Element Exists
fruits = ("Apple", "Banana", "Orange")
item = "Banana"
if item in fruits:
    print ("Elements Exists")
else:
    print("Elements not Found")
# Supermarket Bill Generator
items = [
    ("Apple", 99),
    ("Banana", 99),
    ("Milk", 49)
]
total = 0
print("Item\t\tPrice")
print("-----------------------")
for item, price in items:
    print(f"{item}\t\t{price:.2f}")
    total += price
print("-----------------------")
print(f"Total\t\t{total:.2f}")