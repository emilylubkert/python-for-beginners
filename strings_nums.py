first_name = "Emily"
last_name = "Lubkert"
# print(first_name + last_name)
# print("Hello " + first_name + " " + last_name)

output1 = "Hello, {} {}".format(first_name, last_name)
output2 = "Hello, {0} {1}".format(first_name, last_name)
# only available in Python 3
output3 = f"Hello, {first_name} {last_name}"

# print(output1)
# print(output2)
# print(output3)

# Numeric Data Types
# working with strings + numbers
days_in_feb = 28
#type conversion
# print(str(days_in_feb) + " days in february")

first_num = input("Enter first number")
second_num = input("Enter second number")
# print(int(first_num) + int(second_num))