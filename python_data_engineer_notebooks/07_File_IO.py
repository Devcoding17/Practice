# File I/O
with open("sample.txt", "w") as f:
    f.write("Hello, Data Engineer! "
            "This is a sample file.\n")

with open("sample.txt", "r") as f:
    print(f.read())        # Read entire file
    print(f.readlines())   # Read lines into a list
    print(f.readline())    # Read one line
    # print(f.seek(0))  # Reset file pointer to the beginning

