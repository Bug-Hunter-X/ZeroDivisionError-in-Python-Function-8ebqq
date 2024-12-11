def my_function(a, b):
    if b == 0:
        return "Division by zero!"  # Or raise an exception: raise ZeroDivisionError("Division by zero")
    else:
        return a / b

result = my_function(10, 0)
print(result)  # Output: Division by zero!