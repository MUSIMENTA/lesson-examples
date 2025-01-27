# Python program to solve a puzzle

base_number = 5
expotential_number = 2

power_result = base_number**expotential_number

print(power_result)

#I am working with a large number
large_number = 23

#Quatient division
quotient_division = large_number//base_number

print(quotient_division)

#Exact division
exact_division = large_number/base_number

print(exact_division)

#Final value 
final_value = power_result + quotient_division + exact_division
print(final_value)
print(type(final_value))