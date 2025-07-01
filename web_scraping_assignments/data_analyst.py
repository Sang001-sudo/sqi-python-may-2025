import re

def _write_file(name:str, content):
    with open(name, "a") as f:
        f.writelines(content)

with open("reviews.txt", "r") as f:
    contents = f.read()
    
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_pattern = r"\+234\s?\d{3}\s?\d{3}\s?\d{4}"
emails = re.findall(email_pattern, contents)
phone_no = re.findall(phone_pattern, contents)

for email in emails:
    _write_file("emails.txt", f"{email}\n")

    
for phone in phone_no:
    _write_file("phone_numbers.txt", f"{phone}\n")
