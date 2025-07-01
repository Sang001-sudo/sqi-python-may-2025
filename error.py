# from datetime import datetime

# while True:
#     try:
#         age = int(input("How old are you?: "))
#     except Exception as err:
#         print(f"Error: {err}")
#     else:
#         if age < 1:
#             continue

#         currrent_year = datetime.now().year
#         print(f"Your Birth year is {currrent_year - age}")
#         break



with open("new_file.txt", "r") as f:
    content = f.read()

words = content.split("\n")

for i, _ in enumerate(words, 1):
    print(f"line {str(i)}: {_}")
    # print(f"line {i+1}: {words[i]}")