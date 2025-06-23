# Error Handling
try:
    val = int("abc")
except ValueError as e:
    print("Conversion error:", e)