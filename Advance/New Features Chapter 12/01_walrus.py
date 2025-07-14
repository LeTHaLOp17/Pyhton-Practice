# Walrus operator 
if(n := len([1, 2, 3, 4, 5, 6])) > 3:
    print(f"List is too long ({n} elemnts, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)