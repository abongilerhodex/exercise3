# Question 5: Using a Function as an Argument

def apply_operation(function, n):
  return function(n)


def double(n):
  return n * 2

# combined apply operation function with double function
operation_plus_double = apply_operation(double, 7)
print(operation_plus_double)

# combined apply operation function with square function
def square(n):
  return n ** 2
operation_plus_square = apply_operation(square, 3)
print(operation_plus_square)