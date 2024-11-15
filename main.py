# import array as arr

# Working with python arrays
"""list_array = arr.array("b", [2,1,2,3])
print(type(list_array))
print(list_array.pop(1))
print(list_array)

def myfunction(a,b):
    # This is a function to perform arithmetic operations

    return a + b
print(myfunction(3,2))
"""

# Fizzbuss class Interview Question
# cash_price = [85, 50, 12, 38, 41, 60]
# for i in cash_price:
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
    
#     else:
#         print(i)

# or

# for i, num in enumerate(cash_price):
#     if num % 3 == 0 and num % 5 == 0:
#         cash_price[i] = 'fizzbuzz'
#     elif num % 3 == 0:
#         cash_price[i] = 'fizz'
#     elif num % 5 == 0:
#         cash_price[i] = 'buzz'
# print(cash_price)

print(sorted([85, 50, 12, 38, 41, 60], reverse=True))


# print(ord("N"))
# data = bytes([80, 89, 84, 72, 79, 78])
# print(data)

# string = 'Hello world!'
# encoded = string.encode('utf-8')
# print(encoded)
# # print(type(encoded))

# decoded = encoded.decode('utf-8')
# print(decoded)