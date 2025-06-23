# List Comprehensions
squared = [x*x for x in range(10)]
filtered = [x for x in squared if x > 25]
print(filtered)
print(squared)