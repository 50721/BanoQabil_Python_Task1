
#  1.Declare two variables, num1 and num2, with any integer values. Use these to calculate their sum and print the result. Understand how variables store numerical values and perform basic arithmetic in Python.

# Declare two variables with integer values
num1 = 10
num2 = 5

# Calculate their sum
sum_result = num1 + num2

# Print the result
print("The sum of 10 and 5 is:", sum_result)


# 2.Create a variable called message and give it a string value. Append the string " World!" to it and print the updated message. Explore basic string operations in Python.

# Create a variable called message with a string value
message = "Hello"

# Append the string " World!" to the existing message
message += " World!"

# Print the updated message
print(message)


# 3. Declare a variable, is_python_fun, and assign it a boolean value. Print a statement based on whether Python is considered fun. Learn to use boolean variables for decision-making in Python.


# Declare a boolean variable is_python_fun and assign it a value
is_python_fun = True

# Check the value of the boolean variable and print a statement

if is_python_fun:
    print("Python is considered fun!")
else:
    print("Python may not be considered fun for everyone.")


# 4. Create a list called fruits with at least three different fruit names. Print the list, add a new fruit, and then print the updated list. Understand the basics of working with lists in Python.
    

# Create a list called fruits with at least three different fruit names
fruits = ["Apple", "Banana", "Orange"]

# Print the original list
print("Original list of fruits:", fruits)

# Add a new fruit to the list
new_fruit = "Grapes"
fruits.append(new_fruit)

# Print the updated list
print("Updated list of fruits:", fruits)


# 5. Declare a variable called price with a floating-point value. Convert it to an integer and print both the original and converted values. Explore how to convert between different data types in Python.


# Declare a variable called price with a floating-point value
price = 19.99

# Convert the floating-point value to an integer
price_as_integer = int(price)

# Print both the original and converted values
print("Original price:", price)
print("Converted price as integer:", price_as_integer)


# 6. Create a dictionary named student_info with keys for 'name', 'age', and 'grade'. Assign corresponding values and print the dictionary. Learn how to work with dictionaries, a versatile data structure in Python.

# Create a dictionary named student_info
student_info = {
    'name': 'Abdul Ahad',
    'age': 18,
    'grade': 'A'
}

# Print the dictionary
print("Student Information:")
print("Name:", student_info['name'])
print("Age:", student_info['age'])
print("Grade:", student_info['grade'])

# 7.Combine two strings using concatenation. Use string interpolation to include the length of the resulting string in a print statement. Explore different ways to manipulate strings in Python 


#tow string to combine
str1= "Hello"
str2= "world"

#concatenate the string
combined_string = str1+" "+str2

#print combined string 
print("The combined string is:", combined_string , "and is length is:", len(combined_string))


# 8.Create a tuple named days_of_week with the names of the days. Access and print the third day of the week. Understand the basics of working with tuples in Python.

# Create a tuple named days_of_week
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# Access and print the third day of the week (index 2)
third_day = days_of_week[2]
print("The third day of the week is:", third_day)






