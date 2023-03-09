
print("Welcome to the Grand Circus Room Detail Generator\n")

length = input("Enter the length of the classroom: ")
width = input("Enter the width of the classroom: ")
Area = length * width
Perimeter = (length + width) * 2
print(f"{Area} Sqft.")
print(f"{Perimeter} Sqft.")
if (Area <= 250):
    print("This is a small room.")
elif (Area > 250 and Area < 650):
    print("This is a medium-sized room.")
else:
    print("This is a large room.")

print("Thanks for using the Room Detail Generator.")

