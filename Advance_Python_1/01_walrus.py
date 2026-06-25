# using walrus operator to assign a value to a variable as part of an expression
# The walrus operator (:=) allows you to assign a value to a variable as part of an expression. This can be useful in situations where you want to both use a value and assign it to a variable at the same time.

if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"The length of the list is {n}, which is greater than 3.")
    # Output: The length of the list is 5, which is greater than 3.