import math

print("Exercise 1")
a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

s = (a + b + c) / 2

area = math.sqrt(s * (s-a) * (s-b) * (s-c))
print(area)

print("\nExercise 2")
radius = float(input("Radius: "))
area = 4 * math.pi * radius ** 2
print(area)