with open("text.py", "r") as f:
    content = f.read()
print(content)


with open("me.txt", "w") as f:
    f.write("Hello, my name is awwal")